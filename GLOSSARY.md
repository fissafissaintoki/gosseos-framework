# Glossary

## Purpose

This glossary explains the core terms used in the GosseOS framework.

The goal is simple:
A new reader should understand the method without knowing the internal history behind it.

---

## Core Terms

### Operator Fischer Method

The public working method behind this repository.

It describes how messy input becomes structured, reviewable, reusable work.

```text
Raw input -> problem class -> working mode -> artifact -> review -> reuse
```

In plain language:

```text
Turn unclear input into a useful work product.
```

---

### GosseOS

The workflow and execution structure.

GosseOS defines how work is routed:

- What kind of problem is this?
- Which working mode fits?
- What artifact should be built?
- What risks or assumptions must be checked?
- What should be preserved for reuse?

In plain language:

```text
GosseOS is the operating structure for AI-assisted work.
```

---

### KnowledgeOS

The memory and extraction layer.

KnowledgeOS preserves reusable value from work sessions:

- principles
- prompts
- frameworks
- cases
- templates
- reusable patterns
- canon candidates

In plain language:

```text
KnowledgeOS keeps the useful parts from strong work sessions.
```

---

### Raw Input

Unfiltered starting material.

Examples:

- a messy idea
- a voice note
- a complaint
- a business problem
- a process issue
- a draft prompt
- a rough plan
- a conflict situation

Raw input is not the final task.
It must be interpreted and routed.

---

### Problem Class

The type of work hidden inside the raw input.

Examples:

| Raw Signal | Possible Problem Class |
|---|---|
| "This is unclear" | ambiguity |
| "Check this" | audit / evaluation |
| "What can go wrong?" | risk / red-team review |
| "Build this" | artifact creation |
| "Explain this professionally" | communication / briefing |
| "Make this reusable" | template / framework creation |

Problem class comes before prompting.

---

### Working Mode

A working mode defines how the AI should operate.

Examples:

| Mode | Meaning |
|---|---|
| META | clarify an unclear task |
| ANALYZE | understand structure, causes, patterns |
| BUILD | create a concrete artifact |
| AUDIT | check gaps, risks, weaknesses |
| RED TEAM | stress-test assumptions and failure points |
| BRIEFING | compress into decision-ready language |
| GOVERNANCE | define responsibility, limits, and controls |
| OPTIMIZE | improve an existing output |
| EXECUTE | perform a clear task or produce a deliverable |

In plain language:

```text
The mode tells the system how to think and work.
```

---

### Artifact

A usable work product.

An artifact is not just a response.
It should be structured, reusable, and reviewable.

Examples:

- checklist
- SOP
- decision matrix
- risk register
- management briefing
- prompt framework
- case study
- template
- knowledge extract

In plain language:

```text
An artifact is output that can be used again.
```

---

### Governance Gate

A review checkpoint before an artifact is treated as usable.

It checks:

- assumptions
- risks
- missing data
- operational realism
- responsibility
- escalation needs

Possible classifications:

```text
APPROVED
APPROVED WITH WARNING
LIMITED
ESCALATE TO HUMAN
BLOCKED
```

In plain language:

```text
The Governance Gate prevents uncontrolled output from becoming action.
```

---

### Red Team

A stress-test mode.

Red Team asks:

- What could fail?
- What is overstated?
- What assumption is weak?
- What would a critic attack?
- What risk is hidden?

In plain language:

```text
Red Team improves the result by attacking it before reality does.
```

---

### Router

A routing component that maps raw input to:

- problem class
- primary mode
- secondary mode
- artifact type
- governance signal

In this repository, the router is intentionally simple.
It demonstrates the method rather than claiming to be a full AI system.

---

### Case Library

A collection of before/after examples.

Each case should show:

1. raw input
2. problem class
3. mode routing
4. artifact output
5. review notes
6. reuse potential

In plain language:

```text
The case library proves the method with examples.
```

---

### Knowledge Extract

A condensed reusable lesson from a work session.

A good extract captures:

- what was learned
- what pattern was found
- what can be reused
- what limitations remain
- whether it is working material or a canon candidate

---

### Canon Candidate

A strong idea that may become part of the stable framework, but is not final yet.

Rule:

```text
Strong ideas are not canon automatically.
Reuse, review, and simplification come first.
```

---

## Term Hierarchy

```text
Operator Fischer Method
   -> public working method

GosseOS
   -> workflow and execution structure

KnowledgeOS
   -> memory and extraction layer

Artifacts
   -> reusable outputs

Governance Gate
   -> review and responsibility checkpoint
```

---

## One-Minute Explanation

This repository is about using AI as a structured work system.

Instead of:

```text
prompt -> answer
```

It uses:

```text
raw input -> problem class -> mode -> artifact -> review -> reuse
```

That means the value is not only the generated text.
The value is the repeatable working path.
