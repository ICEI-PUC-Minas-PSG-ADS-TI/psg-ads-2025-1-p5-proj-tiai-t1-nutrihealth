from src import db

nutricionista_cliente = db.Table(
    'nutricionista_cliente',
    db.Column('nutricionista.id', db.Integer, db.ForeignKey('nutricionista.id'), primary_key=True),
    db.Column('cliente_id', db.Integer, db.ForeignKey('cliente.id'), primary_key=True)
)

class Nutricionista(db.Model):
    __tablename__ = "nutricionista"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)

    itens = db.relationship(
        "Cliente",
        secondary=nutricionista_cliente,
        backref="nutricionista"
    )
