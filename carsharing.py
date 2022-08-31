from fastapi import FastAPI
from datetime import datetime
app = FastAPI()


db =  [
        {"id":1, "size": "s", "fuel": "gasoline", "doors": 3, "transmission": "auto"},
        {"id":2, "size": "s", "fuel": "electric", "doors": 3, "transmission": "auto"},
        {"id":3, "size": "s", "fuel": "hybrid", "doors": 5, "transmission": "manual"},
        {"id":4, "size": "m", "fuel": "eletric", "doors": 5, "transmission": "manual"},
        {"id":5, "size": "m", "fuel": "gasoline", "doors": 3, "transmission": "auto"},
        {"id":6, "size": "m", "fuel": "gasoline", "doors": 3, "transmission": "manual"},
        {"id":7, "size": "l", "fuel": "hybird", "doors": 5, "transmission": "auto"},
        {"id":8, "size": "l", "fuel": "eletric", "doors": 5, "transmission": "auto"},
        {"id":9, "size": "l", "fuel": "hybrid", "doors": 5, "transmission": "manual"},
        {"id":1, "size": "s", "fuel": "gasoline", "doors": 3, "transmission": "auto"}
        ]
# Please add an operation call get_cars()
#That is served at /api/cars
#And return all car data

@app.get("/api/cars/")
def get_cars(size: str|None = None, doors: str|None = None) -> list:
    ''' Return details of cars available '''
    result = db
    if size:
        result = [car for car in results if car['size'] == size ]
    if doors:
        doors = int(doors)
        result = [ car for car in results if car['doors'] == doors ]

    return result
        

@app.get("/api/car/")
def get_car(num):
    ''' Return detials of a give car id '''
    num = int(num)
    return db[num]

@app.get("/")
def welcome(name):
    ''' Return a friendly welcome message '''
    return {'message': f"welcome, {name}, to the car sharing service"}

@app.get("/date")
def date():
    ''' Return friendly welcome message '''
    return {'date': datetime.now()}
