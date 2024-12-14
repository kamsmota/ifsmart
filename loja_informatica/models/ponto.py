from config import db
from datetime import datetime


class PontoRegistro:
    __tablename__ = 'registro de ponto'
    colaborador_id = db.Column(db.Integer, primary_key=True, nullable = True)
    data = db.Column(db.DateTime, nullable=False)
    periodo = db.Column(db.String(10), nullable=False)
     
#funcao p pegar o tempo atual e o criar como objeto time
def get_current_time():
    return datetime.now().time()
