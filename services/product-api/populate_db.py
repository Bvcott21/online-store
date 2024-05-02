import random
from faker import Faker
from app import create_app, db
from app.models import Product

def add_products():
    fake = Faker()
    
    app = create_app()
    with app.app_context():
        for _ in range(100):
            # Create a more product-like name
            product_name = f"{fake.color_name()} {fake.word()}"
            description = fake.catch_phrase()
            price = round(random.uniform(10.99, 299.99), 2)
            cost = round(price * random.uniform(0.5, 0.9), 2)  # cost is somewhere between 50% and 90% of price
            current_stock = random.randint(10, 200)
            discontinued = random.choice([True, False])

            product = Product(
                name=product_name,
                description=description,
                price=price,
                cost=cost,
                current_stock=current_stock,
                discontinued=discontinued
            )

            db.session.add(product)

        db.session.commit()
        print("100 products have been added to the database.")

if __name__ == '__main__':
    add_products()