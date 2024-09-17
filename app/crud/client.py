from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client import ClientCreate, ClientUpdate

def create_client(db: Session, client: ClientCreate):
    db_client = Client(name=client.name, phone=client.phone, email=client.email, address=client.address)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(db: Session):
    return db.query(Client).all()

def get_client(db: Session, client_id: int):
    return db.query(Client).filter(Client.id == client_id).first()

def update_client(db: Session, client_id: int, client_update: ClientUpdate):
    db_client = get_client(db, client_id)
    if db_client:
        db_client.name = client_update.name or db_client.name
        db_client.phone = client_update.phone or db_client.phone
        db_client.email = client_update.email or db_client.email
        db_client.address = client_update.address or db_client.address
        db.commit()
        db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = get_client(db, client_id)
    if db_client:
        db.delete(db_client)
        db.commit()
    return db_client
