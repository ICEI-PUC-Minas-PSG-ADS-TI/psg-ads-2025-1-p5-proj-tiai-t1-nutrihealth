from flask import Blueprint, request, jsonify
from .. import db
from ..models.user_model import User
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity
from datetime import timedelta

user_bp = Blueprint("user_bp", __name__)

jwt = JWTManager()

@user_bp.route("/auth/register", methods=["POST"])
def register_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    tipo = data.get("tipo") 

    if not name or not email or not password or not tipo: 
        return jsonify({"error": "Nome, email, senha e tipo são obrigatórios"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Este email já está cadastrado"}), 409

    user = User(name=name, email=email, tipo=tipo)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Usuário registrado com sucesso", "id": user.id}), 201

@user_bp.route("/auth/login", methods=["POST"])
def login_user():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        access_token = create_access_token(identity=str(user.id), expires_delta=timedelta(hours=20))
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Email ou senha inválidos"}), 401

@user_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_user_profile():
    current_user_id = get_jwt_identity()
    user = db.session.get(User, current_user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200

@user_bp.route("/profile/my_recipes", methods=["GET"])
@jwt_required()
def get_user_created_recipes():
    current_user_id = get_jwt_identity()
    user = db.session.get(User, current_user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    
    recipes = [{"id": recipe.id, "nome": recipe.nome} for recipe in user.receitas_criadas]
    return jsonify(recipes), 200

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

@user_bp.route("/users/<int:id>", methods=["PUT"])
@jwt_required()
def update_user(id):
    current_user_id = get_jwt_identity()
    current_user = db.session.get(User, current_user_id)

    if not current_user:
        return jsonify({"error": "Usuário logado não encontrado"}), 401

    if current_user.id != id and current_user.tipo != 'Nutricionista':
        return jsonify({"error": "Acesso negado: Você só pode editar seu próprio perfil, ou deve ser um Nutricionista para editar outros."}), 403

    user_to_update = db.session.get(User, id)
    if not user_to_update:
        return jsonify({"error": "Usuário a ser atualizado não encontrado"}), 404

    data = request.get_json()

    if "name" in data:
        user_to_update.name = data["name"]

    if "email" in data:
        new_email = data["email"]
        if new_email != user_to_update.email:
            if User.query.filter_by(email=new_email).first():
                return jsonify({"error": "Este email já está cadastrado para outro usuário"}), 409
            user_to_update.email = new_email

    if "password" in data:
        user_to_update.set_password(data["password"])

    if "tipo" in data:
        if current_user.tipo != 'Nutricionista':
            return jsonify({"error": "Acesso negado: Somente nutricionistas podem alterar o tipo de usuário."}), 403
        
        new_tipo = data["tipo"]
        if new_tipo not in ['Cliente', 'Nutricionista']:
            return jsonify({"error": "Tipo de usuário inválido. Deve ser 'Cliente' ou 'Nutricionista'."}), 400
        user_to_update.tipo = new_tipo

    db.session.commit()
    return jsonify({"message": "Usuário atualizado com sucesso"}), 200

@user_bp.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = db.session.get(User, id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuário deletado com sucesso"}), 200
