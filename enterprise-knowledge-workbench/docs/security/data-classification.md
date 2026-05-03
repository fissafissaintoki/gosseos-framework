# Data Classification & Security Layer

## Zweck

Dieses Dokument definiert Datenklassen, Zugriffsstufen und Ausschlussregeln für die Enterprise Knowledge & Agent Workbench.

## Grundregel

Keine Agentennutzung ohne Datenklassifikation.

## Datenklassen

| Klasse | Beschreibung | Agentenzugriff |
|---|---|---|
| Public | Öffentlich freigegebene Informationen | erlaubt |
| Internal | interne Arbeitsinformationen ohne sensible Inhalte | eingeschränkt erlaubt |
| Confidential | vertrauliche Geschäfts-, Projekt- oder Vertragsinformationen | nur nach Freigabe |
| Restricted | personenbezogene, rechtliche, finanzielle, sicherheitskritische oder Kundendaten | verboten |

## No-Go-Daten

Folgende Inhalte dürfen nicht in den Pilot-Vault:

- personenbezogene Daten
- Kundendaten
- Personaldaten
- Gehaltsdaten
- Verträge
- Zugangsdaten
- API-Keys
- Quellcode mit Secrets
- Sicherheitsarchitekturdetails ohne Freigabe
- rechtlich sensible Dokumente

## Agentenzugriff

Agenten dürfen nur mit freigegebenen Daten arbeiten.

Erlaubt:
- Public
- Internal, wenn keine sensiblen Inhalte enthalten sind

Nicht erlaubt:
- Restricted
- ungeprüfte Confidential-Daten

## Sicherheitsprüfung vor Nutzung

Vor jedem Agenteneinsatz prüfen:

1. Welche Datenklasse liegt vor?
2. Ist der Ordner freigegeben?
3. Sind personenbezogene oder vertrauliche Inhalte enthalten?
4. Gibt es eine menschliche Freigabe?
5. Muss Inhalt anonymisiert werden?

## Stop-Regel

Wenn die Datenklasse unklar ist, wird der Agent nicht eingesetzt.

```text
UNKNOWN DATA CLASS = NO AGENT ACCESS
```

## Anonymisierung

Bei Unsicherheit:

- Namen entfernen
- Kundennamen ersetzen
- IDs entfernen
- Verträge und Beträge abstrahieren
- technische Secrets entfernen

## Reviewpflicht

Jeder Output mit Datenbezug muss vor Weitergabe geprüft werden.

## Ziel

Kontrollierter Nutzen ohne Datenrisiko.
