from . import db
import uuid
# from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

class Category(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name):
        self.name = name        

product_categories = db.Table('product_categories',
    db.Column('product_id', db.String(36), db.ForeignKey('product.id'), primary_key=True),
    db.Column('category_id', db.String(36), db.ForeignKey('category.id'), primary_key=True)
)
class Product(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255))
    price = db.Column(db.Float, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    current_stock = db.Column(db.Integer, nullable=False)
    discontinued = db.Column(db.Boolean, default=False)
    categories = relationship('Category', secondary=product_categories, backref=db.backref('products', lazy=True))
    
    def __init__(self, name, description, price, cost,
            current_stock, discontinued, categories):
        self.name = name
        self.description = description
        self.price = price
        self.cost = cost
        self.current_stock = current_stock
        self.discontinued = discontinued
        self.categories = categories
        
    @property
    def serialize_product(self):
        """Return object data in easily serializable format"""
        return{
        'id': self.id,
        'name': self.name,
        'description': self.description,
        'price': self.price,
        'cost': self.cost,
        'current_stock': self.current_stock,
        'discontinued': self.discontinued,
        'categories': [category.name for category in self.categories]
    }
        
    @property
    def serialize_category(self):
        return {
            'id': self.id,
            'name': self.name
        }
    

