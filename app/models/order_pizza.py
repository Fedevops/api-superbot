# app/models/order_pizza.py
from sqlalchemy import Column, Integer, ForeignKey, Float
from app.core.database import Base

class OrderPizza(Base):
    __tablename__ = "order_pizzas"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    pizza_id = Column(Integer, ForeignKey("pizzas.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
