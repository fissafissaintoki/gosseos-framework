import uuid
from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Enum as SAEnum, Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.schemas.schemas import ArtifactStatus, ArtifactType, Depth, Mode, ParseStatus, ProblemClass, RouteSource
from app.storage.database import Base


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _uuid() -> str:
    return str(uuid.uuid4())


class Case(Base):
    __tablename__ = "cases"

    case_id: Mapped[str] = mapped_column(String, primary_key=True, default=_uuid)
    title: Mapped[str | None] = mapped_column(String, nullable=True)
    raw_input: Mapped[str] = mapped_column(Text, nullable=False)
    context_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    desired_outcome: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_now, nullable=False)

    routing: Mapped["Routing | None"] = relationship(back_populates="case", uselist=False)
    outputs: Mapped[list["Output"]] = relationship(back_populates="case")
    artifacts: Mapped[list["Artifact"]] = relationship(back_populates="case")


class Routing(Base):
    __tablename__ = "routings"

    routing_id: Mapped[str] = mapped_column(String, primary_key=True, default=_uuid)
    case_id: Mapped[str] = mapped_column(String, ForeignKey("cases.case_id"), nullable=False, unique=True)
    problem_class: Mapped[ProblemClass] = mapped_column(SAEnum(ProblemClass), nullable=False)
    mode: Mapped[Mode] = mapped_column(SAEnum(Mode), nullable=False)
    depth: Mapped[Depth] = mapped_column(SAEnum(Depth), nullable=False)
    artifact_type: Mapped[ArtifactType] = mapped_column(SAEnum(ArtifactType), nullable=False)
    governance_relevance: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    route_source: Mapped[RouteSource] = mapped_column(SAEnum(RouteSource), nullable=False)
    confidence_score: Mapped[float | None] = mapped_column(Float, nullable=True)

    case: Mapped[Case] = relationship(back_populates="routing")


class Output(Base):
    __tablename__ = "outputs"

    output_id: Mapped[str] = mapped_column(String, primary_key=True, default=_uuid)
    case_id: Mapped[str] = mapped_column(String, ForeignKey("cases.case_id"), nullable=False)
    generated_json_text: Mapped[str] = mapped_column(Text, nullable=False)
    integrity_note: Mapped[str | None] = mapped_column(Text, nullable=True)
    parse_status: Mapped[ParseStatus] = mapped_column(SAEnum(ParseStatus), default=ParseStatus.ok, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_now, nullable=False)

    case: Mapped[Case] = relationship(back_populates="outputs")
    artifact: Mapped["Artifact | None"] = relationship(back_populates="output", uselist=False)


class Artifact(Base):
    __tablename__ = "artifacts"

    artifact_id: Mapped[str] = mapped_column(String, primary_key=True, default=_uuid)
    case_id: Mapped[str] = mapped_column(String, ForeignKey("cases.case_id"), nullable=False)
    output_id: Mapped[str] = mapped_column(String, ForeignKey("outputs.output_id"), nullable=False, unique=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[ArtifactStatus] = mapped_column(SAEnum(ArtifactStatus), default=ArtifactStatus.draft, nullable=False)
    domain: Mapped[str] = mapped_column(String, nullable=False)
    problem_class: Mapped[ProblemClass] = mapped_column(SAEnum(ProblemClass), nullable=False)
    mode: Mapped[Mode] = mapped_column(SAEnum(Mode), nullable=False)
    depth: Mapped[Depth] = mapped_column(SAEnum(Depth), nullable=False)
    artifact_type: Mapped[ArtifactType] = mapped_column(SAEnum(ArtifactType), nullable=False)
    purpose: Mapped[str] = mapped_column(Text, nullable=False)
    assumption_level: Mapped[str] = mapped_column(String, nullable=False)
    integrity_status: Mapped[str] = mapped_column(String, nullable=False)
    governance_relevance: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    version: Mapped[str] = mapped_column(String, default="v1", nullable=False)
    reuse_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=_now, nullable=False)
    last_reviewed: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    case: Mapped[Case] = relationship(back_populates="artifacts")
    output: Mapped[Output] = relationship(back_populates="artifact")
