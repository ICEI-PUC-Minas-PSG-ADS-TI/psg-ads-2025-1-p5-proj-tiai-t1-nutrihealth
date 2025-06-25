from flask import Blueprint, request, jsonify
from .. import db
from ..models.ingrediente_model import Ingrediente
from flask_jwt_extended import jwt_required, get_jwt_identity 

ingrediente_bp = Blueprint("ingrediente_bp", __name__)

@ingrediente_bp.route("/ingredientes", methods=["POST"])
@jwt_required()
def create_ingrediente():
    data = request.get_json()
    current_user_id = get_jwt_identity()

    nome = data.get("nome")
    quantidade = data.get("quantidade")
    unidade_de_medida = data.get("unidade_de_medida")
    impacto_ambiental = data.get("impacto_ambiental")

    if not nome or quantidade is None or not unidade_de_medida or not impacto_ambiental:
        return jsonify({"error": "Nome, quantidade, unidade de medida e impacto ambiental são obrigatórios"}), 400

    new_ingrediente = Ingrediente(
        nome=nome,
        quantidade=quantidade,
        unidade_de_medida=unidade_de_medida,
        impacto_ambiental=impacto_ambiental,
        user_id=current_user_id
    )
    db.session.add(new_ingrediente)
    db.session.commit()

    return jsonify({"message": "Ingrediente criado com sucesso", "id": new_ingrediente.id}), 201

@ingrediente_bp.route("/ingredientes", methods=["GET"])
@jwt_required()
def get_all_ingredientes():
    current_user_id = get_jwt_identity()
    ingredientes = Ingrediente.query.filter_by(user_id=current_user_id).all()
    result = []
    for ing in ingredientes:
        result.append({
            "id": ing.id,
            "nome": ing.nome,
            "quantidade": ing.quantidade,
            "unidade_de_medida": ing.unidade_de_medida,
            "impacto_ambiental": ing.impacto_ambiental
        })
    return jsonify(result), 200

@ingrediente_bp.route("/ingredientes/<int:ingrediente_id>", methods=["GET"])
@jwt_required()
def get_ingrediente_details(ingrediente_id):
    current_user_id = get_jwt_identity()
    ingrediente = Ingrediente.query.filter_by(id=ingrediente_id, user_id=current_user_id).first()
    if not ingrediente:
        return jsonify({"error": "Ingrediente não encontrado"}), 404

    return jsonify({
        "id": ingrediente.id,
        "nome": ingrediente.nome,
        "quantidade": ingrediente.quantidade,
        "unidade_de_medida": ingrediente.unidade_de_medida,
        "impacto_ambiental": ingrediente.impacto_ambiental
    }), 200

@ingrediente_bp.route("/ingredientes/<int:ingrediente_id>", methods=["PUT"])
@jwt_required()
def update_ingrediente(ingrediente_id):
    current_user_id = get_jwt_identity()
    ingrediente = Ingrediente.query.filter_by(id=ingrediente_id, user_id=current_user_id).first()
    if not ingrediente:
        return jsonify({"error": "Ingrediente não encontrado"}), 404

    data = request.get_json()

    if "nome" in data:
        ingrediente.nome = data["nome"]
    if "quantidade" in data:
        ingrediente.quantidade = data["quantidade"]
    if "unidade_de_medida" in data:
        ingrediente.unidade_de_medida = data["unidade_de_medida"]
    if "impacto_ambiental" in data:
        ingrediente.impacto_ambiental = data["impacto_ambiental"]

    db.session.commit()
    return jsonify({"message": "Ingrediente atualizado com sucesso"}), 200

@ingrediente_bp.route("/ingredientes/<int:ingrediente_id>", methods=["DELETE"])
@jwt_required()
def delete_ingrediente(ingrediente_id):
    current_user_id = get_jwt_identity()
    ingrediente = Ingrediente.query.filter_by(id=ingrediente_id, user_id=current_user_id).first()
    if not ingrediente:
        return jsonify({"error": "Ingrediente não encontrado"}), 404

    db.session.delete(ingrediente)
    db.session.commit()
    return jsonify({"message": "Ingrediente deletado com sucesso"}), 200
