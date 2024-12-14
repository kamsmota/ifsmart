from flask import Blueprint, render_template, request, redirect, url_for
from config import db
from models.item import Item
from repository.item_repository import ItemRepository

item_controller = Blueprint('item_controller', __name__)

# Página principal que exibe todos os itens
@item_controller.route('/')
def index():
    items = ItemRepository.get_all_items()  # Recupera todos os itens do banco de dados
    return render_template('index.html', items=items)

# Rota para adicionar um novo item
@item_controller.route('/add', methods=['POST'])
def add_item():
    # Pegando os dados do formulário corretamente
    campo1 = request.form.get('campo1')
    campo2 = request.form.get('campo2')
    campo3 = request.form.get('campo3')
    campo4 = request.form.get('campo4')
    
    # Passando os dados para o repositório
    ItemRepository.add_item(campo1, campo2, campo3, campo4)
    return redirect(url_for('item_controller.index'))

# Rota para editar um item
@item_controller.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = Item.query.get(item_id)  # Recupera o item pelo ID
    if request.method == 'POST':
        campo1 = request.form.get('campo1')
        campo2 = request.form.get('campo2')
        campo3 = request.form.get('campo3')
        campo4 = request.form.get('campo4')
        db.session.commit()  # Comita as alterações no banco
        ItemRepository.update_item(item_id, campo1, campo2, campo3, campo4)
        return redirect(url_for('item_controller.index'))
    return render_template('edit.html', item=item)

# Rota para excluir um item
@item_controller.route('/delete/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get(item_id)  # Recupera o item a ser deletado
    db.session.delete(item)  # Marca o item para exclusão
    db.session.commit()  # Comita a exclusão no banco
    ItemRepository.delete_item(item_id)
    return redirect(url_for('item_controller.index'))


