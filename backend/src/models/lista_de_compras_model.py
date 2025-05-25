from src import db

lista_de_compras_ingrediente = db.Table(
    'lista_de_compras_ingrediente',
    db.Column('lista_de_compras.id', db.Integer, db.ForeignKey('lista_de_compras.id'), primary_key=True),
    db.Column('ingrediente_id', db.Integer, db.ForeignKey('ingrediente.id'), primary_key=True)
)

class ListaCompras(db.Model):
    __tablename__ = "lista_de_compras"

    id = db.Column(db.Integer, primary_key=True)
    valor = db.Column(db.Float, nullable=False)

    itens = db.relationship(
        "Ingrediente",
        secondary=lista_de_compras_ingrediente,
        backref="lista_de_compras"
    )
