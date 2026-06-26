"""Hatchery Schemas"""

from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class HatcheryBase(BaseModel):
    """Base hatchery schema"""
    animal_id: int
    batch_name: str
    batch_date: date
    total_eggs: int
    hatch_date_expected: Optional[date] = None
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    status: Optional[str] = "Incubating"
    notes: Optional[str] = None


class HatcheryCreate(HatcheryBase):
    """Hatchery creation schema"""
    pass


class HatcheryUpdate(BaseModel):
    """Hatchery update schema"""
    temperature: Optional[float] = None
    humidity: Optional[float] = None
    eggs_hatched: Optional[int] = None
    status: Optional[str] = None
    notes: Optional[str] = None


class HatcheryResponse(HatcheryBase):
    """Hatchery response schema"""
    id: int
    eggs_hatched: int
    hatch_rate: float
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
