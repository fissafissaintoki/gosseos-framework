# OF-AGENTIC-CREATIVE-LAB — Case 002

## Case-Name

**CASE-002: Recruiting-Agent Workflow / Candidate Funnel Operator**

## Status

**WORKING → Proof-of-Work-Kandidat**

## Zugeordnetes Projekt

**OF-AGENTIC-CREATIVE-LAB-v1**

## Kategorie

GosseOS / KnowledgeOS / Agentic Recruiting / HR / Candidate Funnel / Governance / Proof-of-Work

---

## 1. Ausgangslage

Aus Case 001 wurde abgeleitet: Wenn Agenten Business-Systeme wie Ads-Konten analysieren können, betrifft das nicht nur Performance Marketing, sondern auch Recruiting.

Recruiting-Kampagnen bestehen ebenfalls aus:

- Zielgruppe
- Angebot / Stelle
- Creative / Anzeige
- Landingpage / Bewerbungsstrecke
- Funnel-Daten
- Bewerberqualität
- Kommunikationsgeschwindigkeit
- menschlicher Freigabe
- Datenschutz und Fairness

Der nächste sinnvolle Proof-of-Work ist daher ein kontrollierter Recruiting-Agent-Workflow.

---

## 2. Rohinput

Ausgangspunkt:

> Wir wollen KI-Agenten nutzen, um Recruiting-Kampagnen, Bewerberansprache oder Stellenanzeigen besser zu analysieren und daraus bessere Creatives, Texte, Funnel-Hypothesen und Handlungsempfehlungen abzuleiten — ohne Bewerberdaten unkontrolliert zu verarbeiten oder Entscheidungen automatisiert zu treffen.

---

## 3. Erkannte Problemklasse

Primär:

```text
Agentic Recruiting Workflow
```

Sekundär:

```text
Candidate Funnel Analyse
Recruiting Creative Optimierung
HR-Governance
Human-Approval-Loop
Datenschutz / Fairness / Bias-Risiko
```

---

## 4. Kernproblem

Nicht die Frage „Kann KI Bewerbungen vorsortieren?“ ist der richtige Startpunkt.

Der richtige Startpunkt ist:

```text
Wie kann ein Agent Recruiting-Kampagnen und Bewerberkommunikation unterstützen, ohne menschliche Entscheidung, Fairness, Datenschutz und Verantwortung zu ersetzen?
```

---

## 5. Operator-Fischer-Übersetzung

```text
Recruiting-Rohproblem
→ Zielrolle klären
→ Candidate Funnel analysieren
→ Engpass bestimmen
→ Hypothesen bilden
→ Stellen-/Creative-Varianten erstellen
→ Governance prüfen
→ menschliche Freigabe halten
→ Testplan aufsetzen
→ Ergebnis dokumentieren
```

---

## 6. Agentic Recruiting Workflow

```text
Recruitingziel
→ Rolle / Zielgruppe definieren
→ Datenrahmen begrenzen
→ Funnel analysieren
→ Engpass erkennen
→ Hypothesen bilden
→ Stellen-/Creative-Brief erstellen
→ Governance-Check
→ menschliche Freigabe
→ Test
→ Auswertung
→ Iteration
```

---

## 7. Zugriffsstufen-Modell

### Stufe 1 — READ ONLY

Agent darf:

- Stellenanzeige analysieren
- Kampagnenmetriken lesen
- Funnel-Schritte auswerten
- Bewerberkommunikation als Muster analysieren, sofern anonymisiert
- Engpässe benennen

Agent darf nicht:

- Bewerber ablehnen
- Bewerber bewerten
- persönliche Profile erstellen
- Nachrichten automatisch versenden
- Interviewentscheidungen treffen

### Stufe 2 — DRAFT

Agent darf:

- Stellenanzeigen-Varianten entwerfen
- Creative-Ideen erzeugen
- Interviewfragen vorbereiten
- Antwortvorlagen formulieren
- Funnel-Hypothesen bilden

### Stufe 3 — PREPARE

Agent darf:

- Kampagnenentwürfe vorbereiten
- Scorecard-Vorlagen erstellen
- Kommunikationsentwürfe vorbereiten
- Checklisten für Recruiter bauen

Aber:

- keine automatische Entscheidung
- keine unreviewten Nachrichten
- keine Profiling-Entscheidung

### Stufe 4 — EXECUTE WITH APPROVAL

Agent darf erst nach menschlicher Freigabe:

- vorbereitete Texte verwenden
- Kampagnenvarianten aktivieren
- Follow-up-Entwürfe senden lassen

### Stufe 5 — AUTONOMOUS

Für Recruiting grundsätzlich nur sehr begrenzt geeignet.

Erlaubt höchstens für:

- Terminoptionen vorschlagen
- Erinnerungstexte vorbereiten
- interne Aufgabenlisten aktualisieren

Nicht geeignet für:

- Auswahlentscheidungen
- Ablehnungen
- Eignungsbewertungen
- sensible Kandidatenprofile

**Standardregel:**

```text
Recruiting-Agenten starten immer mit READ ONLY oder DRAFT.
Menschliche Entscheidung bleibt zwingend.
```

---

## 8. Candidate Funnel Diagnose

Zu prüfen:

```text
1. Sichtbarkeit
Wird die Stelle von der richtigen Zielgruppe gesehen?

2. Hook
Spricht die Anzeige das echte Motiv der Zielgruppe an?

3. Angebot
Ist klar, warum jemand wechseln oder sich bewerben soll?

4. Reibung
Ist die Bewerbung zu kompliziert?

5. Qualität
Kommen passende Bewerbungen oder nur viele irrelevante?

6. Kommunikation
Reagiert das Unternehmen schnell und klar?

7. Vertrauen
Wirkt die Stelle realistisch, seriös und konkret?
```

---

## 9. Prompt-Artefakt

```text
AGENTIC RECRUITING OPERATOR — CASE 002 PROMPT

Du arbeitest als kontrollierter Agentic Recruiting Operator, Candidate Funnel Analyst und HR-Governance-Prüfer.

Ziel:
Analysiere eine Recruiting-Kampagne, Stellenanzeige oder Bewerberkommunikation, ohne Bewerberentscheidungen zu automatisieren.

Arbeite in dieser Reihenfolge:

1. Recruitingziel klären
- Welche Rolle soll besetzt werden?
- Welche Zielgruppe wird gesucht?
- Welche Region / Arbeitsform / Qualifikation ist relevant?
- Was ist das zentrale Einstellungsproblem?
- Zu wenig Bewerbungen?
- Falsche Bewerbungen?
- Schlechte Conversion?
- Lange Reaktionszeiten?

2. Zugriffsstufe setzen
Beginne standardmäßig mit READ ONLY.
Du darfst analysieren, berichten und Vorschläge machen.
Du darfst keine Bewerber ablehnen, bewerten oder automatisch kontaktieren.

3. Datenrahmen definieren
Analysiere nur freigegebene und möglichst anonymisierte Daten:
- Stellenanzeige
- Kampagnenmetriken
- Funnel-Daten
- anonymisierte Bewerberfragen
- Kommunikationsvorlagen
- Landingpage / Bewerbungsformular

4. Funnel analysieren
Prüfe:
- Reichweite
- Klickrate
- Bewerbungsrate
- Abbruchstellen
- Bewerberqualität
- Antwortgeschwindigkeit
- Stellenklarheit
- Zielgruppen-Fit

5. Engpass bestimmen
Ordne den Hauptengpass ein:
- Anzeige wird nicht gesehen
- Anzeige wird gesehen, aber nicht geklickt
- Anzeige wird geklickt, aber nicht beworben
- Bewerbungen passen nicht
- Bewerbungsprozess ist zu lang
- Kommunikation ist zu langsam
- Angebot ist unklar

6. Hypothesen bilden
Erstelle 3–5 Hypothesen:
- Beobachtung
- mögliche Ursache
- Risiko
- Testidee
- erwarteter Effekt

7. Recruiting-Creative-Brief erstellen
Erzeuge 3 neue Ansätze:

Für jeden Ansatz:
- Hook
- Zielgruppe
- Kernbotschaft
- Nutzenversprechen
- Realitätscheck
- CTA
- Bild-/Videoidee
- Stellenanzeigen-Textbaustein
- Risiko

8. Governance-Check
Prüfe:
- personenbezogene Daten
- Bewerberdaten
- Diskriminierungsrisiko
- unzulässiges Profiling
- falsche Versprechen
- Gehalts-/Benefits-Übertreibung
- Bias in Sprache oder Zielgruppe
- menschliche Freigabe

9. Testplan erstellen
Gib aus:
- Was wird getestet?
- Zielgruppe
- Variante A/B
- Zeitraum
- Budgetrahmen
- Entscheidungsmetrik
- Stop-Regel
- Freigabe-Regel

Output:
1. Recruitingziel
2. Zugriffsstufe
3. Funnel-Diagnose
4. Hauptengpass
5. Hypothesen
6. Creative-/Stellenanzeigen-Briefs
7. Governance-Check
8. Testplan
9. Freigabe-Checkliste
10. nächster Schritt

Grundsatz:
Der Agent analysiert und bereitet vor.
Der Mensch entscheidet und verantwortet.
Keine automatisierten Bewerberentscheidungen.
```

---

## 10. Governance-Gate

Vor jeder Recruiting-Agent-Nutzung prüfen:

```text
1. Werden personenbezogene Bewerberdaten verarbeitet?
2. Sind die Daten anonymisiert oder minimiert?
3. Wird eine Eignungsentscheidung automatisiert?
4. Gibt es Diskriminierungs- oder Bias-Risiken?
5. Sind Sprache und Zielgruppenansprache fair?
6. Werden falsche Versprechen gemacht?
7. Ist menschliche Freigabe zwingend vorgesehen?
8. Wird dokumentiert, was der Agent vorgeschlagen hat?
9. Gibt es eine klare Stop-Regel?
10. Ist klar, wer verantwortlich entscheidet?
```

**Harte Sperre:**

```text
Agent darf keine Bewerber automatisiert ablehnen, ranken oder final bewerten.
```

---

## 11. Nutzen

Dieser Case zeigt:

- Agentic Marketing lässt sich auf Recruiting übertragen.
- Recruiting-Agenten brauchen deutlich strengere Governance als reine Creative-Agenten.
- Der Operator-Fischer-Ansatz schützt vor blindem Automatisieren von HR-Entscheidungen.
- Der Case liefert Workflow, Prompt, Zugriffsstufenmodell, Funnel-Diagnose und Governance-Gate.

---

## 12. Marketing-Output

### Kurzpost

```text
Case 002 im Agentic Creative Lab:
Recruiting-Agent Workflow.

Viele denken bei KI im Recruiting sofort an Bewerberbewertung.
Genau das ist der falsche Startpunkt.

Der bessere Einstieg:
KI-Agenten analysieren den Recruiting-Funnel, Stellenanzeigen, Creatives und Kommunikationsstrecken — aber sie entscheiden nicht über Menschen.

Agent darf:
- Engpässe erkennen
- Hypothesen bilden
- Stellenanzeigen verbessern
- Creative-Ideen entwickeln
- Antwortentwürfe vorbereiten
- Testpläne erstellen

Agent darf nicht:
- Bewerber automatisch ablehnen
- Menschen ranken
- sensible Profile bauen
- Entscheidungen ersetzen

Die neue Kompetenz ist nicht:
„KI sortiert Bewerber.“

Sondern:
Recruitingziele klar setzen, Daten begrenzen, Fairness prüfen, bessere Ansprache bauen und menschliche Entscheidung halten.

Leitsatz:
Der Agent analysiert und bereitet vor.
Der Mensch entscheidet und verantwortet.
```

### CTA

```text
Kommentiere OPERATOR und ich übersetze deinen Recruiting-Use-Case in einen kontrollierten Agenten-Workflow.
```

---

## 13. Nächster Schritt

Case 002 öffentlich als Proof-of-Work nutzen:

```text
Recruiting-Rohproblem
→ Funnel-Diagnose
→ Agentic Recruiting Prompt
→ HR-Governance-Gate
→ Community-CTA
```

Danach Case 003 bauen:

```text
Business-Post → Creative-Brief-Agent
```

oder

```text
Gemini Workspace → Mail-to-Artefact Recruiting Workflow
```

---

## 14. Owner-Prinzip

```text
Der Agent analysiert und bereitet vor.
Der Mensch entscheidet und verantwortet.
Keine automatisierten Bewerberentscheidungen.
```
