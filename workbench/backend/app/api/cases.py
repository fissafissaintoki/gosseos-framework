from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.db import Case
from app.schemas.schemas import CaseCreate, CaseRecord
from app.storage.database import get_db

router = APIRouter(prefix="/api/cases", tags=["cases"])


@router.post("", response_model=CaseRecord)
def create_case(payload: CaseCreate, db: Session = Depends(get_db)) -> CaseRecord:
    case = Case(
        title=payload.title,
        raw_input=payload.raw_input,
        context_notes=payload.context_notes,
        desired_outcome=payload.desired_outcome,
    )
    db.add(case)
    db.commit()
    db.refresh(case)
    return CaseRecord.model_validate(case)


@router.get("/{case_id}", response_model=CaseRecord)
def get_case(case_id: str, db: Session = Depends(get_db)) -> CaseRecord:
    case = db.query(Case).filter(Case.case_id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Case not found.")
    return CaseRecord.model_validate(case)
