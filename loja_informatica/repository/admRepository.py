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
    
def atualizar_salario(colaborador_id, salario=None):
    from models.colaboradores import Colaboradores
    #att o salário de um colaborador
    colaborador = Colaboradores.query.get(colaborador_id)
    if not colaborador:
        return jsonify({"error": "Colaborador não registrado."}), 404

    if salario is not None:
        colaborador.salario = salario

    db.session.commit()
    return jsonify({"message": f"Dados do colaborador {colaborador.nome} atualizados com sucesso!"})



def cadastrar_colaborador(nome, data_nasci, user, senha, salario=0.0):
        from models.colaboradores import Colaboradores
        novo_colaborador = Colaboradores( #classe importada de colaboradores.py
        nome=nome,
        data_nasci=data_nasci,
        user=user,
        senha=senha,
        salario=salario,
        )
        if not all([nome, data_nasci, user, senha]):
            return jsonify({"error": "Preencha todos os campos obrigatórios."}), 400
        db.session.add(novo_colaborador)
        db.session.commit()
        return jsonify({"message": f"Colaborador {nome} cadastrado com sucesso!"})
