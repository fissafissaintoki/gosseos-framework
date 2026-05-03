# Prompterator Integration – Command to Knowledge System

## Zweck

Dieses Dokument beschreibt, wie Prompterator als Eingabeschicht fuer die Enterprise Knowledge & Agent Workbench genutzt werden kann.

## Kernlogik

```text
Command Input -> Problemklasse -> Template -> Dokument -> Review -> Knowledge Vault
```

## Eingabebeispiele

```text
ANALYSE + DECISION: Welche Knowledge-Struktur braucht Projekt X?
SOP: Prozess fuer Review von Agentenoutputs
KPI: Nutzen eines Knowledge-Vault-Piloten messen
```

## Command Routing

| Command | Zielartefakt | Zielordner |
|---|---|---|
| ANALYSE | Analyse-Dokument | /docs/processes |
| DECISION | Decision Record | /docs/decisions |
| SOP | Prozessdokument | /docs/processes |
| SECURITY | Security Review | /docs/security |
| GOVERNANCE | Governance Note | /docs/governance |
| AGENT | Agent Task | /templates oder /docs/processes |

## Mindestfelder

Jeder Prompterator-Output muss enthalten:

- Titel
- Problemklasse
- Zielartefakt
- Datenklasse
- Zielordner
- Reviewstatus
- naechster Schritt

## Sicherheitsgate

Vor Speicherung im Vault:

1. Datenklasse pruefen
2. Zielordner pruefen
3. sensible Inhalte entfernen
4. Reviewstatus setzen

## Output Status

Standardstatus nach Generierung:

```text
Status: Draft
Review required: yes
```

## Ziel

Prompterator wird zur strukturierten Eingabe- und Routing-Schicht fuer Knowledge-Artefakte.
