"""User Schemas"""

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    """Base user schema"""
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    phone: Optional[str] = None
    farm_name: Optional[str] = None
    farm_location: Optional[str] = None


class UserCreate(UserBase):
    """User creation schema"""
    password: str


class UserLogin(BaseModel):
    """User login schema"""
    username: str
    password: str


class UserResponse(UserBase):
    """User response schema"""
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
