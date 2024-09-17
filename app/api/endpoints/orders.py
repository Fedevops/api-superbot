# app/api/endpoints/orders.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.order import OrderCreate, OrderResponse, OrderUpdate
from app.crud.order import create_order, get_orders, get_order, update_order, delete_order
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OrderResponse)
def create_order_view(order: OrderCreate, db: Session = Depends(get_db)):
    return create_order(db, order)

@router.get("/", response_model=list[OrderResponse])
def get_orders_view(db: Session = Depends(get_db)):
    return get_orders(db)

@router.get("/{order_id}", response_model=OrderResponse)
def get_order_view(order_id: int, db: Session = Depends(get_db)):
    order = get_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.put("/{order_id}", response_model=OrderResponse)
def update_order_view(order_id: int, order_update: OrderUpdate, db: Session = Depends(get_db)):
    order = update_order(db, order_id, order_update)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.delete("/{order_id}")
def delete_order_view(order_id: int, db: Session = Depends(get_db)):
    order = delete_order(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"detail": "Order deleted"}
