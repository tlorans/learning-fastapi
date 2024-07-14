from fastapi import FastAPI, Path
import json
import os

app = FastAPI()

# Define zone mapping including composite zones
zone_mapping = {
    "Zone A": ["Zone A"],
    "Zone B": ["Zone B"],
    "Zone C": ["Zone C"],
    "Zone D": ["Zone D"],
    "Zone E": ["Zone A", "Zone B"],
    "Zone F": ["Zone C", "Zone D"],
    # Add more composite zones as needed
}

@app.get("/")
def index():
    return {"message": "Hello, World"}

@app.get("/investment_zone/{zone}")
def get_stocks_by_zone(zone: str = Path(description="The investment zone of the stocks you want to view")):
    # Load zone mapping from JSON file
    with open("zone_mapping.json", "r") as f:
        zone_mapping = json.load(f)
    
    if zone not in zone_mapping:
        return {"message": "Zone not found"}
    
    constituent_zones = zone_mapping[zone]
    combined_stocks = []

    for constituent_zone in constituent_zones:
        file_path = f"{constituent_zone}.json"
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                combined_stocks.extend(json.load(f))
    
    return combined_stocks

@app.get("/returns/{date}")
def get_returns(date:str = Path(description="The date for which you want to view returns")):
    file_path = f"returns/{date}.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    else:
        return {"message": "No returns available for the specified date"}
    

@app.get("/returns/{zone}/{date}")
def get_zone_returns(zone: str = Path(description="The investment zone of the stocks you want to view"), 
                     date: str = Path(description="The date for which you want to view returns")):
    if zone not in zone_mapping:
        return {"message": "Zone not found"}
    
    constituent_zones = zone_mapping[zone]
    combined_stocks = []

    for constituent_zone in constituent_zones:
        file_path = f"universe/{constituent_zone}.json"
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                combined_stocks.extend(json.load(f))
    
    # Fetch the returns for these stocks
    file_path = f"returns/{date}.json"
    if not os.path.exists(file_path):
        return {"message": "No returns available for the specified date"}
    
    with open(file_path, "r") as f:
        all_returns = json.load(f)
    
    zone_returns = {stock: all_returns.get(stock, None) for stock in combined_stocks}
    
    return zone_returns
