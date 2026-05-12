from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from app.schemas.schemas import ArtifactType, Depth, Mode, ProblemClass, RouteSource, RoutingOverride
from app.services.claude_service import classify_route_via_claude
from app.services.input_parser import ParsedCase

CONFIDENCE_THRESHOLD = 0.6


@dataclass
class RoutingResult:
    problem_class: ProblemClass
    mode: Mode
    depth: Depth
    artifact_type: ArtifactType
    governance_relevance: bool
    route_source: RouteSource
    confidence_score: Optional[float]


def route(case: ParsedCase, override: Optional[RoutingOverride] = None) -> RoutingResult:
    if override is not None:
        return RoutingResult(
            problem_class=override.problem_class,
            mode=override.mode,
            depth=override.depth,
            artifact_type=override.artifact_type,
            governance_relevance=override.governance_relevance,
            route_source=RouteSource.manual,
            confidence_score=1.0,
        )

    rule_result = _rule_based_route(case)
    if rule_result.confidence_score is not None and rule_result.confidence_score < CONFIDENCE_THRESHOLD:
        claude_data = classify_route_via_claude(_combined_text(case))
        if claude_data is not None:
            return RoutingResult(
                problem_class=ProblemClass(claude_data["problem_class"]),
                mode=Mode(claude_data["mode"]),
                depth=Depth(claude_data["depth"]),
                artifact_type=ArtifactType(claude_data["artifact_type"]),
                governance_relevance=bool(claude_data.get("governance_relevance", False)),
                route_source=RouteSource.claude,
                confidence_score=0.85,
            )

    return rule_result


_PROBLEM_CLASS_KEYWORDS: list[tuple[list[str], float, ProblemClass]] = [
    (["analyse", "analysis", "auswerten", "evaluate", "assess"], 0.8, ProblemClass.analysis),
    (["plan", "planning", "roadmap", "strategy", "strategie"], 0.8, ProblemClass.planning),
    (["decide", "decision", "entscheidung", "option", "options"], 0.8, ProblemClass.decision_support),
    (["document", "dokumentation", "spec", "writeup", "documentation"], 0.8, ProblemClass.documentation),
    (["communicate", "kommunikation", "email", "brief", "message"], 0.8, ProblemClass.communication),
    (["risk", "risiko", "governance", "compliance", "audit"], 0.8, ProblemClass.governance_risk),
    (["create", "creative", "design", "concept", "konzept", "idea"], 0.8, ProblemClass.creative_development),
]

_MODE_KEYWORDS: list[tuple[list[str], float, Mode]] = [
    (["architect", "structure", "framework", "design"], 0.7, Mode.architect),
    (["build", "implement", "create", "write", "code"], 0.7, Mode.build),
    (["audit", "review", "check", "validate", "prüf"], 0.7, Mode.audit),
    (["challenge", "red team", "critique", "stress"], 0.7, Mode.red_team),
    (["brief", "summary", "overview", "tldr"], 0.7, Mode.briefing),
]

_ARTIFACT_KEYWORDS: list[tuple[list[str], float, ArtifactType]] = [
    (["one-pager", "one pager", "kurz", "short"], 0.7, ArtifactType.one_pager),
    (["dossier", "deep dive", "full", "komplett"], 0.7, ArtifactType.dossier),
    (["sop", "standard operating", "process", "prozess"], 0.7, ArtifactType.sop),
    (["report", "bericht", "findings"], 0.7, ArtifactType.report),
    (["post", "article", "blog", "artikel"], 0.7, ArtifactType.post),
    (["framework", "model", "modell", "matrix"], 0.7, ArtifactType.framework),
    (["prompt", "instruction", "anweisung"], 0.7, ArtifactType.prompt),
    (["briefing", "briefing note", "executive"], 0.7, ArtifactType.briefing_note),
    (["registry", "entry", "eintrag"], 0.7, ArtifactType.registry_entry),
]

_GOVERNANCE_KEYWORDS = [
    "risk", "risiko", "compliance", "legal", "audit", "governance", "regulation", "policy", "richtlinie"
]

_DEPTH_KEYWORDS: list[tuple[list[str], Depth]] = [
    (["quick", "direct", "fast", "kurz", "schnell"], Depth.direct),
    (["compact", "short", "summary", "kompakt"], Depth.compact),
    (["standard", "normal", "regular"], Depth.standard),
    (["deep", "full", "complete", "endboss", "exhaustive", "komplett"], Depth.endboss),
]


def _rule_based_route(case: ParsedCase) -> RoutingResult:
    text = _combined_text(case).lower()
    problem_class, pc_score = _best_match_weighted(text, _PROBLEM_CLASS_KEYWORDS, ProblemClass.analysis)
    mode, mode_score = _best_match_weighted(text, _MODE_KEYWORDS, Mode.build)
    artifact_type, artifact_score = _best_match_weighted(text, _ARTIFACT_KEYWORDS, ArtifactType.report)
    depth = _match_depth(text)
    governance_relevance = any(keyword in text for keyword in _GOVERNANCE_KEYWORDS)
    confidence = round((pc_score + mode_score + artifact_score) / 3, 2)
    return RoutingResult(
        problem_class=problem_class,
        mode=mode,
        depth=depth,
        artifact_type=artifact_type,
        governance_relevance=governance_relevance,
        route_source=RouteSource.rule,
        confidence_score=confidence,
    )


def _best_match_weighted(text: str, candidates: list[tuple[list[str], float, object]], default: object) -> tuple[object, float]:
    scores: dict[object, float] = {}
    for keywords, weight, value in candidates:
        for keyword in keywords:
            if keyword in text:
                scores[value] = scores.get(value, 0.0) + weight
                break
    if not scores:
        return default, 0.0
    best_value = max(scores, key=lambda key: scores[key])
    return best_value, min(scores[best_value], 1.0)


def _match_depth(text: str) -> Depth:
    for keywords, depth in _DEPTH_KEYWORDS:
        if any(keyword in text for keyword in keywords):
            return depth
    return Depth.standard


def _combined_text(case: ParsedCase) -> str:
    parts = [case.raw_input]
    if case.title:
        parts.append(case.title)
    if case.context_notes:
        parts.append(case.context_notes)
    if case.desired_outcome:
        parts.append(case.desired_outcome)
    return " ".join(parts)
