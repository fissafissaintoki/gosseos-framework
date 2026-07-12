# ERROR-TO-UPGRADE GATE

**System:** GosseOS / Operator Fischer  
**Version:** v1.0  
**Status:** ACTIVE RUNTIME GUARD  
**Owner:** Operator Fischer  
**Created:** 2026-07-12  
**KnowledgeOS Link:** `KOS-0019 — ERROR-TO-UPGRADE PROTOCOL v1.0`

## Purpose

Prevent a correction-worthy failure from repeating unchanged.

## Mandatory gate

Before any tool call or build action:

```text
1. Resolve active state.
2. Detect stop, collection-only, audit-only, or owner-approval requirements.
3. Classify the problem.
4. Retrieve prior artifacts, canon, files, and decisions.
5. Resolve mandatory locks.
6. Execute the smallest allowed action.
7. Verify against invariants.
8. Convert P0/P1 failure into guard + regression + KnowledgeOS artifact.
9. Stop when the requested artifact and proof are complete.
```

## Hard blocks

```text
STOP active                         → no tool call
UPGRADE ON / collection-only        → no generation or editing
repository or existing system       → audit before build
named recurring entity or location  → canon retrieval before build
unresolved required lock            → no generation
failed quality gate                 → no release
```

## Frustration routing

Treat user frustration as a routing signal:

- wrong priority
- too much meta
- no usable artifact
- unwanted new track
- missing closure
- ignored prior system state

Repair the active track. Do not create another project.

## Canon-sensitive visual gate

Required before image generation:

```text
IDENTITY_LOCK
ANATOMY_LOCK
AUGMENTATION_LOCK
WARDROBE_LOCK
LOCATION_LOCK
WORLD_LOCK
RWOM_LOCK
ACTION_LOCK
OUTPUT_LOCK
NEGATIVE_LOCK
```

Only required locks must pass, but every required lock must pass.

## Error conversion

```text
Failure
→ Incident
→ Root Cause
→ Invariant
→ Runtime Guard
→ Regression
→ KnowledgeOS Registration
→ Verification
→ Owner Decision
```

No apology-only close.

## Stop condition

```text
artifact delivered
+ verification recorded
+ no unresolved required lock
+ owner retains release authority
```

Then stop.
