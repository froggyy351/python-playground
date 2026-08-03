from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel

app = FastAPI()
plants = {"エバーフレッシュ": 20000, "アスパラガスナナス": 300, "ポトス": 500, "モンステラ": 8000}

class PlantCreate(BaseModel):
    name: str
    price: int
    
def get_plants_db():
    return plants

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/plants/{plant_name}")
def get_plant_price(plant_name: str, db: dict = Depends(get_plants_db)):
    if plant_name not in db:
        raise HTTPException(status_code=404, detail=f"{plant_name}は見つかりません")
    return db[plant_name]

@app.get("/plants")
def list_plants(min_price: int = 0, db: dict = Depends(get_plants_db)):
    result = {name: price for name, price in db.items() if price >= min_price}
    return result

@app.post("/plants")
def add_plant(plant: PlantCreate):
    plants[plant.name] = plant.price
    return {"message": f"{plant.name}を追加しました", "plants": plants}
