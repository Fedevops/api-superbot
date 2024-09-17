from pydantic import BaseModel

class OrderAccompanimentBase(BaseModel):
    order_id: int
    accompaniment_id: int
    quantity: int
    price: float

class OrderAccompanimentCreate(OrderAccompanimentBase):
    pass

class OrderAccompanimentUpdate(OrderAccompanimentBase):
    quantity: int | None = None
    price: float | None = None

class OrderAccompanimentResponse(OrderAccompanimentBase):
    id: int

    class Config:
        orm_mode = True
