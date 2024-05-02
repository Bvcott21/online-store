from . import db
import uuid

class Product(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    current_stock = db.Column(db.Integer, nullable=False)
    discontinued = db.Column(db.Boolean, default=False)
    
    def __init__(self, name, description, price, cost,
            current_stock, discontinued):
        self.name = name
        self.description = description
        self.price = price
        self.cost = cost
        self.current_stock = current_stock
        self.discontinued = discontinued
        
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return{
        'id': self.id,
        'name': self.name,
        'description': self.description,
        'price': self.price,
        'cost': self.cost,
        'current_stock': self.current_stock,
        'discontinued': self.discontinued
    }
    

