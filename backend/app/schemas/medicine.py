"""Medicine and Treatment Schemas"""

from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class MedicineBase(BaseModel):
    """Base medicine schema"""
    name: str
    medicine_type: Optional[str] = None
    dosage: Optional[str] = None
    quantity_in_stock: Optional[float] = None
    unit: Optional[str] = None
    cost_per_unit: Optional[float] = None
    expiry_date: Optional[date] = None
    supplier: Optional[str] = None


class MedicineCreate(MedicineBase):
    """Medicine creation schema"""
    pass


class MedicineResponse(MedicineBase):
    """Medicine response schema"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class TreatmentBase(BaseModel):
    """Base treatment schema"""
    animal_id: int
    medicine_id: int
    disease_diagnosed: str
    start_date: date
    end_date: Optional[date] = None
    dosage: Optional[str] = None
    frequency: Optional[str] = None
    status: Optional[str] = "Ongoing"
    notes: Optional[str] = None


class TreatmentCreate(TreatmentBase):
    """Treatment creation schema"""
    pass


class TreatmentResponse(TreatmentBase):
    """Treatment response schema"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
