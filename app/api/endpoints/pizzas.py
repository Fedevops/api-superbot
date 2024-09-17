# app/api/endpoints/pizzas.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.pizza import PizzaCreate, PizzaResponse, PizzaUpdate
from app.crud.pizza import create_pizza, get_pizzas, get_pizza, update_pizza, delete_pizza
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PizzaResponse)
def create_pizza_view(pizza: PizzaCreate, db: Session = Depends(get_db)):
    return create_pizza(db, pizza)

@router.get("/", response_model=list[PizzaResponse])
def get_pizzas_view(db: Session = Depends(get_db)):
    return get_pizzas(db)

@router.get("/{pizza_id}", response_model=PizzaResponse)
def get_pizza_view(pizza_id: int, db: Session = Depends(get_db)):
    pizza = get_pizza(db, pizza_id)
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return pizza

@router.put("/{pizza_id}", response_model=PizzaResponse)
def update_pizza_view(pizza_id: int, pizza_update: PizzaUpdate, db: Session = Depends(get_db)):
    pizza = update_pizza(db, pizza_id, pizza_update)
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return pizza

@router.delete("/{pizza_id}")
def delete_pizza_view(pizza_id: int, db: Session = Depends(get_db)):
    pizza = delete_pizza(db, pizza_id)
    if not pizza:
        raise HTTPException(status_code=404, detail="Pizza not found")
    return {"detail": "Pizza deleted"}
