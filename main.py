from fastapi import FastAPI, Path
import json
import os
import my_data_package

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
    zone_mapping = my_data_package.get_zone_mapping()
    
    if zone not in zone_mapping:
        return {"message": "Zone not found"}
    
    constituent_zones = zone_mapping[zone]
    combined_stocks = []

    for constituent_zone in constituent_zones:
        combined_stocks.extend(my_data_package.load_universe(constituent_zone))
    
    return combined_stocks

@app.get("/returns/{date}")
def get_returns(date:str = Path(description="The date for which you want to view returns")):
    returns_data = my_data_package.load_returns(date)
    if not returns_data:
        return {"message": "No returns available for the specified date"}
    return returns_data
    

@app.get("/zone_returns/{zone}/{date}")
def get_zone_returns(zone: str = Path(description="The investment zone of the stocks you want to view"), 
                     date: str = Path(description="The date for which you want to view returns")):
    if zone not in zone_mapping:
        return {"message": "Zone not found"}
    
    constituent_zones = zone_mapping[zone]
    combined_stocks = []

    for constituent_zone in constituent_zones:
        combined_stocks.extend(my_data_package.load_universe(constituent_zone))
    
    returns_data = my_data_package.load_returns(date)
    if not returns_data:
        return {"message": "No returns available for the specified date"}

    zone_returns = {stock: returns_data.get(stock, None) for stock in combined_stocks}
    
    return zone_returns
