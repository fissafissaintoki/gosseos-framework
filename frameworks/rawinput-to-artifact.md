# Raw Input to Artifact Framework

## Purpose

This framework turns messy input into a reusable work artifact.

It is the core operating pattern behind the Operator Fischer Method and GosseOS.

The goal is not to produce a clever answer.
The goal is to create structured work that can be checked, reused, improved, and explained to other people.

---

## Core Chain

```text
Raw Input -> Problem Class -> Working Mode -> Structure -> Artifact -> Review -> Reuse
```

---

## 1. Raw Input

Raw input is the unfiltered starting material.

It can be:

- a messy idea
- a voice note
- a complaint
- an operational problem
- a business case
- a process issue
- a prompt draft
- a job application angle
- a project concept
- a risk signal

Do not treat raw input as the final task.
Raw input is material that must be routed.

### Raw Input Capture Questions

```text
What is being said?
What is actually needed?
What is the hidden pressure behind the request?
What would be useful as a final artifact?
What should not be assumed yet?
```

---

## 2. Problem Class

The problem class defines what kind of work this is.

Most weak AI results happen because the task is framed incorrectly.

Example:

```text
"Write me a response" may actually be:
- conflict de-escalation
- formal documentation
- legal-risk-sensitive communication
- emotional sorting
- evidence structuring
```

### Common Problem Classes

| Problem Class | Signal | Typical Output |
|---|---|---|
| Ambiguity | unclear idea, scattered notes | clarified work frame |
| Analysis | understand causes or structure | analysis brief |
| Decision | compare options | decision matrix |
| Process | improve or document workflow | SOP, process map, checklist |
| Risk | expose failure points | risk register, red-team review |
| Communication | explain something clearly | letter, briefing, post |
| Positioning | present capability or project | profile, pitch, README |
| Governance | define control and responsibility | gate, policy, escalation logic |
| Reuse | preserve strong work | template, prompt, extract |

---

## 3. Working Mode

A working mode defines how the AI should operate.

| Mode | Use When | Output Discipline |
|---|---|---|
| META | the task itself is unclear | clarify frame before building |
| ANALYZE | causes and structure matter | separate facts, assumptions, patterns |
| BUILD | a concrete asset is required | produce a reusable artifact |
| AUDIT | something must be checked | identify gaps, risks, weaknesses |
| RED TEAM | failure would matter | attack assumptions and harden result |
| BRIEFING | audience needs fast orientation | compress into decision-ready form |
| GOVERNANCE | responsibility/control matters | define owner, gate, escalation, limits |
| OPTIMIZE | output exists but is weak | improve clarity, usability, impact |
| EXECUTE | action is clear | give steps or produce deliverable |

Rule:
Use one primary mode and at most one secondary mode unless the task is explicitly complex.

---

## 4. Structure

Before writing the final output, define the structure.

Minimum structure:

```text
1. Goal
2. Context
3. Problem Class
4. Mode
5. Artifact Type
6. Constraints
7. Review Criteria
8. Final Output
```

If this step is skipped, the output usually becomes a text wall.

---

## 5. Artifact

An artifact is a usable work product.

It should be:

- clear
- reusable
- reviewable
- named
- versionable
- understandable outside the original chat

### Artifact Examples

| Need | Artifact |
|---|---|
| compare options | decision matrix |
| control risk | risk register |
| explain to management | briefing note |
| repeat a task | checklist or SOP |
| reuse a method | framework |
| improve a prompt | prompt template |
| document a case | case study |
| preserve learning | knowledge extract |

---

## 6. Review

Every artifact gets reviewed before release.

Minimum review gate:

```text
Clarity: Can an outsider understand it?
Utility: Can someone use it immediately?
Accuracy: Are claims grounded and not overstated?
Risk: What could go wrong if this is used?
Governance: Who remains responsible?
Reuse: Can this be adapted later?
```

Classification:

```text
APPROVED
APPROVED WITH WARNING
LIMITED
ESCALATE TO HUMAN
BLOCKED
```

---

## 7. Reuse

Strong outputs should not disappear in chat history.

After review, convert the result into one of these:

- template
- case
- prompt
- checklist
- framework
- knowledge extract
- README section
- public explanation

Reuse rule:

```text
If a result solves a recurring problem, it should become an asset.
```

---

## End-to-End Example

### Raw Input

```text
I need to answer an organization, but I am annoyed because they did not respond clearly.
```

### Routed Work

```text
Problem Class: Formal communication + conflict de-escalation
Mode: BUILD + AUDIT
Artifact: factual response letter
Governance: check tone, claims, evidence, and escalation risk
```

### Output Target

```text
A polite, firm, factual letter that states the issue, requests written clarification, and avoids emotional escalation.
```

---

## Anti-Patterns

Do not:

- write immediately from emotional raw input
- hide assumptions
- create outputs that only make sense inside the chat
- use many modes without reason
- call something a system when it is only a text
- skip review because the first draft sounds good

---

## Core Principle

A prompt creates an answer.

A routed workflow creates repeatable working capability.
