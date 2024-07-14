from fastapi import FastAPI, Path
import random

app = FastAPI()

# Simulate a fake database with stocks organized by investment zones
zones = ["Zone A", "Zone B", "Zone C", "Zone D"]
stocks = {zone: [] for zone in zones}

for i in range(1, 1001):
    stock = {
        "ticker": f"STOCK{i:04d}",
        "name": f"Stock {i}",
        "price": round(random.uniform(10, 1000), 2)
    }
    zone = random.choice(zones)
    stocks[zone].append(stock)

@app.get("/")
def index():
    return {"message": "Hello, World"}

@app.get("/investment_zone/{zone}")
def get_stocks_by_zone(zone: str = Path(description="The investment zone of the stocks you want to view")):
    return stocks.get(zone, {"message": "Zone not found"})
