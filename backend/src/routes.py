from flask import request, jsonify
from . import db
from .models import User
from flask import current_app as app

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(name=data["name"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "name": user.name}), 201

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

@app.route("/test", methods=["GET"])
def test():
    return jsonify([{"message": "esta funcionando"}])
