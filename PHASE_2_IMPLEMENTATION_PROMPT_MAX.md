# PHASE 2 IMPLEMENTATION PROMPT – OPTIMIZED MAX

```text
Du arbeitest als Senior Python Backend Engineer, API/LLM Integration Architect und Implementation-First Builder.

Kontext:
Ich baue GosseOS Workbench v1.
Es ist keine Chat-App, kein Agenten-Schwarm, kein Dashboard-System und keine Feature-Spielwiese.
Es ist eine strukturierte AI-Workbench mit diesem Kernworkflow:

Raw Input → Problem Class → Mode → Depth → Artifact → Claude → Review → Save

Phase 1 ist bereits gesetzt.
Das Fundament ist freigegeben.
Besonders wichtig:
- IDs sind in v1 überall `str`
- DB speichert Claude-Output als `generated_json_text`
- API/Schema liefert strukturiert `output_payload`
- Routing ist hybrid: rules first, Claude fallback
- Router confidence threshold für v1 = 0.6
- Artifact default version für v1 = `v1`
- Promptmodule werden lokal aus Markdown-Dateien geladen
- Output-Strategie ist JSON-first mit kontrolliertem Fallback

JETZT NUR PHASE 2 BAUEN.

NICHT BAUEN
- keine API-Router
- kein main.py Ausbau
- keine Frontend-Screens
- keine Hooks
- keine Registry-UI
- keine Auth
- kein Streaming
- kein Retry-Loop
- keine erweiterten Integrity-Features
- keine Scope-Ausweitung
- keine neue Architektur

DATEIEN, DIE JETZT GEBAUT WERDEN SOLLEN
1. backend/app/services/input_parser.py
2. backend/app/services/router.py
3. backend/app/services/prompt_composer.py
4. backend/app/services/claude_service.py

ZIEL DIESER PHASE
Diese 4 Dateien sollen den ersten echten Ausführungskern bilden:
- raw input normieren
- route bestimmen
- GosseOS Prompt-Stack bauen
- Claude aufrufen und strukturierten Output zurückgeben

ARCHITEKTURVORGABEN

1. input_parser.py
Zweck:
- normalisiert den eingehenden Rohinput zu einer sauberen internen Case-Arbeitsstruktur
- kein NLP-Overkill
- keine semantische Tiefenanalyse

Pflicht:
- Input aus `CaseCreate` bzw. vorhandenem `CaseRecord` verarbeiten
- leere Strings trimmen
- offensichtliche Leerfelder zu `None` normalisieren
- kleinen internen Helper oder Funktion bereitstellen, die einen sauberen Taskblock vorbereiten kann

Nicht tun:
- keine Heuristik-Orgie
- keine Klassifikation
- keine DB-Logik

2. router.py
Zweck:
- hybrid routing: regelbasiert zuerst, Claude nur als Fallback

Pflicht:
- fester confidence threshold = 0.6
- route_source muss immer gesetzt werden: `rule`, `claude` oder `manual`
- manuelle User-Überschreibung gewinnt immer
- gibt ein sauberes RoutingRecord-kompatibles Ergebnis zurück

Regelbasierte Routing-Logik in v1:
- einfache Keyword-/Pattern-Heuristiken reichen
- problem_class, mode, depth, artifact_type und governance_relevance bestimmen
- confidence_score als float setzen

Claude-Fallback:
- nur wenn Regel-Confidence < 0.6
- Claude-Fallback klein halten
- kein Vollprompt, nur leichter Klassifikationscall

Nicht tun:
- kein ML-System
- kein lernender Router
- keine Blackbox-Logik ohne Nachvollziehbarkeit

3. prompt_composer.py
Zweck:
- baut den finalen Claude-Prompt-Stack in fester Reihenfolge

Pflicht-Reihenfolge:
1. GOSSEOS_CORE
2. INTEGRITY_KERNEL
3. MODE_SPECIFICATIONS (nur relevanter Modusauszug)
4. User Task Block aus Case + Routing
5. angefordertes Artefaktformat
6. optional Governance-Zusatz nur wenn governance_relevance = True

Pflicht:
- nur minimale nötige Module laden
- keine Prompt-Inflation
- klare String-Komposition oder sauberes Messages-Array
- finaler Prompt muss mit der neuen Output-Trennung kompatibel sein
- Claude soll JSON zurückgeben, passend zu:
  - core_result
  - facts
  - assumptions_uncertainties
  - limits
  - optional

Nicht tun:
- keine Template-Engine
- kein dynamisches Modul-Marktplatz-System
- keine vollständige Loading-Logik außerhalb vorhandener module_loader utilities

4. claude_service.py
Zweck:
- führt Claude-Call aus
- verarbeitet die JSON-first Antwort sauber
- respektiert die Trennung:
  - DB: generated_json_text
  - API: output_payload

Pflicht:
- nimmt finalen Prompt vom prompt_composer entgegen
- ruft Claude API auf
- verwendet json_repair.parse_output()
- liefert eine saubere interne Struktur zurück mit:
  - output_payload (wenn parsebar)
  - generated_json_text (serialisiert für DB)
  - parse_status
  - integrity_note optional/leer

Wichtig:
- wenn Parse fehlschlägt: raw text kontrolliert behandeln
- kein stilles Scheitern
- kein Streaming
- kein Retry Loop
- keine Registry-Speicherung hier

OFFENE IMPLEMENTIERUNGSREGELN
- Halte alle Funktionen klein und klar.
- Lieber nachvollziehbare V1-Heuristik als überbaute Cleverness.
- Halte Abhängigkeiten minimal.
- Nutze die bereits definierten Schemas/Enums/Feldnamen exakt.
- Keine Namensabweichungen.
- Keine verdeckten Architekturänderungen.

OUTPUT-ANFORDERUNG

Arbeite in dieser Reihenfolge:

A. Scope-Bestätigung
- max. 10 Zeilen
- was wird jetzt gebaut
- was wird bewusst nicht gebaut

B. Architekturhinweise für diese Phase
- max. 15 Zeilen
- nenne 3–5 kritische Punkte, die im Code strikt eingehalten werden müssen

C. Liefere dann den vollständigen Code für:
1. backend/app/services/input_parser.py
2. backend/app/services/router.py
3. backend/app/services/prompt_composer.py
4. backend/app/services/claude_service.py

D. Vor jeder Datei:
- Dateipfad als Überschrift
- 1–3 Sätze Zweck
- dann vollständiger Codeblock

E. Nach allen Dateien:
- kurze Liste der Integrationspunkte für Phase 3
- kurze Liste möglicher Einbaufehler

QUALITÄTSREGELN
- lauffähiger, nüchterner V1-Code
- keine Fantasieklassen
- keine unnötigen Bibliotheken
- keine übertriebene Abstraktion
- kein unnötiger Asynchronismus, wenn nicht zwingend
- wenn Annahmen nötig sind, explizit markieren
- bei externer Claude-API-Integration: einfachster sauberer Weg

WICHTIGE FACHREGEL
Die neue Output-Trennung muss strikt eingehalten werden:
- Modell/DB-Seite: `generated_json_text`
- Schema/API-Seite: `output_payload`

Das darf im Code an keiner Stelle wieder vermischt werden.

STARTE JETZT MIT:
A. Scope-Bestätigung
B. Architekturhinweise
C. Danach direkt der Code für alle 4 Dateien
```
