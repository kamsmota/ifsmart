from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.user import User
from config import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from controllers.cart_controller import load_cart_from_db , save_cart_to_db
from repository.user_repository import UserRepository
from dao.user_dao import UserDAO

auth_bp = Blueprint('auth', __name__)



# Rota para cadastro de usuários
@auth_bp.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        # Verifica se o nome de usuário já existe
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Nome de usuário já existe. Escolha outro.", "error")
            return redirect(url_for('auth.signup'))

        # Gera o hash da senha
        hashed_password = generate_password_hash(password)

        # Lógica para salvar o usuário no banco de dados
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        load_cart_from_db()
        flash("Cadastro realizado com sucesso! Agora, faça login.", "success")
        return redirect(url_for('auth.login'))

    return render_template('cadastro.html')


# Rota para login de usuários
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verificação do banco de dados
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            # Realiza o login do usuário
            load_cart_from_db()
            #flash('Login realizado com sucesso!', 'success')

            # Verifica se o usuário é admin
            if user.role == 'admin':  # Verifica o papel de administrador
                login_user(user, remember=True)
                return redirect(url_for('item_controller.index'))  # Redireciona para a página de itens se for admin
            else:
                login_user(user, remember=True)
                return redirect(url_for('product_bp.index'))  # Redireciona para a página de produtos se não for admin
            
        else:
            flash("Nome de usuário ou senha inválidos.", "error")

    return render_template('login.html')  # Retorna o formulário de login

# Rota para logout de usuários
@auth_bp.route('/logout')
def logout():
    save_cart_to_db()
    logout_user()  # Remove o usuário da sessão
    flash("Você foi desconectado.", "info")
    return redirect(url_for('auth.login'))
