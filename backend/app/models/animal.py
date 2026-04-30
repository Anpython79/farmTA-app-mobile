"""Animal Model"""

from sqlalchemy import Column, Integer, String, Float, Date, DateTime, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum


class GenderEnum(str, enum.Enum):
    """Gender enumeration"""
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class HealthStatusEnum(str, enum.Enum):
    """Health status enumeration"""
    HEALTHY = "Healthy"
    SICK = "Sick"
    RECOVERING = "Recovering"
    QUARANTINE = "Quarantine"


class Animal(Base):
    """Animal model"""
    __tablename__ = "animals"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(100), nullable=False, index=True)
    species = Column(String(50), nullable=False, index=True)  # Chicken, Duck, Pig, etc.
    breed = Column(String(100))
    line = Column(String(100))  # Chicken line/bloodline
    gender = Column(Enum(GenderEnum), default=GenderEnum.OTHER)
    date_of_birth = Column(Date)
    weight = Column(Float)  # in kg
    health_status = Column(Enum(HealthStatusEnum), default=HealthStatusEnum.HEALTHY)
    color_marking = Column(String(255))  # Physical description
    microchip_id = Column(String(50), unique=True)
    identification_photo = Column(Text)  # URL or path
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    vaccinations = relationship("Vaccination", back_populates="animal")
    breeding_records = relationship("BreedingHistory", foreign_keys="BreedingHistory.male_id", back_populates="male")
    lineage = relationship("Lineage", back_populates="animal")
    hatchery = relationship("Hatchery", back_populates="animal")
    treatments = relationship("Treatment", back_populates="animal")
    health_records = relationship("HealthRecord", back_populates="animal")
    
    class Config:
        from_attributes = True
