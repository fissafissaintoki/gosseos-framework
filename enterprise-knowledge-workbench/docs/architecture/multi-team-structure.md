# Multi-Team Vault Architecture

## Zweck

Skalierung der Knowledge & Agent Workbench auf mehrere Teams.

## Grundprinzip

Nicht ein großer Vault, sondern strukturierte Trennung.

## Struktur

```text
vault-root/
├── global/
│   ├── governance/
│   ├── templates/
│   └── security/
├── team-A/
│   ├── docs/
│   ├── decisions/
│   └── processes/
├── team-B/
│   ├── docs/
│   ├── decisions/
│   └── processes/
└── projects/
    ├── project-1/
    └── project-2/
```

## Regeln

- globale Standards im global-Vault
- Teams arbeiten isoliert
- Projekte sind eigene Einheiten

## Zugriff

| Ebene | Zugriff |
|---|---|
| global | read-only fuer Teams |
| team | team-intern |
| project | projektbezogen |

## Vorteile

- keine Datenvermischung
- klare Verantwortlichkeiten
- einfache Skalierung

## Risiken

- zu viele Vaults
- inkonsistente Nutzung

## Gegenmaßnahmen

- klare Naming-Regeln
- zentrale Templates
- Governance durch global Layer

## Ziel

Skalierbare, kontrollierte Knowledge-Struktur fuer mehrere Teams.
