from .. import db

class User(db.Model):
    __tablename__ = "usuarios" 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column("nome_completo", db.String(80), nullable=False) 

