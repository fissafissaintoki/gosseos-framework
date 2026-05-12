# ARCHITECTURE DECISIONS V1

## Purpose

This document fixes the first three implementation decisions for GosseOS Workbench v1.

These decisions are intentionally biased toward:
- fast buildability
- clear architecture
- low complexity in v1
- controlled Claude usage
- modular upgrade paths later

---

## Decision 1 – GosseOS module source

### Decision
Use **local markdown files from the repository** as the primary GosseOS module source in v1.

### Included modules
- `GOSSEOS_CORE.md`
- `INTEGRITY_KERNEL.md`
- `MODE_SPECIFICATIONS.md`
- `KNOWLEDGEOS_CORE.md`
- `ARTIFACT_REGISTRY_SPEC.md`

### Why
This is the simplest and most controllable option for v1.
It gives:
- explicit version control
- predictable prompt composition
- no additional service dependency
- easy local development
- easy Git-based iteration

### Not chosen in v1
A separate module service is **not** required in v1.
That would introduce:
- extra complexity
- API dependency
- synchronization burden
- unnecessary architectural overhead too early

### Future upgrade path
If v1 proves useful, a separate module service can later be introduced for:
- central module management
- dynamic prompt assembly
- version pinning by environment
- multi-app reuse

---

## Decision 2 – Router logic

### Decision
Use a **hybrid router**:
- **rule-based routing first**
- **optional Claude classification fallback second**

### v1 default
The router should start with deterministic rule-based routing.
Examples:
- keyword mapping
- simple heuristics
- explicit user selections
- default artifact suggestions

### Fallback
If rule confidence is weak or input is ambiguous, the backend may call Claude for a lightweight classification step.

### Why
Pure Claude routing in v1 would make the system:
- harder to debug
- less predictable
- more expensive
- more opaque

Pure rule-based routing is easier to control, but too rigid alone.
So the best v1 balance is:

**deterministic first, Claude only when needed**

### Operational rule
If the user manually overrides the route, the manual decision wins.

---

## Decision 3 – Output parsing

### Decision
Use **structured JSON output from Claude** wherever possible.

### v1 output contract
Claude should return a fixed JSON structure aligned to GosseOS output discipline.
Recommended fields:
- `core_result`
- `facts`
- `assumptions_uncertainties`
- `limits`
- `optional`

### Why
JSON is preferred because it gives:
- stable rendering in the app
- cleaner persistence
- better integrity checks
- easier registry save flow
- clearer artifact sectioning

### Fallback behavior
If Claude returns malformed or partial JSON:
- backend attempts safe repair/parsing
- if repair fails, mark output as parse-failed
- render raw text in a controlled fallback view
- do not silently pretend the structure was valid

### Not chosen in v1
Freeform text split by headings alone is not the primary strategy.
That approach is too fragile for:
- reliable rendering
- artifact storage
- integrity checks
- future compare / reload features

Freeform section parsing can remain only as an emergency fallback.

---

## Compact summary

### 1. GosseOS module source
**Local repo markdown first.**
No separate module service in v1.

### 2. Router logic
**Hybrid routing.**
Rule-based first, Claude fallback when ambiguity is high.

### 3. Output parsing
**Structured JSON first.**
Controlled raw-text fallback only if parsing fails.

---

## Practical design formula

**v1 = local module files + deterministic routing core + JSON output contract**

This keeps the first build:
- simple enough to ship
- strong enough to scale later
- and disciplined enough to remain GosseOS instead of drifting into a generic chat app
