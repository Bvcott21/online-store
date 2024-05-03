from flask_restful import Resource, reqparse
from ..model.category import Category
from .. import db

def category_parser():
    parser = reqparse.RequestParser()
    category_parser.add_argument('name', required=True, help="Name cannot be blank")
    return parser    

class CategoryList(Resource):
    def get(self):
        categories = Category.query.all()
        return {'categories': [
            {
                'id': category.id, 
                'name': category.name
            } 
            for category in categories
            ]
        }
        
    def post(self):
        args = category_parser().parse_args()
        category = Category(name=args['name'])
        db.session.add(category)
        db.session.commit()
        return {
            'message': 'Category created successfully',
            'category': category.serialize_category
        }

class CategoryDetail(Resource):
    def get(self, category_id):
        category = Category.query.get_or_404(category_id)
        return {'category': category.serialize_category}