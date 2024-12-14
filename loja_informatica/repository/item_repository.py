# repository/item_repository.py
from models.item import Item
from config import db

class ItemRepository:
    
    @staticmethod
    def get_all_items():
        return Item.query.all()  # Retorna todos os itens

    @staticmethod
    def add_item(campo1, campo2, campo3, campo4):
        # Criando um novo item com os dados passados
        new_item = Item(campo1=campo1, campo2=campo2, campo3=campo3, campo4=campo4)
        db.session.add(new_item)
        db.session.commit()  # Comita a sessão no banco

    @staticmethod
    def get_item_by_id(item_id):
        return Item.query.get(item_id)  # Retorna um item pelo ID

    @staticmethod
    def update_item(item_id, campo1, campo2, campo3, campo4):
        item = Item.query.get(item_id)  # Recupera o item pelo ID
        if item:
            item.campo1 = campo1
            item.campo2 = campo2
            item.campo3 = campo3
            item.campo4 = campo4
            db.session.commit()  # Comita as alterações no banco

    @staticmethod
    def delete_item(item_id):
        item = Item.query.get(item_id)  # Recupera o item pelo ID
        if item:
            db.session.delete(item)  # Deleta o item
            db.session.commit()  # Comita a exclusão no banco
