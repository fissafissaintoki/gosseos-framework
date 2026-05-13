from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Optional

from sqlalchemy.orm import Session

from app.models.db import Artifact, Output
from app.schemas.schemas import ArtifactCreate, ArtifactRecord, ArtifactUpdate


def create_artifact(db: Session, payload: ArtifactCreate) -> Artifact:
    artifact = Artifact(
        case_id=payload.case_id,
        output_id=payload.output_id,
        title=payload.title,
        status=payload.status,
        domain=payload.domain,
        problem_class=payload.problem_class,
        mode=payload.mode,
        depth=payload.depth,
        artifact_type=payload.artifact_type,
        purpose=payload.purpose,
        assumption_level=payload.assumption_level,
        integrity_status=payload.integrity_status,
        governance_relevance=payload.governance_relevance,
        version=payload.version,
        reuse_notes=payload.reuse_notes,
    )
    db.add(artifact)
    db.commit()
    db.refresh(artifact)
    return artifact


def get_artifact(db: Session, artifact_id: str) -> Optional[Artifact]:
    return db.query(Artifact).filter(Artifact.artifact_id == artifact_id).first()


def list_artifacts(
    db: Session,
    status: Optional[str] = None,
    domain: Optional[str] = None,
    mode: Optional[str] = None,
    artifact_type: Optional[str] = None,
) -> list[Artifact]:
    query = db.query(Artifact)
    if status:
        query = query.filter(Artifact.status == status)
    if domain:
        query = query.filter(Artifact.domain == domain)
    if mode:
        query = query.filter(Artifact.mode == mode)
    if artifact_type:
        query = query.filter(Artifact.artifact_type == artifact_type)
    return query.order_by(Artifact.created_at.desc()).all()


def update_artifact(db: Session, artifact: Artifact, payload: ArtifactUpdate) -> Artifact:
    if payload.status is not None:
        artifact.status = payload.status
    if payload.reuse_notes is not None:
        artifact.reuse_notes = payload.reuse_notes
    if payload.version is not None:
        artifact.version = payload.version
    if payload.last_reviewed is not None:
        artifact.last_reviewed = payload.last_reviewed
    db.commit()
    db.refresh(artifact)
    return artifact


def build_artifact_response(artifact: Artifact, output: Optional[Output] = None) -> dict:
    content = None
    if output is not None:
        try:
            content = json.loads(output.generated_json_text)
        except Exception:
            content = {"raw": output.generated_json_text}

    return {
        "artifact": ArtifactRecord.model_validate(artifact),
        "content": content,
    }


def mark_reviewed_now(db: Session, artifact: Artifact) -> Artifact:
    artifact.last_reviewed = datetime.now(timezone.utc)
    db.commit()
    db.refresh(artifact)
    return artifact
