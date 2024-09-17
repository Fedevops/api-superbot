# app/schemas/order.py
from pydantic import BaseModel
from typing import List
from app.schemas.pizza import PizzaResponse
from app.schemas.accompaniment import AccompanimentResponse

class OrderBase(BaseModel):
    client_id: int
    restaurant_id: int
    total_price: float

class OrderCreate(OrderBase):
    pizzas: List[PizzaResponse]
    accompaniments: List[AccompanimentResponse] | None = None

class OrderUpdate(OrderBase):
    total_price: float | None = None
    pizzas: List[PizzaResponse] | None = None
    accompaniments: List[AccompanimentResponse] | None = None

class OrderResponse(OrderBase):
    id: int
    pizzas: List[PizzaResponse]
    accompaniments: List[AccompanimentResponse] | None = None

    class Config:
        orm_mode = True
