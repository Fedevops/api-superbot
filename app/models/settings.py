# app/models/settings.py
from sqlalchemy import Column, Integer, String,ForeignKey, Boolean, Float
from app.core.database import Base

class Settings(Base):
    __tablename__ = "settings"

    id = Column(Integer, primary_key=True, index=True)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    is_delivery_available = Column(Boolean, default=True)
    delivery_fee = Column(Float, nullable=True)
    minimum_order_value = Column(Float, nullable=True)
    open_time = Column(String, nullable=True)
    close_time = Column(String, nullable=True)
