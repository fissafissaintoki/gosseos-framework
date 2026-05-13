from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.models.db import Artifact, Output
from app.schemas.schemas import ArtifactCreate, ArtifactRecord, ArtifactUpdate
from app.services.registry_service import build_artifact_response, create_artifact, get_artifact, list_artifacts, mark_reviewed_now, update_artifact
from app.storage.database import get_db

router = APIRouter(prefix="/api/artifacts", tags=["artifacts"])


@router.post("", response_model=ArtifactRecord)
def create_artifact_endpoint(payload: ArtifactCreate, db: Session = Depends(get_db)) -> ArtifactRecord:
    output = db.query(Output).filter(Output.output_id == payload.output_id).first()
    if not output:
        raise HTTPException(status_code=404, detail="Output not found.")
    artifact = create_artifact(db, payload)
    return ArtifactRecord.model_validate(artifact)


@router.get("/{artifact_id}")
def get_artifact_endpoint(artifact_id: str, db: Session = Depends(get_db)) -> dict:
    artifact = get_artifact(db, artifact_id)
    if not artifact:
        raise HTTPException(status_code=404, detail="Artifact not found.")
    output = db.query(Output).filter(Output.output_id == artifact.output_id).first()
    return build_artifact_response(artifact, output)


@router.get("", response_model=list[ArtifactRecord])
def list_artifacts_endpoint(
    status: Optional[str] = Query(default=None),
    domain: Optional[str] = Query(default=None),
    mode: Optional[str] = Query(default=None),
    artifact_type: Optional[str] = Query(default=None),
    db: Session = Depends(get_db),
) -> list[ArtifactRecord]:
    artifacts = list_artifacts(db, status=status, domain=domain, mode=mode, artifact_type=artifact_type)
    return [ArtifactRecord.model_validate(item) for item in artifacts]


@router.patch("/{artifact_id}", response_model=ArtifactRecord)
def update_artifact_endpoint(
    artifact_id: str,
    payload: ArtifactUpdate,
    mark_reviewed: bool = Query(default=False),
    db: Session = Depends(get_db),
) -> ArtifactRecord:
    artifact = get_artifact(db, artifact_id)
    if not artifact:
        raise HTTPException(status_code=404, detail="Artifact not found.")

    artifact = update_artifact(db, artifact, payload)
    if mark_reviewed:
        artifact = mark_reviewed_now(db, artifact)
    return ArtifactRecord.model_validate(artifact)
