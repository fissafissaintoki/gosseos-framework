import json
import re
from typing import Optional

from app.schemas.schemas import ParseStatus

_REQUIRED_KEYS = {
    "core_result",
    "facts",
    "assumptions_uncertainties",
    "limits",
}


def parse_output(raw: str) -> tuple[Optional[dict], ParseStatus]:
    """
    Attempt to parse a Claude response string into an OutputPayload-shaped dict.

    Repair steps in order:
    1. direct JSON parse
    2. strip markdown code fences and parse again
    3. remove trailing commas and parse again
    """
    try:
        data = json.loads(raw)
        if _has_required_keys(data):
            return data, ParseStatus.ok
    except json.JSONDecodeError:
        pass

    cleaned = _strip_fences(raw)
    try:
        data = json.loads(cleaned)
        if _has_required_keys(data):
            return data, ParseStatus.repaired
    except json.JSONDecodeError:
        pass

    repaired = _remove_trailing_commas(cleaned)
    try:
        data = json.loads(repaired)
        if _has_required_keys(data):
            return data, ParseStatus.repaired
    except json.JSONDecodeError:
        pass

    return None, ParseStatus.failed


def _has_required_keys(data: object) -> bool:
    return isinstance(data, dict) and _REQUIRED_KEYS.issubset(data.keys())


def _strip_fences(text: str) -> str:
    match = re.match(r"^```(?:json)?\s*\n?(.*?)\n?```$", text.strip(), re.DOTALL)
    return match.group(1).strip() if match else text.strip()


def _remove_trailing_commas(text: str) -> str:
    return re.sub(r",\s*([}\]])", r"\1", text)
