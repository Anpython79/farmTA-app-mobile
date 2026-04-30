"""Lineage/Pedigree Model"""

from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Lineage(Base):
    """Pedigree/Lineage tracking model"""
    __tablename__ = "lineage"
    
    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(Integer, ForeignKey("animals.id"), nullable=False, index=True)
    father_id = Column(Integer, ForeignKey("animals.id"), index=True)
    mother_id = Column(Integer, ForeignKey("animals.id"), index=True)
    generation = Column(Integer, default=0)
    line_name = Column(String(100))  # e.g., "Brown Leghorn Line A"
    line_characteristics = Column(Text)  # Key traits of this line
    coi = Column(Float, default=0.0)  # Coefficient of Inbreeding
    inbreeding_warning = Column(String(255))  # Warning message if high COI
    genetic_notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    animal = relationship("Animal", foreign_keys=[animal_id], back_populates="lineage")
    
    class Config:
        from_attributes = True
