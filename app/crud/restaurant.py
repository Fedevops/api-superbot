from sqlalchemy.orm import Session
from app.models.restaurant import Restaurant
from app.schemas.restaurant import RestaurantCreate, RestaurantUpdate

def create_restaurant(db: Session, restaurant: RestaurantCreate):
    db_restaurant = Restaurant(name=restaurant.name, address=restaurant.address, phone=restaurant.phone, email=restaurant.email)
    db.add(db_restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant

def get_restaurants(db: Session):
    return db.query(Restaurant).all()

def get_restaurant(db: Session, restaurant_id: int):
    return db.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

def update_restaurant(db: Session, restaurant_id: int, restaurant_update: RestaurantUpdate):
    db_restaurant = get_restaurant(db, restaurant_id)
    if db_restaurant:
        db_restaurant.name = restaurant_update.name or db_restaurant.name
        db_restaurant.address = restaurant_update.address or db_restaurant.address
        db_restaurant.phone = restaurant_update.phone or db_restaurant.phone
        db_restaurant.email = restaurant_update.email or db_restaurant.email
        db.commit()
        db.refresh(db_restaurant)
    return db_restaurant

def delete_restaurant(db: Session, restaurant_id: int):
    db_restaurant = get_restaurant(db, restaurant_id)
    if db_restaurant:
        db.delete(db_restaurant)
        db.commit()
    return db_restaurant
