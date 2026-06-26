"""Cost Management Routes"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Cost
from app.schemas import CostCreate, CostUpdate, CostResponse
from typing import List, Dict
from datetime import date, timedelta

router = APIRouter(prefix="/costs", tags=["Costs"])


@router.get("/", response_model=List[CostResponse])
async def list_costs(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """List all costs"""
    costs = db.query(Cost).offset(skip).limit(limit).all()
    return costs


@router.get("/{cost_id}", response_model=CostResponse)
async def get_cost(cost_id: int, db: Session = Depends(get_db)):
    """Get cost by ID"""
    cost = db.query(Cost).filter(Cost.id == cost_id).first()
    if not cost:
        raise HTTPException(status_code=404, detail="Cost not found")
    return cost


@router.post("/", response_model=CostResponse)
async def create_cost(cost: CostCreate, db: Session = Depends(get_db)):
    """Create new cost record"""
    db_cost = Cost(**cost.dict())
    db.add(db_cost)
    db.commit()
    db.refresh(db_cost)
    return db_cost


@router.put("/{cost_id}", response_model=CostResponse)
async def update_cost(
    cost_id: int,
    cost: CostUpdate,
    db: Session = Depends(get_db)
):
    """Update cost record"""
    db_cost = db.query(Cost).filter(Cost.id == cost_id).first()
    if not db_cost:
        raise HTTPException(status_code=404, detail="Cost not found")
    
    update_data = cost.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_cost, key, value)
    
    db.commit()
    db.refresh(db_cost)
    return db_cost


@router.delete("/{cost_id}")
async def delete_cost(cost_id: int, db: Session = Depends(get_db)):
    """Delete cost record"""
    db_cost = db.query(Cost).filter(Cost.id == cost_id).first()
    if not db_cost:
        raise HTTPException(status_code=404, detail="Cost not found")
    
    db.delete(db_cost)
    db.commit()
    return {"message": "Cost deleted successfully"}


@router.get("/summary/monthly", response_model=Dict)
async def get_monthly_summary(db: Session = Depends(get_db)):
    """Get monthly cost summary"""
    costs = db.query(Cost).all()
    
    summary = {}
    for cost in costs:
        month = cost.cost_date.strftime("%Y-%m")
        if month not in summary:
            summary[month] = 0
        summary[month] += cost.amount
    
    return summary


@router.get("/summary/category", response_model=Dict)
async def get_category_summary(db: Session = Depends(get_db)):
    """Get cost summary by category"""
    costs = db.query(Cost).all()
    
    summary = {}
    for cost in costs:
        category = cost.category
        if category not in summary:
            summary[category] = 0
        summary[category] += cost.amount
    
    return summary
