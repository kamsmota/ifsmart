from flask import Flask, redirect, url_for
from config import Config, db
from controllers.product_controller import product_bp
from controllers.auth_controller import auth_bp
from controllers.cart_controller import cart_bp
from controllers.item_controller import item_controller
from flask_login import LoginManager
from models.user import User  

app = Flask(__name__)
app.config.from_object(Config)

# Inicialize o SQLAlchemy com o app
db.init_app(app)

# Inicializa o LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# Função para carregar o usuário
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Retorna o usuário a partir do ID

# Registra os blueprints
app.register_blueprint(cart_bp)
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(item_controller, url_prefix='/items')



@app.route('/')
def home():
    return redirect(url_for('product_bp.index'))  # Direciona para o controller de produtos

if __name__ == "__main__":
    with app.app_context():
        db.metadata.clear()
        db.create_all()
        db.create_all()  # Cria as tabelas no banco de dados
    app.run(debug=True)
