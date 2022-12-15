from typing import List
import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name="James", age=22),
    Person(id=2, name="Alex", age=38)   
]

# image = "plane.jpg"
# result = requests.post("http://localhost:8000/;)
# files={"file": open(image, "rb")}) 


@app.get("/api")
def read_root():
    return DB
