# Case: Prompt Generator Concept

## Purpose

This case shows how a vague AI tool idea can become a structured product concept.

The goal is to turn inspiration into a usable MVP frame.

---

## 1. Raw Input Type

Typical input:

```text
I want to build a prompt generator where people enter messy input and get a useful prompt or work mode back.
```

---

## 2. Problem Class

This is not only a prompt-writing task.

It combines:

- product concept design
- user workflow design
- problem classification
- prompt architecture
- output standardization
- usability control
- governance framing

---

## 3. Mode Routing

| Layer | Selection |
|---|---|
| Primary Mode | ARCHITECT |
| Secondary Mode | BUILD |
| Verification Mode | AUDIT |
| Artifact Type | MVP concept + workflow specification |
| Governance Signal | APPROVED WITH WARNING |

Reason:

A prompt generator must not only generate text.
It must understand the user intent, choose the correct output type, and prevent weak or unsafe outputs.

---

## 4. Product Definition

A prompt generator should answer four questions:

```text
1. What does the user want to achieve?
2. What problem class is behind the request?
3. Which working mode fits the task?
4. What output should be generated?
```

---

## 5. Minimal MVP Workflow

```text
User input
   ↓
Intent detection
   ↓
Problem-class routing
   ↓
Mode selection
   ↓
Prompt / artifact generation
   ↓
Quality and governance check
   ↓
Reusable output
```

---

## 6. MVP Feature Set

| Feature | Purpose |
|---|---|
| single input field | capture messy raw input |
| mode router | classify task type |
| output selector | prompt, checklist, briefing, framework, template |
| quality gate | check clarity and usability |
| governance warning | flag risk-sensitive tasks |
| copy-ready output | let user reuse result immediately |
| use case library | show examples and patterns |

---

## 7. Example User Flow

### User Input

```text
I need to explain a messy warehouse issue to management.
```

### Router Result

```text
Problem Class: Operational process communication
Primary Mode: BRIEFING
Secondary Mode: AUDIT
Output Type: management briefing prompt
Governance: APPROVED WITH WARNING
```

### Generated Prompt

```text
Create a management briefing about the following warehouse issue.
First separate facts, assumptions, risks, and required decisions.
Then produce a concise briefing with situation, impact, root causes, options, recommendation, and open data needs.
Keep the tone professional and operational.

Raw input:
[insert issue]
```

---

## 8. Red-Team Review

A weak prompt generator fails when it:

- gives generic prompts for every task
- ignores problem class
- hides risk
- produces impressive but unusable text
- has no examples
- has no quality gate

A strong prompt generator:

- routes the task first
- explains the selected mode
- creates a structured output
- provides a reusable result
- flags governance-sensitive situations

---

## 9. Governance Notes

The generator should warn users when input involves:

- legal claims
- medical advice
- financial decisions
- personal data
- workplace conflict
- safety-critical operations
- compliance-sensitive documentation

Classification:

```text
APPROVED WITH WARNING
```

---

## 10. Reuse Note

This concept can be reused for:

- a web prompt generator
- a GitHub demo
- a no-code prototype
- a community tool
- an internal AI assistant
- a case-library based learning system

---

## Core Principle

A useful prompt generator does not only improve wording.

It routes intent into the right working logic.
