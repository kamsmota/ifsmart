# dao/cart_item_dao.py
from models.cart_item import CartItem
from config import db

class CartItemDAO:
    @staticmethod
    def get_item(cart_id, product_id):
        return CartItem.query.filter_by(cart_id=cart_id, product_id=product_id).first()

    @staticmethod
    def create_item(cart_id, product_id, title, price, quantity):
        new_item = CartItem(cart_id=cart_id, product_id=product_id, title=title, price=price, quantity=quantity)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @staticmethod
    def update_item(item):
        db.session.commit()

    @staticmethod
    def remove_item(cart_id, product_id):
        item_to_remove = CartItem.query.filter_by(cart_id=cart_id, product_id=product_id).first()
        if item_to_remove:
            db.session.delete(item_to_remove)
            db.session.commit()
            return True
        return False
