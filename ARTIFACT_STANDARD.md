# Artifact Standard

## Purpose

This file defines the internal quality rule for every reusable artifact in the GosseOS framework.

The goal is simple:
No new file should be added only because it sounds interesting.
Every artifact must be understandable, usable, reviewable, and reusable.

---

## Core Rule

Every artifact must answer these seven questions:

```text
1. What is the purpose?
2. What input does it handle?
3. What problem class does it belong to?
4. Which working mode does it use?
5. What output does it produce?
6. What governance or quality check applies?
7. How can it be reused?
```

If a file cannot answer these questions, it is not yet a valid artifact.

---

## Required Artifact Structure

Every major artifact should follow this structure:

```markdown
# [Artifact Name]

## Purpose
Explain what this artifact is for.

## Input Type
Define what kind of raw input this artifact handles.

## Problem Class
Name the type of problem this artifact addresses.

## Working Mode
Define the primary and optional secondary mode.

## Output
Describe what the artifact produces.

## Workflow
Show the step-by-step transformation logic.

## Governance Check
List assumptions, risks, limits, and escalation triggers.

## Quality Check
Check clarity, usefulness, accuracy, risk, and reuse potential.

## Reuse Note
Explain how this artifact can be reused or adapted.
```

---

## Minimum Quality Checklist

Before an artifact is accepted, check:

| Check | Question | Required |
|---|---|---|
| Clarity | Can a new reader understand it without chat context? | Yes |
| Utility | Can someone use it directly? | Yes |
| Structure | Does it follow a clear format? | Yes |
| Scope | Is the artifact focused and not overloaded? | Yes |
| Risk | Are assumptions and limits visible? | Yes |
| Governance | Is human responsibility clear where needed? | Yes |
| Reuse | Can this be adapted for another case? | Yes |
| Linkability | Can it be referenced from README, Navigator, or another file? | Preferred |

---

## Classification System

Every artifact should receive one classification:

```text
DRAFT
USABLE
APPROVED WITH WARNING
APPROVED
DEPRECATED
```

### DRAFT

The artifact is incomplete or still exploratory.

Use when:

- structure is not final
- examples are missing
- governance check is weak
- use case is unclear

### USABLE

The artifact can be used, but is not fully hardened.

Use when:

- structure is clear
- purpose is understandable
- still needs examples or red-team review

### APPROVED WITH WARNING

The artifact is useful, but depends on context, data, expert review, or operational validation.

Use when:

- risk-sensitive context exists
- assumptions are visible
- human review remains important

### APPROVED

The artifact is clear, reusable, and low-risk.

Use when:

- scope is stable
- examples are included
- governance check is complete
- no major unresolved risks exist

### DEPRECATED

The artifact is outdated or replaced.

Use when:

- terminology changed
- framework logic moved elsewhere
- a newer version exists

---

## Governance Trigger Rules

Add a governance warning if the artifact touches:

- legal matters
- medical or health topics
- finance or investment decisions
- workplace conflict
- personal data
- safety-critical operations
- compliance-sensitive workflows
- claims about professional qualification
- operational changes with real-world consequences

Governance warning format:

```text
Governance Warning:
This artifact supports structure and decision preparation. It does not replace human responsibility, expert review, legal review, medical advice, compliance validation, or operational approval where required.
```

---

## Red-Team Questions

Before release, ask:

```text
What could be misunderstood?
What is overstated?
What assumption is hidden?
Where could this fail in reality?
What would a critic attack first?
Does this still make sense outside the original chat?
Can this be used safely by someone else?
```

If the answer reveals weakness, fix the artifact before release.

---

## Anti-Patterns

Do not add files that are:

- impressive but vague
- too internal to understand
- only useful inside one chat
- missing purpose
- missing input type
- missing review logic
- full of claims without constraints
- named like a system but written like a note
- too broad to use directly

---

## Naming Standard

Use clear file names.

Preferred:

```text
rawinput-to-artifact.md
universal-artifact-builder.md
formal-response-letter.md
logistics-decision-model.md
governance-gate.md
```

Avoid:

```text
final-final-v3.md
new-idea.md
system-master-ultra.md
random-notes.md
```

File names should describe what the artifact does.

---

## Versioning Rule

If an artifact changes meaning, create a new version or clearly update the status.

Recommended version note:

```text
Status: USABLE
Version: v1.0
Last Review: YYYY-MM-DD
```

For public files, avoid excessive internal version noise unless needed.

---

## Release Rule

A new public artifact should not be considered ready until it has:

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

---

## Final Rule

No artifact leaves the system as loose text.

Every strong output should become one of the following:

- framework
- case
- template
- prompt
- checklist
- matrix
- briefing
- knowledge extract
- review file

If it cannot become one of these, it is probably not an artifact yet.
