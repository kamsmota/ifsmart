from config import db
from flask import jsonify
from datetime import datetime
from models.colaboradores import Colaboradores

# Modelo Administradores
class Administradores(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    data_nasci = db.Column(db.Date, nullable=False)
    user = db.Column(db.String(50), nullable=False, unique=True)
    senha = db.Column(db.Text, nullable=False)

# Funções relacionadas aos administradores

# Função para listar todos os pontos de colaboradores
def listar_todos_pontos(pontos):
    return jsonify({"pontos": pontos})

# Função para cadastrar um novo colaborador
def cadastrar_colaborador(nome, data_nasci, user, senha, salario=0.0):
    novo_colaborador = Colaboradores(
        nome=nome,
        data_nasci=data_nasci,
        user=user,
        senha=senha,
        salario=salario,
    )
    db.session.add(novo_colaborador)
    db.session.commit()
    return jsonify({"message": f"Colaborador {nome} cadastrado com sucesso!"})

# Função para registrar salário ou férias de um colaborador
def atualizar_salario_ferias(colaborador_id, salario=None, ferias=None):
    """Atualiza o salário ou status de férias de um colaborador."""
    colaborador = Colaboradores.query.get(colaborador_id)
    if not colaborador:
        return jsonify({"error": "Colaborador não encontrado."}), 404

    if salario is not None:
        colaborador.salario = salario

    if ferias is not None:
        colaborador.ferias = ferias

    db.session.commit()
    return jsonify({"message": f"Dados do colaborador {colaborador.nome} atualizados com sucesso!"})
