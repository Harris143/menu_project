from fastapi import FastAPI, HTTPException, Query
from typing import Optional
from schemas import MenuItemCreate, MenuItemResponse
from menu_model import MenuItem
import menu_crud
from fastapi import status


app = FastAPI(title="Menu Management API")


@app.get("/menu", response_model=dict)
def get_all_menu():
    items = menu_crud.get_all_items()
    if not items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return {"data": items, "msg": "Success"}


@app.get("/menu/item", response_model=MenuItemResponse)
def get_menu_item(id: Optional[int] = Query(default=None),
                  name: Optional[str] = Query(default=None)):
    if not id and not name:
        raise HTTPException(status_code=400, detail="Bad request - must provide 'id' or 'name'")

    if id:
        item = menu_crud.get_item_by_id(id)
    else:
        item = menu_crud.get_item_by_name(name)

    if not item:
        raise HTTPException(status_code=404, detail="Not found")

    return item


@app.post("/menu", response_model=dict, status_code=status.HTTP_201_CREATED)
def post_menu(item: MenuItemCreate):
    if item.id is None or item.name is None:
        raise HTTPException(status_code=400, detail={"msg": "missing field"})

    new_item = MenuItem(**item.model_dump())
    menu_crud.insert_or_update(new_item)
    return {"msg": "Item created successfully"}


@app.put("/menu/{item_id}", response_model=dict)
def put_menu(item_id: int, item: MenuItemCreate):
    if item.id != item_id:
        raise HTTPException(status_code=400, detail={"msg": "ID update not allowed"})

    updated = menu_crud.update_item(item_id, MenuItem(**item.model_dump()))
    if not updated:
        raise HTTPException(status_code=404, detail={"msg": "Failed to update, record not found"})
    return {"msg": "Item updated successfully"}


@app.delete("/menu/{item_id}")
def delete_menu(item_id: int):
    success = menu_crud.delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail={"msg": "Failed to delete, record not found"})
    return {"msg": "Item Deleted successfully"}
