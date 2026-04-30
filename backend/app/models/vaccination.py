"""Vaccination Model"""

from sqlalchemy import Column, Integer, String, Date, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Vaccination(Base):
    """Vaccination record model"""
    __tablename__ = "vaccinations"
    
    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(Integer, ForeignKey("animals.id"), nullable=False, index=True)
    vaccine_name = Column(String(100), nullable=False)
    vaccine_type = Column(String(100))  # Inactivated, Live, etc.
    vaccination_date = Column(Date, nullable=False, index=True)
    next_vaccination_date = Column(Date)
    veterinarian = Column(String(100))
    batch_number = Column(String(100))
    side_effects = Column(Text)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    animal = relationship("Animal", back_populates="vaccinations")
    
    class Config:
        from_attributes = True
