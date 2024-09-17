# app/schemas/settings.py
from pydantic import BaseModel

class SettingsBase(BaseModel):
    restaurant_id: int
    is_delivery_available: bool | None = True
    delivery_fee: float | None = None
    minimum_order_value: float | None = None
    open_time: str | None = None
    close_time: str | None = None

class SettingsCreate(SettingsBase):
    pass

class SettingsUpdate(SettingsBase):
    pass

class SettingsResponse(SettingsBase):
    id: int

    class Config:
        orm_mode = True
