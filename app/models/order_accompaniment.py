# app/models/order_accompaniment.py
from sqlalchemy import Column, Integer, ForeignKey, Float
from app.core.database import Base

class OrderAccompaniment(Base):
    __tablename__ = "order_accompaniments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    accompaniment_id = Column(Integer, ForeignKey("accompaniments.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
