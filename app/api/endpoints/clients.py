# app/api/endpoints/clients.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.client import ClientCreate, ClientResponse, ClientUpdate
from app.crud.client import create_client, get_clients, get_client, update_client, delete_client
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ClientResponse)
def create_client_view(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, client)

@router.get("/", response_model=list[ClientResponse])
def get_clients_view(db: Session = Depends(get_db)):
    return get_clients(db)

@router.get("/{client_id}", response_model=ClientResponse)
def get_client_view(client_id: int, db: Session = Depends(get_db)):
    client = get_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/{client_id}", response_model=ClientResponse)
def update_client_view(client_id: int, client_update: ClientUpdate, db: Session = Depends(get_db)):
    client = update_client(db, client_id, client_update)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.delete("/{client_id}")
def delete_client_view(client_id: int, db: Session = Depends(get_db)):
    client = delete_client(db, client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"detail": "Client deleted"}
