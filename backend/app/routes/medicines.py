"""Medicine Routes"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Medicine, Treatment
from app.schemas import MedicineCreate, MedicineResponse, TreatmentCreate, TreatmentResponse
from typing import List

router = APIRouter(prefix="/medicines", tags=["Medicines"])


@router.get("/", response_model=List[MedicineResponse])
async def list_medicines(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    """List all medicines"""
    medicines = db.query(Medicine).offset(skip).limit(limit).all()
    return medicines


@router.get("/{medicine_id}", response_model=MedicineResponse)
async def get_medicine(medicine_id: int, db: Session = Depends(get_db)):
    """Get medicine by ID"""
    medicine = db.query(Medicine).filter(Medicine.id == medicine_id).first()
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicine not found")
    return medicine


@router.post("/", response_model=MedicineResponse)
async def create_medicine(medicine: MedicineCreate, db: Session = Depends(get_db)):
    """Create new medicine"""
    db_medicine = Medicine(**medicine.dict())
    db.add(db_medicine)
    db.commit()
    db.refresh(db_medicine)
    return db_medicine


@router.post("/treatments/", response_model=TreatmentResponse)
async def create_treatment(treatment: TreatmentCreate, db: Session = Depends(get_db)):
    """Create new treatment record"""
    db_treatment = Treatment(**treatment.dict())
    db.add(db_treatment)
    db.commit()
    db.refresh(db_treatment)
    return db_treatment


@router.get("/treatments/animal/{animal_id}", response_model=List[TreatmentResponse])
async def get_animal_treatments(
    animal_id: int,
    db: Session = Depends(get_db)
):
    """Get all treatments for an animal"""
    treatments = db.query(Treatment).filter(Treatment.animal_id == animal_id).all()
    return treatments
