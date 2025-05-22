from flask import Blueprint, request, jsonify
from app.services.user_service import add_user, list_users
from app.schemas.user_schema import UserSchema

user_bp = Blueprint('user_bp', __name__)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

@user_bp.route("/", methods=["GET"])
def get_users():
    users = list_users()
    return jsonify(users_schema.dump(users))

@user_bp.route("/", methods=["POST"])
def create_user():
    data = request.json
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    user = add_user(data)
    return jsonify(user_schema.dump(user)), 201
