import json
from pydantic import BaseModel

class car(BaseModel):
    id: int
    size: str
    fuel: str | None = "electric"
    doors: int
    transmission: str | None = "auto"


def load_db() -> list[car]:
    ''' Load a list of car objects from a json file '''
    with open("cars_json.json") as f:
        return [car.parse_obj(obj) for obj in json.load(f)]

