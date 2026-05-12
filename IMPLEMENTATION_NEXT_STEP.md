# IMPLEMENTATION NEXT STEP

## Decision

The next step is:

**Start Phase 1 implementation.**

Do not continue with files 11–31 yet.
Do not hold the build for additional architecture discussion.

---

## Why this is the right next move

The project already has:
- app specification
- architecture decisions
- implementation plan
- finalized project structure
- first-file priority order

At this point, more planning creates diminishing returns.
The system now needs the first executable foundation.

---

## Phase 1 start order

1. `backend/app/schemas/schemas.py`
2. `backend/app/storage/database.py`
3. `backend/app/models/db.py`
4. `backend/app/utils/module_loader.py`
5. `backend/app/utils/json_repair.py`
6. `frontend/src/types/index.ts`

---

## Micro-decisions that should be fixed now and not reopen the build

### Router confidence threshold
Set the v1 fallback threshold to:

**0.6**

This should be hardcoded as a named constant and documented.

### Artifact version field
Use a simple v1-compatible rule:
- default initial value = `v1`
- manual increment later
- no semantic versioning logic in v1

This is enough for the first build.

---

## Explicit non-goals right now

Do not do these before Phase 1 is built:
- complete file-by-file expansion for all remaining files
- feature additions
- UI polish
- auth
- module service
- advanced integrity logic
- streaming / retry logic

---

## Build rule

**Stabilize the foundation first. Expand later.**

That means:
- data contracts first
- storage first
- persistence model first
- prompt loading utilities first
- frontend type mirror after backend schemas

Only then move into services and API routes.

---

## Compact formula

**Next step = Phase 1 now, with threshold 0.6 and artifact default version v1 fixed upfront.**
