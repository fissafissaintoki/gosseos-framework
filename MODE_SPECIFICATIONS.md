# MODE SPECIFICATIONS

## Purpose

This document defines the five core GosseOS modes as operational work modules.

The goal is to prevent mode confusion and to make routing, execution, and artifact expectations clear.

Core modes:
- Architect
- Build
- Audit
- Red Team
- Briefing

These modes are not stylistic labels.
They are different ways of working on different kinds of problems.

---

## 1. ARCHITECT

### Purpose
Use Architect mode when the task is to structure, model, frame, or design a system, method, workflow, or logic.

### Use when
- the problem is still unstructured
- architecture or framework is needed
- a system map is needed
- roles, layers, flows, or logic must be defined
- complexity needs a strong skeleton before execution

### Typical outputs
- system maps
- frameworks
- operating models
- logic trees
- workflow designs
- governance structures
- concept papers

### What Architect does well
- turns chaos into structure
- defines components and relationships
- clarifies what belongs to the system and what does not
- creates reusable models

### What Architect does not do
- final production wording
- detailed operational rollout by itself
- hostile testing
- pure summary work

### Typical failure mode
Using Architect when a direct execution artifact is needed.
Result: elegant system thinking, but no finished deliverable.

---

## 2. BUILD

### Purpose
Use Build mode when the task is to produce the actual artifact.

### Use when
- the structure is already clear enough
- a concrete output is required
- a deliverable must be created now
- translation from logic into form is needed

### Typical outputs
- one-pagers
- dossiers
- SOP-like structures
- templates
- posts
- documents
- prompts
- application attachments
- reports

### What Build does well
- creates usable outputs
- turns plans into artifacts
- makes ideas operational
- converts structure into concrete deliverables

### What Build does not do
- deep adversarial challenge by default
- governance review by default
- fundamental architecture redesign by default

### Typical failure mode
Using Build too early, before the problem class or structure is clear.
Result: polished output built on weak logic.

---

## 3. AUDIT

### Purpose
Use Audit mode when the task is to inspect, evaluate, verify, diagnose, or identify weaknesses.

### Use when
- quality must be checked
- drift or hallucination risk is suspected
- governance needs review
- a framework or artifact needs diagnosis
- strengths and weaknesses must be separated cleanly

### Typical outputs
- review notes
- weakness maps
- risk assessments
- quality checks
- integrity checks
- gap analyses
- decision memos

### What Audit does well
- identifies weak points
- checks coherence
- distinguishes strong from fragile elements
- surfaces hidden risks

### What Audit does not do
- produce the final polished artifact as its main goal
- attack as hard as Red Team
- create new architecture from scratch as its main goal

### Typical failure mode
Using Audit when the real need is output production.
Result: sharp diagnosis, but no deliverable.

---

## 4. RED TEAM

### Purpose
Use Red Team mode when the task is to challenge, pressure-test, break, falsify, or expose failure points under stress.

### Use when
- claims need hostile testing
- manipulation or collapse patterns matter
- governance failure must be simulated
- the system must be stress-tested, not politely reviewed
- robustness matters more than comfort

### Typical outputs
- attack surfaces
- collapse patterns
- adversarial tests
- contradiction exposure
- failure scenarios
- pressure-test reports

### What Red Team does well
- finds what normal review misses
- pressures weak logic
- reveals hidden contradictions
- shows how systems break under load or manipulation

### What Red Team does not do
- gentle improvement language
- polished final communication
- neutral executive summary by default

### Typical failure mode
Using Red Team too early on fragile early-stage work.
Result: destruction without enough structure to improve.

---

## 5. BRIEFING

### Purpose
Use Briefing mode when the task is to condense complex material into clear, decisionable, management-ready form.

### Use when
- leadership needs the essence
- a long discussion must be compressed
- signal must be separated from noise
- decisionability matters more than detail
- the output must be understandable fast

### Typical outputs
- executive summaries
- briefing notes
- concise memos
- talking points
- compact overviews
- key finding extracts

### What Briefing does well
- condenses complexity
- preserves signal
- improves readability and decision speed
- creates portable summaries

### What Briefing does not do
- deep build work
- full architecture design
- detailed adversarial pressure testing

### Typical failure mode
Using Briefing too early when the underlying work is still weak.
Result: compact summary of unclear thinking.

---

## Cross-mode rule

Do not treat modes as aesthetic flavors.
Treat them as different operational forms.

A good routing question is:

- Do I need structure? → Architect
- Do I need a deliverable? → Build
- Do I need diagnosis? → Audit
- Do I need pressure-testing? → Red Team
- Do I need compression for decisionability? → Briefing

---

## Compact formula

**Architect builds the logic.**
**Build produces the artifact.**
**Audit checks the quality.**
**Red Team tests the breakpoints.**
**Briefing compresses the signal.**
