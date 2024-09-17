# app/api/endpoints/settings.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.settings import SettingsCreate, SettingsResponse, SettingsUpdate
from app.crud.settings import create_settings, get_settings, update_settings
from app.core.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=SettingsResponse)
def create_settings_view(settings: SettingsCreate, db: Session = Depends(get_db)):
    return create_settings(db, settings)

@router.get("/{restaurant_id}", response_model=SettingsResponse)
def get_settings_view(restaurant_id: int, db: Session = Depends(get_db)):
    settings = get_settings(db, restaurant_id)
    if not settings:
        raise HTTPException(status_code=404, detail="Settings not found for this restaurant")
    return settings

@router.put("/{restaurant_id}", response_model=SettingsResponse)
def update_settings_view(restaurant_id: int, settings_update: SettingsUpdate, db: Session = Depends(get_db)):
    settings = update_settings(db, restaurant_id, settings_update)
    if not settings:
        raise HTTPException(status_code=404, detail="Settings not found for this restaurant")
    return settings
