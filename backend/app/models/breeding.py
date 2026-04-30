"""Breeding History Model"""

from sqlalchemy import Column, Integer, Date, DateTime, Text, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class BreedingHistory(Base):
    """Breeding history record model"""
    __tablename__ = "breeding_history"
    
    id = Column(Integer, primary_key=True, index=True)
    male_id = Column(Integer, ForeignKey("animals.id"), nullable=False, index=True)
    female_id = Column(Integer, ForeignKey("animals.id"), nullable=False, index=True)
    breeding_date = Column(Date, nullable=False, index=True)
    expected_birth_date = Column(Date)
    actual_birth_date = Column(Date)
    number_of_offspring = Column(Integer)
    number_survived = Column(Integer)
    breeding_status = Column(String(50))  # In progress, Completed, Failed
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    male = relationship("Animal", foreign_keys=[male_id], back_populates="breeding_records")
    female = relationship("Animal", foreign_keys=[female_id])
    
    class Config:
        from_attributes = True
