from flask import Blueprint, render_template
from repository.admRepository import atualizar_salario, cadastrar_colaborador
from repository.pontoRepository import listar_todos_pontos
from models.ponto import *

admController = Blueprint("adm", __name__)

# pagina inicial de adms
@admController.route('/')
def mostrar_homepage_adm():
    return render_template("admin_painel.html")

# listar todos os pontos dos colaboradores
@admController.route('/pontos', methods=['GET'])
def listar_pontos():
    return listar_todos_pontos()


# cadastrar um novo colaborador
@admController.route('/novocolaborador', methods=['POST'])
def adicionar_colaborador():
    return cadastrar_colaborador()

# atualizar salário de um colaborador
@admController.route('/<int:colaborador_id>', methods=['GET','PUT'])
def att_salary():
    return atualizar_salario()
