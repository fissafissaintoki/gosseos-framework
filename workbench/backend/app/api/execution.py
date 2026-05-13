from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models.db import Case, Output, Routing
from app.schemas.schemas import OutputRecord, RoutingRecord
from app.services.claude_service import execute
from app.services.input_parser import parse_case_record
from app.services.prompt_composer import compose_prompt
from app.storage.database import get_db

router = APIRouter(prefix="/api/cases", tags=["execution"])


@router.post("/{case_id}/execute", response_model=OutputRecord)
def execute_case(case_id: str, db: Session = Depends(get_db)) -> OutputRecord:
    case = db.query(Case).filter(Case.case_id == case_id).first()
    if not case:
        raise HTTPException(status_code=404, detail="Case not found.")

    routing = db.query(Routing).filter(Routing.case_id == case_id).first()
    if not routing:
        raise HTTPException(status_code=400, detail="Case has no routing yet. Route the case first.")

    parsed_case = parse_case_record(case)
    routing_record = RoutingRecord.model_validate(routing)
    messages, system_content = compose_prompt(parsed_case, routing_record)
    result = execute(messages, system_content)

    output = Output(
        case_id=case_id,
        generated_json_text=result.generated_json_text,
        integrity_note=result.integrity_note,
        parse_status=result.parse_status,
    )
    db.add(output)
    db.commit()
    db.refresh(output)

    if result.output_payload is None:
        raise HTTPException(
            status_code=502,
            detail={
                "message": "Claude output could not be parsed into structured payload.",
                "output_id": output.output_id,
                "parse_status": output.parse_status.value,
                "integrity_note": output.integrity_note,
            },
        )

    return OutputRecord(
        output_id=output.output_id,
        case_id=output.case_id,
        output_payload=result.output_payload,
        integrity_note=output.integrity_note,
        parse_status=output.parse_status,
        created_at=output.created_at,
    )
