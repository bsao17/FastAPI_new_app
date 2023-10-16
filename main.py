from urllib import request

from fastapi import FastAPI
from enum import Enum

app = FastAPI()


class Person(str, Enum):
    John = "John"
    Jane = "Jane"


@app.get("/{person}")
async def persons(person: Person):
    if person is person.John:
        return {"message": f"Hello {person} Doe"}
    else:
        return {"message": f"Hello {person} Doe"}


