from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

relatorio_bp = Blueprint("relatorio_bp", __name__)

@relatorio_bp.route("/relatorio/mensal", methods=["GET"])
@jwt_required()
def get_relatorio_mensal():
    current_user_id = get_jwt_identity()
    mes = request.args.get("mes", datetime.now().strftime("%m-%Y"))
    print(mes)

    data = {
        "usuario_id": current_user_id,
        "mes": mes,
        "total_refeicoes": 85,
        "media_calorias_dia": 2100,
        "alimento_mais_usado": "Quinoa",
        "desperdicio_alimentar": "320g",
        "co2_salvo": "45kg",
        "itens_mais_desperdicados": [
            {"nome": "Ervas Frescas", "quantidade": "120g"},
            {"nome": "Folhas verdes", "quantidade": "95g"},
            {"nome": "Pão", "quantidade": "85g"}
        ],
        "dica_do_mes": "Armazene as ervas em um copo de água com um saco plástico sobre elas para prolongar sua vida útil em até 2 semanas."
    }

    return jsonify(data), 200

@relatorio_bp.route("/relatorio/semanal", methods=["GET"])
@jwt_required()
def get_relatorio_semanal():
    current_user_id = get_jwt_identity()

    data = {
        "usuario_id": current_user_id,
        "semana": "17/06/2025 - 23/06/2025",
        "total_refeicoes": 20,
        "media_calorias_dia": 2150,
        "desperdicio_alimentar": "75g",
        "co2_salvo": "12kg",
        "itens_mais_desperdicados": [
            {"nome": "Folhas verdes", "quantidade": "35g"},
            {"nome": "Pão", "quantidade": "25g"},
            {"nome": "Tomate", "quantidade": "15g"}
        ],
        "dica_da_semana": "Evite lavar folhas verdes antes de guardar. Isso ajuda a preservar por mais tempo."
    }

    return jsonify(data), 200
