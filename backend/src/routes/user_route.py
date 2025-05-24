from flask import Blueprint, request, jsonify
from .. import db
from ..models.user_model import User

user_bp = Blueprint("user_bp", __name__)

@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(name=data["name"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "name": user.name}), 201

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

@user_bp.route("/test", methods=["GET"])
def test():
    return jsonify([{"message": "esta funcionando"}])
