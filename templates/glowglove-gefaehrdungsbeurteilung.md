# GlowGlove Gefährdungsbeurteilung Template

Status: DRAFT
Version: v0.1

## Purpose

This template supports a structured risk assessment for the GlowGlove Picking System.

It is designed for concept hardening, MVP review, pilot preparation, and occupational safety discussion.

It is not a legal release, product certification, or approval for operational deployment.

---

## Scope

System under assessment:

```text
GlowGlove Picking System
```

Process idea:

```text
Red glove -> target shown on palm display -> vibration signal -> picker moves to target -> location validated -> glove turns green -> pick action -> confirmation -> event log -> next task
```

Assessment scope:

- picking activity
- wearable glove use
- palm display
- vibration signal
- red / green status logic
- sensor-based validation
- event logging
- fallback process
- worker instruction
- pilot readiness

---

## BGHW / DGUV-Oriented Process Logic

This template follows the general occupational safety logic:

1. Arbeitsbereich und Tätigkeit festlegen
2. Gefährdungen ermitteln
3. Risiken beurteilen
4. Maßnahmen festlegen
5. Maßnahmen umsetzen
6. Wirksamkeit prüfen
7. Gefährdungsbeurteilung fortschreiben

---

## Required Roles

| Role | Responsibility |
|---|---|
| Unternehmer / Arbeitgeber | overall responsibility for occupational safety |
| Führungskraft / Bereichsleitung | implementation and process ownership |
| Fachkraft für Arbeitssicherheit | safety assessment support |
| Betriebsarzt / Betriebsärztin | health and ergonomic assessment support where required |
| Datenschutz / Betriebsrat if applicable | review of worker data and monitoring boundaries |
| IT / WMS owner | technical integration and system reliability |
| Pilot lead | limited pilot setup, documentation, and feedback loop |
| Beschäftigte / Kommissionierer | practical feedback and safe use after instruction |

---

## Status Values

Use one of these values per line item:

```text
OPEN
IN REVIEW
MEASURE DEFINED
IMPLEMENTED
EFFECTIVE
NOT EFFECTIVE
ESCALATED
BLOCKED
```

---

## Risk Rating

Use a simple 1-5 scale.

| Score | Severity | Probability |
|---:|---|---|
| 1 | negligible | very unlikely |
| 2 | minor | unlikely |
| 3 | moderate | possible |
| 4 | serious | likely |
| 5 | severe | very likely |

Risk priority:

```text
Risk Priority = Severity x Probability
```

| Risk Priority | Rating | Action |
|---:|---|---|
| 1-5 | Low | monitor |
| 6-10 | Medium | define measure |
| 11-15 | High | implement before pilot |
| 16-25 | Critical | block until reduced |

---

## Core Assessment Table

| Tätigkeit | Gefährdung | Ursache | Risiko | Maßnahme | Verantwortung | Prüfung | Status |
|---|---|---|---|---|---|---|---|
| Kommissionierer erhält Pickauftrag über Handschuh | Ablenkung durch Display | Blick in Handfläche während Bewegung | Stolpern, Kollision, unaufmerksames Verhalten | Display nur mit Kurzinfo; keine langen Texte; Lesen nur im sicheren Stand; Unterweisung | Bereichsleitung + FASI | Beobachtung im Testlauf; Nutzerfeedback; Beinaheereignisse prüfen | OPEN |
| Kommissionierer bewegt sich zum Zielplatz | Fehlleitung durch falsche Anzeige | falsche Taskdaten, Verbindungsfehler, Softwarefehler | falscher Gang, Zeitverlust, Prozessfehler | WMS-Datenvalidierung; Fallback auf Scanner; Unsicherheit = Rot | IT / WMS Owner | Test mit falschen Daten; Fail-Safe-Prüfung | OPEN |
| Standort wird validiert | Handschuh wird fälschlich grün | Sensor erkennt falschen Ort als korrekt | Fehlpick, Qualitätsrisiko, Kundenfehler | Zwei-Faktor-Validierung für Pilot: Standortcode + Taskabgleich; Grün nur bei eindeutiger Validierung | IT + Pilot Lead | Negativtest: falscher Platz darf nicht grün werden | OPEN |
| Kommissionierer pickt Ware | Griff-/Bewegungseinschränkung | Handschuh zu schwer, steif oder rutschig | Fehlgriff, Überlastung, Produktbeschädigung | Ergonomietest; Größenkonzept; rutschhemmendes Material; keine Einschränkung der Schutzfunktion | FASI + Betriebsarzt + Bereichsleitung | Praxistest mit typischen Pickbewegungen | OPEN |
| Nutzung in Kälte-/Frischebereich | Material-/Akkuversagen | Temperatur, Feuchtigkeit, Kondensation | Ausfall, Fehlfunktion, Haut-/Komfortrisiko | Temperaturfreigabe definieren; Akkuprüfung; Feuchtigkeitsschutz; Ersatzgerät | IT + Arbeitsschutz | Kälte-/Feuchtigkeitstest; Geräteinspektion | OPEN |
| Vibration signalisiert Aktion | Schreckreaktion oder Fehlinterpretation | zu starke Vibration, unklare Muster | Fehlbewegung, Ablenkung, Stress | klare Vibrationsmuster; begrenzte Intensität; Unterweisung; Test mit Beschäftigten | Pilot Lead + FASI | Nutzerfeedback; Fehlinterpretationen protokollieren | OPEN |
| Handschuh leuchtet rot/grün | Verwechslung der Signale | Farben nicht sichtbar, Farbsehschwäche, Lichtverhältnisse | falsche Handlung trotz Signal | Farbe plus Text/Icon; keine reine Farblogik; Kontrasttest | UX / Pilot Lead | Test bei Lichtbedingungen und mit Nutzergruppen | OPEN |
| Elektronischer Handschuh wird geladen | Brand-/Akkurisiko | beschädigter Akku, falsches Ladegerät, Feuchtigkeit | Brand, Hitze, Gerätedefekt | geprüfte Ladegeräte; Ladeplatzregel; Defektquarantäne; Sichtprüfung vor Nutzung | IT / Technik + Bereichsleitung | Ladeprotokoll; Sichtprüfung; Defektliste | OPEN |
| Handschuh fällt während Auftrag aus | Prozessunterbrechung | Akku leer, Verbindung weg, Display defekt | Unsicherheit, Fehlpick, Zeitverlust | Fail-Safe: Rot/Stop; Fallback auf bestehenden Prozess; Ersatzgerät | Bereichsleitung + IT | Ausfallsimulation; Fallback-Test | OPEN |
| Event-Log erfasst Pickdaten | Datenschutz-/Monitoringrisiko | personenbezogene Leistungsdaten | Misstrauen, rechtliches Risiko, Zweckentfremdung | Datenminimierung; Zweckbindung; Rollenrechte; Löschfristen; Betriebsrat/DSB prüfen | Datenschutz + Bereichsleitung | Datenschutzprüfung; Zugriffskontrolle testen | OPEN |
| Beschäftigte verwenden neues System | Fehlbedienung | unzureichende Unterweisung | Fehlpick, unsichere Nutzung, Frustration | dokumentierte Unterweisung; Kurzkarte; Einweisung vor Pilot; Feedbackschleife | Bereichsleitung | Unterweisungsnachweis; praktische Verständnisprüfung | OPEN |
| Pilotbetrieb mit realen Waren | Unklare Verantwortlichkeit | System gibt Signal, Mensch handelt, Prozess haftet unklar | Verantwortungsdiffusion | Rollen klären: Mensch bleibt verantwortlich; System assistiert; manuelle Eskalation möglich | Arbeitgeber + Bereichsleitung | Pilotfreigabe dokumentieren | OPEN |

---

## TOP Measure Hierarchy

When defining measures, use the TOP logic:

```text
T = Technical measures
O = Organizational measures
P = Personal measures
```

Priority:

1. Avoid or remove the hazard where possible.
2. Reduce the hazard technically.
3. Reduce the hazard organizationally.
4. Use personal measures such as instruction or PPE only as the final layer.

---

## Minimum Pilot Gate

A real warehouse pilot must not start until the following items are at least `MEASURE DEFINED` and safety-critical items are `IMPLEMENTED`:

| Gate | Required Status |
|---|---|
| Gefährdungsbeurteilung documented | MEASURE DEFINED |
| Fail-safe red-state logic tested | IMPLEMENTED |
| Wrong-location green signal blocked | IMPLEMENTED |
| Fallback process documented | IMPLEMENTED |
| Worker instruction prepared | IMPLEMENTED |
| Electrical / battery risk assessed | IN REVIEW or better |
| Ergonomic test completed | IN REVIEW or better |
| Data protection boundary defined | IN REVIEW or better |
| Pilot scope limited and documented | IMPLEMENTED |

---

## Effectiveness Check

After each measure, document:

```text
Measure implemented on:
Checked by:
Check method:
Result:
New hazards created? yes/no
Residual risk:
Next review date:
```

---

## Fortschreibung / Review Triggers

Repeat or update the assessment when:

- hardware design changes
- sensor logic changes
- WMS integration changes
- battery or charging process changes
- workplace layout changes
- incident or near miss occurs
- workers report usability or safety problems
- pilot scope expands
- new legal or DGUV/BGHW information becomes relevant
- at least annually during active use or pilot preparation

---

## Deployment Decision

| Deployment Stage | Decision |
|---|---|
| Software simulation | GO |
| Tabletop process test | GO |
| Non-operational wearable demo | CONDITIONAL GO |
| Real picking pilot | HOLD until pilot gate passed |
| Operational rollout | BLOCKED until full validation |

---

## Governance Warning

This template supports structured occupational safety preparation.
It does not replace the employer's legal responsibility, a formal Gefährdungsbeurteilung, expert review by a Fachkraft für Arbeitssicherheit, Betriebsarzt/Betriebsärztin where required, data protection review, or operational approval.

---

## Reuse Note

This template can be reused for:

- GlowGlove pilot preparation
- wearable warehouse technology assessment
- pick-by-light / pick-by-wearable concepts
- logistics innovation safety review
- human-machine-interface risk assessment
- governance documentation for MVP-to-pilot transition
