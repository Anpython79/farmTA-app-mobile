"""Cost Schemas"""

from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class CostBase(BaseModel):
    """Base cost schema"""
    user_id: int
    category: str
    description: str
    amount: float
    currency: Optional[str] = "VND"
    cost_date: date
    payment_method: Optional[str] = None
    animal_id: Optional[int] = None
    notes: Optional[str] = None


class CostCreate(CostBase):
    """Cost creation schema"""
    pass


class CostUpdate(BaseModel):
    """Cost update schema"""
    description: Optional[str] = None
    amount: Optional[float] = None
    category: Optional[str] = None
    notes: Optional[str] = None


class CostResponse(CostBase):
    """Cost response schema"""
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
