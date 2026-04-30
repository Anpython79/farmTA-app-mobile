"""Hatchery Model for Egg Incubation Tracking"""

from sqlalchemy import Column, Integer, String, Date, DateTime, Text, ForeignKey, Float, Boolean, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum


class HatcheryStatusEnum(str, enum.Enum):
    """Hatchery batch status"""
    INCUBATING = "Incubating"
    HATCHING = "Hatching"
    COMPLETED = "Completed"
    FAILED = "Failed"


class EggStatusEnum(str, enum.Enum):
    """Individual egg status"""
    FERTILE = "Fertile"
    INFERTILE = "Infertile"
    DEAD = "Dead"
    HATCHED = "Hatched"
    DISCARDED = "Discarded"


class Hatchery(Base):
    """Hatchery batch tracking model"""
    __tablename__ = "hatchery"
    
    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(Integer, ForeignKey("animals.id"), nullable=False)  # Female parent
    batch_name = Column(String(100), nullable=False)
    batch_date = Column(Date, nullable=False, index=True)
    total_eggs = Column(Integer, nullable=False)
    hatch_date_expected = Column(Date)
    hatch_date_actual = Column(Date)
    eggs_hatched = Column(Integer, default=0)
    hatch_rate = Column(Float, default=0.0)  # Percentage
    temperature = Column(Float)  # Current temperature in Celsius
    humidity = Column(Float)  # Current humidity percentage
    status = Column(Enum(HatcheryStatusEnum), default=HatcheryStatusEnum.INCUBATING)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    animal = relationship("Animal", back_populates="hatchery")
    eggs = relationship("HatcheryEgg", back_populates="hatchery")
    
    class Config:
        from_attributes = True


class HatcheryEgg(Base):
    """Individual egg tracking in hatchery"""
    __tablename__ = "hatchery_eggs"
    
    id = Column(Integer, primary_key=True, index=True)
    hatchery_id = Column(Integer, ForeignKey("hatchery.id"), nullable=False, index=True)
    egg_number = Column(Integer, nullable=False)
    status = Column(Enum(EggStatusEnum), default=EggStatusEnum.FERTILE)
    weight = Column(Float)  # grams
    candling_date = Column(Date)  # Date of candling (checking embryo development)
    candling_result = Column(String(100))  # Good, Development issue, Dead, etc.
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    hatchery = relationship("Hatchery", back_populates="eggs")
    
    class Config:
        from_attributes = True
