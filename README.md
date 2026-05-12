# GosseOS Framework — Operator Fischer Method

**GosseOS is a structured AI work system for turning messy input into reusable, reviewable work artifacts.**

This repository is not a random prompt collection.
It is a public framework for operating AI more like a work system:

```text
raw input -> problem class -> working mode -> artifact -> review -> reusable knowledge
```

The core idea is simple:

> A prompt creates an answer. An operator system creates repeatable working capability.

---

## What this project solves

Most AI workflows fail in the same places:

- the input is messy
- the problem type is unclear
- the output format is not defined
- assumptions are not checked
- good results disappear in chat history
- prompts are reused without context or quality control

GosseOS addresses this by adding structure before generation.

Instead of asking AI for a direct answer, the workflow first asks:

1. What kind of problem is this?
2. Which working mode fits the task?
3. What artifact should be built?
4. What risks, assumptions, or governance limits matter?
5. What should be saved for reuse?

---

## The operating model

```text
Human owner
   ↓
Raw input / idea / problem / case
   ↓
Problem-class detection
   ↓
Mode routing
   ↓
Artifact building
   ↓
Red-team and governance review
   ↓
KnowledgeOS extraction
   ↓
Case library / reusable framework / public proof of work
```

---

## Key concepts

### GosseOS

The workflow and execution structure.

It structures the work through problem classes, modes, artifact logic, review gates, and controlled execution.

### KnowledgeOS

The memory and extraction layer.

It preserves reusable principles, prompts, frameworks, cases, and canon candidates instead of letting valuable work disappear inside chat sessions.

### Operator Fischer Method

The public working method behind the system.

It translates raw input into structured, reusable work through a repeatable chain:

```text
raw input -> problem class -> mode -> structure -> artifact -> review -> reuse
```

For simple definitions, see the [Glossary](./GLOSSARY.md).

---

## Working modes

| Mode | Purpose |
|---|---|
| ANALYZE | Understand the problem, context, causes, and constraints |
| BUILD | Create a usable artifact such as a checklist, framework, prompt, or briefing |
| AUDIT | Check weaknesses, gaps, risks, and missing evidence |
| RED TEAM | Attack assumptions and improve robustness |
| BRIEFING | Compress complex material into management-ready form |
| GOVERNANCE | Define boundaries, ownership, escalation, and review logic |
| LOGISTICS | Structure operational process and supply-chain problems |

---

## Typical artifacts

| Artifact | Use |
|---|---|
| Decision matrix | Make options comparable and reviewable |
| Checklist | Turn quality requirements into repeatable checks |
| SOP / process instruction | Standardize recurring work |
| Management briefing | Create fast orientation for decision-makers |
| Prompt framework | Make AI usage reusable instead of improvised |
| Risk matrix | Make operational or governance risks visible |
| Case study | Show before/after transformation and proof of work |
| Knowledge extract | Preserve reusable principles from a work session |

---

## Quality standard

Every reusable artifact should follow the internal [Artifact Standard](./ARTIFACT_STANDARD.md).

Minimum rule:

```text
Purpose -> Input Type -> Problem Class -> Working Mode -> Output -> Governance Check -> Reuse Note
```

If a file cannot answer these questions, it is not yet a valid artifact.

---

## Start here

If you are new, use this path:

1. [Start in 2 Minutes](./START_IN_2_MIN.md)
2. [Public Short Description](./PUBLIC_SHORT_DESCRIPTION.md)
3. [Glossary](./GLOSSARY.md)
4. [Artifact Standard](./ARTIFACT_STANDARD.md)
5. [Run the GosseOS Workflow](./RUN_GOSSEOS_WORKFLOW.md)
6. [Navigator](./NAVIGATOR.md)
7. [Raw Input to Artifact Framework](./frameworks/rawinput-to-artifact.md)
8. [Universal Artifact Builder Prompt](./prompts/universal-artifact-builder.md)
9. [Red-Team Review](./reviews/RED_TEAM_REVIEW.md)

---

## Repository map

```text
gosseos-framework/
├── README.md
├── START_IN_2_MIN.md
├── PUBLIC_SHORT_DESCRIPTION.md
├── GLOSSARY.md
├── ARTIFACT_STANDARD.md
├── RUN_GOSSEOS_WORKFLOW.md
├── NAVIGATOR.md
├── frameworks/
│   └── rawinput-to-artifact.md
├── prompts/
│   └── universal-artifact-builder.md
├── cases/
│   ├── formal-response-letter.md
│   ├── logistics-decision-model.md
│   └── prompt-generator-concept.md
├── templates/
├── reviews/
│   └── RED_TEAM_REVIEW.md
└── knowledgeos/
```

---

## Example use cases

### Formal response

Raw input: emotional, unclear situation with an organization, service provider, insurer, or authority.

Output: structured, polite, factual response letter with a clear objective.

### Logistics decision model

Raw input: operational issue in warehousing, cold chain, replenishment, inventory, picking, or transport.

Output: decision matrix, control checklist, risk classification, and management summary.

### Prompt generator concept

Raw input: vague idea for an AI tool or workflow.

Output: target user, workflow, feature set, MVP structure, prompt logic, and risk controls.

---

## Governance principle

The human remains the owner.

AI can help structure, analyze, draft, and review work.
It must not replace human responsibility for decisions, risk, compliance, or execution.

---

## What this is not

This is not:

- a hype-first AI project
- a random list of clever prompts
- a single-model fan project
- an automation system without review logic
- a substitute for professional responsibility

---

## One-line summary

**GosseOS turns messy input into structured, reviewable, reusable work.**
