# app/db.py
from pymongo import MongoClient

MONGO_URI = "mongodb+srv://vinayjain:RnnKbXa1c7s4HRt1@cluster0.mvczp9p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)

db = client["customer_report"]

customers_collection = db["customers"]
orders_collection = db["orders"]
