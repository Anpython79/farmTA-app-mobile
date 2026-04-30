"""Cost Management Model"""

from sqlalchemy import Column, Integer, String, Float, Date, DateTime, Text, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum


class CostCategoryEnum(str, enum.Enum):
    """Cost category enumeration"""
    FEED = "Feed"
    MEDICINE = "Medicine"
    VACCINE = "Vaccine"
    LABOR = "Labor"
    UTILITIES = "Utilities"
    EQUIPMENT = "Equipment"
    MAINTENANCE = "Maintenance"
    TRANSPORT = "Transport"
    OTHER = "Other"


class Cost(Base):
    """Cost tracking model"""
    __tablename__ = "costs"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    animal_id = Column(Integer, ForeignKey("animals.id"), index=True)  # Optional - for specific animal
    category = Column(Enum(CostCategoryEnum), nullable=False, index=True)
    description = Column(String(255), nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String(3), default="VND")  # ISO 4217 currency code
    cost_date = Column(Date, nullable=False, index=True)
    payment_method = Column(String(50))  # Cash, Check, Card, Bank Transfer, etc.
    reference_number = Column(String(100))  # Invoice number, receipt, etc.
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    class Config:
        from_attributes = True
