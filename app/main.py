from typing import Union
import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: int
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/charge/device")
def return_random_device():
    return {"Hello": random.random()}

@app.get("/health", include_in_schema=False)
async def health_check():
    return {"status": "ok"}