# app/api/endpoints/restaurants.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.restaurant import RestaurantCreate, RestaurantResponse, RestaurantUpdate
from app.crud.restaurant import create_restaurant, get_restaurant, get_restaurants, update_restaurant, delete_restaurant
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=RestaurantResponse)
def create_restaurant_view(restaurant: RestaurantCreate, db: Session = Depends(get_db)):
    return create_restaurant(db, restaurant)

@router.get("/", response_model=list[RestaurantResponse])
def get_restaurants_view(db: Session = Depends(get_db)):
    return get_restaurants(db)

@router.get("/{restaurant_id}", response_model=RestaurantResponse)
def get_restaurant_view(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = get_restaurant(db, restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant

@router.put("/{restaurant_id}", response_model=RestaurantResponse)
def update_restaurant_view(restaurant_id: int, restaurant_update: RestaurantUpdate, db: Session = Depends(get_db)):
    restaurant = update_restaurant(db, restaurant_id, restaurant_update)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return restaurant

@router.delete("/{restaurant_id}")
def delete_restaurant_view(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = delete_restaurant(db, restaurant_id)
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return {"detail": "Restaurant deleted"}
