# 🧩 Project Report

## 🗃️ Database
- **MongoDB** used.
- Two collections: `customers`, `orders`

## 📐 Schema
- `customers`: `{ _id, name, email }`
- `orders`: `{ customerId, amount, category, date }`

## 🔁 Workflow
1. Customers and orders generated using `Faker`.
2. Orders randomly assigned over last year.
3. API `/high-value-customers` aggregates data:
   - Groups by customer.
   - Calculates spend, favorite category, loyalty tier.
   - Filters out customers with totalSpent < 500.
   - Marks `isActive` if purchased within 6 months.

## 🔐 Security
See `SECURITY.md` file for details.
