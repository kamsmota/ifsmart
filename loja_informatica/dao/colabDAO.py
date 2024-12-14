from models.colaboradores import*
from config import db

class ColaboradoresDAO:
    @staticmethod
    def get_colaborador(id):
        return Colaboradores.query.get(id)

    @staticmethod
    def get_all_colaboradores():
        return Colaboradores.query.all()

    @staticmethod
    def add_colaborador(nome, email):
        colaborador = colaborador(nome=nome, email=email)
        db.session.add(colaborador)
        db.session.commit()
        return colaborador

    @staticmethod
    def att_colaborador(id, nome, email):
        colaborador = ColaboradoresDAO.get_colaborador(id)
        if colaborador:
            colaborador.nome = nome
            colaborador.email = email
            db.session.commit()
        return colaborador

    @staticmethod
    def del_colaborador(id):
        colaborador = ColaboradoresDAO.get_colaborador(id)
        if colaborador:
            db.session.delete(colaborador)
            db.session.commit()
        return colaborador
