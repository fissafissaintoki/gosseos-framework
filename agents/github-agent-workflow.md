# GitHub Agent Workflow

Status: DRAFT
Version: v0.1

## Purpose

This workflow explains how to use GitHub as the controlled work environment for the Operator Upgrade Agent.

The goal is to improve working method, artifacts, cases, prompts, and documentation without drifting into uncontrolled system expansion.

---

## Core Principle

```text
GitHub is the artifact workspace.
The agent is the reviewer, builder, and structure assistant.
The human remains the owner.
```

---

## Recommended Workflow

```text
Issue -> Agent Diagnosis -> Artifact Proposal -> File Change -> Red-Team Review -> Human Approval -> Merge / Keep Draft
```

---

## 1. Create an Issue

Every new workstream should start as an issue.

Issue title format:

```text
[MODE] Short artifact goal
```

Examples:

```text
[BUILD] Create GlowGlove MVP workflow
[AUDIT] Review README for public clarity
[RED TEAM] Stress-test GlowGlove safety assumptions
[OPTIMIZE] Simplify Operator Fischer Method explanation
[GOVERNANCE] Add pilot gate for wearable logistics systems
```

---

## 2. Issue Template

Use this structure:

```markdown
## Raw Input

## Goal

## Problem Class

## Suggested Mode

## Target Artifact

## Constraints

## Risk / Governance Notes

## Definition of Done
```

If problem class or mode is unclear, set:

```text
Problem Class: unknown
Suggested Mode: META
```

---

## 3. Agent Diagnosis

The Operator Upgrade Agent should respond with:

```markdown
# Operator Upgrade Result

## 1. Interpreted Task
## 2. Problem Class
## 3. Selected Mode
## 4. Proposed Artifact
## 5. Upgrade Actions
## 6. Red-Team Findings
## 7. Governance Check
## 8. Reuse / KnowledgeOS Note
## 9. Final Status
```

The agent must identify whether the task is:

- worth building
- needs simplification
- should be merged with existing files
- requires governance review
- should remain a draft
- should be rejected as drift

---

## 4. File Placement Rules

| Artifact Type | Folder |
|---|---|
| method or framework | frameworks/ |
| reusable prompt | prompts/ |
| practical example | cases/ |
| reusable form or checklist | templates/ |
| safety / audit / red-team result | reviews/ |
| agent specification | agents/ |
| local scripts | tools/ |
| preserved extracts | knowledgeos/ |
| app prototype | app/ |

---

## 5. Artifact Standard Gate

Before file creation or update, check:

```text
Purpose
Input Type
Problem Class
Working Mode
Output
Governance Check
Reuse Note
Status Classification
```

If missing, classify as:

```text
DRAFT
```

---

## 6. Red-Team Gate

The agent must check:

```text
Is this too abstract?
Is this duplicating an existing file?
Is terminology drifting?
Is there a concrete artifact?
Can a new reader understand it?
Could this create safety, compliance, privacy, or operational risk?
Does the output overclaim?
```

---

## 7. Governance Gate

Required when the artifact involves:

- safety
- worker data
- logistics operations
- legal / medical / financial matters
- workplace conflict
- compliance
- real-world deployment
- automation or agent execution

Governance result must be one of:

```text
APPROVED
APPROVED WITH WARNING
LIMITED
ESCALATE TO HUMAN
BLOCKED
```

---

## 8. Pull Request Rule

For larger changes, use a branch and PR.

PR title format:

```text
[MODE] Add / improve artifact name
```

PR body:

```markdown
## Purpose

## Changed Files

## Artifact Standard Check

## Red-Team Findings

## Governance Check

## Remaining Limitations
```

---

## 9. Anti-Drift Rule

If a change adds more abstraction than practical value, the agent should respond:

```text
This appears to be system drift.
Reduce scope to one concrete artifact, one target user, and one reuse path.
```

---

## 10. Recommended First Issues

```text
[BUILD] Create GlowGlove MVP app specification
[RED TEAM] Review GlowGlove data protection risks
[OPTIMIZE] Simplify README for non-technical readers
[BUILD] Add Case Study template
[GOVERNANCE] Add wearable logistics pilot gate
```

---

## Final Rule

No issue should become a file until it has a clear artifact target.

No file should be treated as stable until it passes artifact standard, red-team review, and governance check where required.
