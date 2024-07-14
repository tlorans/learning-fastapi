from fastapi import FastAPI, Path, Depends
from .loader import Loader
from .auth import get_current_user, app as auth_app

app = FastAPI()

# Include the auth routes
app.mount("/auth", auth_app)

zone_mapping = Loader.load_zone_mapping()

@app.get("/")
def index():
    return {"message": "Hello, World"}

@app.get("/investment_zone/{zone}")
def get_stocks_by_zone(
    zone: str = Path(description="The investment zone of the stocks you want to view"),
    current_user: dict = Depends(get_current_user)  # Authentication dependency
):
    if zone not in zone_mapping:
        return {"message": "Zone not found"}
    
    constituent_zones = zone_mapping[zone]
    combined_stocks = []

    for constituent_zone in constituent_zones:
        combined_stocks.extend(Loader.load_universe(constituent_zone))
    
    return combined_stocks

@app.get("/returns/{date}")
def get_returns(
    date: str = Path(description="The date for which you want to view returns"),
    current_user: dict = Depends(get_current_user)  # Authentication dependency
):
    returns_data = Loader.load_returns(date)
    if not returns_data:
        return {"message": "No returns available for the specified date"}
    return returns_data

@app.get("/zone_returns/{zone}/{date}")
def get_zone_returns(
    zone: str = Path(description="The investment zone of the stocks you want to view"), 
    date: str = Path(description="The date for which you want to view returns"),
    current_user: dict = Depends(get_current_user)  # Authentication dependency
):
    if zone not in zone_mapping:
        return {"message": "Zone not found"}
    
    constituent_zones = zone_mapping[zone]
    combined_stocks = []

    for constituent_zone in constituent_zones:
        combined_stocks.extend(Loader.load_universe(constituent_zone))
    
    returns_data = Loader.load_returns(date)
    if not returns_data:
        return {"message": "No returns available for the specified date"}

    zone_returns = {stock: returns_data.get(stock, None) for stock in combined_stocks}
    
    return zone_returns
