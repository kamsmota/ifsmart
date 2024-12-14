from flask import Blueprint, render_template, request, redirect, url_for
from config import db
from models.item import Item

item_controller = Blueprint('item_controller', __name__)

# Página principal que exibe todos os itens
@item_controller.route('/')
def index():
    items = Item.query.all()  # Recupera todos os itens do banco de dados
    return render_template('index.html', items=items)

# Rota para adicionar um novo item
@item_controller.route('/add', methods=['POST'])
def add_item():
    new_item = Item(
        campo1=request.form['campo1'],
        campo2=request.form['campo2'],
        campo3=request.form['campo3'],
        campo4=request.form['campo4']
    )
    db.session.add(new_item)  # Adiciona o novo item à sessão
    db.session.commit()  # Comita a sessão para persistir no banco
    return redirect(url_for('item_controller.index'))

# Rota para editar um item
@item_controller.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit_item(item_id):
    item = Item.query.get(item_id)  # Recupera o item pelo ID
    if request.method == 'POST':
        item.campo1 = request.form['campo1']
        item.campo2 = request.form['campo2']
        item.campo3 = request.form['campo3']
        item.campo4 = request.form['campo4']
        db.session.commit()  # Comita as alterações no banco
        return redirect(url_for('item_controller.index'))
    return render_template('edit.html', item=item)

# Rota para excluir um item
@item_controller.route('/delete/<int:item_id>')
def delete_item(item_id):
    item = Item.query.get(item_id)  # Recupera o item a ser deletado
    db.session.delete(item)  # Marca o item para exclusão
    db.session.commit()  # Comita a exclusão no banco
    return redirect(url_for('item_controller.index'))


