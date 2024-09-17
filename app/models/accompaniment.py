# app/models/accompaniment.py
from sqlalchemy import Column, Integer, String, Float
from app.core.database import Base

class Accompaniment(Base):
    __tablename__ = "accompaniments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    price = Column(Float, nullable=False)
