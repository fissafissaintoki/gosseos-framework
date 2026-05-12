# GlowGlove Worker Instruction Template

Status: DRAFT
Version: v0.1

## Purpose

This template supports worker instruction for the GlowGlove Picking System.

It is intended for pilot preparation, safety briefing, user onboarding, and documented instruction before any practical test with workers.

It does not replace the employer's legal responsibility, the formal risk assessment, occupational safety review, data protection review, or operational approval.

---

## Scope

System:

```text
GlowGlove Picking System
```

Instruction applies to:

- pickers / Kommissionierer
- pilot participants
- supervisors
- trainers
- support staff handling charging, inspection, or defect reporting

Process covered:

```text
Task received -> signal interpreted -> location approached -> location validated -> pick released -> pick confirmed -> event logged -> next task
```

---

## Instruction Metadata

| Field | Entry |
|---|---|
| Company / Site |  |
| Department / Area |  |
| Instructor |  |
| Date |  |
| Version of Instruction | v0.1 |
| Related Risk Assessment | templates/glowglove-gefaehrdungsbeurteilung.md |
| Pilot / Test Scope |  |
| Participants |  |

---

## 1. System Purpose

The GlowGlove supports picking work by showing task information directly on the glove.

It can provide:

- target location on the palm display
- quantity and article information
- vibration signals
- red / green status signals
- error or correction messages
- pick confirmation status

Important:

```text
The glove supports the picker.
It does not replace attention, responsibility, safe movement, or manual checking.
```

---

## 2. Signalbedeutung

| Signal | Meaning | Required Worker Action |
|---|---|---|
| Red | Do not pick / action not released / waiting / error / unsafe state | Stop pick action, check display, follow fallback if unclear |
| Green | Correct location validated / pick action released | Pick only the displayed article and quantity |
| Flashing red | Error / wrong location / blocked task | Do not pick, check message, escalate if unresolved |
| Flashing green | Pick step confirmed or completed | Continue to next instruction |
| Short vibration | New task or attention signal | Look at display only when safe to do so |
| Repeated vibration | Warning, correction, or unresolved issue | Stop, check display, escalate if needed |
| No signal / black display | Device failure or inactive state | Stop using glove and switch to fallback process |

Core rule:

```text
No clear green validation = no pick.
```

Fail-safe rule:

```text
Unclear signal = treat as red.
```

---

## 3. Display Content

The palm display may show:

```text
Location
Quantity
Article code
Status
Error message
Next action
```

Worker rules:

- Do not read long text while walking.
- Stop safely before reading the display.
- Do not rely only on color if the text indicates an error.
- If display and physical location do not match, do not pick.
- If article, quantity, or location appears wrong, escalate.

---

## 4. Fehlerverhalten

### Wrong Location

If the glove shows wrong location, flashing red, or error:

```text
1. Do not pick.
2. Check displayed target location.
3. Compare with physical location label.
4. Retry validation if instructed.
5. If still wrong, use fallback process and inform supervisor.
```

### Wrong Article or Quantity

If the displayed article or quantity does not match the physical item:

```text
1. Do not pick.
2. Keep glove state red / blocked.
3. Check article label and quantity.
4. Report mismatch.
5. Follow supervisor instruction or fallback process.
```

### Device Failure

If display, vibration, sensor, connection, or battery fails:

```text
1. Stop using the glove for active picking.
2. Do not continue based on memory.
3. Switch to approved fallback process.
4. Report defect.
5. Mark device as defective if required.
```

### Unsafe Situation

If the signal distracts, startles, or creates unsafe movement:

```text
1. Stop work safely.
2. Move out of traffic or hazard zone if needed.
3. Inform supervisor.
4. Do not continue until the situation is clarified.
```

---

## 5. Fallback-Prozess

The fallback process must be defined before pilot or use.

Minimum fallback:

```text
If the glove is unclear, unavailable, defective, or unsafe, the picker returns to the approved standard picking process.
```

Fallback options:

- handheld scanner
- paper list
- terminal confirmation
- supervisor-directed picking
- manual WMS confirmation
- task reassignment

Fallback rule:

```text
The fallback process has priority over uncertain glove signals.
```

Required local definition:

| Situation | Fallback Action | Responsible Person |
|---|---|---|
| Device battery low |  |  |
| Display not readable |  |  |
| Wrong location signal |  |  |
| Sensor does not validate |  |  |
| Worker feels unsafe |  |  |
| WMS mismatch |  |  |

---

## 6. Sichtprüfung vor Nutzung

Before each shift or pilot test, the worker or responsible person checks:

| Check | OK | Not OK | Action if Not OK |
|---|---|---|---|
| Glove visibly undamaged |  |  | remove from use |
| Display readable |  |  | report defect |
| LEDs / red-green signal visible |  |  | report defect |
| Vibration works |  |  | report defect |
| Battery sufficient |  |  | charge / replace |
| No heat, swelling, smell, or battery damage |  |  | quarantine device |
| Fit and grip acceptable |  |  | use correct size or stop test |
| No hygiene issue |  |  | clean / replace |
| Sensor or scan function works |  |  | fallback / report |

Rule:

```text
A defective or questionable glove must not be used.
```

---

## 7. Laden / Defektmeldung

### Charging Rules

- Use only approved charging equipment.
- Charge only at defined charging locations.
- Do not charge wet, damaged, overheated, or visibly defective gloves.
- Do not cover devices during charging.
- Do not use private chargers or improvised adapters.
- Report unusual heat, smell, swelling, sparks, or display defects immediately.

### Defect Reporting

If a defect is suspected:

```text
1. Stop using the glove.
2. Mark device as defective.
3. Remove it from operational use.
4. Inform supervisor or technical contact.
5. Document defect in device log.
```

Defect log fields:

| Field | Entry |
|---|---|
| Date / Time |  |
| Device ID |  |
| Worker / Reporter |  |
| Defect Type |  |
| Situation |  |
| Immediate Action |  |
| Responsible Follow-Up |  |
| Status |  |

---

## 8. Datenschutzhinweis

The GlowGlove may create event data, such as:

- task time
- location validation
- pick confirmation
- error events
- device status
- exception logs

Worker information:

```text
Event data must be used only for the defined operational and safety purpose.
It must not be misused for hidden personal surveillance or uncontrolled performance monitoring.
```

Minimum data protection boundaries:

- purpose must be explained before use
- only necessary data should be collected
- access must be limited
- retention period must be defined
- workers must know what is logged
- personal evaluation use must be reviewed separately
- data protection officer / works council review may be required

Local clarification:

| Question | Answer |
|---|---|
| What data is logged? |  |
| Why is it logged? |  |
| Who can access it? |  |
| How long is it stored? |  |
| Is personal performance evaluation excluded? |  |
| Has data protection / works council review occurred? |  |

---

## 9. Worker Responsibilities

The worker must:

- follow red / green signal logic
- stop if the signal is unclear
- not pick without clear validation
- use fallback process when required
- report defects immediately
- avoid unsafe reading while walking
- report discomfort, distraction, or usability issues
- follow charging and storage rules
- participate in feedback during pilot testing

---

## 10. Supervisor Responsibilities

The supervisor or pilot lead must:

- ensure instruction before use
- define fallback process
- ensure device inspection logic
- document participants
- collect feedback and incidents
- stop pilot if safety concerns appear
- ensure no operational pressure overrides safety rules
- coordinate with occupational safety, IT, data protection, and workers

---

## 11. Stop Criteria

The pilot or use must be stopped if:

- glove gives wrong green validation
- workers report unsafe distraction
- device overheats or battery damage appears
- repeated sensor errors occur
- fallback process is unclear
- data protection scope is unclear
- incidents or near misses occur
- workers cannot reliably interpret signals

Stop rule:

```text
Safety overrides productivity.
```

---

## 12. Confirmation of Instruction

By signing, the participant confirms that the following points were explained:

| Topic | Confirmed |
|---|---|
| System purpose |  |
| Red / green signal meaning |  |
| Vibration signal meaning |  |
| Display content and safe reading behavior |  |
| No clear green = no pick |  |
| Error behavior |  |
| Fallback process |  |
| Sichtprüfung before use |  |
| Charging rules |  |
| Defect reporting |  |
| Data protection information |  |
| Stop criteria |  |
| Contact person for questions/problems |  |

Participant confirmation:

| Name | Date | Signature |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |

Instructor confirmation:

| Instructor | Date | Signature |
|---|---|---|
|  |  |  |

---

## 13. Open Questions Before Pilot

| Question | Status | Owner |
|---|---|---|
| Is the glove PPE or only an assistive wearable? | OPEN |  |
| Is the fallback process approved? | OPEN |  |
| Has electrical / battery safety been reviewed? | OPEN |  |
| Has ergonomic testing been performed? | OPEN |  |
| Has data protection been reviewed? | OPEN |  |
| Has the risk assessment been completed? | OPEN |  |
| Is the pilot scope clearly limited? | OPEN |  |

---

## Governance Warning

This instruction template supports preparation and documentation.
It does not replace the formal Gefährdungsbeurteilung, legal obligations, occupational safety review, data protection review, worker participation requirements, or operational release.

---

## Reuse Note

This template can be reused for:

- GlowGlove pilot instruction
- wearable warehouse device onboarding
- pick-by-light worker briefing
- assistive technology pilot documentation
- safety-oriented MVP-to-pilot transition
