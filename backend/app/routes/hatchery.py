"""Hatchery Routes"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Hatchery
from app.schemas import HatcheryCreate, HatcheryUpdate, HatcheryResponse
from typing import List

router = APIRouter(prefix="/hatchery", tags=["Hatchery"])


@router.get("/", response_model=List[HatcheryResponse])
async def list_hatchery(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """List all hatchery batches"""
    batches = db.query(Hatchery).offset(skip).limit(limit).all()
    return batches


@router.get("/{hatchery_id}", response_model=HatcheryResponse)
async def get_hatchery(hatchery_id: int, db: Session = Depends(get_db)):
    """Get hatchery batch by ID"""
    hatchery = db.query(Hatchery).filter(Hatchery.id == hatchery_id).first()
    if not hatchery:
        raise HTTPException(status_code=404, detail="Hatchery batch not found")
    return hatchery


@router.post("/", response_model=HatcheryResponse)
async def create_hatchery(hatchery: HatcheryCreate, db: Session = Depends(get_db)):
    """Create new hatchery batch"""
    db_hatchery = Hatchery(**hatchery.dict())
    db.add(db_hatchery)
    db.commit()
    db.refresh(db_hatchery)
    return db_hatchery


@router.put("/{hatchery_id}", response_model=HatcheryResponse)
async def update_hatchery(
    hatchery_id: int,
    hatchery: HatcheryUpdate,
    db: Session = Depends(get_db)
):
    """Update hatchery batch"""
    db_hatchery = db.query(Hatchery).filter(Hatchery.id == hatchery_id).first()
    if not db_hatchery:
        raise HTTPException(status_code=404, detail="Hatchery batch not found")
    
    # Calculate hatch rate
    update_data = hatchery.dict(exclude_unset=True)
    if "eggs_hatched" in update_data:
        update_data["hatch_rate"] = (update_data["eggs_hatched"] / db_hatchery.total_eggs) * 100
    
    for key, value in update_data.items():
        setattr(db_hatchery, key, value)
    
    db.commit()
    db.refresh(db_hatchery)
    return db_hatchery


@router.delete("/{hatchery_id}")
async def delete_hatchery(hatchery_id: int, db: Session = Depends(get_db)):
    """Delete hatchery batch"""
    db_hatchery = db.query(Hatchery).filter(Hatchery.id == hatchery_id).first()
    if not db_hatchery:
        raise HTTPException(status_code=404, detail="Hatchery batch not found")
    
    db.delete(db_hatchery)
    db.commit()
    return {"message": "Hatchery batch deleted successfully"}
