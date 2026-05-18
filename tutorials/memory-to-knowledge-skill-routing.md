# Tutorial: Memory-to-Knowledge Skill Routing

## Purpose

This tutorial explains the operating principle behind Operator Fischer's Memory and Knowledge separation.

The central rule:

```text
Memory = small, stable, routing-oriented
Knowledge = large, modular, artifact-oriented
```

Memory should not become a dumping ground for every detail. It should behave like a selection and routing layer that detects what kind of problem is present and activates the right KnowledgeOS skill.

---

## Layer model

| Layer | Function |
|---|---|
| Memory | Stable identity, principles, routing logic, recurring preferences |
| KnowledgeOS | Skills, workflows, SOPs, cases, prompts, reusable artifacts |
| Runtime | Current session, temporary context, active task execution |
| Verification | Review, risk control, quality gate |
| Artifact Layer | Final reusable output |

---

## Memory as a routing agent

Memory should act like a lightweight internal router:

```text
Incoming request
-> detect problem class
-> detect objective
-> detect risk level
-> detect expected output type
-> select matching Knowledge skill
-> pin relevant skill into active context
-> route task to correct model or mode
```

This means the agentic behavior begins at Memory level.

Memory does not need to store every script, case, or document. It only needs to know which kind of reusable capability exists and when to activate it.

---

## What belongs in Memory

| Type | Example |
|---|---|
| Core operating principles | Human remains owner, AI remains tool |
| Stable work logic | Raw input -> problem class -> mode -> artifact -> review -> reuse |
| Routing preferences | Code to Codex, documentation/governance to Claude |
| Persistent constraints | macOS-only, structured outputs, no Windows default |
| Skill index awareness | Multi-Agent Prompt Orchestration exists as Knowledge skill |

---

## What belongs in KnowledgeOS

| Type | Example |
|---|---|
| Skills | Multi-Agent Prompt Orchestration |
| SOPs | Storage cleanup procedure |
| Workflows | Codex -> Claude -> verification chain |
| Cases | Storage Recovery Operation: 100 GB free without deleting files |
| Prompts | Codex handoff, Claude handoff, cooperation protocol |
| Templates | Governance gate, artifact standard, review checklist |

---

## Example: activating the Multi-Agent skill

### User request

```text
I need Codex and Claude to work together on a terminal-based cleanup operation.
```

### Memory detection

```text
Problem class: System operation / automation
Risk: Medium to high, because files may be moved
Output type: Bash script + validation + governance
Needed skill: Multi-Agent Prompt Orchestration
Target models: Codex + Claude
```

### Skill activation

Memory pins:

```text
knowledgeos/skills/multi-agent-prompt-orchestration.md
```

### Runtime routing

```text
ChatGPT -> architecture and handoff prompts
Codex -> Bash logic and technical implementation
Claude -> operation plan, documentation, risk review
Operator Fischer -> final approval
```

---

## Governance rule

The more operational risk a task has, the more explicit the review gate must be.

For file operations:

- dry-run first
- no deletion by default
- external target path must be validated
- move operations must be logged
- rollback notes must exist

---

## Minimal trigger rule

If a request contains any of the following signals, Memory should consider Multi-Agent Prompt Orchestration:

- Codex + Claude
- Bash automation
- terminal operation
- handoff prompt
- agent chain
- system operation
- reusable workflow
- skill registry
- governance review
- artifact creation

---

## End state

The Operator Fischer architecture becomes more robust when:

```text
Memory selects.
Knowledge stores.
Runtime executes.
Verification hardens.
Artifacts preserve.
```
