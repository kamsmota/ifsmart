from config import db  

class CartItem(db.Model):
    __tablename__ = 'cart_item'

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, default=1)
    title = db.Column(db.String, nullable=True)
    price = db.Column(db.Float, nullable=True)  # Adicione este campo se necessário
    permalink = db.Column(db.String(255), nullable=True)
    thumbnail = db.Column(db.String(255), nullable=True)

    def __init__(self, cart_id, product_id, quantity, title, price, permalink=None):
        self.cart_id = cart_id
        self.product_id = product_id
        self.quantity = quantity
        self.title = title
        self.price = price
        self.permalink = permalink  # pode ser None se não for informado
