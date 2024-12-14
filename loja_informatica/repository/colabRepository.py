from dao.colabDAO import ColaboradoresDAO
from flask import *
from datetime import datetime
from models.colaboradores import *
from models.ponto import *

class ColaboradoresRepository:
    def __init__(self) -> None:
        self.ColabsDao = ColaboradoresDAO()

    def get_all_colaboradores(self):
        return self.ColabsDao.get_all_colaboradores()


    def create_colaborador(self, nome, email):
        return self.ColabsDao.add_colaborador(nome, email)

    def update_colaborador(self, colaborador_id, nome, email):
        return self.ColabsDao.att_colaborador(colaborador_id, nome, email)

    def delete_colaborador(self, colaborador_id):
        return self.ColabsDao.del_colaborador(colaborador_id)

    #funcao p realmente bater ponto
    def ponto():
        from models.ponto import PontoRegistro
        data = request.json
        colaborador_id = data.get('colaborador_id')
        periodo = data.get('periodo')

        if periodo not in ['entrada_manha', 'saida_manha', 'entrada_tarde', 'saida_tarde']:
            return jsonify({"error": "Período inválido."}), 400

        if not colaborador_id:
            return jsonify({"error": "Colaborador não encontrado."}), 400

        colaborador = next((c for c in Colaboradores if c['id'] == int(colaborador_id)), None)
        if not colaborador:
            return jsonify({"error": "Colaborador não encontrado."}), 404

        dia = datetime.now().date()
        registro = next((c for c in PontoRegistro if c['colaborador_id'] == colaborador_id and c['dia'] == dia), None)

        if not registro:
            registro = {
                'colaborador_id': colaborador_id,
                'dia': dia,
                'entrada_manha': None,
                'saida_manha': None,
                'entrada_tarde': None,
                'saida_tarde': None,
            }
            PontoRegistro.append(registro) #"registro" p nao confundir com a lista "ponto"
        registro[periodo] = get_current_time()
        return jsonify(registro)

    #funcao p pontos do colaborador selecionado pelo id
    def get_ponto(colaborador_id):
        colaborador_pontos = [registro for registro in PontoRegistro if registro['colaborador_id'] == colaborador_id]
    
        if not colaborador_pontos:
            return jsonify({"message": "Nenhum ponto registrado ainda."}), 404

        return jsonify(colaborador_pontos)

