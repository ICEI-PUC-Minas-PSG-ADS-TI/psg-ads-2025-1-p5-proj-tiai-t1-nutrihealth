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

    if not name or not email or not password:
        return jsonify({"error": "Nome, email e senha são obrigatórios"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Este email já está cadastrado"}), 409

    user = User(name=name, email=email)
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
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=24))
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Email ou senha inválidos"}), 401

@user_bp.route("/profile", methods=["GET"])
@jwt_required()
def get_user_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 200

@user_bp.route("/profile/my_recipes", methods=["GET"])
@jwt_required()
def get_user_created_recipes():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    
    recipes = [{"id": recipe.id, "nome": recipe.nome} for recipe in user.receitas_criadas]
    return jsonify(recipes), 200

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

@user_bp.route("/users", methods=["POST"])
def create_user_legacy():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email") 
    password = data.get("password")
    
    if not name or not email or not password:
        return jsonify({"error": "Nome, email e senha são obrigatórios"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Este email já está cadastrado"}), 409

    user = User(name=name, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201

@user_bp.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuário deletado com sucesso"}), 200
