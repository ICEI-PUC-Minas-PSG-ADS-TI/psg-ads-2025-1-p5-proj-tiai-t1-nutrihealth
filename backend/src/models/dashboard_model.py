# models/dashboard_model.py

from src import db

class Dashboard(db.Model):
    __tablename__ = 'dashboard'

    id_dashboard = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    mes = db.Column(db.String(10), nullable=False)
    total_refeicoes = db.Column(db.Integer)
    media_calorias_dia = db.Column(db.Float)
    alimento_mais_usado = db.Column(db.String(100))
    desperdicio_alimentar = db.Column(db.String(20))
    co2_salvo = db.Column(db.String(20))
    itens_mais_desperdicados = db.Column(db.Text)
    dica_do_mes = db.Column(db.Text)

    user = db.relationship("User", backref="dashboards")
