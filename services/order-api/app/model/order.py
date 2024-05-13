from .. import db
import uuid
from sqlalchemy.orm import relationship
from .order_item import order_item

class Order(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    total_price = db.Column(db.Float, default = 0.0)
    total_cost = db.Column(db.Float, default = 0.0)
    basket_items = relationship('OrderItem', back_populates='order')
    
    def calculate_totals(self):
        """Calculate the total price and cost of the order based on the basket items"""
        self.total_price = sum(item.product.price * item.quantity for item in self.basket_items)
        self.total_cost = sum(item.product.cost * item.quantity for item in self.basket_items)
    
    def __init__(self, basket_items=[]):
        self.basket_items = basket_items
        self.calculate_totals()
    
    @property
    def serialize_order(self):
        """return object data in easily serializable format"""
        return {
            'id': self.id,
            'total_price': self.total_price,
            'total_cost': self.total_cost,
            'basket_items': [item.serializable_order_item for item in self.basket_items]
        }
    