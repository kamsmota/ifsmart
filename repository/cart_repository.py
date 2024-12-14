# repository/cart_repository.py
from dao.cart_dao import CartDAO
from dao.cart_item_dao import CartItemDAO
from flask import session, flash
from flask_login import current_user

class CartRepository:
    @staticmethod
    def get_cart_for_user(user_id):
        return CartDAO.get_cart_by_user(user_id)

    @staticmethod
    def create_new_cart_for_user(user_id):
        return CartDAO.create_cart(user_id)

    @staticmethod
    def save_item_in_cart(cart_id, product_id, title, price, quantity):
        # Verifica se o item já existe no carrinho
        existing_item = CartItemDAO.get_item(cart_id, product_id)
        if existing_item:
            # Se o item já existe, aumenta a quantidade
            existing_item.quantity += quantity
            CartItemDAO.update_item(existing_item)
        else:
            # Caso contrário, cria um novo item
            CartItemDAO.create_item(cart_id, product_id, title, price, quantity)

    @staticmethod
    def remove_item_from_cart(cart_id, product_id):
        # Remove item do carrinho
        return CartItemDAO.remove_item(cart_id, product_id)

    @staticmethod
    def load_cart_from_db():
        if current_user.is_authenticated:
            user_cart = CartRepository.get_cart_for_user(current_user.id)
            if user_cart:
                # Se o carrinho existe, carregue os itens
                cart_items = []
                for item in user_cart.items:
                    cart_items.append({
                        'id': item.product_id,
                        'title': item.title,
                        'price': item.price,
                        'quantity': item.quantity,
                        'thumbnail': item.thumbnail
                    })
                session['cart'] = cart_items
