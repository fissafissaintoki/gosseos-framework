# GosseOS Tools

This folder contains minimal executable components of the GosseOS system.

The goal is not to simulate a full AI stack.
The goal is to prove the operating logic.

---

## gosseos_router.py

### Purpose

Classify raw input into:
- problem class
- working mode
- artifact type
- governance signal

---

## How to run

```bash
python gosseos_router.py "I have problems in my cold chain logistics"
```

Or interactive:

```bash
python gosseos_router.py
```

---

## Example Output

Input:

> I need to audit my logistics process

Output:

- Problem Class: Operational Logistics Process
- Primary Mode: AUDIT
- Secondary Mode: BUILD
- Artifact Type: Process Audit or Risk Matrix
- Governance Signal: APPROVED WITH WARNING

---

## Why this exists

Most AI usage is:

prompt → answer

GosseOS introduces:

input → classification → mode → artifact → governance

This tool demonstrates the classification step.

---

## Next Step

Combine router output with:

- templates (MODE_ROUTING_MATRIX)
- governance gate
- case structures

---

## Limitation

This is rule-based.

It is not meant to be "smart".
It is meant to make the logic visible and testable.
