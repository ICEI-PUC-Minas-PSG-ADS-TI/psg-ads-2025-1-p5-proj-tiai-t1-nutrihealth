from src import db

receita_ingrediente = db.Table(
    'receita_ingrediente',
    db.Column('receita_id', db.Integer, db.ForeignKey('receita.id'), primary_key=True),
    db.Column('ingrediente_id', db.Integer, db.ForeignKey('ingrediente.id'), primary_key=True)
)

class Receita(db.Model):
    __tablename__ = "receita"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    tempo_preparo = db.Column(db.DateTime, nullable=False)

    ingredientes = db.relationship(
        "Ingrediente", 
        secondary=receita_ingrediente,
        backref="receitas"
    )
