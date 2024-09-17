# app/models/order.py
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    restaurant_id = Column(Integer, ForeignKey("restaurants.id"), nullable=False)
    total_price = Column(Float, nullable=False)
    order_date = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    client = relationship("Client", back_populates="orders")
    restaurant = relationship("Restaurant", back_populates="orders")
    pizzas = relationship("OrderPizza", back_populates="order")
    accompaniments = relationship("OrderAccompaniment", back_populates="order")
