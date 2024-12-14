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
#lsita vazia p armazenar os pontos
ponto_registro = []

colaboradores = Colaboradores.query.all()

#funcao p pegar o tempo atual e o criar como objeto time
def get_current_time():
    return datetime.now().time()

#funcao p realmente bater ponto
def ponto():
    data = request.json
    colaborador_id = data.get('colaborador_id')
    periodo = data.get('periodo')

    if periodo not in ['entrada_manha', 'saida_manha', 'entrada_tarde', 'saida_tarde']:
        return jsonify({"error": "Período inválido."}), 400

    if not colaborador_id:
        return jsonify({"error": "Colaborador não encontrado."}), 400

    colaborador = next((c for c in colaboradores if c['id'] == int(colaborador_id)), None)
    if not colaborador:
        return jsonify({"error": "Colaborador não encontrado."}), 404

    dia = datetime.now().date()
    registro = next((c for c in ponto if c['colaborador_id'] == colaborador_id and c['dia'] == dia), None)

    if not registro:
        registro = {
            'colaborador_id': colaborador_id,
            'dia': dia,
            'entrada_manha': None,
            'saida_manha': None,
            'entrada_tarde': None,
            'saida_tarde': None,
        }
        ponto_registro.append(registro) #"registro" p nao confundir com a lista "ponto"

    registro[periodo] = get_current_time()
    return jsonify(registro)

#funcao p pontos do colaborador selecionado pelo id
def get_ponto(colaborador_id):
    colaborador_pontos = [registro for registro in ponto_registro if registro['colaborador_id'] == colaborador_id]
    
    if not colaborador_pontos:
        return jsonify({"message": "Nenhum ponto registrado ainda."}), 404

    return jsonify(colaborador_pontos)

