# app/schemas/pizza.py
from pydantic import BaseModel
from enum import Enum

class PizzaSizeEnum(str, Enum):
    small = "Small"
    medium = "Medium"
    large = "Large"

class PizzaStatusEnum(str, Enum):
    available = "Available"
    unavailable = "Unavailable"

class PizzaBase(BaseModel):
    name: str
    size: PizzaSizeEnum
    status: PizzaStatusEnum
    price: float
    ingredients: str

class PizzaCreate(PizzaBase):
    pass

class PizzaUpdate(PizzaBase):
    name: str | None = None
    size: PizzaSizeEnum | None = None
    status: PizzaStatusEnum | None = None
    price: float | None = None
    ingredients: str | None = None

class PizzaResponse(PizzaBase):
    id: int

    class Config:
        orm_mode = True
