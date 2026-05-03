# Start GosseOS in 2 Minutes

## What this is

GosseOS is a structured AI workflow system.

It turns messy input into controlled work:

```text
raw input -> problem class -> mode -> artifact -> governance -> reusable knowledge
```

---

## 1. Clone the repository

```bash
cd ~/Desktop
git clone https://github.com/fissafissaintoki/gosseos-framework.git
cd gosseos-framework
```

---

## 2. Run the router

```bash
python3 tools/gosseos_router.py "I have problems in my cold chain logistics"
```

Expected result:

```text
Problem Class: Operational Logistics Process
Primary Mode: AUDIT
Secondary Mode: BUILD
Artifact Type: Process Audit, Risk Matrix, or Decision Framework
Governance Signal: APPROVED WITH WARNING
```

---

## 3. Read the matching workflow

Open:

```text
RUN_GOSSEOS_WORKFLOW.md
```

Follow the chain:

```text
Input -> Router -> Mode -> Template -> Case -> Governance -> KnowledgeOS Extract
```

---

## 4. Use a template

Start with:

```text
templates/MODE_ROUTING_MATRIX.md
templates/GOVERNANCE_GATE.md
```

These files tell you:

- which mode to use
- which artifact to build
- how to check risk and assumptions

---

## 5. Study the proof cases

Open:

```text
cases/LOGISTICS_COLD_CHAIN_RISK_CASE.md
cases/COLD_CHAIN_REAL_IMPACT.md
```

These show how operational problems become structured artifacts.

---

## 6. Core idea

Do not ask AI for a random answer.

Route the work first.

Then build the artifact.

Then run the governance check.

---

## 7. Minimal Example

Raw input:

```text
Our warehouse process is unstable and we need a structured improvement plan.
```

GosseOS output target:

```text
Problem Class: Operational Process
Mode: AUDIT + BUILD
Artifact: Process Audit + Control Checklist
Governance: APPROVED WITH WARNING
KnowledgeOS: reusable process improvement pattern
```

---

## One sentence

GosseOS is not about better prompting.

It is about controlled AI work.
