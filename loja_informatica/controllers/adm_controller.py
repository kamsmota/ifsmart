from flask import Blueprint, request, render_template, jsonify
from models.adm import listar_todos_pontos, cadastrar_colaborador, atualizar_salario
from models.colaboradores import ponto
from models.adm import *

admController = Blueprint("adm", __name__)

# pagina inicial de adms
@admController.route('/')
def mostrar_homepage_adm():
    return render_template("admin_painel.html")

# listar todos os pontos dos colaboradores
@admController.route('/pontos', methods=['GET'])
def listar_pontos():
    return render_template("admin_painel.html", pontos_registro=ponto_registro)


# cadastrar um novo colaborador
@admController.route('/novocolaborador', methods=['POST'])
def adicionar_colaborador():
    return cadastrar_colaborador()

# atualizar salário de um colaborador
@admController.route('/<int:colaborador_id>', methods=['GET','PUT'])
def att_salary():
    return atualizar_salario()