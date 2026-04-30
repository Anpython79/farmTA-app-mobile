"""Medicine and Treatment Models"""

from sqlalchemy import Column, Integer, String, Date, DateTime, Text, ForeignKey, Float, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base
import enum


class MedicineTypeEnum(str, enum.Enum):
    """Medicine type"""
    ANTIBIOTIC = "Antibiotic"
    ANTIVIRAL = "Antiviral"
    ANTIFUNGAL = "Antifungal"
    ANTIPARA = "Antiparasitic"
    VITAMIN = "Vitamin"
    SUPPLEMENT = "Supplement"
    OTHER = "Other"


class TreatmentStatusEnum(str, enum.Enum):
    """Treatment status"""
    ONGOING = "Ongoing"
    COMPLETED = "Completed"
    DISCONTINUED = "Discontinued"


class Medicine(Base):
    """Medicine inventory model"""
    __tablename__ = "medicines"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    medicine_type = Column(Enum(MedicineTypeEnum))
    description = Column(Text)
    active_ingredient = Column(String(255))
    dosage = Column(String(100))  # e.g., "500mg per tablet"
    administration_route = Column(String(50))  # Oral, Injectable, Topical, etc.
    quantity_in_stock = Column(Float)
    unit = Column(String(20))  # Tablets, ml, grams, etc.
    cost_per_unit = Column(Float)
    expiry_date = Column(Date)
    supplier = Column(String(100))
    side_effects = Column(Text)
    contraindications = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    treatments = relationship("Treatment", back_populates="medicine")
    
    class Config:
        from_attributes = True


class Treatment(Base):
    """Treatment record model"""
    __tablename__ = "treatments"
    
    id = Column(Integer, primary_key=True, index=True)
    animal_id = Column(Integer, ForeignKey("animals.id"), nullable=False, index=True)
    medicine_id = Column(Integer, ForeignKey("medicines.id"), nullable=False)
    disease_diagnosed = Column(String(255), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)
    dosage = Column(String(100))
    frequency = Column(String(100))  # e.g., "2 times daily for 5 days"
    status = Column(Enum(TreatmentStatusEnum), default=TreatmentStatusEnum.ONGOING)
    recovery_date = Column(Date)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    animal = relationship("Animal", back_populates="treatments")
    medicine = relationship("Medicine", back_populates="treatments")
    
    class Config:
        from_attributes = True
