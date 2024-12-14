from config import db
from models.item import Item

class ItemDAO:
    @staticmethod
    def add_item(campo1, campo2, campo3, campo4):
        new_item = Item(campo1=campo1, campo2=campo2, campo3=campo3, campo4=campo4)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    @staticmethod
    def get_all_items():
        return Item.query.all()

    @staticmethod
    def get_item_by_id(item_id):
        return Item.query.get(item_id)

    @staticmethod
    def update_item(item_id, campo1, campo2, campo3, campo4):
        item = Item.query.get(item_id)
        if item:
            item.campo1 = campo1
            item.campo2 = campo2
            item.campo3 = campo3
            item.campo4 = campo4
            db.session.commit()
        return item

    @staticmethod
    def delete_item(item_id):
        item = Item.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
        return item
