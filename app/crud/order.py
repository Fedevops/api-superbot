from sqlalchemy.orm import Session
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate

def create_order(db: Session, order: OrderCreate):
    db_order = Order(client_id=order.client_id, restaurant_id=order.restaurant_id, total_price=order.total_price)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_orders(db: Session):
    return db.query(Order).all()

def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()

def update_order(db: Session, order_id: int, order_update: OrderUpdate):
    db_order = get_order(db, order_id)
    if db_order:
        db_order.total_price = order_update.total_price or db_order.total_price
        db.commit()
        db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int):
    db_order = get_order(db, order_id)
    if db_order:
        db.delete(db_order)
        db.commit()
    return db_order
