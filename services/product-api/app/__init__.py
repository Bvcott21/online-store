from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app, resources={
        r'/*': 
            {"origins": 
                [
                    'http://localhost:3000',
                    
                ]
            }
        }
    )
    app.config.from_object(Config)
    db.init_app(app)
    api = Api(app)

    from .routes import ProductList, ProductDetail, ProductSearchByName, CategoryList, CategoryDetail
    
    api.add_resource(ProductList, '/products')
    api.add_resource(ProductDetail, '/products/<string:product_id>')
    api.add_resource(ProductSearchByName, '/products/find-by-name/<string:name>')    
    api.add_resource(CategoryList, '/categories')
    api.add_resource(CategoryDetail, '/categories/<int:category_id>')
    return app