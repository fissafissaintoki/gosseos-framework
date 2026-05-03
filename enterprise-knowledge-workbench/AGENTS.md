# AGENTS.md

## Zweck

Diese Datei definiert die Arbeitsregeln für Agenten (z. B. Claude Code) innerhalb dieses Projekts.

## Grundprinzip

Agenten sind unterstützende Werkzeuge, keine autonomen Entscheider.

## Zugriff

Erlaubt:
- Lesen: /docs, /templates
- Schreiben: nur nach expliziter Freigabe

Verboten:
- Zugriff auf externe Systeme
- Zugriff auf sensible Daten
- Zugriff auf nicht definierte Ordner

## Aktionen

Erlaubt:
- Dokumentation erstellen
- bestehende Inhalte strukturieren
- Vorschläge machen

Nur mit Review:
- Änderungen an bestehenden Dokumenten
- Erstellung neuer Struktur

Verboten:
- automatische Löschung
- eigenständige Strukturänderung
- Commit ohne Review

## Review-Regel

Jede Änderung muss von einem Menschen geprüft werden.

## Logging

Alle Änderungen müssen nachvollziehbar dokumentiert werden.

## No-Go

Agent darf nicht:
- Entscheidungen ohne Kontext treffen
- Inhalte erfinden
- Policies umgehen

## Ziel

Kontrollierte Unterstützung bei Struktur, Dokumentation und Analyse.
