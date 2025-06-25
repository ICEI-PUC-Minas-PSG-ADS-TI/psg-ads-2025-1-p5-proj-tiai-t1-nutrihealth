from src import db
from src.models.user_model import User

class Ingrediente(db.Model):
    __tablename__ = "ingrediente"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), nullable=False)
    quantidade = db.Column(db.Float, nullable=False)
    unidade_de_medida = db.Column("unidade de medida", db.String(20), nullable=False)
    impacto_ambiental = db.Column("impacto ambiental", db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    user = db.relationship('User', backref='ingredientes')
