from .. import db
import uuid
from sqlalchemy.orm import relationship

class Product(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    price = db.Column(db.Float, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    current_stock = db.Column(db.Integer, nullable=False)
    discontinued = db.Column(db.Boolean, default=False)
    
    def __init__(self, id, price, cost, current_stock, discontinued):
        self.id = id
        self.price = price
        self.cost = cost
        self.current_stock = current_stock
        self.discontinued = discontinued
    
    @property
    def serialize_product(self):
        return {
            'id': self.id,
            'price': self.price,
            'cost': self.cost,
            'current_stock': self.current_stock,
            'discontinued': self.discontinued
        }