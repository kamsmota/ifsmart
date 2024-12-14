from dao.admDAO import AdministradoresDAO

class AdministradoresRepository:
    def __init__(self) -> None:
        self.AdmsDao = AdministradoresDAO()

    def get_all_adms(self):
        return self.AdmsDao.get_all_adms()

    def get_adms_by_id(self, adm_id):
        return self.AdmsDao.get_adms_by_id(adm_id)

    def create_adm(self, name, email):
        return self.AdmsDao.create_adms(name, email)

    def update_adm(self, adm_id, name, email):
        return self.AdmsDao.update_adms(adm_id, name, email)

    def delete_adm(self, adm_id):
        return self.AdmsDao.delete_adms(adm_id)