from config import *
class Item(db.Model):
    __tablename__ = 'items' 

    
    id = db.Column(db.Integer, primary_key=True)
    campo1 = db.Column(db.String(100), nullable=False)
    campo2 = db.Column(db.String(100), nullable=False)
    campo3 = db.Column(db.String(100), nullable=False)
    campo4 = db.Column(db.String(100), nullable=False)

    def __init__(self, campo1, campo2, campo3, campo4):
        self.campo1 = campo1
        self.campo2 = campo2
        self.campo3 = campo3
        self.campo4 = campo4

    def to_dict(self):
        return {
            'id': self.id,
            'campo1': self.campo1,
            'campo2': self.campo2,
            'campo3': self.campo3,
            'campo4': self.campo4
        }
