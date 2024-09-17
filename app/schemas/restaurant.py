# app/schemas/restaurant.py
from pydantic import BaseModel
from enum import Enum

class RestaurantStatusEnum(str, Enum):
    active = "Active"
    inactive = "Inactive"
    blocked = "Blocked"


class RestaurantBase(BaseModel):
    name: str
    address: str
    status: RestaurantStatusEnum
    phone: str
    email: str | None = None
    cnpj: str | None = None

class RestaurantCreate(RestaurantBase):
    pass

class RestaurantUpdate(RestaurantBase):
    name: str | None = None
    address: str | None = None
    status: RestaurantStatusEnum | None = None
    phone: str | None = None
    email: str | None = None
    cnpj: str | None = None

class RestaurantResponse(RestaurantBase):
    id: int

    class Config:
        orm_mode = True
