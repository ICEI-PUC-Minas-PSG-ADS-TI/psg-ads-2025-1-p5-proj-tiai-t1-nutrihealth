from .. import db

class Venda(db.Model):
    __tablename__ = "vendas" 

    id = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)

    user = db.relationship("User", backref="vendas")
