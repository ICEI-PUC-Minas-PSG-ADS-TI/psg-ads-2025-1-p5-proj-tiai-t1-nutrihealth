from .. import db
from datetime import date
from enum import Enum

class DiaSemanaEnum(Enum):
    Segunda = "Segunda"
    Terca = "Terça"
    Quarta = "Quarta"
    Quinta = "Quinta"
    Sexta = "Sexta"
    Sabado = "Sábado"
    Domingo = "Domingo"

class TipoRefeicaoEnum(Enum):
    Cafe = "Café da manhã"
    Almoco = "Almoço"
    Jantar = "Jantar"

class PlanejamentoSemanal(db.Model):
    __tablename__ = "planejamento_semanal"

    id = db.Column(db.Integer, primary_key=True)
    dia_semana = db.Column(db.Enum(DiaSemanaEnum), nullable=False)
    tipo_refeicao = db.Column(db.Enum(TipoRefeicaoEnum), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    receita_id = db.Column(db.Integer, db.ForeignKey("receita.id"), nullable=False)

    user = db.relationship("User", backref="planejamentos")
    receita = db.relationship("Receita")
