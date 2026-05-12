from __future__ import annotations

import json
import os
from dataclasses import dataclass
from typing import Any, Optional

import anthropic

from app.schemas.schemas import ArtifactType, Depth, Mode, OutputPayload, ParseStatus, ProblemClass
from app.utils.json_repair import parse_output

MODEL_NAME = "claude-sonnet-4-20250514"

_CLASSIFIER_SYSTEM_PROMPT = """You are a routing classifier for a structured AI workbench.\nReturn only valid JSON with these fields:\n{\n  \"problem_class\": one of [analysis, planning, decision_support, documentation, communication, governance_risk, creative_development],\n  \"mode\": one of [Architect, Build, Audit, Red Team, Briefing],\n  \"depth\": one of [Direct, Compact, Standard, Endboss],\n  \"artifact_type\": one of [one-pager, dossier, SOP, report, post, framework, prompt, briefing_note, registry_entry],\n  \"governance_relevance\": true or false\n}\nNo markdown. No explanation. JSON only."""


@dataclass
class ExecutionResult:
    output_payload: Optional[OutputPayload]
    generated_json_text: str
    parse_status: ParseStatus
    integrity_note: Optional[str]
    raw_text: str


def execute(messages: list[dict[str, str]], system_content: str) -> ExecutionResult:
    client = _get_client()
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=4096,
        system=system_content,
        messages=messages,
    )
    raw_text = _extract_text_response(response)
    return _process_response(raw_text)


def classify_route_via_claude(user_text: str) -> Optional[dict[str, Any]]:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model=MODEL_NAME,
        max_tokens=256,
        system=_CLASSIFIER_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_text[:1500]}],
    )

    raw_text = _extract_text_response(response)
    try:
        data = json.loads(raw_text)
        # light validation to keep the router minimal and explicit
        ProblemClass(data["problem_class"])
        Mode(data["mode"])
        Depth(data["depth"])
        ArtifactType(data["artifact_type"])
        data["governance_relevance"] = bool(data.get("governance_relevance", False))
        return data
    except Exception:
        return None


def _get_client() -> anthropic.Anthropic:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise EnvironmentError("ANTHROPIC_API_KEY is not set.")
    return anthropic.Anthropic(api_key=api_key)


def _extract_text_response(response: Any) -> str:
    if not getattr(response, "content", None):
        raise ValueError("Claude returned an empty response.")
    first_block = response.content[0]
    text = getattr(first_block, "text", None)
    if not text:
        raise ValueError("Claude returned a non-text or empty first content block.")
    return text.strip()


def _process_response(raw_text: str) -> ExecutionResult:
    parsed_dict, parse_status = parse_output(raw_text)

    if parse_status == ParseStatus.failed or parsed_dict is None:
        # On parse failure, the DB side still needs a persistable JSON string.
        # This envelope is a technical fallback envelope, not original model JSON.
        fallback_envelope = {
            "core_result": raw_text,
            "facts": "",
            "assumptions_uncertainties": "",
            "limits": "",
            "optional": None,
        }
        return ExecutionResult(
            output_payload=None,
            generated_json_text=json.dumps(fallback_envelope, ensure_ascii=False),
            parse_status=ParseStatus.failed,
            integrity_note="Parse failed. Raw Claude output was wrapped in a technical fallback envelope.",
            raw_text=raw_text,
        )

    output_payload = OutputPayload(
        core_result=parsed_dict.get("core_result", ""),
        facts=parsed_dict.get("facts", ""),
        assumptions_uncertainties=parsed_dict.get("assumptions_uncertainties", ""),
        limits=parsed_dict.get("limits", ""),
        optional=parsed_dict.get("optional"),
    )

    integrity_note = None
    if parse_status == ParseStatus.repaired:
        integrity_note = "Output was repaired before parsing. Verify structure carefully."

    return ExecutionResult(
        output_payload=output_payload,
        generated_json_text=json.dumps(parsed_dict, ensure_ascii=False),
        parse_status=parse_status,
        integrity_note=integrity_note,
        raw_text=raw_text,
    )
