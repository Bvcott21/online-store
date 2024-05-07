from flask_restful import Resource, reqparse
from ..model.category import Category
from ..model.product import Product
from .. import db

class ProductList(Resource):
    def get(self):
        products = Product.query.all()
        return {'products': [product.serialize_product for product in products]}
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, help="Name cannot be blank")
        parser.add_argument('description', required=True, help="Description cannot be blank")
        parser.add_argument('price', type=float, required=True, help="Price cannot be blank")
        parser.add_argument('cost', type=float, required=True, help="Cost cannot be blank.")
        parser.add_argument('current_stock', type=int, required=True, help="Current stock cannot be blank.")
        parser.add_argument('discontinued', type=bool,required=True, help="Discontinued cannot be blank.")
        parser.add_argument('category_ids', type=str, help="Comma-separated category IDs")
        args = parser.parse_args()
        
        category_ids = args['category_ids'].split(',') if args['category_ids'] else []
        categories = Category.query.filter(Category.id.in_(category_ids)).all()
        
        if args['price'] <= 0:
            return {'message': 'Price cannot be 0 or negative.'}, 400
        
        if args['cost'] <= 0:
            return {'message': 'Cost cannot be 0 or negative.'}, 400
        
        if args['current_stock'] < 0:
            return {'message': "Stock cannot be negative"}, 400
        
        product = Product(
            name = args['name'],
            description = args['description'],
            price = args['price'],
            cost = args['cost'],
            current_stock = args['current_stock'],
            discontinued = args['discontinued'],
            categories = categories
        )
        
        db.session.add(product)
        db.session.commit()
        
        return {'product': product.serialize_product}, 201

class ProductDetail(Resource):
    def get(self, product_id):
        product = Product.query.get(product_id)
        if not product:
            return {'message': 'Product not found'}, 404
        return {'product': product.serialize_product}
    
    def put(self, product_id):
        parser = reqparse.RequestParser()
        
        parser.add_argument('name', type=str, help="Name of the product")
        parser.add_argument('description', type=str, help='Description of the product')
        parser.add_argument('price', type=float, help='Price of the Product')
        parser.add_argument('cost', type=float, help='Cost of the product')
        parser.add_argument('current_stock', type=int, help='Current stock of the product')
        parser.add_argument('discontinued', type=bool, help='Is the product discontinued')
        parser.add_argument('category_ids', type=str, help="Comma-separated category IDs")
        
        product = Product.query.get_or_404(product_id)
        args = parser.parse_args()
        
        if args['category_ids'] is not None:
            category_ids = args['category_ids'].split(',')
            categories = Category.query.filter(Category.id.in_(category_ids)).all()
            product.categories = categories
        
        product.name = args['name'] if args['name'] is not None else product.name
        product.description = args['description'] if args['description'] is not None else product.description
        product.price = args['price'] if args['price'] is not None else product.price
        product.cost = args['cost'] if args['cost'] is not None else product.cost
        product.current_stock = args['current_stock'] if args['current_stock'] is not None else product.current_stock
        product.discontinued = args['discontinued'] if args['discontinued'] is not None else product.discontinued
        
        if product.price <= 0:
            return {'message': 'Price cannot be 0 or negative.'}, 400
        
        if product.cost <= 0:
            return {'message': 'Cost cannot be 0 or negative.'}, 400
        
        if product.current_stock < 0:
            return {'message': "Stock cannot be negative"}, 400
            
        db.session.commit()
        
        return {
            'message': 'Product updated successfully', 
            'product': product.serialize_product
        }, 
        200
    
class ProductSearchByName(Resource):
    def get(self, name):
        products = Product.query.filter(Product.name.ilike(f"%{name}%")).all()
    
        if not products:
            return {'message': 'No products found'}, 404
        return {'products': [product.serialize_product for product in products]}