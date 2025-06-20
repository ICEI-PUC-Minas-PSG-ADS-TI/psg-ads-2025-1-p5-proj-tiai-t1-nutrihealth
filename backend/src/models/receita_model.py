from src import db

receita_ingrediente = db.Table(
    'receita_ingrediente',
    db.Column('receita_id', db.Integer, db.ForeignKey('receita.id'), primary_key=True),
    db.Column('ingrediente_id', db.Integer, db.ForeignKey('ingrediente.id'), primary_key=True)
)

receitas_salvas = db.Table(
    'receitas_salvas',
    db.Column('user_id', db.Integer, db.ForeignKey('usuarios.id'), primary_key=True),
    db.Column('receita_id', db.Integer, db.ForeignKey('receita.id'), primary_key=True)
)

class Receita(db.Model):
    __tablename__ = "receita"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(120), nullable=False)
    tempo_preparo = db.Column(db.DateTime, nullable=False)
    impacto_ambiental = db.Column(db.String(50), nullable=False)
    modo_preparo = db.Column(db.String(120), nullable=False)
    tipo_dieta = db.Column(db.String(50), nullable=False)
    tipo_refeicao = db.Column(db.String(50), nullable=False)
    estilo_preparo = db.Column(db.String(50), nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    user = db.relationship("User", backref="receitas_criadas") 

    ingredientes = db.relationship(
        "Ingrediente", 
        secondary=receita_ingrediente,
        backref="receitas"
    )
