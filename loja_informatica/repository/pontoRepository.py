from datetime import datetime
from flask import jsonify

def get_current_time():
    return datetime.now().time()





def listar_todos_pontos():
    from models.ponto import PontoRegistro
    # Busca todos os registros do banco de dados
    registros = PontoRegistro.query.all()

    if not registros:
        return jsonify({"message": "Nenhum registro encontrado ainda."}), 404

    # Converte cada registro para dicionário
    registros_json = [registro.to_dict() for registro in registros]

    return jsonify(registros_json)