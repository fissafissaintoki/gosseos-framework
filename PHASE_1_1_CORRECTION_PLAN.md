# PHASE 1.1 – CORRECTION PLAN

## Purpose

This document fixes the main consistency and cleanliness issues discovered after the initial Phase 1 foundation draft.

The goal is not to expand scope.
The goal is to make the foundation stable before Phase 2 begins.

---

## Corrections to apply

### 1. Clean separation for output payload storage vs API schema

Use **Option B**:

- database model field: `generated_json_text`
- API schema field: `output_payload`

Rationale:
- the database stores serialized JSON text
- the API exposes structured payload
- storage concerns and API concerns remain separate

This removes the strongest current semantic mismatch.

---

### 2. ID consistency for v1

Use **string IDs everywhere** in schemas and frontend types.

Do not keep UUID typing in schemas for v1.

Rationale:
- SQLite stores them as strings
- SQLAlchemy models already use string fields
- this avoids unnecessary ORM/Pydantic friction in v1

---

### 3. Enforce one-to-one relationships at DB level

Add uniqueness where the architecture already assumes one-to-one:

- `Routing.case_id` must be `unique=True`
- `Artifact.output_id` must be `unique=True`

Rationale:
- architectural intent should be enforced technically
- do not leave one-to-one logic as implicit application behavior only

---

### 4. Extend routing schema for traceability

Add to routing records:
- `route_source`
- `confidence_score`

Recommended values for `route_source`:
- `rule`
- `claude`
- `manual`

Rationale:
- hybrid routing needs explicit provenance
- later debugging and review depend on this information

---

### 5. Fix artifact status logic

Use the stronger registry-aligned status set:
- `draft`
- `working`
- `validated`
- `canonical`
- `archived`

Rationale:
- this matches the earlier registry logic
- it is more useful than `reviewed/approved` for KnowledgeOS-style asset management

---

### 6. Keep JSON repair behavior honest

Do not claim repairs the code does not actually perform.

Current allowed repair scope in v1:
- remove markdown fences
- remove trailing commas
- retry parse

Do not document unimplemented bracket-repair behavior unless it is actually added.

---

## Scope rule

These corrections are **Phase 1.1 only**.
Do not add:
- new features
- routing logic expansion
- API endpoints
- screens
- advanced integrity logic
- auth or platform behavior

---

## Compact formula

**Phase 1.1 = consistency fixes, not feature growth.**
