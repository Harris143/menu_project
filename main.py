from fastapi import FastAPI, HTTPException
from menu_model import MenuItem
import menu_crud

app = FastAPI()

@app.get("/menu", response_model=list[MenuItem])
def get_menu():
    return menu_crud.get_menu_items()

@app.post("/menu", response_model=MenuItem)
def post_menu_item(item: MenuItem):
    return menu_crud.add_or_update_menu_item(item)

@app.put("/menu/{item_id}", response_model=MenuItem)
def put_menu_item(item_id: int, item: MenuItem):
    updated_item = menu_crud.update_menu_item(item_id, item)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return updated_item

@app.delete("/menu/{item_id}")
def delete_menu_item(item_id: int):
    success = menu_crud.delete_menu_item(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Menu item not found")
    return {"ok": True}
