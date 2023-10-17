from urllib import request
from typing import Optional, Union
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class Person(str, Enum):
    John = "John"
    Jane = "Jane"


"""
Retrieves items from the fake_items_db based on the given skip and limit parameters.

Parameters:
    skip (Union[int, None], optional): The number of items to skip. Defaults to 0.
    limit (Union[int, None], optional): The maximum number of items to retrieve. Defaults to 10.

Returns:
    List: A list of items retrieved from fake_items_db.
"""


@app.get("/items/")
async def read_item(skip: Union[int, None] = 0, limit: Union[int, None] = 10):
    return fake_items_db[skip: skip + limit]


@app.get("/{person}")
async def persons(person: Person):
    """
    A function that handles requests to the "/{person}" endpoint.

    Parameters:
    - person (Person): The person object representing the person being requested.

    Returns:
    - dict: A dictionary containing the response message.
    """
    if request is person.John:
        return {"message": f"Hello {person} Doe"}
    else:
        return {"message": f"Hello {person} Doe"}
