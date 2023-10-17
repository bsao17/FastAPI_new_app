from urllib import request
from typing import Optional, Union
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class Person(str, Enum):
    John = "John"
    Jane = "Jane"


@app.get("/items/")
async def read_item(skip: Union[int, None] = 0, limit: Union[int, None] = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/{person}")
async def persons(person: Person):
    if request is person.John:
        return {"message": f"Hello {person} Doe"}
    else:
        return {"message": f"Hello {person} Doe"}
