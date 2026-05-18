# Skill: Multi-Agent Prompt Orchestration

## Status

Canon candidate / active working skill.

## Purpose

This skill defines how Operator Fischer uses multiple AI systems as a coordinated working chain instead of treating each model as an isolated chatbot.

The skill is designed for situations where one model should structure, another should execute technical work, and another should validate, document, or harden the output.

---

## Core idea

A single prompt creates an answer.

A coordinated multi-model workflow creates reusable operating capability.

```text
Operator Fischer
-> Architecture / Routing Model
-> Codex
-> Claude
-> Target System
-> Verification
-> Artifact
-> Knowledge Layer
-> Reuse
```

---

## Role model

| Actor | Role |
|---|---|
| Operator Fischer | Human owner, final decision-maker, governance authority |
| ChatGPT | Architecture, routing, context management, prompt engineering, quality control |
| Codex | Code generation, Bash automation, runtime logic, technical execution |
| Claude | Long-form analysis, documentation, refactoring, safety validation, governance review |

---

## When to use this skill

Use this skill when the problem requires:

- technical execution plus structured planning
- Bash, code, automation, or system operations
- documentation and validation of operational steps
- clean handoff prompts between AI systems
- repeatable artifact production
- human-controlled agent-style workflows

Typical problem classes:

- Storage cleanup / file migration
- Repository refactoring
- Web app improvement
- Workflow automation
- SOP creation
- Prompt system construction
- Governance review of technical procedures

---

## Routing logic

```text
Raw input
-> identify problem class
-> select working mode
-> select target model
-> generate handoff prompt
-> execute / analyze / validate
-> produce artifact
-> extract reusable knowledge
```

### Model routing

| Task type | Target |
|---|---|
| Architecture, structure, orchestration | ChatGPT |
| Bash, code, automation, system operations | Codex |
| Long-form analysis, documentation, governance, validation | Claude |
| Final approval, risk acceptance, real-world execution | Operator Fischer |

---

## Standard handoff format

### Codex handoff

```text
# CODEX TASK
ZIEL: [precise technical objective]
INPUT: [available context, files, assumptions]
OUTPUT: [script, command set, patch, automation, report]
REGELN: [constraints, safety boundaries, macOS assumptions]
KONTEXT: [why the task matters and how it fits the workflow]
```

### Claude handoff

```text
# CLAUDE TASK
ZIEL: [precise analysis or documentation objective]
INPUT: [available context, draft, code, or operation]
OUTPUT: [review, plan, documentation, governance report]
FOKUS: [analysis / documentation / governance / refactoring]
KONTEXT: [system background and intended reuse]
```

---

## Runtime states

| State | Meaning |
|---|---|
| ANALYZE | Understand context, constraints, risks, and target state |
| PLAN | Define workflow, steps, dependencies, and review points |
| BUILD | Produce the artifact, script, prompt, or implementation |
| VERIFY | Check quality, safety, completeness, and assumptions |
| EXECUTE | Perform reversible or approved action |
| REPORT | Summarize outcome, remaining risks, and reuse value |
| SAFE MODE | Limit operation to non-destructive analysis or dry-run |

---

## Governance rules

- Human remains owner.
- AI systems are tools, not autonomous authorities.
- No irreversible operation without explicit review.
- No destructive file operation by default.
- Critical actions must be marked with `[KRITISCH]`.
- Assumptions must be marked with `[ANNAHME]`.
- Uncertainty must be visible.
- Every operational workflow needs a dry-run or reviewable plan when possible.

---

## Confidence layer

Outputs should mark confidence where relevant:

| Label | Meaning |
|---|---|
| Sicher | Strongly grounded in input or verified source |
| Annahme | Plausible but not verified |
| Unsicher | Missing information or unresolved ambiguity |
| Risiko | Could cause damage, data loss, wrong decision, or operational disruption |

---

## Failure handling

Escalate to Operator Fischer when:

- target path is unknown
- external storage is not confirmed
- operation could delete, overwrite, or corrupt data
- model output conflicts with previous constraints
- system state is not known
- requested action exceeds safe operating boundaries

Default fallback:

```text
Switch to SAFE MODE:
- analyze only
- create report
- produce dry-run commands
- request explicit operator review before execution
```

---

## Example case: Storage Recovery Operation

### Problem

The internal macOS storage is full. The Downloads folder contains many files. The objective is to free at least 100 GB without deleting anything.

### Workflow

```text
Operator Fischer
-> ChatGPT creates architecture and routing
-> Codex builds Bash-controlled file analysis and move logic
-> Claude validates the operation plan and documents risk/recovery
-> Operator Fischer approves execution
-> Results are stored as a reusable case
```

### Target behavior

- Analyze `~/Downloads`
- Identify duplicate files by hash
- Move duplicates to external storage folder `Dopplung`
- Move large non-critical files to external archive folders
- Do not delete files
- Validate recovered internal storage
- Produce an operation report

---

## Reuse note

This skill should be referenced whenever Operator Fischer wants to coordinate ChatGPT, Codex, and Claude through a structured prompt chain.

It belongs to KnowledgeOS as a skill artifact. Memory should only retain the routing principle and activate this skill when matching problem classes appear.
