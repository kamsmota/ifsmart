from dao.colabDAO import ColaboradoresDAO

class ColaboradoresDAORepository:
    def __init__(self) -> None:
        self.ColabsDao = ColaboradoresDAO()

    def get_all_colaboradores(self):
        return self.ColabsDao.get_all_colaboradores()

    def get_colaboradores_by_id(self, colaborador_id):
        return self.ColabsDao.get_colaboradores_by_id(colaborador_id)

    def create_colaborador(self, name, email):
        return self.ColabsDao.create_colaboradores(name, email)

    def update_colaborador(self, colaborador_id, name, email):
        return self.ColabsDao.update_colaboradores(colaborador_id, name, email)

    def delete_colaborador(self, colaborador_id):
        return self.ColabsDao.delete_colaboradores(colaborador_id)