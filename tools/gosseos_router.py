#!/usr/bin/env python3
"""
GosseOS Router

A minimal local router that classifies raw input into:
- problem class
- primary mode
- artifact type
- governance signal

This is intentionally simple.
It proves the operating logic without pretending to be a full AI system.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass
class RoutingResult:
    problem_class: str
    primary_mode: str
    secondary_mode: str
    artifact_type: str
    governance_signal: str
    rationale: str


RULES = [
    {
        "keywords": ["risk", "risiko", "weakness", "failure", "fail", "problem", "kritisch", "red team"],
        "result": RoutingResult(
            problem_class="Risk / Failure Analysis",
            primary_mode="RED TEAM",
            secondary_mode="AUDIT",
            artifact_type="Risk Map or Failure Mode Review",
            governance_signal="APPROVED WITH WARNING",
            rationale="The input asks for weak points, risks, or failure logic. It should be stress-tested before execution.",
        ),
    },
    {
        "keywords": ["build", "baue", "create", "erstellen", "system", "framework", "template", "artefakt"],
        "result": RoutingResult(
            problem_class="Artifact Creation",
            primary_mode="BUILD",
            secondary_mode="ARCHITECT",
            artifact_type="Reusable Framework, Template, or System Draft",
            governance_signal="APPROVED WITH WARNING",
            rationale="The input asks for a concrete reusable asset. Build mode should produce an artifact, not a loose answer.",
        ),
    },
    {
        "keywords": ["audit", "prüfe", "bewerte", "score", "analyse", "review", "einschätzen"],
        "result": RoutingResult(
            problem_class="Evaluation / Assessment",
            primary_mode="AUDIT",
            secondary_mode="RED TEAM",
            artifact_type="Assessment, Scorecard, or Gap Analysis",
            governance_signal="APPROVED WITH WARNING",
            rationale="The input asks for structured evaluation. Audit mode should separate signal, weakness, and decision relevance.",
        ),
    },
    {
        "keywords": ["strategy", "strategie", "positioning", "bewerbung", "profil", "github", "linkedin"],
        "result": RoutingResult(
            problem_class="Positioning / Strategic Framing",
            primary_mode="ARCHITECT",
            secondary_mode="BRIEFING",
            artifact_type="Positioning Brief, Profile Narrative, or Strategic Structure",
            governance_signal="APPROVED WITH WARNING",
            rationale="The input concerns external framing or strategic visibility. It needs structure, message discipline, and proof.",
        ),
    },
    {
        "keywords": ["logistik", "supply chain", "cold chain", "kühl", "tk", "wareneingang", "kommissionierung"],
        "result": RoutingResult(
            problem_class="Operational Logistics Process",
            primary_mode="AUDIT",
            secondary_mode="BUILD",
            artifact_type="Process Audit, Risk Matrix, or Decision Framework",
            governance_signal="APPROVED WITH WARNING",
            rationale="The input belongs to operational logistics. It should be turned into process logic, controls, and measurable artifacts.",
        ),
    },
]

DEFAULT_RESULT = RoutingResult(
    problem_class="Ambiguous / Needs Structuring",
    primary_mode="META",
    secondary_mode="BUILD",
    artifact_type="Clarified Work Frame",
    governance_signal="LIMITED",
    rationale="The input is not specific enough for direct execution. First clarify goal, context, constraints, and desired artifact.",
)


def route_input(text: str) -> RoutingResult:
    normalized = text.lower()
    best_result = DEFAULT_RESULT
    best_score = 0

    for rule in RULES:
        score = sum(1 for keyword in rule["keywords"] if keyword in normalized)
        if score > best_score:
            best_score = score
            best_result = rule["result"]

    return best_result


def print_result(text: str, result: RoutingResult) -> None:
    print("\nGosseOS Router Result")
    print("=" * 24)
    print(f"Input: {text}")
    print(f"Problem Class: {result.problem_class}")
    print(f"Primary Mode: {result.primary_mode}")
    print(f"Secondary Mode: {result.secondary_mode}")
    print(f"Artifact Type: {result.artifact_type}")
    print(f"Governance Signal: {result.governance_signal}")
    print(f"Rationale: {result.rationale}")
    print("\nNext Action:")
    print("Turn the input into the proposed artifact and run the Governance Gate before final use.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Route raw input through the GosseOS mode logic.")
    parser.add_argument("input", nargs="*", help="Raw input to classify")
    args = parser.parse_args()

    text = " ".join(args.input).strip()
    if not text:
        text = input("Enter raw input: ").strip()

    result = route_input(text)
    print_result(text, result)


if __name__ == "__main__":
    main()
