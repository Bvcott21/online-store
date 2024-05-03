from .. import db
import uuid
from sqlalchemy.orm import relationship

class Category(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name):
        self.name = name 
        
    @property
    def serialize_category(self):
        return {
            'id': self.id,
            'name': self.name
        }