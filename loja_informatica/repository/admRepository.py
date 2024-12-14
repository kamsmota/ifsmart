from dao.admDAO import AdministradoresDAO
from config import db
from flask import *

class AdministradoresRepository:
    def __init__(self) -> None:
        self.AdmsDao = AdministradoresDAO()

    def get_all_adms(self):
        return self.AdmsDao.get_all_adms()

    def create_adm(self, name, email):
        return self.AdmsDao.add_adm(name, email)

    def update_adm(self, adm_id, name, email):
        return self.AdmsDao.att_adm(adm_id, name, email)

    def delete_adm(self, adm_id):
        return self.AdmsDao.del_adm(adm_id)
