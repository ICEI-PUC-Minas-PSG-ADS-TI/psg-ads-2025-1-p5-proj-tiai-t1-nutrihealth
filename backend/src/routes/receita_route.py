from flask import Blueprint, request, jsonify
from .. import db
from ..models.receita_model import Receita, receita_ingrediente, receitas_salvas
from ..models.ingrediente_model import Ingrediente
from ..models.user_model import User
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

receita_bp = Blueprint("receita_bp", __name__)
#a

@receita_bp.route("/recipes", methods=["POST"])
@jwt_required()
def create_recipe():
    data = request.get_json()
    nome = data.get("nome")
    descricao = data.get("descricao")
    tempo_preparo_str = data.get("tempo_preparo")
    ingredientes_data = data.get("ingredientes")
    impacto_ambiental = data.get("impacto_ambiental")
    modo_preparo = data.get("modo_preparo")
    tipo_dieta = data.get("tipo_dieta")
    tipo_refeicao = data.get("tipo_refeicao")
    estilo_preparo = data.get("estilo_preparo")

    current_user_id = get_jwt_identity()
    print("====="*20)
    print(current_user_id)
    if not nome or not descricao or not tempo_preparo_str or not ingredientes_data:
        return jsonify({"error": "Nome, descrição, tempo de preparo e ingredientes são obrigatórios"}), 400

    try:
        tempo_preparo = datetime.strptime(tempo_preparo_str, "%H:%M")
    except ValueError:
        return jsonify({"error": "Formato de tempo_preparo inválido. Use HH:MM"}), 400

    new_recipe = Receita(nome=nome, descricao=descricao, tempo_preparo=tempo_preparo, user_id=current_user_id, modo_preparo=modo_preparo, impacto_ambiental=impacto_ambiental, tipo_dieta=tipo_dieta, tipo_refeicao=tipo_refeicao,estilo_preparo=estilo_preparo)
    db.session.add(new_recipe)
    db.session.commit() 

    for ing_data in ingredientes_data:
        ingrediente = db.session.get(Ingrediente, ing_data["id"])
        if ingrediente:
            new_recipe.ingredientes.append(ingrediente)
    db.session.commit()

    return jsonify({"message": "Receita criada com sucesso", "id": new_recipe.id}), 201

@receita_bp.route("/recipes", methods=["GET"])
def get_all_recipes():
    recipes = Receita.query.all()
    result = [{
        "id": recipe.id,
        "nome": recipe.nome,
        "descricao": recipe.descricao,
        "tempo_preparo": recipe.tempo_preparo.isoformat() if recipe.tempo_preparo else None,
        "modo_preparo": recipe.modo_preparo,
        "impacto_ambiental": recipe.impacto_ambiental,
        "tipo_dieta": recipe.tipo_dieta,
        "tipo_refeicao": recipe.tipo_refeicao,
        "estilo_preparo": recipe.estilo_preparo,
        "ingredientes": [{
            "id": ingrediente.id,
            "nome": ingrediente.nome,
            "quantidade": ingrediente.quantidade
        } for ingrediente in recipe.ingredientes]
    } for recipe in recipes]
    return jsonify(result), 200


@receita_bp.route("/recipes/<int:recipe_id>", methods=["GET"])
def get_recipe_details(recipe_id):
    recipe = db.session.get(Receita, recipe_id)
    if not recipe:
        return jsonify({"error": "Receita não encontrada"}), 404

    ingredientes_list = [
        {"id": ing.id, "nome": ing.nome, "quantidade": ing.quantidade, "unidade_de_medida": ing.unidade_de_medida, "impacto_ambiental": ing.impacto_ambiental}
        for ing in recipe.ingredientes 
    ]

    return jsonify({
        "id": recipe.id,
        "nome": recipe.nome,
        "descricao": recipe.descricao,
        "tempo_preparo": recipe.tempo_preparo.isoformat(),
        "modo_preparo": recipe.modo_preparo,
        "impacto_ambiental": recipe.impacto_ambiental,
        "tipo_dieta": recipe.tipo_dieta,
        "tipo_refeicao": recipe.tipo_refeicao,
        "estilo_preparo": recipe.estilo_preparo,
        "ingredientes": ingredientes_list
    }), 200

@receita_bp.route("/recipes/save/<int:recipe_id>", methods=["POST"])
@jwt_required()
def save_recipe(recipe_id):
    current_user_id = get_jwt_identity()
    user = db.session.get(User, current_user_id)
    recipe = db.session.get(Receita, recipe_id)

    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    if not recipe:
        return jsonify({"error": "Receita não encontrada"}), 404

    if recipe in user.receitas_salvas:
        return jsonify({"message": "Receita já está salva"}), 200

    user.receitas_salvas.append(recipe)
    db.session.commit()
    return jsonify({"message": "Receita salva com sucesso"}), 201

@receita_bp.route("/profile/saved_recipes", methods=["GET"])
@jwt_required()
def get_saved_recipes_for_user():
    current_user_id = get_jwt_identity()
    user = db.session.get(User, current_user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    saved_recipes = [{"id": recipe.id, "nome": recipe.nome} for recipe in user.receitas_salvas]
    return jsonify(saved_recipes), 200


@receita_bp.route("/recipes/<int:recipe_id>", methods=["DELETE"])
def delete_recipe(recipe_id):
    recipe = db.session.get(Receita, recipe_id)
    if not recipe:
        return jsonify({"error": "Receita não encontrada"}), 404
    db.session.delete(recipe)
    db.session.commit()
    return jsonify({"message": "Receita excluída com sucesso"}), 200

@receita_bp.route("/recipes/user", methods=["GET"])
@jwt_required()
def get_user_recipes():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    user_recipes = Receita.query.filter_by(user_id=current_user_id).all()

    result = [{
        "id": r.id,
        "nome": r.nome,
        "descricao": r.descricao,
        "tempo_preparo": r.tempo_preparo.isoformat() if r.tempo_preparo else None,
        "modo_preparo": r.modo_preparo,
        "impacto_ambiental": r.impacto_ambiental,
        "tipo_dieta": r.tipo_dieta,
        "tipo_refeicao": r.tipo_refeicao,
        "estilo_preparo": r.estilo_preparo,
        "ingredientes": [{
            "id": ing.id,
            "nome": ing.nome,
            "quantidade": ing.quantidade
        } for ing in r.ingredientes]
    } for r in user_recipes]

    return jsonify(result), 200
