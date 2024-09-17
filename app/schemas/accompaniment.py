# app/schemas/accompaniment.py
from pydantic import BaseModel

class AccompanimentBase(BaseModel):
    name: str
    price: float

class AccompanimentCreate(AccompanimentBase):
    pass

class AccompanimentUpdate(AccompanimentBase):
    name: str | None = None
    price: float | None = None

class AccompanimentResponse(AccompanimentBase):
    id: int

    class Config:
        orm_mode = True
