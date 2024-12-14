from models.colaboradores import*
from config import db

class ColaboradoresDAO:
    @staticmethod
    def get_colaborador(id):
        return colaboradores.query.get(id)

    @staticmethod
    def get_all_colaboradores():
        return colaboradores.query.all()

    @staticmethod
    def add_colaborador(name, email):
        colaborador = colaborador(name=name, email=email)
        db.session.add(colaborador)
        db.session.commit()
        return colaborador

    @staticmethod
    def att_colaborador(id, name, email):
        colaborador = ColaboradoresDAO.get_colaborador(id)
        if colaborador:
            colaborador.name = name
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