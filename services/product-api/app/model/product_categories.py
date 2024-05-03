from .. import db

product_categories = db.Table('product_categories',
    db.Column('product_id', db.String(36), db.ForeignKey('product.id'), primary_key=True),
    db.Column('category_id', db.String(36), db.ForeignKey('category.id'), primary_key=True)
)