from pydantic import BaseModel

class MenuItem(BaseModel):
    id: int
    name: str
    price: float
    description: str = ""
