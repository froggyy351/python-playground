from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
plants = {"エバーフレッシュ": 20000, "アスパラガスナナス": 300, "ポトス": 500, "モンステラ": 8000}

class PlantCreate(BaseModel):
    name: str
    price: int


@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/plants/{plant_name}")
def get_plant_price(plant_name: str):
    if plant_name not in plants:
        raise HTTPException(status_code=404, detail=f"{plant_name}は見つかりません")
    return plants[plant_name]

@app.get("/plants")
def list_plants(min_price: int = 0):
    result = {name: price for name, price in plants.items() if price >= min_price}
    return result

@app.post("/plants")
def add_plant(plant: PlantCreate):
    plants[plant.name] = plant.price
    return {"message": f"{plant.name}を追加しました", "plants": plants}
