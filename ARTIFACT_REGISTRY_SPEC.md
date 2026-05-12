# ARTIFACT REGISTRY SPEC

## Purpose

The Artifact Registry is the operational storage and indexing layer for reusable outputs inside the GosseOS / KnowledgeOS architecture.

Its purpose is to ensure that strong outputs do not disappear into chat history, folder chaos, or memory overload.

The Artifact Registry makes artifacts:
- identifiable
- versioned
- classifiable
- reloadable
- comparable
- auditable
- reusable

It is not the same as the active memory core.
The active memory core holds the governing logic.
The Artifact Registry holds concrete reusable outputs.

---

## Registry principle

**Do not keep artifacts as vague remembered fragments. Register them as reusable units.**

---

## What counts as an artifact

An artifact is any output that has durable reuse value.
Typical examples:
- one-pagers
- dossiers
- SOP-like structures
- frameworks
- decision sheets
- evaluation models
- templates
- prompt families
- reports
- portfolio assets
- decks
- specs
- policy drafts
- case documents

Outputs that are only temporary or conversational do not need to enter the registry.

---

## Minimum registry schema

Each registered artifact should have these fields:

### 1. Artifact ID
Unique identifier.
Recommended format:

`[DOMAIN]-[TYPE]-[YYYYMMDD]-[SHORTNAME]-v[VERSION]`

Examples:
- GOV-DOS-20260419-integrity-kernel-v1
- OPS-SOP-20260419-cold-chain-check-v2
- COM-ONE-20260419-public-short-description-v1

### 2. Title
Clear human-readable title.

### 3. Status
Recommended values:
- draft
- working
- validated
- canonical
- archived

### 4. Domain
Examples:
- governance
- operations
- logistics
- community
- branding
- application
- research
- creative

### 5. Problem Class
What kind of problem the artifact addresses.
Examples:
- analysis
- decision support
- planning
- communication
- documentation
- governance / risk
- creative development

### 6. Mode
Which GosseOS mode primarily generated or shaped it.
Examples:
- Architect
- Build
- Audit
- Red Team
- Briefing

### 7. Depth
Which processing depth was used.
Examples:
- Direct
- Compact
- Standard
- Endboss

### 8. Artifact Type
Examples:
- one-pager
- dossier
- SOP
- framework
- registry entry
- report
- post
- spec
- deck
- checklist

### 9. Purpose
Short statement describing what the artifact is for.

### 10. Source Input
Short statement describing what triggered or fed the artifact.

### 11. Assumption Level
Recommended values:
- low
- medium
- high

This indicates how much of the artifact depends on assumptions rather than stable facts.

### 12. Integrity Status
Recommended values:
- unchecked
- checked
- stable
- drift-risk
- needs-review

### 13. Governance Relevance
Recommended values:
- low
- medium
- high
- critical

### 14. File Location
Path or storage location of the artifact.

### 15. Version
Integer or semantic version.
Examples:
- v1
- v2
- v1.1

### 16. Last Reviewed
Date of latest explicit review.

### 17. Reuse Notes
Short note on where and how the artifact can be reused.

---

## Recommended extended schema

For more mature registry use, add:
- owner
- linked artifacts
- supersedes
- superseded by
- related cases
- public/internal classification
- confidence note
- reload test status
- comparison test status

---

## Registry status logic

### draft
Initial version. Not yet stable.

### working
Usable, but still evolving.

### validated
Reviewed and practically sound.

### canonical
Reference-grade artifact. Should be treated as a leading version.

### archived
No longer active, but still preserved.

---

## Integrity and reload rule

A registered artifact should be reloadable into another model or session without losing its basic:
- meaning
- structure
- intended use
- coherence

Minimum reload questions:
- does the artifact still make sense when reloaded?
- does its logic still hold?
- are assumptions still visible?
- did the artifact drift away from its original purpose?
- can another model interpret it consistently?

---

## Relationship to KnowledgeOS

KnowledgeOS is the knowledge and condensation layer.
The Artifact Registry is one of its operational storage mechanisms.

KnowledgeOS answers:
- what should be preserved?
- what remains valuable?
- what becomes canonical?

The Artifact Registry answers:
- where is it?
- what is its status?
- how is it classified?
- can it be reused and reloaded?

---

## Relationship to GosseOS

GosseOS work logic:

**Problem Class → Mode → Depth → Artifact → Verification**

The registry mainly stabilizes the final two parts:
- artifact persistence
- artifact verification / reuse

It converts outputs from temporary responses into managed reusable units.

---

## Minimal registry entry template

```md
ID: 
Title: 
Status: 
Domain: 
Problem Class: 
Mode: 
Depth: 
Artifact Type: 
Purpose: 
Source Input: 
Assumption Level: 
Integrity Status: 
Governance Relevance: 
File Location: 
Version: 
Last Reviewed: 
Reuse Notes: 
```

---

## Compact formula

**Artifact Registry = ID + Status + Classification + Location + Reuseability**

Without it, strong outputs disappear.
With it, outputs become reusable system assets.
