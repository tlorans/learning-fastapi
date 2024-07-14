from fastapi import FastAPI, Path
import json
import os

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello, World"}

@app.get("/investment_zone/{zone}")
def get_stocks_by_zone(zone: str = Path(description="The investment zone of the stocks you want to view")):
    file_path = f"{zone}.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            stocks = json.load(f)
        return stocks
    else:
        return {"message": "Zone not found"}
