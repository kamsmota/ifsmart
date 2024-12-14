from models.adm import*
from config import db

class AdministradoresDAO:
    @staticmethod
    def get_adm(id):
        return adms.query.get(id)

    @staticmethod
    def get_all_adms():
        return adms.query.all()

    @staticmethod
    def add_adm(name, email):
        adm = adm(name=name, email=email)
        db.session.add(adm)
        db.session.commit()
        return adm

    @staticmethod
    def att_adm(id, name, email):
        adm = AdministradoresDAO.get_adm(id)
        if adm:
            adm.name = name
            adm.email = email
            db.session.commit()
        return adm

    @staticmethod
    def del_adm(id):
        adm = AdministradoresDAO.get_adm(id)
        if adm:
            db.session.delete(adm)
            db.session.commit()
        return adm