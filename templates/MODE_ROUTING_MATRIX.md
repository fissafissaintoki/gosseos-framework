# GosseOS Mode Routing Matrix

## Purpose

The Mode Routing Matrix translates raw input into the right working logic.

Most AI workflows fail because every request is treated as the same kind of task.
GosseOS starts by identifying the problem class before choosing the execution mode.

---

## Core Routing Logic

| Input Signal | Problem Class | Primary Mode | Output Type |
|---|---|---|---|
| Vague idea, messy note, unclear intention | Ambiguity | META | clarified structure, working frame |
| Existing text, plan, workflow, or claim needs evaluation | Evaluation | AUDIT | assessment, gaps, risks, score |
| Weaknesses, failure points, hidden risks needed | Stress test | RED TEAM | risk map, counterarguments, failure modes |
| New concept, system, document, or framework required | Creation | BUILD | artifact, template, system draft |
| Strategic positioning, narrative, public framing needed | Positioning | ARCHITECT | strategy, message, structure |
| Existing output needs to become sharper or cleaner | Improvement | OPTIMIZE | upgraded version, simplification |
| Clear operational action is required | Execution | EXECUTE | step-by-step runbook or deliverable |
| Management-ready summary is required | Communication | BRIEFING | executive summary, decision note |

---

## Default Decision Rule

1. Identify the actual problem class.
2. Select one dominant mode.
3. Add one secondary mode only if needed.
4. Produce an artifact, not a loose answer.
5. Run a verification or governance check before final output.

---

## Mode Definitions

### META
Used when the request itself is unclear.
Goal: convert chaos into a usable work frame.

### AUDIT
Used when something must be reviewed, scored, or evaluated.
Goal: separate signal from weakness.

### RED TEAM
Used when failure points matter.
Goal: expose risks before reality does.

### BUILD
Used when a concrete asset must be created.
Goal: produce a reusable artifact.

### ARCHITECT
Used for system design, positioning, or strategic structure.
Goal: define the operating model.

### OPTIMIZE
Used when something exists but is not strong enough.
Goal: improve clarity, usability, and impact.

### EXECUTE
Used when the next action is known.
Goal: perform or specify the work clearly.

### BRIEFING
Used for decision-maker communication.
Goal: compress complexity into decision-ready language.

---

## Example

Raw input:

> I have a logistics process problem and need to explain it professionally.

Routing:

- Problem class: process clarification + business communication
- Primary mode: BUILD
- Secondary mode: BRIEFING
- Artifact: structured process note or management one-pager
- Governance gate: check assumptions, operational feasibility, missing data

---

## Anti-Pattern

Wrong:

> Ask AI to write something immediately.

Right:

> Route the work first, then build the artifact.

---

## GosseOS Principle

A prompt asks.
A mode works.
A routed mode produces controlled output.
