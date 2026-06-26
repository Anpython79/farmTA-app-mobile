"""Animal Schemas"""

from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class AnimalBase(BaseModel):
    """Base animal schema"""
    name: str
    species: str
    breed: Optional[str] = None
    line: Optional[str] = None
    gender: Optional[str] = "Other"
    date_of_birth: Optional[date] = None
    weight: Optional[float] = None
    health_status: Optional[str] = "Healthy"
    color_marking: Optional[str] = None
    microchip_id: Optional[str] = None
    notes: Optional[str] = None


class AnimalCreate(AnimalBase):
    """Animal creation schema"""
    user_id: int


class AnimalUpdate(BaseModel):
    """Animal update schema"""
    name: Optional[str] = None
    weight: Optional[float] = None
    health_status: Optional[str] = None
    notes: Optional[str] = None


class AnimalResponse(AnimalBase):
    """Animal response schema"""
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
