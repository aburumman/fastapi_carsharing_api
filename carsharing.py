import uvicorn
from fastapi import FastAPI, HTTPException
from datetime import datetime
from schemas import load_db

app = FastAPI()

db = load_db()

@app.get("/api/cars/")
def get_cars(size: str|None = None, doors: int|None = None) -> list:
    ''' Return details of cars available '''
    result = db
    if size:
        result = [car for car in result if car.size == size ]
    if doors:
        #doors = int(doors)
        result = [ car for car in result if car.doors == doors ]

    return result

@app.get("/api/cars/{id}")
def car_by_id(id: int) -> dict:
    result = [car for car in db if car.id == id ]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, details= f" {id} not in car data")

        

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

if __name__ == '__main__':
    uvicorn.run("carsharing:app", reload=True)
