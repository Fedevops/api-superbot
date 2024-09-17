from sqlalchemy.orm import Session
from app.models.pizza import Pizza
from app.schemas.pizza import PizzaCreate, PizzaUpdate

def create_pizza(db: Session, pizza: PizzaCreate):
    db_pizza = Pizza(name=pizza.name, size=pizza.size, price=pizza.price, ingredients=pizza.ingredients)
    db.add(db_pizza)
    db.commit()
    db.refresh(db_pizza)
    return db_pizza

def get_pizzas(db: Session):
    return db.query(Pizza).all()

def get_pizza(db: Session, pizza_id: int):
    return db.query(Pizza).filter(Pizza.id == pizza_id).first()

def update_pizza(db: Session, pizza_id: int, pizza_update: PizzaUpdate):
    db_pizza = get_pizza(db, pizza_id)
    if db_pizza:
        db_pizza.name = pizza_update.name or db_pizza.name
        db_pizza.size = pizza_update.size or db_pizza.size
        db_pizza.price = pizza_update.price or db_pizza.price
        db_pizza.ingredients = pizza_update.ingredients or db_pizza.ingredients
        db.commit()
        db.refresh(db_pizza)
    return db_pizza

def delete_pizza(db: Session, pizza_id: int):
    db_pizza = get_pizza(db, pizza_id)
    if db_pizza:
        db.delete(db_pizza)
        db.commit()
    return db_pizza
