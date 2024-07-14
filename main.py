from fastapi import FastAPI, Path, Query
import random

app = FastAPI()

# Simulate a fake database with a thousand stocks
stocks = [
    {
        "ticker": f"STOCK{i:04d}",
        "name": f"Stock {i}",
        "investment_zone": random.choice(["Zone A", "Zone B", "Zone C", "Zone D"]),
        "price": round(random.uniform(10, 1000), 2)
    }
    for i in range(1, 1001)
]

@app.get("/")
def index():
    return {"message": "Hello, World"}


@app.get("/stocks/")
def get_stocks(investment_zone: str = Query(None, description="The investment zone of the stocks you want to view")):
    if investment_zone:
        filtered_stocks = [stock for stock in stocks if stock["investment_zone"] == investment_zone]
        return filtered_stocks
    return stocks

