import json
from fastapi import FastAPI
from models import StoreItem


app = FastAPI()

with open("store_items.json", "r") as f:
    data: list[dict] = json.load(f)


items: list[StoreItem] = []

for item in data:
    items.append(StoreItem(**item))

@app.get("/items")
async def get_items() -> list[StoreItem]:
    return items

@app.post("/items")
async def create_item(store_item: StoreItem):
    items.append(store_item)

@app.put("/items/{item_id}")
async def update_item(item_id: int, updated_item: StoreItem) -> None:
    for i, item in enumerate(items):
        if item.id == item_id:
            items[i] = updated_item
            return
        
@app.delete("/items/{item_id}")
async def delete_item(item_id: int) -> None:
    for i, item in enumerate(items):
        if item.id == item_id:
            items.pop(i)
            return

