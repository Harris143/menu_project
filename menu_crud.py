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
