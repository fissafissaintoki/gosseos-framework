# OF-AGENTIC-CREATIVE-LAB — Case 004

## Case-Name

**CASE-004: Gemini Workspace → Mail-to-Artefact Business Workflow**

## Status

**WORKING → Proof-of-Work-Kandidat**

## Zugeordnetes Projekt

**OF-AGENTIC-CREATIVE-LAB-v1**

## Kategorie

GosseOS / KnowledgeOS / Gemini / Google Workspace / Mail-to-Artefact / Governance / Proof-of-Work

---

## 1. Ausgangslage

Viele Business-Inputs entstehen nicht als sauberer Auftrag, sondern als Mail, Mailfolge, Kommentar, Notiz oder Dokumentfragment.

Typisches Problem:

```text
Eine Mail kommt rein.
Sie enthält Aufgaben, Erwartungen, offene Punkte, Fristen, Tonalität und manchmal Konfliktpotenzial.
Der Mensch muss daraus erst verstehen: Was ist wirklich zu tun?
```

Gemini kann im Google-Workspace-Kontext nahe an Gmail, Docs, Sheets und Drive arbeiten. Daraus entsteht ein starker Use Case: Mails nicht nur beantworten, sondern in Arbeitsartefakte übersetzen.

---

## 2. Rohinput

> Eine Mail oder Mailfolge soll nicht nur zusammengefasst werden. Sie soll in ein nutzbares Arbeitsergebnis übersetzt werden: Kernanliegen, Aufgaben, Antwortentwurf, Risiken, nächste Schritte und optional ein Briefing, eine Checkliste oder ein Mini-Projektplan.

---

## 3. Erkannte Problemklasse

Primär:

```text
Workspace-to-Artefact Workflow
```

Sekundär:

```text
Mail-Triage
Business-Kommunikation
Task Extraction
Governance / Datenschutz
Human-Approval-Loop
```

---

## 4. Kernproblem

Nicht jede Mail braucht eine Antwort.

Viele Mails brauchen zuerst eine Struktur:

```text
Was will die Person?
Was ist meine Aufgabe?
Welche Frist gilt?
Was ist riskant?
Was muss geprüft werden?
Welches Artefakt entsteht daraus?
```

---

## 5. Operator-Fischer-Übersetzung

```text
Mail / Mailfolge
→ Kernanliegen erkennen
→ Aufgaben extrahieren
→ Problemklasse bestimmen
→ Antwort oder Artefakt wählen
→ Governance prüfen
→ Entwurf bauen
→ menschliche Freigabe
→ nächster Schritt
```

---

## 6. Agentic Workflow

```text
Mail-Input
→ Kurzfassung
→ Kernanliegen
→ Aufgaben / Fristen
→ Problemklasse
→ Artefaktklasse
→ Antwortentwurf
→ Governance-Check
→ Freigabe
→ Dokumentation / Follow-up
```

---

## 7. Zugriffsstufen-Modell

### Stufe 1 — READ ONLY

Agent darf:

- Mail lesen
- zusammenfassen
- Aufgaben extrahieren
- Risiken markieren
- Antwortoptionen vorschlagen

Agent darf nicht:

- Mails senden
- Zusagen machen
- Termine buchen
- vertrauliche Inhalte weiterleiten

### Stufe 2 — DRAFT

Agent darf:

- Antwortentwürfe schreiben
- To-do-Listen erzeugen
- Briefings bauen
- Rückfragen formulieren

### Stufe 3 — PREPARE

Agent darf:

- Entwürfe in Arbeitsform bringen
- Checklisten vorbereiten
- Follow-up-Struktur erzeugen
- mögliche nächste Schritte vorschlagen

Aber:

- keine automatische Versendung
- keine verbindlichen Zusagen
- keine externen Aktionen ohne Freigabe

### Stufe 4 — EXECUTE WITH APPROVAL

Agent darf nur nach Freigabe:

- finalen Antworttext verwenden
- Aufgaben in Tools übertragen
- Follow-up vorbereiten

### Stufe 5 — AUTONOMOUS

Für Business-Mails nur sehr begrenzt geeignet.

Erlaubt höchstens für:

- interne Markierung
- Entwurfserstellung
- einfache Sortierung

Nicht geeignet für:

- rechtsverbindliche Aussagen
- HR-/Gesundheits-/Finanzthemen
- sensible Kundenkommunikation

**Standardregel:**

```text
Mail-Agenten starten mit READ ONLY oder DRAFT.
Mensch prüft vor Versand.
```

---

## 8. Prompt-Artefakt

```text
GEMINI MAIL-TO-ARTEFACT OPERATOR — CASE 004 PROMPT

Du arbeitest als Workspace-Assistent, Mail-Strukturierer, Business-Kommunikationsberater und Governance-Prüfer.

Ziel:
Analysiere eine Mail oder Mailfolge und übersetze sie in ein konkretes Arbeitsergebnis.

Arbeite in dieser Reihenfolge:

1. Kurzfassung
Fasse die Mail in maximal 5 Sätzen zusammen.

2. Kernanliegen
Bestimme:
- Was will die andere Person?
- Was wird von mir erwartet?
- Gibt es eine Frist?
- Gibt es versteckte Aufgaben?
- Gibt es Konflikt- oder Eskalationspotenzial?

3. Aufgaben extrahieren
Erstelle:
- offene Aufgaben
- Verantwortlichkeiten
- Fristen
- benötigte Informationen
- Rückfragen

4. Problemklasse bestimmen
Ordne ein:
- einfache Antwort
- Terminabstimmung
- Entscheidungsbedarf
- Konflikt / Klärung
- Projektaufgabe
- Dokumentationsbedarf
- Follow-up
- Eskalation

5. Artefakt wählen
Bestimme, was gebraucht wird:
- Antwortmail
- To-do-Liste
- Kurzbriefing
- Rückfragenliste
- Entscheidungsnotiz
- Checkliste
- Mini-Projektplan
- Follow-up-Entwurf

6. Governance-Check
Prüfe:
- personenbezogene Daten
- vertrauliche Inhalte
- Gesundheitsdaten
- HR-Themen
- Finanz-/Rechtsrisiken
- Aussagen, die nicht ungeprüft versendet werden dürfen

7. Antwort oder Artefakt bauen
Erstelle das gewählte Artefakt.

Regeln:
- Keine Mail automatisch versenden.
- Keine Fakten erfinden.
- Keine Zusagen machen, die nicht im Input stehen.
- Sensible Daten minimieren.
- Unsicherheiten markieren.

Output:
1. Kurzfassung
2. Kernanliegen
3. Aufgaben
4. Problemklasse
5. empfohlenes Artefakt
6. gebautes Artefakt
7. Governance-Check
8. Freigabehinweis
9. nächster Schritt

Grundsatz:
Der Agent strukturiert und bereitet vor.
Der Mensch prüft, entscheidet und versendet.
```

---

## 9. Governance-Gate

Vor Nutzung auf Mails prüfen:

```text
1. Enthält die Mail personenbezogene Daten?
2. Enthält sie Gesundheits-, HR-, Finanz- oder Rechtsinformationen?
3. Dürfen Inhalte in einem Cloud-Workspace verarbeitet werden?
4. Muss anonymisiert werden?
5. Enthält der Antwortentwurf Zusagen?
6. Gibt es Fristen oder Haftungsrisiken?
7. Muss eine Fachperson prüfen?
8. Wird nichts automatisch versendet?
9. Sind Annahmen markiert?
10. Ist klar, wer final verantwortlich ist?
```

---

## 10. Nutzen

Dieser Case zeigt:

- Workspace-KI wird nicht nur als Textassistent genutzt, sondern als Arbeitsartefakt-Generator.
- Mails werden von Kommunikation zu steuerbaren Aufgabenpaketen.
- Der Workflow ist direkt alltagstauglich.
- Governance ist zwingend, weil Mails oft personenbezogene und vertrauliche Inhalte enthalten.

---

## 11. Marketing-Output

```text
Case 004 im Agentic Creative Lab:
Gemini Workspace → Mail-to-Artefact Workflow.

Viele nutzen KI in Mails nur für Antwortvorschläge.

Ich sehe den größeren Hebel:
Eine Mail ist oft ein Rohinput.
Darin stecken Aufgaben, Fristen, Erwartungen, Risiken und mögliche Artefakte.

Mein Workflow:
Mail rein → Kernanliegen erkennen → Aufgaben extrahieren → Problemklasse bestimmen → Artefakt bauen → Governance prüfen → Antwortentwurf freigeben.

Nicht:
KI, schreib mal zurück.

Sondern:
KI, zeig mir erst, was hier wirklich zu tun ist.

Der Agent strukturiert und bereitet vor.
Der Mensch prüft, entscheidet und versendet.
```

### CTA

```text
Kommentiere OPERATOR und ich übersetze deinen Mail- oder Workspace-Use-Case in einen kontrollierten Agenten-Workflow.
```

---

## 12. Nächster Schritt

Case 004 praktisch testen:

```text
Gmail-Mailfolge
→ Kurzfassung
→ Aufgaben
→ Antwortentwurf
→ Governance-Check
→ Freigabe
```

---

## 13. Owner-Prinzip

```text
Der Agent strukturiert und bereitet vor.
Der Mensch prüft, entscheidet und versendet.
```
