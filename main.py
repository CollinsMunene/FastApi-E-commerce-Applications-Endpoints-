# import optional
from typing import Optional

# import FastAPI
from fastapi import FastAPI

# import BaseModel
from pydantic import BaseModel

# create a model
class Item(BaseModel):
    name:str
    description:Optional[str] = None
    price:float
    tax:Optional[float] = None

# create a FastApi instance
app = FastAPI()

@app.post("/items/")
async def root(item:Item):
    return item