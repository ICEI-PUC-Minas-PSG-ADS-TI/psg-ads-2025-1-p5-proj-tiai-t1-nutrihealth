from .. import db
from werkzeug.security import generate_password_hash, check_password_hash
from .receita_model import receitas_salvas
from sqlalchemy import Enum

class User(db.Model):
    __tablename__ = "usuarios" 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("nome_completo", db.String(80), nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    tipo = db.Column(Enum('Cliente', 'Nutricionista', name='user_type'), nullable=False) 


    receitas_salvas = db.relationship(
        "Receita",
        secondary=receitas_salvas,
        backref="usuarios_que_salvaram"
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
