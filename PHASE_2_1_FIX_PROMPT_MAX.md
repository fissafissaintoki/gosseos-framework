# PHASE 2.1 FIX PROMPT – OPTIMIZED MAX

```text
Du arbeitest als Senior Python Backend Engineer und Consistency-Fix Implementer.

Kontext:
Phase 2 für GosseOS Workbench v1 wurde bereits entworfen.
Der Scope ist im Kern richtig, aber es gibt einige technische Bruchstellen, die vor Phase 3 korrigiert werden müssen.

WICHTIG:
- Kein Neubau
- Keine Scope-Ausweitung
- Keine zusätzlichen Features
- Keine API-Router
- Kein Frontend
- Keine Registry-Logik
- Keine Integrity-Service-Logik
- Keine neue Architektur
- Nur gezielte Korrekturen an vorhandenen Phase-2-Dateien

ZU KORRIGIEREN

1. prompt_composer.py
- Der Rückgabetyp muss korrekt sein.
- `compose_prompt()` gibt aktuell faktisch `(messages, system_content)` zurück.
- Die Typannotation und Signatur müssen dazu passen.
- Kein irreführender Rückgabetyp.

2. prompt_composer.py
- Die Modus-Extraktion muss robust werden.
- Aktuell wird vermutlich nach `## Architect` gesucht.
- Das muss mit realistischen Header-Varianten funktionieren, insbesondere wenn MODE_SPECIFICATIONS.md eher wie `## 1. ARCHITECT` oder ähnliche Varianten strukturiert ist.
- Ziel: relevanten Modus sauber extrahieren, Prompt-Inflation vermeiden.
- Fallback auf Volltext bleibt erlaubt, aber nur wenn Extraktion wirklich scheitert.

3. router.py
- Claude-Fallback architektonisch sauberer anbinden.
- Vermeide doppelte Claude-API-Logik im Router.
- Der Router soll nicht eigenständig eine zweite vollwertige Claude-Integrationswelt aufmachen.
- Nutze einen kleinen, klar abgegrenzten Klassifikations-Helper oder eine zentrale Claude-Funktion.
- Halte es V1-kompatibel und minimal.

4. claude_service.py
- Parse-Fail-Semantik klarziehen.
- Wenn Parse fehlschlägt, muss deutlich sein:
  - `output_payload = None`
  - `generated_json_text` ist dann ein technisches Fallback-Envelope und nicht das originale Modell-JSON
- Kommentiere und benenne das sauber.
- Kein stilles Verwischen zwischen Originalantwort und Fallback-Struktur.

5. claude_service.py
- Modellname als Konstante auslagern.
- Kein harter Modellstring mitten im Call.
- V1 darf weiterhin einen festen Modellnamen nutzen, aber sauber als Konstante.

6. db.py
- Entferne ungenutzte Imports, insbesondere `UniqueConstraint`, falls weiterhin ungenutzt.
- Prüfe außerdem `DateTime(timezone=True)` für die UTC-aware Timestamps.
- Wenn du es änderst, dann konsistent und ohne Seiteneffekte.

DATEIEN, DIE DU JETZT ÜBERARBEITEN SOLLST
1. backend/app/services/prompt_composer.py
2. backend/app/services/router.py
3. backend/app/services/claude_service.py
4. backend/app/models/db.py

NUR FALLS ZWINGEND NOTWENDIG UND KLAR BEGRÜNDET:
5. backend/app/utils/module_loader.py

OUTPUT-FORMAT

A. Scope-Bestätigung
- max. 10 Zeilen
- was wird korrigiert
- was bleibt bewusst unberührt

B. Korrekturprinzipien
- max. 10 Zeilen
- welche Architekturregeln jetzt stabilisiert werden

C. Für jede geänderte Datei:
- Dateipfad als Überschrift
- 1–3 Sätze, was korrigiert wurde
- vollständiger finaler Codeblock

D. Am Ende:
- Liste der exakt behobenen Probleme
- Liste verbleibender akzeptierter V1-Risiken
- klare Aussage: Phase 3 freigegeben oder nicht

QUALITÄTSREGELN
- so wenig Änderung wie möglich, so viel wie nötig
- keine Fantasie-Verbesserungen
- keine neuen Features
- keine unnötigen Bibliotheken
- keine unnötige Abstraktion
- alle bestehenden Namen und Verträge respektieren, außer dort, wo die Korrektur genau das verlangt

WICHTIGE FACHREGEL
Die Output-Trennung bleibt strikt:
- DB/Modell-Seite: `generated_json_text`
- Schema/API-Seite: `output_payload`

Das darf an keiner Stelle verwischt werden.

STARTE JETZT MIT:
A. Scope-Bestätigung
B. Korrekturprinzipien
C. Danach direkt die korrigierten Dateien
```