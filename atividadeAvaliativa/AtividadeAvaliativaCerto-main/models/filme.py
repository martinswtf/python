from . import db
from .base import ModeloBase


class Filme(ModeloBase):
    __tablename__ = "filmes"

    #  ALUNO: duracao_min (Integer), classificacao (String 5)
    titulo = db.Column(db.String(150), nullable=False)
    duracao_min = db.column(db.Integer, nullable = False)
    classificacao= db.column(db.String(5), nullable = False)

    #  ALUNO: relationship sessoes
    filme = db.relationship("Sessao", back_populates = "filme")

    @classmethod
    def listar(cls):
        return cls.query.order_by(cls.titulo).all()
