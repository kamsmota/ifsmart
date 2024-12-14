from config import db
from datetime import datetime
from flask import *
from models.adm import Administradores

#cria objeto colaboradores e a tabela de banco de dados com sqlalchemy
class Colaboradores(Administradores):
    __tablename__ = 'colaboradores'
    salario = db.Column(db.Float, nullable=False, default=0.0) # add uma info a mais a classe de adms

    def __repr__(self):
        return f'{self.nome}, {self.data_nasci}, {self.user}, {self.senha}, {self.salario}'

    def toJson(self):
        return {"id": self.id, "nome": self.nome, "user": self.user, "senha": self.senha, "salário": self.salario}



