# app/main.py
from fastapi import FastAPI
from app.utils import get_high_value_customers

app = FastAPI()


@app.get("/high-value-customers")
def high_value_customers():
    return {"report": get_high_value_customers()}
