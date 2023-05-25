from flask_restful import fields
from helpers.database import db

periodo_fields = {
    'id': fields.Integer,
    'semestrereferencia': fields.String
}

class Periodo(db.Model):
    __tablename__ = "periodo"

    id = db.Column(db.Integer, primary_key=True)
    semestrereferencia = db.Column(db.String, nullable=False)

    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'))
    aluno = db.relationship("Aluno", backref="periodo")

    def __init__(self, semestrereferencia):
        self.semestrereferencia = semestrereferencia

    def __repr__(self):
        return f'<Periodo {self.semestrereferencia}>'
