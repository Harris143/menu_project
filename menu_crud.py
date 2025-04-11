from typing import List, Optional
from menu_model import MenuItem
from database import menu_db

def get_all_items() -> List[MenuItem]:
    return list(menu_db.values())

def insert_or_update(item: MenuItem) -> MenuItem:
    menu_db[item.id] = item
    return item

def update_item(item_id: int, item: MenuItem) -> Optional[MenuItem]:
    if item_id in menu_db:
        menu_db[item_id] = item
        return item
    return None

def delete_item(item_id: int) -> bool:
    return menu_db.pop(item_id, None) is not None

def get_item_by_id(item_id: int) -> Optional[MenuItem]:
    return menu_db.get(item_id)

def get_item_by_name(name: str) -> Optional[MenuItem]:
    for item in menu_db.values():
        if item.name.lower() == name.lower():
            return item
    return None
