# routes/dashboard_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from src import db
from src.models.dashboard_model import Dashboard
from datetime import datetime
import json

dashboard_bp = Blueprint("dashboard_bp", __name__)

@dashboard_bp.route("/dashboard", methods=["POST"])
@jwt_required()
def save_dashboard():
    current_user_id = get_jwt_identity()
    data = request.get_json()

    try:
        dashboard = Dashboard(
            usuario_id=current_user_id,
            mes=data.get("mes", datetime.now().strftime("%m-%Y")),
            total_refeicoes=data.get("total_refeicoes"),
            media_calorias_dia=data.get("media_calorias_dia"),
            alimento_mais_usado=data.get("alimento_mais_usado"),
            desperdicio_alimentar=data.get("desperdicio_alimentar"),
            co2_salvo=data.get("co2_salvo"),
            itens_mais_desperdicados=json.dumps(data.get("itens_mais_desperdicados", [])),  
            dica_do_mes=data.get("dica_do_mes")
        )
        db.session.add(dashboard)
        db.session.commit()
        return jsonify({"message": "Dashboard salvo com sucesso"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@dashboard_bp.route("/dashboard", methods=["GET"])
@jwt_required()
def get_dashboard():
    current_user_id = get_jwt_identity()
    mes = request.args.get("mes", datetime.now().strftime("%m-%Y"))

    dashboard = Dashboard.query.filter_by(usuario_id=current_user_id, mes=mes).first()
    if not dashboard:
        return jsonify({"message": "Nenhum dashboard encontrado para este mês"}), 404

    return jsonify({
        "usuario_id": dashboard.usuario_id,
        "mes": dashboard.mes,
        "total_refeicoes": dashboard.total_refeicoes,
        "media_calorias_dia": dashboard.media_calorias_dia,
        "alimento_mais_usado": dashboard.alimento_mais_usado,
        "desperdicio_alimentar": dashboard.desperdicio_alimentar,
        "co2_salvo": dashboard.co2_salvo,
        "itens_mais_desperdicados": json.loads(dashboard.itens_mais_desperdicados),
        "dica_do_mes": dashboard.dica_do_mes
    }), 200
