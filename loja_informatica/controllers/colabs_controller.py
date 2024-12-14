from flask import *
from models.colaboradores import *
from repository.colabRepository import get_ponto, ponto


colabsController = Blueprint("colaboradores", __name__)

# pagina inicial de colaboradores
@colabsController.route('/')
def mostrar_homepage_colabs():
    return render_template("colabs_painel.html")

#registro de pontos
@colabsController.route('/espelhodeponto', methods=['POST'])
def registrar_ponto():
    return ponto()

#obter pontos ja registrados
@colabsController.route('/obter_pontos/<int:colaborador_id>', methods=['GET'])
def obter_ponto(colaborador_id):
    return get_ponto(colaborador_id)

