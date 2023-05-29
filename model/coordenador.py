from flask_restful import fields
from helpers.database import db
from model.professor import Professor

coordenador_fields = {
    'id': fields.Integer,
    'registrodeTrabalho': fields.String
}

class Coordenador(Professor):
    __tablename__ = 'coordenador'
    id = db.Column(db.Integer, db.ForeignKey('professor.id'), primary_key=True)
    registrodeTrabalho = db.Column(db.String, nullable=False)

    instituicao_id = db.Column(db.Integer, db.ForeignKey('instituicao.id'))
    instituicao = db.relationship("Instituicao", backref="coordenadores")

    __mapper_args__ = {
        'polymorphic_identity': 'coordenador'
    }

    def __init__(self, nome, email, senha, telefone, disciplina, registrodeTrabalho, instituicao):
        super().__init__(nome, email, senha, telefone, disciplina)
        self.registrodeTrabalho = registrodeTrabalho
        self.instituicao = instituicao
    
    def __repr__(self):
        return f'<Coordenador {self.registrodeTrabalho}>'