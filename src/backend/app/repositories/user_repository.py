from app import db
from app.models.user import Test_User
from ..models.usuario import Usuario

def create_user(name, email):
    user = Test_User(name=name, email=email)
    db.session.add(user)
    db.session.commit()
    return user

def get_all_users():
    return Test_User.query.all()
