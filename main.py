from urllib import request

from pydantic import BaseModel
from tinydb import TinyDB, Query
from typing import Optional, Union, List
from fastapi import FastAPI, Query
from enum import Enum

app = FastAPI()
db = TinyDB("db.json")

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}, {"item_name": "Boz"}]


class Person(str, Enum):
    John = "John"
    Jane = "Jane"


class Users(BaseModel):
    user_id: int
    item_id: int
    q: str | None = Query(default=None, max_length=50)
    short: bool | None = True


@app.get("/item/")
async def fake_item(skip: int = 0, limit: int | None = 3):
    """
    Retrieves items from the fake_items_db based on the given skip and limit parameters.

    Parameters:
    - skip (Union[int, None], optional): The number of items to skip. Defaults to 0.
    - limit (Union[int, None], optional): The maximum number of items to retrieve. Defaults to 10.

    Returns:
    - List: A list of items retrieved from fake_items_db.
    """
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool | None = None):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an item that does not have a description"}
        )
    return item


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


@app.get("/iterable/{item}")
def iterable(item: int):
    items = [x for x in range(item)]
    return {"items": items}


@app.get("/listing/")
async def listening(q: List[str] | None = Query(default=None)):
    query_items = {"q": q}
    return query_items


@app.post("/add_user/")
async def add_new_user(user: Users):
    """
    Adds a new user to the database.

    Parameters:
    - user (Users): The user object containing the user ID, item ID, q, and short.

    Returns:
    - Users: The added user object.
    """
    all_item = db.all()
    all_id = []
    for item in all_item:
        all_id.append(item["user_id"])
    if user.user_id in all_id:
        pass
    else:
        db.insert({"user_id": user.user_id, "item_id": user.item_id, "q": user.q, "short": user.short})
    return user
