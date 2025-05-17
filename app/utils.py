from datetime import datetime
from collections import defaultdict
from app.db import customers_collection, orders_collection


def determine_loyalty_tier(total: float) -> str:
    if total < 1000:
        return "Bronze"
    elif 1000 <= total <= 3000:
        return "Silver"
    else:
        return "Gold"


def is_active(last_purchase_date: datetime) -> bool:
    return (datetime.now() - last_purchase_date).days <= 180  # 6 months


def get_favorite_category(category_spend: dict) -> str:
    if not category_spend:
        return None
    max_spent = max(category_spend.values())
    fav_categories = [cat for cat,
                      amt in category_spend.items() if amt == max_spent]
    return sorted(fav_categories)[0]  # resolve tie alphabetically


def get_high_value_customers() -> list:
    report = []
    customers = list(customers_collection.find())

    for customer in customers:
        customer_id = customer["_id"]
        orders = list(orders_collection.find({"customerId": customer_id}))

        if not orders:
            continue

        total_spent = sum(o["amount"] for o in orders)
        if total_spent < 500:
            continue

        avg_order_value = total_spent / len(orders)

        # Convert order date to datetime if needed (should already be datetime)
        last_purchase = max(
            o["date"] if isinstance(o["date"], datetime) else datetime.combine(
                o["date"], datetime.min.time())
            for o in orders
        )

        category_spend = defaultdict(float)
        for o in orders:
            category_spend[o["category"]] += o["amount"]

        customer_report = {
            "customerId": str(customer_id),
            "name": customer["name"],
            "email": customer["email"],
            "totalSpent": round(total_spent, 2),
            "averageOrderValue": round(avg_order_value, 2),
            "favoriteCategory": get_favorite_category(category_spend),
            "loyaltyTier": determine_loyalty_tier(total_spent),
            "lastPurchaseDate": last_purchase.strftime("%Y-%m-%d"),
            "isActive": is_active(last_purchase),
            "categoryWiseSpend": {k: round(v, 2) for k, v in category_spend.items()}
        }

        report.append(customer_report)

    return report
