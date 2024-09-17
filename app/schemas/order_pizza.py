# app/schemas/order_pizza.py
from pydantic import BaseModel

class OrderPizzaBase(BaseModel):
    order_id: int
    pizza_id: int
    quantity: int
    price: float

class OrderPizzaCreate(OrderPizzaBase):
    pass

class OrderPizzaUpdate(OrderPizzaBase):
    quantity: int | None = None
    price: float | None = None

class OrderPizzaResponse(OrderPizzaBase):
    id: int

    class Config:
        orm_mode = True
