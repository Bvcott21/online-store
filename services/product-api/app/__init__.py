from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    api = Api(app)

    from .routes import ProductList
    api.add_resource(ProductList, '/products')
    # api.add_resource(ProductDetail, '/products/<string:product_id>')
    
    return app