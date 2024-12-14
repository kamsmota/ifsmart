# models/cart.py
from config import db  # db é a instância do SQLAlchemy configurada em outro lugar
from sqlalchemy.orm import relationship

class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Relacionamento com a tabela User
    is_active = db.Column(db.Boolean, default=True)

    # Relacionamento com o modelo User
    user = relationship('User', back_populates='carts')
    items = db.relationship('CartItem', backref='cart', lazy=True)
    def __init__(self, user=None,user_id=user_id):
        self.user = user
        self.user_id = user_id
  
 
        
