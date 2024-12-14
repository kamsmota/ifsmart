from datetime import datetime
from flask import jsonify

def get_current_time():
    return datetime.now().time()

def listar_todos_pontos():
    from models.ponto import PontoRegistro
    if not PontoRegistro:
        return jsonify({"message": "Nenhum registrado ainda."}), 404
    return jsonify(PontoRegistro)
