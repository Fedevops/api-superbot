# app/models/pizza.py
from sqlalchemy import Column, Integer, String, Float, Enum as SQLAlchemyEnum
from app.core.database import Base
from enum import Enum


class PizzaSizeEnum(str, Enum):
    small = "Small"
    medium = "Medium"
    large = "Large"

class PizzaStatusEnum(str, Enum):
    available = "Available"
    unavailable = "Unavailable"


class Pizza(Base):
    __tablename__ = "pizzas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    size = Column(SQLAlchemyEnum(PizzaSizeEnum), nullable=False)  # Enum para os tamanhos da pizza
    price = Column(Float, nullable=False)
    ingredients = Column(String, nullable=False) 
    status =  Column(SQLAlchemyEnum(PizzaStatusEnum), nullable=False)  
