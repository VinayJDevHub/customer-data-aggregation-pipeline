from faker import Faker
import random
from datetime import datetime
from app.db import customers_collection, orders_collection

fake = Faker()

CATEGORIES = ['Electronics', 'Clothing', 'Books', 'Grocery', 'Fitness']


def generate_sample_data():
    # Clean old data
    customers_collection.delete_many({})
    orders_collection.delete_many({})

    for i in range(8):
        customer = {
            "name": fake.name(),
            "email": fake.email(),
        }
        customer_id = customers_collection.insert_one(customer).inserted_id

        # Force 2 customers to be low-spending (i.e. < ₹500)
        if i < 2:
            order_count = random.randint(2, 4)
            min_amount, max_amount = 20, 80  # low spend
        else:
            order_count = random.randint(6, 12)
            min_amount, max_amount = 100, 500  # regular spend

        for _ in range(order_count):
            order_date = fake.date_between(start_date='-1y', end_date='today')
            order = {
                "customerId": customer_id,
                "amount": round(random.uniform(min_amount, max_amount), 2),
                "category": random.choice(CATEGORIES),
                "date": datetime.combine(order_date, datetime.min.time()),
            }
            orders_collection.insert_one(order)

    print("✅ Sample data with mixed spending generated.")


if __name__ == "__main__":
    generate_sample_data()
