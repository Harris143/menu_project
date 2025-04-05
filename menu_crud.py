from typing import Dict, List
from menu_model import MenuItem

menu_db: Dict[int, MenuItem] = {}

def get_menu_items() -> List[MenuItem]:
    return list(menu_db.values())

def add_or_update_menu_item(item: MenuItem) -> MenuItem:
    menu_db[item.id] = item
    return item

def update_menu_item(item_id: int, item: MenuItem) -> MenuItem:
    if item_id in menu_db:
        menu_db[item_id] = item
        return item
    return None

def delete_menu_item(item_id: int) -> bool:
    return menu_db.pop(item_id, None) is not None
