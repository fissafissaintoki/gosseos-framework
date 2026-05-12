# Universal Case Study Template

Status: USABLE
Version: v1.0

## Purpose

This template standardizes future case-study files in the GosseOS framework.

It ensures that every case is understandable, reusable, reviewable, and aligned with the Operator Fischer Method.

Use this template when turning raw input, a practical idea, a workflow, a product concept, or an operational problem into a structured case artifact.

---

## When to Use This Template

Use for:

- logistics use cases
- AI workflow cases
- process improvement cases
- governance cases
- MVP concepts
- innovation ideas
- public proof-of-work examples
- before/after transformations
- workplace or operational problem-solving cases

Do not use for:

- random notes
- purely speculative concepts without artifact target
- claims without evidence or assumptions
- legal, medical, financial, or safety decisions without governance warning

---

## Required Case Structure

Every case study should include:

```text
Purpose
Raw Input
Problem Class
Working Mode
Context
Process Logic
Artifact Output
Governance Check
Red-Team Notes
Quality Check
Reuse Note
Status Classification
```

---

## Copyable Markdown Skeleton

```markdown
# Case: [Case Name]

Status: DRAFT
Version: v0.1

## Purpose

Explain what this case is for and why it matters.

---

## 1. Raw Input

Describe the original idea, problem, situation, or user input.

```text
[Insert raw input here]
```

---

## 2. Problem Class

Define the type of problem.

Possible classes:

- operational process problem
- logistics / supply chain problem
- AI workflow problem
- communication problem
- governance / control problem
- safety / compliance problem
- product / MVP concept
- documentation / template problem
- decision-support problem

Selected problem class:

```text
[Problem Class]
```

Reason:

```text
[Why this class fits]
```

---

## 3. Working Mode

| Layer | Selection |
|---|---|
| Primary Mode | [BUILD / AUDIT / ANALYZE / RED TEAM / BRIEFING / GOVERNANCE / OPTIMIZE / EXECUTE] |
| Secondary Mode | [optional] |
| Verification Mode | [AUDIT / RED TEAM / GOVERNANCE] |
| Artifact Type | [case / template / matrix / workflow / prompt / MVP spec] |
| Status | DRAFT |

---

## 4. Context

Describe the operational, business, technical, or communication context.

Include:

- target user
- environment
- constraints
- stakeholders
- existing process
- pain points
- relevant assumptions

---

## 5. Current Problem / Before State

Describe the current state before the proposed solution.

```text
What is inefficient, unclear, risky, slow, unsafe, manual, error-prone, or hard to scale?
```

---

## 6. Proposed Solution / After State

Describe the improved state.

```text
What changes?
What becomes clearer?
What becomes safer, faster, more reusable, or more measurable?
```

---

## 7. Process Logic

Show the transformation or workflow.

```text
Step 1
   ↓
Step 2
   ↓
Step 3
   ↓
Result
```

---

## 8. Artifact Output

Define the concrete artifact produced by this case.

Possible outputs:

- workflow map
- decision matrix
- process checklist
- MVP specification
- prompt framework
- governance gate
- risk assessment
- worker instruction
- presentation concept
- case study
- app prototype

Selected output:

```text
[Artifact Output]
```

---

## 9. Value / Benefit

List expected benefits.

Examples:

- fewer errors
- faster orientation
- better communication
- clearer responsibility
- reusable process logic
- better documentation
- improved onboarding
- stronger auditability
- clearer decision-making

---

## 10. Risks and Assumptions

### Assumptions

- [Assumption 1]
- [Assumption 2]
- [Assumption 3]

### Risks

- [Risk 1]
- [Risk 2]
- [Risk 3]

---

## 11. Governance Check

Governance Warning:
This artifact supports structure and decision preparation. It does not replace human responsibility, expert review, compliance validation, legal review, safety approval, medical advice, financial advice, or operational release where required.

Classification:

```text
[APPROVED / APPROVED WITH WARNING / LIMITED / ESCALATE TO HUMAN / BLOCKED]
```

Reason:

```text
[Explain classification]
```

Required human review:

- [Owner / expert / responsible role]

---

## 12. Red-Team Notes

Ask:

```text
What could fail?
What is overstated?
What is missing?
What would a critic attack?
What could be misunderstood?
Where does this need validation?
```

Findings:

- [Finding 1]
- [Finding 2]
- [Finding 3]

---

## 13. Quality Check

| Check | Result |
|---|---|
| Purpose clear | [yes/no] |
| Input type defined | [yes/no] |
| Problem class defined | [yes/no] |
| Working mode defined | [yes/no] |
| Output defined | [yes/no] |
| Governance check included | [yes/no] |
| Reuse note included | [yes/no] |
| Risks visible | [yes/no] |
| Understandable without chat context | [yes/no] |

---

## 14. Reuse Note

Explain how this case can be reused.

Possible reuse:

- future case study
- presentation
- MVP build
- template
- prompt
- management briefing
- safety review
- public proof of work

---

## 15. Next Action

Define the next concrete step.

```text
[Next action]
```

---

## Core Principle

State the one-sentence principle behind this case.

```text
[Core principle]
```
```

---

## Status Classification Guide

Use one status per case:

```text
DRAFT
USABLE
APPROVED WITH WARNING
APPROVED
DEPRECATED
```

### DRAFT
Use when the case is incomplete or exploratory.

### USABLE
Use when the case is structured and can guide work, but still needs validation.

### APPROVED WITH WARNING
Use when the case is useful but depends on safety, compliance, real data, expert review, or operational validation.

### APPROVED
Use when the case is complete, low-risk, and reusable.

### DEPRECATED
Use when the case is outdated or replaced.

---

## Governance Trigger Checklist

Add a governance warning when the case involves:

- workplace safety
- worker monitoring or personal data
- legal claims
- medical topics
- financial decisions
- operational deployment
- compliance-sensitive workflows
- real-world automation
- vulnerable persons
- public claims about capability or certification

---

## Anti-Patterns

Avoid case files that:

- sound impressive but do not define a real problem
- introduce unnecessary system names
- skip the before/after logic
- hide assumptions
- claim production-readiness without validation
- ignore safety, privacy, or compliance risks
- contain no concrete artifact output
- cannot be understood outside the original chat

---

## Good Case Standard

A good case should let a new reader understand:

```text
What was the raw problem?
What problem class was detected?
Which mode was used?
What artifact was created?
What risks were found?
How can the result be reused?
```

---

## Final Rule

A case study is not a story.

A case study is proof that raw input was transformed into structured, reviewable, reusable work.
