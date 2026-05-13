from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.db import Output
from app.schemas.schemas import IntegrityResult
from app.services.integrity_service import review_output
from app.storage.database import get_db

router = APIRouter(prefix="/api/outputs", tags=["integrity"])


@router.post("/{output_id}/integrity-review", response_model=IntegrityResult)
def integrity_review(output_id: str, db: Session = Depends(get_db)) -> IntegrityResult:
    output = db.query(Output).filter(Output.output_id == output_id).first()
    if not output:
        raise HTTPException(status_code=404, detail="Output not found.")
    return review_output(output)
