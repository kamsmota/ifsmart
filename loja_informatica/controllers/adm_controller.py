from flask import Blueprint, request, render_template, jsonify
from models.adm import listar_todos_pontos, cadastrar_colaborador, atualizar_salario_ferias
from models.colaboradores import ponto

admController = Blueprint("adm", __name__)

# rota p página inicial de administradores
@admController.route('/')
def mostrar_homepage_adm():
    return render_template("admin_painel.html")

# listar todos os pontos dos colaboradores
@admController.route('/pontos', methods=['GET'])
def listar_pontos():
    return listar_todos_pontos()

# cadastro de um novo colaborador
@admController.route('/colaboradores', methods=['POST'])
def adicionar_colaborador():
    data = request.json
    nome = data.get("nome")
    data_nasci = data.get("data_nasci")
    user = data.get("user")
    senha = data.get("senha")
    salario = data.get("salario", 0.0)

    if not all([nome, data_nasci, user, senha]):
        return jsonify({"error": "Preencha todos os campos obrigatórios."}), 400

    return cadastrar_colaborador(nome, data_nasci, user, senha, salario)

# att salário de um colaborador
@admController.route('/colaboradores/<int:colaborador_id>', methods=['PUT'])
def atualizar_dados_colaborador(colaborador_id):
    data = request.json
    salario = data.get("salario")

    if salario is None:
        return jsonify({"error": "Selecione o campo para atualização."}), 400

    return atualizar_salario_ferias(colaborador_id, salario=salario)
