import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, Set
import asyncio

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: Set[str] = []

@app.post("/items/", response_model=Item, summary="Create an item")
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    \f
    :param item: User input.
    """
    return item

async def goto_sleep(text, sleeptime):
    print(f"before sleep {text}")
    await asyncio.sleep(sleeptime)
    print(f"after sleep {text}")
    return f"{text} {sleeptime}"

@app.get("/slow")
async def slowresponse(st: int = 5):
    print("below slowresponse starts")
    sleptfor_one, sleptfor_two = await asyncio.gather(
        goto_sleep("one", st),
        goto_sleep("two", st),
    )
    print("after slowresponse {} {}".format(sleptfor_one, sleptfor_two))
    
    return {"slow": "completed"}

if __name__ == "__main__":
    uvicorn.run("fastapi_runner:app")
