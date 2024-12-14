# models/product.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)  # Nome do produto
    price = db.Column(db.Float, nullable=False)  # Preço do produto
    description = db.Column(db.String(500))  # Descrição do produto (opcional)
    permalink = db.Column(db.String(255), nullable=False)  # Link do produto
    thumbnail = db.Column(db.String(255))  # Imagem do produto (opcional)


    def __repr__(self):
        return f'<Product {self.title}>'
