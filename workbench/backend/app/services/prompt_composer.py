from __future__ import annotations

import re
from typing import Optional

from app.schemas.schemas import ArtifactType, Mode, RoutingRecord
from app.services.input_parser import ParsedCase, build_task_block
from app.utils.module_loader import load_module

_OUTPUT_CONTRACT = """You must respond with ONLY a valid JSON object. No markdown. No explanation.\nThe JSON must contain these fields exactly:\n{\n  \"core_result\": \"<main result as string>\",\n  \"facts\": \"<key facts as string>\",\n  \"assumptions_uncertainties\": \"<assumptions and uncertainties as string>\",\n  \"limits\": \"<limits of this output as string>\",\n  \"optional\": \"<optional extension as string or null>\"\n}"""

_GOVERNANCE_ADDON = """GOVERNANCE NOTE:\nThis case has been flagged as governance-relevant.\nApply additional scrutiny. Surface regulatory, compliance, policy, and risk implications explicitly in the relevant output fields.\nDo not hide uncertainty."""


def compose_prompt(case: ParsedCase, routing: RoutingRecord) -> tuple[list[dict[str, str]], str]:
    system_parts: list[str] = []
    system_parts.append(load_module("gosseos_core"))
    system_parts.append(load_module("integrity_kernel"))

    full_mode_spec = load_module("mode_specifications")
    mode_section = _extract_mode_section(routing.mode, full_mode_spec)
    system_parts.append(f"MODE: {routing.mode.value}\n\n{mode_section}")

    if routing.governance_relevance:
        system_parts.append(_GOVERNANCE_ADDON)

    system_parts.append(_OUTPUT_CONTRACT)
    system_content = "\n\n---\n\n".join(system_parts)

    task_block = build_task_block(case)
    artifact_block = _artifact_format_block(routing.artifact_type)
    user_content = f"{task_block}\n\n---\n\n{artifact_block}"

    messages = [{"role": "user", "content": user_content}]
    return messages, system_content


def _artifact_format_block(artifact_type: ArtifactType) -> str:
    return (
        f"ARTIFACT FORMAT: {artifact_type.value}\n"
        "Structure the output according to the conventions for this artifact type. "
        "Keep the response aligned to the requested format and requested depth."
    )


def _extract_mode_section(mode: Mode, full_spec: str) -> str:
    """
    Extract the relevant mode section from MODE_SPECIFICATIONS.md.
    Supports header variants such as:
    - ## Architect
    - ## ARCHITECT
    - ## 1. ARCHITECT
    - ## 1. Architect
    Falls back to full document if extraction fails.
    """
    lines = full_spec.splitlines()
    start_index: Optional[int] = None
    target = re.escape(mode.value)
    header_pattern = re.compile(rf"^##\s+(?:\d+\.\s*)?{target}\s*$", re.IGNORECASE)
    next_header_pattern = re.compile(r"^##\s+")

    for index, line in enumerate(lines):
        if header_pattern.match(line.strip()):
            start_index = index
            break

    if start_index is None:
        return full_spec

    section_lines: list[str] = []
    for line in lines[start_index + 1 :]:
        if next_header_pattern.match(line.strip()):
            break
        section_lines.append(line)

    section = "\n".join(section_lines).strip()
    return section if section else full_spec
