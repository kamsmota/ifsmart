from config import db
from datetime import datetime
from flask import *
from models.adm import Administradores

#cria objeto colaboradores e a tabela de banco de dados com sqlalchemy
class Colaboradores(Administradores):
    __tablename__ = 'colaboradores'
    salário = db.Column(db.Float, nullable=False, default=0.0) # add uma info a mais a classe de adms


#lsita vazia p armazenar os pontos
ponto = []

colaboradores =[]

#funcao p pegar o tempo atual e o criar como objeto time
def get_current_time():
    return datetime.now().time()

#funcao p realmente bater ponto
def ponto():
    data = request.json
    colaborador_id = data.get('colaborador_id')
    periodo = data.get('periodo')

    if not colaborador_id or not periodo:
        return jsonify({"error": "Dados incompletos."}), 400

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
        ponto.append(registro) #"registro" p nao confundir com a lista "ponto"

    registro[periodo] = get_current_time()
    return jsonify(registro)

def get_ponto():
    return jsonify(ponto)
