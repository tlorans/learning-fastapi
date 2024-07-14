import json
import random


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

# Save each zone's stocks to a JSON file
for zone, stock_list in stocks.items():
    with open(f"{zone}.json", "w") as f:
        json.dump(stock_list, f)
