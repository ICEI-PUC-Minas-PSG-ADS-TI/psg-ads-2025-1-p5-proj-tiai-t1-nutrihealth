from flask import Blueprint, request, jsonify
from .. import db
from ..models.venda_model import Venda
from ..models.user_model import User

venda_bp = Blueprint("venda_bp", __name__)

@venda_bp.route("/vendas", methods=["GET"])
def get_vendas():
    vendas = Venda.query.all()
    result = [
        {
            "id": venda.id,
            "preco": venda.preco,
            "user_id": venda.user_id,
            "user_name": venda.user.name if venda.user else None
        }
        for venda in vendas
    ]
    return jsonify(result), 200


@venda_bp.route("/vendas", methods=["POST"])
def create_venda():
    data = request.get_json()
    preco = data.get("preco")
    user_id = data.get("user_id")

    if not preco or not user_id:
        return jsonify({"error": "preco e user_id são obrigatórios"}), 400

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    nova_venda = Venda(preco=preco, user_id=user_id)
    db.session.add(nova_venda)
    db.session.commit()

    return jsonify({"message": "Venda criada com sucesso", "id": nova_venda.id}), 201


@venda_bp.route("/vendas/<int:id>", methods=["PUT"])
def update_venda(id):
    venda = Venda.query.get(id)
    if not venda:
        return jsonify({"error": "Venda não encontrada"}), 404

    data = request.get_json()
    venda.preco = data.get("preco", venda.preco)
    user_id = data.get("user_id", venda.user_id)

    if user_id != venda.user_id:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "Usuário não encontrado"}), 404
        venda.user_id = user_id

    db.session.commit()

    return jsonify({"message": "Venda atualizada com sucesso"}), 200

@venda_bp.route("/vendas/<int:id>", methods=["DELETE"])
def delete_venda(id):
    venda = Venda.query.get(id)
    if not venda:
        return jsonify({"error": "Venda não encontrada"}), 404

    db.session.delete(venda)
    db.session.commit()
    return jsonify({"message": "Venda deletada com sucesso"}), 200
