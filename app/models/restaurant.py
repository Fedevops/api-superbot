# app/models/restaurant.py
from sqlalchemy import Column, Integer, String, Enum as SQLAlchemyEnum
from app.core.database import Base
from enum import Enum

class RestaurantStatusEnum(str, Enum):
    active = "Active"
    inactive = "Inactive"
    blocked = "Blocked"

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False, unique=True)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=True)
    cnpj = Column(String, nullable=False, unique=True)
    status =  Column(SQLAlchemyEnum(RestaurantStatusEnum), nullable=False)  

