# app/schemas/client.py
from pydantic import BaseModel

class ClientBase(BaseModel):
    name: str
    phone: str
    email: str | None = None
    address: str | None = None

class ClientCreate(ClientBase):
    pass

class ClientUpdate(ClientBase):
    name: str | None = None
    phone: str | None = None
    email: str | None = None
    address: str | None = None

class ClientResponse(ClientBase):
    id: int

    class Config:
        orm_mode = True
