"""Animal Routes"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Animal
from app.schemas import AnimalCreate, AnimalUpdate, AnimalResponse
from typing import List

router = APIRouter(prefix="/animals", tags=["Animals"])


@router.get("/", response_model=List[AnimalResponse])
async def list_animals(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """List all animals"""
    animals = db.query(Animal).offset(skip).limit(limit).all()
    return animals


@router.get("/{animal_id}", response_model=AnimalResponse)
async def get_animal(animal_id: int, db: Session = Depends(get_db)):
    """Get animal by ID"""
    animal = db.query(Animal).filter(Animal.id == animal_id).first()
    if not animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    return animal


@router.post("/", response_model=AnimalResponse)
async def create_animal(animal: AnimalCreate, db: Session = Depends(get_db)):
    """Create new animal"""
    db_animal = Animal(**animal.dict())
    db.add(db_animal)
    db.commit()
    db.refresh(db_animal)
    return db_animal


@router.put("/{animal_id}", response_model=AnimalResponse)
async def update_animal(
    animal_id: int,
    animal: AnimalUpdate,
    db: Session = Depends(get_db)
):
    """Update animal"""
    db_animal = db.query(Animal).filter(Animal.id == animal_id).first()
    if not db_animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    
    update_data = animal.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_animal, key, value)
    
    db.commit()
    db.refresh(db_animal)
    return db_animal


@router.delete("/{animal_id}")
async def delete_animal(animal_id: int, db: Session = Depends(get_db)):
    """Delete animal"""
    db_animal = db.query(Animal).filter(Animal.id == animal_id).first()
    if not db_animal:
        raise HTTPException(status_code=404, detail="Animal not found")
    
    db.delete(db_animal)
    db.commit()
    return {"message": "Animal deleted successfully"}
