from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ProblemClass(str, Enum):
    analysis = "analysis"
    planning = "planning"
    decision_support = "decision_support"
    documentation = "documentation"
    communication = "communication"
    governance_risk = "governance_risk"
    creative_development = "creative_development"


class Mode(str, Enum):
    architect = "Architect"
    build = "Build"
    audit = "Audit"
    red_team = "Red Team"
    briefing = "Briefing"


class Depth(str, Enum):
    direct = "Direct"
    compact = "Compact"
    standard = "Standard"
    endboss = "Endboss"


class ArtifactType(str, Enum):
    one_pager = "one-pager"
    dossier = "dossier"
    sop = "SOP"
    report = "report"
    post = "post"
    framework = "framework"
    prompt = "prompt"
    briefing_note = "briefing_note"
    registry_entry = "registry_entry"


class ArtifactStatus(str, Enum):
    draft = "draft"
    working = "working"
    validated = "validated"
    canonical = "canonical"
    archived = "archived"


class ParseStatus(str, Enum):
    ok = "ok"
    repaired = "repaired"
    failed = "failed"


class RouteSource(str, Enum):
    rule = "rule"
    claude = "claude"
    manual = "manual"


class CaseCreate(BaseModel):
    title: Optional[str] = None
    raw_input: str
    context_notes: Optional[str] = None
    desired_outcome: Optional[str] = None


class CaseRecord(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    case_id: str
    title: Optional[str]
    raw_input: str
    context_notes: Optional[str]
    desired_outcome: Optional[str]
    created_at: datetime


class RoutingOverride(BaseModel):
    problem_class: ProblemClass
    mode: Mode
    depth: Depth
    artifact_type: ArtifactType
    governance_relevance: bool = False


class RoutingRecord(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    routing_id: str
    case_id: str
    problem_class: ProblemClass
    mode: Mode
    depth: Depth
    artifact_type: ArtifactType
    governance_relevance: bool
    route_source: RouteSource
    confidence_score: Optional[float] = None


class OutputPayload(BaseModel):
    core_result: str
    facts: str
    assumptions_uncertainties: str
    limits: str
    optional: Optional[str] = None


class OutputRecord(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    output_id: str
    case_id: str
    output_payload: OutputPayload
    integrity_note: Optional[str]
    parse_status: ParseStatus
    created_at: datetime


class IntegrityResult(BaseModel):
    output_id: str
    drift: bool
    hallucination_risk: bool
    artifact_mismatch: bool
    unsupported_claims: bool
    note: Optional[str] = None


class ArtifactCreate(BaseModel):
    case_id: str
    output_id: str
    title: str
    status: ArtifactStatus = ArtifactStatus.draft
    domain: str
    problem_class: ProblemClass
    mode: Mode
    depth: Depth
    artifact_type: ArtifactType
    purpose: str
    assumption_level: str
    integrity_status: str
    governance_relevance: bool = False
    version: str = "v1"
    reuse_notes: Optional[str] = None


class ArtifactRecord(ArtifactCreate):
    model_config = ConfigDict(from_attributes=True)

    artifact_id: str
    created_at: datetime
    last_reviewed: Optional[datetime]


class ArtifactUpdate(BaseModel):
    status: Optional[ArtifactStatus] = None
    reuse_notes: Optional[str] = None
    version: Optional[str] = None
    last_reviewed: Optional[datetime] = None
