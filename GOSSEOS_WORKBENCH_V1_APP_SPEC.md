# GOSSEOS WORKBENCH V1 – APP SPECIFICATION

## Purpose

GosseOS Workbench v1 is the first practical app shell for the GosseOS architecture.

It is not a generic chat clone.
It is a structured AI workbench that turns raw input into routed, mode-aware, artifact-based output with optional registry persistence.

The core workflow is:

**Raw Input → Problem Class → Mode → Depth → Artifact → Claude → Review → Save**

---

## Product goal

Version 1 should prove one thing:

A structured GosseOS workflow produces better, more controllable, and more reusable results than normal freeform chat.

The app should feel like a workbench, not like a toy.

---

## What v1 is

- a structured single-user workbench
- a Claude-powered GosseOS execution shell
- a routing-aware artifact generator
- a first registry-connected work surface

---

## What v1 is not

- not a full autonomous agent swarm
- not a multi-user platform
- not a workflow marketplace
- not an enterprise governance dashboard
- not a generic chatbot product
- not a no-code automation suite

v1 must stay narrow and disciplined.

---

## Core user flow

### Step 1 – Input
The user enters raw input, a case, a problem, or an idea.

### Step 2 – Routing
The app determines or suggests:
- problem class
- mode
- depth
- artifact type

The user can confirm or adjust.

### Step 3 – Claude execution
The backend composes the right prompt stack from GosseOS modules and sends the request to Claude.

### Step 4 – Structured output
The app displays the output in a disciplined format.

### Step 5 – Review and save
The user reviews the result and can save it into the Artifact Registry.

---

## Main screens

## Screen 1 – Input
### Purpose
Capture the raw case.

### Fields
- Input title (optional)
- Main raw input text area
- Context notes (optional)
- Desired outcome (optional)

### Actions
- Analyze input
- Clear

---

## Screen 2 – Routing
### Purpose
Turn raw input into structured GosseOS execution settings.

### Fields
- Problem Class
- Mode
- Depth
- Artifact Type
- Governance relevance flag (optional)

### Actions
- Accept routing
- Adjust routing manually
- Continue to execution

### Default route dimensions
#### Problem Class examples
- analysis
- planning
- decision support
- documentation
- communication
- governance / risk
- creative development

#### Mode examples
- Architect
- Build
- Audit
- Red Team
- Briefing

#### Depth values
- Direct
- Compact
- Standard
- Endboss

#### Artifact Type examples
- one-pager
- dossier
- SOP-like structure
- report
- post
- framework
- prompt
- briefing note
- registry entry

---

## Screen 3 – Output
### Purpose
Show Claude output as a work artifact, not as an endless chat stream.

### Standard display structure
- Core result
- Facts
- Assumptions / uncertainties
- Limits
- Optional extension

### Actions
- Copy result
- Re-run
- Run integrity review
- Save to registry

---

## Screen 4 – Registry Save
### Purpose
Turn a useful output into a managed reusable artifact.

### Fields
- Artifact ID
- Title
- Status
- Domain
- Problem Class
- Mode
- Depth
- Artifact Type
- Purpose
- Source Input
- Assumption Level
- Integrity Status
- Governance Relevance
- Version
- Reuse Notes

### Actions
- Save artifact
- Cancel

---

## Screen 5 – Artifact View (basic)
### Purpose
View a saved artifact.

### Fields / sections
- Metadata header
- Main content
- Status
- Version
- Last reviewed
- Reuse notes

### Actions
- Open
- Duplicate
- Mark reviewed
- Archive

---

## Backend logic

The backend should not send one giant universal prompt.
It should compose the request modularly.

## Prompt composition order
1. GosseOS core logic
2. Integrity Kernel
3. Selected mode specification
4. User task block
5. Requested artifact format
6. Optional governance add-on if needed

This keeps the request disciplined and avoids unnecessary prompt inflation.

---

## Minimal backend modules

### 1. Input parser
Reads raw input and basic context.

### 2. Router
Maps input to:
- problem class
- mode
- depth
- artifact type

### 3. Prompt composer
Builds the Claude request from the active GosseOS documents.

### 4. Claude execution service
Calls Claude and receives structured output.

### 5. Integrity review service (basic)
Runs lightweight checks for:
- drift
- hallucination risk
- artifact mismatch
- unsupported claims

### 6. Registry service
Stores approved outputs as reusable artifacts.

---

## Data model (minimum)

### Case record
- case_id
- title
- raw_input
- context_notes
- desired_outcome
- created_at

### Routing record
- case_id
- problem_class
- mode
- depth
- artifact_type
- governance_relevance

### Output record
- output_id
- case_id
- generated_text
- integrity_note
- created_at

### Artifact record
- artifact_id
- case_id
- output_id
- title
- status
- domain
- problem_class
- mode
- depth
- artifact_type
- purpose
- assumption_level
- integrity_status
- governance_relevance
- version
- reuse_notes
- created_at
- last_reviewed

---

## Recommended stack

### Frontend
- Next.js or React

### Backend
- FastAPI

### Model layer
- Claude API

### Storage
- SQLite first
- Postgres later if needed

### Source of system logic
- markdown files from the GosseOS repository

---

## V1 design principles

1. One clear workflow
2. No feature sprawl
3. Route before generate
4. Artifact before chat feeling
5. Save reusable results
6. Keep integrity visible
7. Do not hide assumptions

---

## Success criteria for v1

v1 is successful if it proves:
- routing improves output quality
- the workbench produces reusable artifacts
- results are more stable than freeform prompting
- the registry captures durable outputs
- the app feels like disciplined work, not random chat

---

## Build sequence

### Phase 1
- Input screen
- Routing screen
- Output screen

### Phase 2
- Registry save flow
- Artifact view

### Phase 3
- Lightweight integrity review
- basic compare / rerun logic

---

## Compact formula

**GosseOS Workbench v1 = structured input + routed Claude execution + artifact output + registry persistence**
