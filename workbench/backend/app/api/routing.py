from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.db import Case, Routing
from app.schemas.schemas import RoutingOverride, RoutingRecord
from app.services.input_parser import parse_case_record
from app.services.router import route
from app.storage.database import get_db

router = APIRouter(prefix="/api/cases", tags=["routing"])


@router.post("/{case_id}/route", response_model=RoutingRecord)
def route_case(
    case_id: str,
    override: RoutingOverride | None = None,
    db: Session = Depends(get_db),
) -> RoutingRecord:
    case = db.query(Case).filter(Case.case_id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Case not found.")

    parsed_case = parse_case_record(case)
    decision = route(parsed_case, override=override)

    routing = db.query(Routing).filter(Routing.case_id == case_id).first()
    if routing is None:
        routing = Routing(case_id=case_id)
        db.add(routing)

    routing.problem_class = decision.problem_class
    routing.mode = decision.mode
    routing.depth = decision.depth
    routing.artifact_type = decision.artifact_type
    routing.governance_relevance = decision.governance_relevance
    routing.route_source = decision.route_source
    routing.confidence_score = decision.confidence_score

    db.commit()
    db.refresh(routing)
    return RoutingRecord.model_validate(routing)
