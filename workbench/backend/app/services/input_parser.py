from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from app.schemas.schemas import CaseCreate, CaseRecord


@dataclass
class ParsedCase:
    case_id: Optional[str]
    title: Optional[str]
    raw_input: str
    context_notes: Optional[str]
    desired_outcome: Optional[str]


def parse_case_create(data: CaseCreate) -> ParsedCase:
    return ParsedCase(
        case_id=None,
        title=_clean(data.title),
        raw_input=_require(data.raw_input, "raw_input"),
        context_notes=_clean(data.context_notes),
        desired_outcome=_clean(data.desired_outcome),
    )


def parse_case_record(record: CaseRecord) -> ParsedCase:
    return ParsedCase(
        case_id=record.case_id,
        title=_clean(record.title),
        raw_input=_require(record.raw_input, "raw_input"),
        context_notes=_clean(record.context_notes),
        desired_outcome=_clean(record.desired_outcome),
    )


def build_task_block(case: ParsedCase) -> str:
    parts: list[str] = []
    if case.title:
        parts.append(f"TITLE:\n{case.title}")
    parts.append(f"INPUT:\n{case.raw_input}")
    if case.context_notes:
        parts.append(f"CONTEXT:\n{case.context_notes}")
    if case.desired_outcome:
        parts.append(f"DESIRED OUTCOME:\n{case.desired_outcome}")
    return "\n\n".join(parts)


def _clean(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    value = value.strip()
    return value if value else None


def _require(value: Optional[str], field: str) -> str:
    cleaned = _clean(value)
    if not cleaned:
        raise ValueError(f"Required field '{field}' is missing or empty.")
    return cleaned
