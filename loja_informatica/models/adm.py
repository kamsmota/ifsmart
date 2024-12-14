from config import db
from flask import jsonify

class Administradores(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, nullable=False)
    data_nasci = db.Column(db.Date, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    user = db.Column(db.String(50), nullable=False, unique=True)
    senha = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'{self.nome}, {self.data_nasci}, {self.user}, {self.senha}'

    def toJson(self):
        return {"id": self.id, "nome": self.nome, "user": self.user, "senha": self.senha}


def atualizar_salario(colaborador_id, salario=None):
    from models.colaboradores import Colaboradores
    #att o salário de um colaborador
    colaborador = Colaboradores.query.get(colaborador_id)
    if not colaborador:
        return jsonify({"error": "Colaborador não registrado."}), 404

    if salario is not None:
        colaborador.salario = salario

    db.session.commit()
    return jsonify({"message": f"Dados do colaborador {colaborador.nome} atualizados com sucesso!"})

def listar_todos_pontos():
    from models.ponto import PontoRegistro
    if not PontoRegistro:
        return jsonify({"message": "Nenhum registrado ainda."}), 404
    return jsonify(PontoRegistro)

def cadastrar_colaborador(nome, data_nasci, user, senha, salario=0.0):
        from models.colaboradores import Colaboradores
        novo_colaborador = Colaboradores( #classe importada de colaboradores.py
        nome=nome,
        data_nasci=data_nasci,
        user=user,
        senha=senha,
        salario=salario,
        )
        if not all([nome, data_nasci, user, senha]):
            return jsonify({"error": "Preencha todos os campos obrigatórios."}), 400
        db.session.add(novo_colaborador)
        db.session.commit()
        return jsonify({"message": f"Colaborador {nome} cadastrado com sucesso!"})
