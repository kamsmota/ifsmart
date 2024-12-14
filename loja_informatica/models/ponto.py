from config import *
from datetime import datetime

class PontoRegistro(db.Model):  # A classe herda de db.Model
    __tablename__ = 'registro_de_ponto'  # Nome da tabela no banco de dados

    colaborador_id = db.Column(db.Integer, primary_key=True)  # Coluna da chave primária
    data = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # Data com valor padrão
    periodo = db.Column(db.String(10), nullable=False)  # Coluna para período

    # Método para converter o objeto em um dicionário JSON serializável
    def to_dict(self):
        return {
            "colaborador_id": self.colaborador_id,
            "data": self.data.strftime("%Y-%m-%d %H:%M:%S"),
            "periodo": self.periodo
        }

def get_current_time():
    return datetime.now().time()
