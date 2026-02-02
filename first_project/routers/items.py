from fastapi import APIRouter, HTTPException
from fastapi import status 
from typing import List
from first_project.schemes.item import Item
from first_project.dummy_db import items


router = APIRouter()


@router.get("/items")
async def show_all_items() -> List:
    return list(items.values())




@router.get("/items/{item_id}")
async def get_item_using_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return items[item_id]



@router.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: Item) -> Item:
    new_id = max(items.keys()) + 1
    items[new_id] = {'id': new_id, **item.dict()}
    return items[new_id]



@router.put("/items/{item_id}", response_model=Item, status_code=status.HTTP_200_OK)
async def update_item(item_id: int, new_item: Item) -> Item:
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    items[item_id] = {'id': item_id, **new_item.dict()}
    return items[item_id]

@router.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int) -> None:
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    del items[item_id]
    return None


