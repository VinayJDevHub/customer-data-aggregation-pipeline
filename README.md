# 🧩 Customer Data Aggregation Pipeline

This project generates a high-value customer report from e-commerce purchase data.

## 🚀 Tech Stack
- Python, FastAPI
- MongoDB
- Pydantic, Faker
- Uvicorn

## 📊 Report Fields
- `customerId`, `name`, `email`
- `totalSpent`, `averageOrderValue`
- `favoriteCategory` (tie resolved alphabetically)
- `loyaltyTier` (Bronze < 1000, Silver 1000–3000, Gold > 3000)
- `lastPurchaseDate`, `isActive` (if purchase in last 6 months)
- `categoryWiseSpend`

## ✅ Filters
- Only includes customers with `totalSpent ≥ 500`

## 📦 API Usage

### GET /high-value-customers
Returns a list of customer report entries:
```json
{
  "report": [
    {
      "customerId": "...",
      "name": "...",
      "email": "...",
      "totalSpent": 1345.50,
      "averageOrderValue": 191.30,
      "favoriteCategory": "Electronics",
      "loyaltyTier": "Silver",
      "lastPurchaseDate": "2025-04-29",
      "isActive": true,
      "categoryWiseSpend": {
        "Electronics": 500,
        "Books": 845.50
      }
    }
  ]
}

## 🛠️ How to Run

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/customer-data-aggregation-pipeline.git
cd customer-data-aggregation-pipeline

Create and activate a Python virtual environment

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install dependencies

pip install -r requirements.txt
Configure MongoDB connection
Edit the MongoDB URI in app/db.py to point to your MongoDB instance.

(Optional) Generate sample data

python seed_data.py
Start the FastAPI server

uvicorn main:app --reload
Explore the API
Open your browser and navigate to http://localhost:8000/docs to access interactive API documentation.


Let me know if you want me to generate the full README with this included!
