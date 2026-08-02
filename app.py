from fastapi import FastAPI

app = FastAPI()
plants = {"エバーフレッシュ": 20000, "アスパラガスナナス": 300, "ポトス": 500, "モンステラ": 8000}

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/plants/{plant_name}")
def get_plant_price(plant_name: str):
    plant_price = plants[plant_name]
    return plant_price

