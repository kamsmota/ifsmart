from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin  
from models.cart import Cart  
from config import *
from sqlalchemy.orm import relationship



class User(db.Model, UserMixin):  # Herdando de UserMixin
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_cart_active = db.Column(db.Boolean, default=True)  
    carts = relationship('Cart', back_populates='user')
    role = db.Column(db.String(50), default='user')
    def __repr__(self):
        return f'<User {self.username}>'

    def set_password(self, password):
        self.password = generate_password_hash(password)  # Salva o hash da senha

    def check_password(self, password):
        return check_password_hash(self.password, password)  # Verifica o hash da senha

    def get_id(self):
        return str(self.id)  # Retorna o ID do usuário como uma string

    # Não sobrescrever o método is_active do UserMixin
    # Caso queira um comportamento customizado, utilize um outro nome de método para lógica adicional

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
