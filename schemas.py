from pydantic import BaseModel

class MenuItemCreate(BaseModel):
    id: int
    name: str
    price: float
    description: str = ""

class MenuItemResponse(MenuItemCreate):
    pass
