# app/crud/settings.py
from sqlalchemy.orm import Session
from app.models.settings import Settings
from app.schemas.settings import SettingsCreate, SettingsUpdate

def create_settings(db: Session, settings: SettingsCreate):
    db_settings = Settings(
        restaurant_id=settings.restaurant_id,
        is_delivery_available=settings.is_delivery_available,
        delivery_fee=settings.delivery_fee,
        minimum_order_value=settings.minimum_order_value,
        open_time=settings.open_time,
        close_time=settings.close_time,
    )
    db.add(db_settings)
    db.commit()
    db.refresh(db_settings)
    return db_settings

def get_settings(db: Session, restaurant_id: int):
    return db.query(Settings).filter(Settings.restaurant_id == restaurant_id).first()

def update_settings(db: Session, restaurant_id: int, settings_update: SettingsUpdate):
    db_settings = get_settings(db, restaurant_id)
    if db_settings:
        db_settings.is_delivery_available = settings_update.is_delivery_available or db_settings.is_delivery_available
        db_settings.delivery_fee = settings_update.delivery_fee or db_settings.delivery_fee
        db_settings.minimum_order_value = settings_update.minimum_order_value or db_settings.minimum_order_value
        db_settings.open_time = settings_update.open_time or db_settings.open_time
        db_settings.close_time = settings_update.close_time or db_settings.close_time
        db.commit()
        db.refresh(db_settings)
    return db_settings
