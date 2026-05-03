# Enterprise Knowledge & Agent Workbench v1

## Zweck

Dieses Artefakt beschreibt eine kontrollierte Zusatz-Workbench für Teams, die Obsidian als Markdown-basierte Wissensschicht und Claude Code als begrenzten Agenten im Projektkontext einsetzen wollen.

Nicht als Tool-Spielerei. Nicht als unkontrollierter Notiz-Wildwuchs. Sondern als pilotierbare Knowledge- und Agentenarchitektur.

## Kernthese

Die Leitfrage ist nicht: Kann man Obsidian + Claude Code im Enterprise einsetzen?

Die Leitfrage ist: Kann man daraus eine kontrollierte Workbench bauen, bei der Datenzugriff, Dateistruktur, Rechte, Review und Governance sauber geregelt sind?

## Systemlogik

```text
Enterprise Knowledge Workbench = Vault-Struktur + Agentenregeln + Datenmodell + Review + Governance
```

## Komponenten

1. Knowledge Layer
   - Markdown Vault
   - klare Ordnerstruktur
   - Templates
   - Namenskonventionen
   - Dokumenttypen

2. Agent Control Layer
   - AGENTS.md
   - erlaubte Ordner
   - verbotene Ordner
   - erlaubte Aktionen
   - Reviewpflicht
   - Logging

3. Governance Layer
   - Datenklassen
   - Zugriffsklassen
   - No-Go-Daten
   - DLP-/Security-Prüfung
   - Offboarding
   - Backup/Recovery

4. Value Layer
   - Fileserver-Cleanup
   - Projektdokumentation
   - Architekturentscheidungen
   - SOPs
   - Prozesswissen
   - Team-Onboarding

## Pilot-Prinzip

Nicht direkt Enterprise-Rollout.

Pilot:
- ein Team
- ein Projekt
- ein Vault
- keine sensiblen Daten
- klare Agentenregeln
- Reviewpflicht vor Merge oder Veröffentlichung
- Änderungslog dokumentieren

## Mindeststruktur

```text
enterprise-knowledge-workbench/
├── README.md
├── AGENTS.md
├── docs/
│   ├── architecture/
│   ├── decisions/
│   ├── processes/
│   ├── security/
│   └── governance/
├── templates/
│   ├── decision-record.md
│   ├── process.md
│   ├── security-review.md
│   └── agent-task.md
└── pilot-plan.md
```

## Nicht-Ziele

Diese Workbench ist nicht:
- Ersatz für Microsoft 365 Governance
- Freigabe für sensible Daten
- autonomer Produktionsagent
- DMS-Ersatz ohne Records-/Retention-Konzept
- rechtliche oder IT-Security-Freigabe

## Qualitätskriterien

Eine Workbench gilt nur dann als belastbar, wenn:
- Datenklassen definiert sind
- erlaubte/verbotene Inhalte dokumentiert sind
- Agentenregeln schriftlich existieren
- Änderungen reviewpflichtig sind
- Nutzen anhand konkreter Cases gemessen wird
- ein Offboarding- und Backup-Konzept existiert

## Kurzpositionierung

Claude + Obsidian ist im Enterprise nicht primär eine Toolfrage, sondern eine Frage kontrollierter Knowledge Architecture.

Der stärkste Use Case ist ein kontrollierter Projekt-Vault als agentische Knowledge-Workbench.
