from __future__ import annotations

import json

from app.models.db import Output
from app.schemas.schemas import IntegrityResult, ParseStatus


def review_output(output: Output) -> IntegrityResult:
    """
    Lightweight v1 integrity review.

    This is intentionally simple for v1:
    - parse failure => hallucination/structure risk
    - missing required payload sections in stored JSON => unsupported/mismatch risk
    - otherwise return a low-friction baseline result
    """
    drift = False
    hallucination_risk = output.parse_status == ParseStatus.failed
    artifact_mismatch = False
    unsupported_claims = False
    note = None

    try:
        payload = json.loads(output.generated_json_text)
        required = {"core_result", "facts", "assumptions_uncertainties", "limits"}
        if not isinstance(payload, dict) or not required.issubset(payload.keys()):
            artifact_mismatch = True
            unsupported_claims = True
            note = "Stored output JSON is missing required output sections."
    except Exception:
        artifact_mismatch = True
        unsupported_claims = True
        note = "Stored output JSON could not be decoded during integrity review."

    if output.parse_status == ParseStatus.repaired and not note:
        note = "Output was repaired before parsing. Review advised."
    elif output.parse_status == ParseStatus.failed and not note:
        note = "Parse failed. Technical fallback envelope stored; manual review required."

    return IntegrityResult(
        output_id=output.output_id,
        drift=drift,
        hallucination_risk=hallucination_risk,
        artifact_mismatch=artifact_mismatch,
        unsupported_claims=unsupported_claims,
        note=note,
    )
