import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "minha-chave-secreta"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "mysql+pymysql://usuario:Fink061277@localhost/loja_informatica"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


