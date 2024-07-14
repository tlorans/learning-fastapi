import json
import os
import random
import pandas as pd

# Create directories if they don't exist
os.makedirs("data/universe", exist_ok=True)
os.makedirs("data/returns", exist_ok=True)

# Define zones
zones = ["Zone A", "Zone B", "Zone C", "Zone D"]
zone_mapping = {
    "Zone A": ["Zone A"],
    "Zone B": ["Zone B"],
    "Zone C": ["Zone C"],
    "Zone D": ["Zone D"],
    "Zone E": ["Zone A", "Zone B"],
    "Zone F": ["Zone C", "Zone D"],
    # Add more composite zones as needed
}

# Simulate stocks and assign them to zones
stocks = {zone: [] for zone in zones}
all_stocks = []

for i in range(1, 1001):
    stock = {
        "ticker": f"STOCK{i:04d}",
        "name": f"Stock {i}",
    }
    zone = random.choice(zones)
    stocks[zone].append(stock["ticker"])  # Use ticker instead of name
    all_stocks.append(stock["ticker"])

# Save each zone's stock names to a JSON file in the universe folder
for zone, stock_list in stocks.items():
    with open(f"data/universe/{zone}.json", "w") as f:
        json.dump(stock_list, f)

# Save zone mapping to a JSON file
with open("data/zone_mapping.json", "w") as f:
    json.dump(zone_mapping, f)


#### Returns 


# Define date range for monthly returns
date_range = pd.date_range(start='2020-01-01', end='2023-01-01', freq='ME')

# Simulate monthly returns for each date and save to JSON files
for date in date_range:
    monthly_returns = {}
    for stock in all_stocks:
        monthly_returns[stock] = round(random.uniform(-0.2, 0.2), 4)
    
    date_str = date.strftime('%Y-%m')
    with open(f"data/returns/{date_str}.json", "w") as f:
        json.dump(monthly_returns, f)
