from flask_restful import Resource, reqparse
from .models import Product
from . import db

parser = reqparse.RequestParser()
parser.add_argument('name', required=True, help="Name cannot be blank")
parser.add_argument('description', required=True, help="Description cannot be blank")
parser.add_argument('price', type=float, required=True, help="Price cannot be blank")
parser.add_argument('cost', type=float, required=True, help="Cost cannot be blank.")
parser.add_argument('current_stock', type=int, required=True, help="Current stock cannot be blank.")
parser.add_argument('discontinued', type=bool,required=True, help="Discontinued cannot be blank.")

class ProductList(Resource):
    def get(self):
        products = Product.query.all()
        return {'products': [product.serialize for product in products]}
    
    def post(self):
        args = parser.parse_args()
        
        product = Product(
            name = args['name'],
            description = args['description'],
            price = args['price'],
            cost = args['cost'],
            current_stock = args['current_stock'],
            discontinued = args['discontinued']
        )
        
        db.session.add(product)
        db.session.commit()
        
        return {'product': product.serialize}, 201