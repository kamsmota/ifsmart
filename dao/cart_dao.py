# dao/cart_dao.py
from models.cart import Cart
from config import db

class CartDAO:
    @staticmethod
    def get_cart_by_user(user_id):
        return Cart.query.filter_by(user_id=user_id, is_active=True).first()

    @staticmethod
    def create_cart(user_id):
        new_cart = Cart(user_id=user_id)
        db.session.add(new_cart)
        db.session.commit()
        return new_cart

    @staticmethod
    def update_cart(cart):
        db.session.commit()

    @staticmethod
    def remove_cart(cart):
        db.session.delete(cart)
        db.session.commit()
