from models.adm import*
from config import db

class AdministradoresDAO:
    @staticmethod
    def get_adm(id):
        return Administradores.query.get(id)

    @staticmethod
    def get_all_adms():
        return Administradores.query.all()

    @staticmethod
    def add_adm(nome, email):
        adm = adm(nome=nome, email=email)
        db.session.add(adm)
        db.session.commit()
        return adm

    @staticmethod
    def att_adm(id, nome, user):
        adm = AdministradoresDAO.get_adm(id)
        if adm:
            Administradores.nome = nome
            Administradores.user = user
            db.session.commit()
        return adm

    @staticmethod
    def del_adm(id):
        adm = AdministradoresDAO.get_adm(id)
        if adm:
            db.session.delete(adm)
            db.session.commit()
        return adm
