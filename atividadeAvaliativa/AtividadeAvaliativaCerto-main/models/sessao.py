from . import db
from .base import ModeloBase


class Sessao(ModeloBase):
    __tablename__ = "sessoes"

    # TODO ALUNO: FK filme_id → filmes.id
    filme_id = db.Column(db.Integer, db.ForeignKey("filmes.id"), nullable=False)
    
    # TODO ALUNO: FK sala_id → salas.id
    sala_id = db.Column(db.Integer, db.ForeignKey("salas.id"), nullable=False)
    
    data_hora = db.Column(db.DateTime, nullable=False)
    preco = db.Column(db.Float, nullable=False)

    #  ALUNO: relationship filme, sala, ingressos
    filme = db.relationship("Ingresso", back_populates = "sessao")
    filme = db.relationship("Sala", back_populates = "sessao")
    filme = db.relationship("Filme", back_populates = "sessao")

    @classmethod
    def listar_com_detalhes(cls):
        return cls.query.order_by(cls.data_hora.desc()).all()
