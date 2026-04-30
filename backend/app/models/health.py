"""Health Record Model"""

from sqlalchemy import Column, Integer, String, Date, DateTime, Text, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class HealthRecord(Base):
    """Health record model for tracking illnesses and conditions"""
    __tablename__ = "health_records"
    
    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(Integer, ForeignKey("animals.id"), nullable=False, index=True)
    record_date = Column(Date, nullable=False, index=True)
    disease_name = Column(String(100))
    symptoms = Column(Text)
    diagnosis = Column(Text)
    treatment_applied = Column(Text)
    recovery_date = Column(Date)
    temperature = Column(Float)  # in Celsius
    weight = Column(Float)  # in kg
    appetite = Column(String(50))  # Normal, Reduced, Absent
    behavior_notes = Column(Text)
    veterinarian_notes = Column(Text)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    animal = relationship("Animal", back_populates="health_records")
    
    class Config:
        from_attributes = True
