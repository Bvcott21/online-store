from .. import db
from sqlalchemy.orm import relationship

class OrderItem(db.Model):
    order_id = db.Column(db.String(36), db.ForeignKey('order.id'), primary_key=True)
    product_id = db.Column(db.String(36), db.ForeignKey('product.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable = False)
    
    order = relationship('Order', back_populates='basket_items')
    product = relationship('Product')
    
    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity
    
    @property
    def serialize_order_item(self):
        """Return object data in easily serializable format"""
        return {
            'product_id': self.product_id,
            'quantity': self.quantity,
            'product_details': {
                'name': self.product.name,
                'price': self.product.price,
                'cost': self.product.cost
            }
        }