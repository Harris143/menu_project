from fastapi import FastAPI, HTTPException
from schemas import MenuItemCreate, MenuItemResponse
from menu_model import MenuItem
import menu_crud

app = FastAPI(title="Menu Management API")

@app.get("/menu", response_model=list[MenuItemResponse])
def get_menu():
    return menu_crud.get_all_items()

@app.post("/menu", response_model=MenuItemResponse)
def post_menu(item: MenuItemCreate):
    new_item = MenuItem(**item.model_dump())
    return menu_crud.insert_or_update(new_item)

@app.put("/menu/{item_id}", response_model=MenuItemResponse)
def put_menu(item_id: int, item: MenuItemCreate):
    updated = menu_crud.update_item(item_id, MenuItem(**item.model_dump()))
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return updated

@app.delete("/menu/{item_id}")
def delete_menu(item_id: int):
    success = menu_crud.delete_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"ok": True}
