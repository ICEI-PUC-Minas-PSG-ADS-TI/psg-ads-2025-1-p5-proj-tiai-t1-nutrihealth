from flask import Blueprint, request, jsonify
from .. import db
from ..models.planejamento_sema_model import PlanejamentoSemanal, DiaSemanaEnum, TipoRefeicaoEnum
from ..models.user_model import User
from ..models.receita_model import Receita
from flask_jwt_extended import jwt_required, get_jwt_identity

planejamento_bp = Blueprint("planejamento_bp", __name__)

@planejamento_bp.route("/planejamento", methods=["POST"])
@jwt_required()
def criar_planejamento():
    data = request.get_json()
    current_user_id = get_jwt_identity()

    dia_semana = data.get("dia_semana")
    tipo_refeicao = data.get("tipo_refeicao")
    receita_id = data.get("receita_id")

    if not dia_semana or not tipo_refeicao or not receita_id:
        return jsonify({"erro": "Dados incompletos"}), 400

    try:
        dia_enum = DiaSemanaEnum[dia_semana]
        refeicao_enum = TipoRefeicaoEnum[tipo_refeicao]
    except KeyError:
        return jsonify({"erro": "Dia da semana ou tipo de refeição inválido"}), 400

    planejamento_existente = PlanejamentoSemanal.query.filter_by(
        user_id=current_user_id,
        dia_semana=dia_enum,
        tipo_refeicao=refeicao_enum
    ).first()

    if planejamento_existente:
        planejamento_existente.receita_id = receita_id
    else:
        planejamento_existente = PlanejamentoSemanal(
            dia_semana=dia_enum,
            tipo_refeicao=refeicao_enum,
            user_id=current_user_id,
            receita_id=receita_id
        )
        db.session.add(planejamento_existente)

    db.session.commit()
    return jsonify({"message": "Planejamento criado/atualizado com sucesso"}), 201


@planejamento_bp.route("/planejamento", methods=["GET"])
@jwt_required()
def listar_planejamento():
    current_user_id = get_jwt_identity()
    planejamentos = PlanejamentoSemanal.query.filter_by(user_id=current_user_id).all()

    response = [
        {
            "id": p.id,
            "dia_semana": p.dia_semana.value,
            "tipo_refeicao": p.tipo_refeicao.value,
            "receita_id": p.receita.id,
            "receita_nome": p.receita.nome
        }
        for p in planejamentos
    ]
    return jsonify(response), 200
