from flask import Blueprint, render_template, session, request, redirect, url_for, flash
import requests
from flask_login import current_user
from models.cart import Cart
from models.cart_item import CartItem
from config import db


cart_bp = Blueprint('cart_bp', __name__)

MERCADO_LIVRE_API_BASE = "https://api.mercadolivre.com"

# Função para adicionar produto ao carrinho
@cart_bp.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
    if 'user_id' not in session:
        flash("Você precisa estar logado para adicionar produtos ao carrinho.", "error")
        return redirect(url_for('auth.login'))

    # Verifica se o produto já existe no carrinho
    cart = session.get('cart', [])

    # Faz a requisição para obter os detalhes do produto
    response = requests.get(f"{MERCADO_LIVRE_API_BASE}/items/{product_id}")
    if response.status_code == 200:
        product_data = response.json()

        # Verifica se o produto já está no carrinho
        existing_product = next((item for item in cart if item["id"] == product_data["id"]), None)

        if existing_product:
            # Se o produto já estiver no carrinho, aumente a quantidade
            existing_product["quantity"] += 1
        else:
            # Caso contrário, adicione o produto com a quantidade 1
            product = {
                "id": product_data["id"],
                "title": product_data["title"],
                "price": product_data["price"],
                "permalink": product_data["permalink"],
                "thumbnail": product_data.get("thumbnail", ""),
                "quantity": 1  # Inicializa a quantidade como 1
            }
            cart.append(product)

        # Atualiza o carrinho na sessão
        session['cart'] = cart
        flash("Produto adicionado ao carrinho!", "success")
    else:
        flash("Erro ao carregar os detalhes do produto.", "error")

    return redirect(url_for('product_bp.index'))

# Função para exibir o carrinho de compras
@cart_bp.route('/cart')
def view_cart():
    if 'user_id' not in session:
        flash("Você precisa estar logado para ver seu carrinho.", "error")
        return redirect(url_for('auth.login'))

    # Obtém o carrinho da sessão
    cart = session.get('cart', [])

    if not cart:
        flash("Seu carrinho está vazio.", "info")

    return render_template('cart.html', cart=cart)

# Função para remover um produto do carrinho
@cart_bp.route('/remove_from_cart/<product_id>')
def remove_from_cart(product_id):
    if 'user_id' not in session:
        flash("Você precisa estar logado para remover produtos do carrinho.", "error")
        return redirect(url_for('auth.login'))

    # Obtém o carrinho da sessão
    cart = session.get('cart', [])
    cart = [product for product in cart if product["id"] != product_id]  # Remove o produto do carrinho
    session['cart'] = cart  # Atualiza o carrinho na sessão
    remove_item_from_db(product_id)
    print("foi")
    flash("Produto removido do carrinho!", "success")
    return redirect(url_for('cart_bp.view_cart'))

# Função para aumentar a quantidade de um produto no carrinho
@cart_bp.route('/increase_quantity/<product_id>')
def increase_quantity(product_id):
    if 'user_id' not in session:
        flash("Você precisa estar logado para alterar a quantidade.", "error")
        return redirect(url_for('auth.login'))

    cart = session.get('cart', [])
    product = next((item for item in cart if item['id'] == product_id), None)
    
    if product:
        product['quantity'] += 1
        session['cart'] = cart
        flash("Quantidade aumentada!", "success")
    else:
        flash("Produto não encontrado no carrinho.", "error")
    
    return redirect(url_for('cart_bp.view_cart'))

# Função para diminuir a quantidade do produto no carrinho
@cart_bp.route('/decrease_quantity/<product_id>')
def decrease_quantity(product_id):
    if 'user_id' not in session:
        flash("Você precisa estar logado para alterar a quantidade.", "error")
        return redirect(url_for('auth.login'))

    cart = session.get('cart', [])
    product = next((item for item in cart if item['id'] == product_id), None)
    
    if product:
        if product['quantity'] > 1:
            product['quantity'] -= 1
            session['cart'] = cart
            flash("Quantidade diminuída!", "success")
        else:
            flash("A quantidade não pode ser menor que 1.", "error")
    else:
        flash("Produto não encontrado no carrinho.", "error")
    
    return redirect(url_for('cart_bp.view_cart'))


def save_cart_to_db():
    if current_user.is_authenticated:
        # Verifica se já existe um carrinho ativo
        user_cart = Cart.query.filter_by(user_id=current_user.id, is_active=True).first()
        
        if not user_cart:
            # Se não houver um carrinho ativo, cria um novo carrinho
            user_cart = Cart(user_id=current_user.id)
            db.session.add(user_cart)
            db.session.commit()

        # Obtém o carrinho da sessão
        cart = session.get('cart', [])

        # Salva ou atualiza os itens do carrinho no banco de dados
        for item in cart:
            existing_item = CartItem.query.filter_by(cart_id=user_cart.id, product_id=item['id']).first()
            if existing_item:
                existing_item.quantity += item['quantity']
            else:
                new_item = CartItem(
                    cart_id=user_cart.id,
                    product_id=item['id'],
                    title=item['title'],
                    price=item['price'],
                    quantity=item['quantity']
                )
                db.session.add(new_item)

        db.session.commit()

        # Limpa o carrinho da sessão após salvar
        session.pop('cart', None)

        flash("Carrinho salvo no banco de dados!", "success")
    else:
        flash("Você precisa estar logado para salvar seu carrinho.", "error")

    return redirect(url_for('cart_bp.view_cart'))



def load_cart_from_db():
    if current_user.is_authenticated:
        print("TOVIVO")
        # Tenta recuperar o carrinho ativo do banco de dados
        user_cart = Cart.query.filter_by(user_id=current_user.id, is_active=True).first()
        
        if user_cart:
            # Se o carrinho existir no banco, adiciona os itens ao carrinho da sessão
            cart = []
            for item in user_cart.items:
                cart.append({
                    'id': item.product_id,
                    'title': item.title,
                    'price': item.price,
                    'quantity': item.quantity,
                    'thumbnail': item.thumbnail  # Adicione o thumbnail, se necessário
                })
            session['cart'] = cart


def remove_item_from_db(product_id):
    if current_user.is_authenticated:
        # Verifica se o carrinho ativo existe no banco
        user_cart = Cart.query.filter_by(user_id=current_user.id, is_active=True).first()

        if user_cart:
            # Remove o item do banco de dados
            item_to_remove = CartItem.query.filter_by(cart_id=user_cart.id, product_id=product_id).first()
            if item_to_remove:
                db.session.delete(item_to_remove)  # Remove o item
                db.session.commit()
                flash("Produto removido do banco de dados.", "success")
            else:
                flash("Produto não encontrado no carrinho no banco de dados.", "error")
        else:
            flash("Carrinho não encontrado no banco de dados.", "error")
    else:
        flash("Você precisa estar logado para remover um produto.", "error")