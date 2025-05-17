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
🛠️ How to Run
Clone the repository

bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/customer-data-aggregation-pipeline.git
cd customer-data-aggregation-pipeline
Create and activate a Python virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # For Windows: venv\Scripts\activate
Install dependencies

nginx
Copy
Edit
pip install -r requirements.txt
Configure MongoDB URI
Edit the MongoDB connection string in app/db.py file to connect to your MongoDB instance.

(Optional) Generate sample data

nginx
Copy
Edit
python seed_data.py
Start the FastAPI server

css
Copy
Edit
uvicorn main:app --reload
Explore the API
Open your browser and visit:
http://localhost:8000/docs