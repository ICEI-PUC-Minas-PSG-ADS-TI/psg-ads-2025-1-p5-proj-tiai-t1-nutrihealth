from src import db
from sqlalchemy.dialects.postgresql import ARRAY

cliente_receitas = db.Table(
    'cliente_receitas',
    db.Column('cliente_id', db.Integer, db.ForeignKey('cliente.id'), primary_key=True),
    db.Column('receita_id', db.Integer, db.ForeignKey('receita.id'), primary_key=True)
) 

class Cliente(db.Model):
    __tablename__ = "cliente" 

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    idade = db.Column(db.Int, nullable=False)

    receitas = db.relationship(
        "Receita",
        secondary=cliente_receitas,
        backref="cliente"
    )
