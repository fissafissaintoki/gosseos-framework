# Run the GosseOS Workflow

## Purpose

This guide connects the core parts of the repository into one usable workflow.

The goal is simple:

```text
raw input -> router -> mode -> template -> artifact -> governance -> KnowledgeOS extract
```

---

## 1. Start With Raw Input

Raw input can be messy.

Example:

```text
We have problems in cold chain logistics. Picking is unstable, errors happen, and temperature deviations create risk.
```

Do not generate an answer immediately.

First route the work.

---

## 2. Run the Router

Use the local router tool:

```bash
python3 tools/gosseos_router.py "We have problems in cold chain logistics. Picking is unstable, errors happen, and temperature deviations create risk."
```

Expected routing:

```text
Problem Class: Operational Logistics Process
Primary Mode: AUDIT
Secondary Mode: BUILD
Artifact Type: Process Audit, Risk Matrix, or Decision Framework
Governance Signal: APPROVED WITH WARNING
```

---

## 3. Select the Correct Mode Logic

Open:

```text
templates/MODE_ROUTING_MATRIX.md
```

Use it to confirm:

- problem class
- primary mode
- secondary mode
- expected artifact

For this example:

```text
AUDIT + BUILD
```

---

## 4. Choose an Artifact Pattern

For logistics work, use:

```text
cases/LOGISTICS_COLD_CHAIN_RISK_CASE.md
cases/COLD_CHAIN_REAL_IMPACT.md
```

These files provide:

- risk areas
- KPI logic
- control measures
- before/after structure
- governance classification

---

## 5. Build the Artifact

The target artifact should contain:

1. Raw situation
2. Problem class
3. Mode routing
4. KPI or risk structure
5. Control measures
6. Governance gate
7. Red-team notes
8. Reusable conclusion

Recommended artifact types:

- process audit
- risk matrix
- decision framework
- management briefing
- KPI improvement case

---

## 6. Run the Governance Gate

Open:

```text
templates/GOVERNANCE_GATE.md
```

Check:

- assumptions
- missing data
- operational realism
- risks
- need for human escalation

Classify the artifact:

```text
APPROVED
APPROVED WITH WARNING
LIMITED
ESCALATE TO HUMAN
BLOCKED
```

---

## 7. Extract Reusable Knowledge

If the result is valuable, create a KnowledgeOS extract.

Extract should capture:

- reusable principle
- artifact type
- problem class
- mode combination
- future reuse cases
- limitations

Example:

```text
Cold chain logistics problems should not be treated as generic process issues.
They require combined AUDIT + BUILD + RED TEAM routing because performance, compliance, staffing, and temperature risk are linked.
```

---

## 8. Full Example Chain

```text
Raw Input:
Cold chain performance and error problems.

Router:
Operational Logistics Process -> AUDIT + BUILD.

Template:
Mode Routing Matrix confirms process audit path.

Case Pattern:
Cold Chain Risk Case provides KPI and risk structure.

Artifact:
Cold Chain Risk Matrix + Control Checklist.

Governance:
APPROVED WITH WARNING because site data must validate assumptions.

KnowledgeOS:
Save reusable logistics audit pattern.
```

---

## 9. Anti-Pattern

Wrong:

```text
Ask AI for advice and accept the first answer.
```

Right:

```text
Route the input, select mode, build artifact, verify governance, extract reusable knowledge.
```

---

## 10. Core Principle

GosseOS is not a prompt collection.

It is a workflow control system.

The value is not the answer.

The value is the repeatable path from messy input to controlled work.
