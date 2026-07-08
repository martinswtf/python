from . import db
from .base import ModeloBase


class Sala(ModeloBase):
    __tablename__ = "salas"

    numero = db.Column(db.Integer, nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)
    #  ALUNO: relationship sessoes

    sessoes = db.relationship("Sessao", back_populates="sala", lazy=True)


    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.numero).all()
