from app import create_app, db  # Ensure you're importing your Flask app and db correctly
from app.model.category import Category
from app.model.product import Product

products_data = [
    # Electronics
    {"name": "Apple iPhone 13 Pro", "description": "256GB - Sierra Blue", "price": 999.00, "cost": 500.00, "current_stock": 100, "discontinued": False, "categories": ["Electronics"]},
    {"name": "Samsung Galaxy S21", "description": "128GB - Phantom Black", "price": 800.00, "cost": 400.00, "current_stock": 150, "discontinued": False, "categories": ["Electronics"]},
    {"name": "Google Pixel 6", "description": "128GB - Sorta Seafoam", "price": 599.00, "cost": 300.00, "current_stock": 200, "discontinued": False, "categories": ["Electronics"]},
    {"name": "Dell XPS 13", "description": "13 inch - 11th Gen Intel Core i7", "price": 1120.00, "cost": 700.00, "current_stock": 150, "discontinued": False, "categories": ["Electronics"]},
    {"name": "Apple MacBook Air", "description": "M1 Chip - 256GB SSD", "price": 999.00, "cost": 650.00, "current_stock": 120, "discontinued": False, "categories": ["Electronics"]},
    {"name": "Sony WH-1000XM4", "description": "Wireless Noise Cancelling Headphones", "price": 348.00, "cost": 175.00, "current_stock": 200, "discontinued": False, "categories": ["Electronics"]},
    {"name": "Apple Watch Series 7", "description": "GPS + Cellular, 45mm", "price": 749.00, "cost": 380.00, "current_stock": 100, "discontinued": False, "categories": ["Electronics"]},
    {"name": "Amazon Echo Dot 4th Gen", "description": "Smart speaker with Alexa", "price": 49.99, "cost": 24.00, "current_stock": 500, "discontinued": False, "categories": ["Electronics"]},
    {"name": "Nikon D3500", "description": "DSLR Camera Kit with 18-55mm and 70-300mm Lenses", "price": 846.95, "cost": 500.00, "current_stock": 90, "discontinued": False, "categories": ["Electronics"]},
    {"name": "Fitbit Charge 4", "description": "Fitness and Activity Tracker with Built-in GPS", "price": 129.95, "cost": 65.00, "current_stock": 300, "discontinued": False, "categories": ["Electronics"]},
    # Books
    {"name": "1984 by George Orwell", "description": "Dystopian novel exploring intensive governmental surveillance", "price": 7.99, "cost": 2.50, "current_stock": 300, "discontinued": False, "categories": ["Books"]},
    {"name": "To Kill a Mockingbird by Harper Lee", "description": "Classic American literature about racial injustice", "price": 8.99, "cost": 3.00, "current_stock": 300, "discontinued": False, "categories": ["Books"]},
    {"name": "The Great Gatsby by F. Scott Fitzgerald", "description": "A novel of decadence and excess of the jazz age", "price": 10.00, "cost": 4.00, "current_stock": 400, "discontinued": False, "categories": ["Books"]},
    {"name": "Pride and Prejudice by Jane Austen", "description": "Romantic novel of manners", "price": 9.50, "cost": 2.70, "current_stock": 300, "discontinued": False, "categories": ["Books"]},
    {"name": "The Catcher in the Rye by J.D. Salinger", "description": "A story about the realities of growing up", "price": 6.99, "cost": 3.50, "current_stock": 500, "discontinued": False, "categories": ["Books"]},
    {"name": "The Hobbit by J.R.R. Tolkien", "description": "A fantasy novel and prelude to the Lord of the Rings", "price": 10.99, "cost": 5.50, "current_stock": 300, "discontinued": False, "categories": ["Books"]},
    {"name": "Harry Potter and the Sorcerer's Stone by J.K. Rowling", "description": "The first novel in the Harry Potter series and Rowling's debut novel", "price": 12.99, "cost": 4.20, "current_stock": 500, "discontinued": False, "categories": ["Books"]},
    {"name": "Moby Dick by Herman Melville", "description": "Epic tale of a sea captain's quest for a white whale", "price": 15.00, "cost": 5.00, "current_stock": 200, "discontinued": False, "categories": ["Books"]},
    {"name": "The Da Vinci Code by Dan Brown", "description": "Mystery thriller that explores the hidden secrets of Christianity", "price": 9.99, "cost": 4.50, "current_stock": 300, "discontinued": False, "categories": ["Books"]},
    {"name": "The Lord of the Rings by J.R.R. Tolkien", "description": "Epic high fantasy novel", "price": 25.00, "cost": 12.00, "current_stock": 400, "discontinued": False, "categories": ["Books"]},
    # Clothing
    {"name": "Levi's 501 Original Jeans", "description": "Men's Jeans - Classic Straight Leg Style", "price": 59.95, "cost": 30.00, "current_stock": 250, "discontinued": False, "categories": ["Clothing"]},
    {"name": "Nike Air Force 1", "description": "Unisex Classic White Sneakers", "price": 90.00, "cost": 45.00, "current_stock": 300, "discontinued": False, "categories": ["Clothing"]},
    {"name": "Patagonia Better Sweater", "description": "Women's Fleece Jacket - Birch White", "price": 139.00, "cost": 70.00, "current_stock": 200, "discontinued": False, "categories": ["Clothing"]},
    {"name": "The North Face Borealis Backpack", "description": "Laptop Backpack - Black", "price": 89.00, "cost": 44.50, "current_stock": 150, "discontinued": False, "categories": ["Clothing"]},
    {"name": "Adidas Ultraboost 21", "description": "Running Shoes - Cloud White/Core Black", "price": 180.00, "cost": 90.00, "current_stock": 200, "discontinued": False, "categories": ["Clothing"]},
    # Home Goods
    {"name": "Instant Pot Duo 7-in-1", "description": "Electric Pressure Cooker, 6 Quart, Stainless Steel", "price": 89.00, "cost": 45.00, "current_stock": 500, "discontinued": False, "categories": ["Home & Garden"]},
    {"name": "Dyson V11 Torque Drive", "description": "Cordless Vacuum Cleaner", "price": 599.99, "cost": 300.00, "current_stock": 100, "discontinued": False, "categories": ["Home & Garden"]},
    {"name": "Keurig K-Classic Coffee Maker", "description": "Single Serve K-Cup Pod Coffee Brewer, 6 to 10 Oz. Brew Sizes, Black", "price": 119.99, "cost": 60.00, "current_stock": 200, "discontinued": False, "categories": ["Home & Garden"]},
    {"name": "iRobot Roomba 675", "description": "Robot Vacuum-Wi-Fi Connectivity, Works with Alexa, Good for Pet Hair, Carpets, Hard Floors, Self-Charging", "price": 279.99, "cost": 140.00, "current_stock": 150, "discontinued": False, "categories": ["Home & Garden"]},
    {"name": "YETI Rambler 20 oz Tumbler", "description": "Stainless Steel, Vacuum Insulated with MagSlider Lid, Black", "price": 29.98, "cost": 15.00, "current_stock": 500, "discontinued": False, "categories": ["Home & Garden"]},
    # Toys
    {"name": "LEGO Creator Expert NASA Apollo 11 Lunar Lander", "description": "Adult Building Kit for Display (1087 Pieces)", "price": 99.99, "cost": 50.00, "current_stock": 200, "discontinued": False, "categories": ["Toys"]},
    {"name": "PlayStation 5 Console", "description": "Next Gen Console from Sony", "price": 499.99, "cost": 250.00, "current_stock": 100, "discontinued": False, "categories": ["Electronics", "Toys"]},
    {"name": "Xbox Series X", "description": "Next Generation Console by Microsoft", "price": 499.99, "cost": 250.00, "current_stock": 100, "discontinued": False, "categories": ["Electronics", "Toys"]},
    {"name": "Nintendo Switch", "description": "Console with Neon Blue and Neon Red Joy‑Con", "price": 299.99, "cost": 150.00, "current_stock": 300, "discontinued": False, "categories": ["Electronics", "Toys"]},
    {"name": "UNO Card Game", "description": "Classic Card Game, Family and Party Game for 2 to 10 players", "price": 9.99, "cost": 5.00, "current_stock": 600, "discontinued": False, "categories": ["Toys"]},
    # Sports
    {"name": "Wilson Evolution Game Basketball", "description": "Official Size (29.5\"), Black", "price": 64.95, "cost": 32.48, "current_stock": 300, "discontinued": False, "categories": ["Sports"]},
    {"name": "Yonex Astrox 99 Badminton Racket", "description": "Cherry Sunburst, Unstrung", "price": 234.95, "cost": 117.48, "current_stock": 100, "discontinued": False, "categories": ["Sports"]},
    {"name": "Adidas Men's Soccer Cleats", "description": "Predator 20.3 Firm Ground", "price": 80.00, "cost": 40.00, "current_stock": 200, "discontinued": False, "categories": ["Sports"]},
    {"name": "TaylorMade M6 Driver", "description": "460cc", "price": 499.99, "cost": 249.99, "current_stock": 150, "discontinued": False, "categories": ["Sports"]},
    {"name": "Callaway Golf Men's Strata Complete Set", "description": "12 Piece, Right Hand, Steel", "price": 399.99, "cost": 200.00, "current_stock": 120, "discontinued": False, "categories": ["Sports"]},
    # Beauty
    {"name": "Estée Lauder Advanced Night Repair", "description": "Synchronized Multi-Recovery Complex (50ml)", "price": 100.00, "cost": 50.00, "current_stock": 200, "discontinued": False, "categories": ["Beauty"]},
    {"name": "Chanel No. 5 Perfume", "description": "Eau de Parfum Spray, 100ml", "price": 130.00, "cost": 65.00, "current_stock": 150, "discontinued": False, "categories": ["Beauty"]},
    {"name": "MAC Lipstick Matte Finish", "description": "Shade: Ruby Woo", "price": 19.00, "cost": 9.50, "current_stock": 300, "discontinued": False, "categories": ["Beauty"]},
    {"name": "Dyson Corrale Hair Straightener", "description": "Cord-free, with manganese copper alloy plates", "price": 499.99, "cost": 249.99, "current_stock": 100, "discontinued": False, "categories": ["Beauty"]},
    {"name": "Kiehl's Ultra Facial Cream", "description": "24-hour daily face moisturizer, 50ml", "price": 32.00, "cost": 16.00, "current_stock": 200, "discontinued": False, "categories": ["Beauty"]},
    # More entries can be added following this format to reach a total of 100
]



def create_or_get_category(name):
    category = Category.query.filter_by(name=name).first()
    if not category:
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
    return category

def insert_products(products):
    for product in products:
        categories = [create_or_get_category(name) for name in product['categories']]
        new_product = Product(
            name=product['name'],
            description=product['description'],
            price=product['price'],
            cost=product['cost'],
            current_stock=product['current_stock'],
            discontinued=product['discontinued'],
            categories=categories
        )
        db.session.add(new_product)
    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    # This ensures the script is executed within the Flask application context
    with app.app_context():
        insert_products(products_data)
        print("Database populated with products and categories.")