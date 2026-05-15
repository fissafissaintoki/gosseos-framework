# Deployment auf prompterator.de bei checkdomain

## Ziel

`site/index.html` wird als Startseite auf `prompterator.de` hochgeladen.

## Upload-Pfad

Bei klassischem checkdomain-Webhosting in der Regel:

```text
/htdocs/index.html
```

## Minimaler Upload

Nur diese Datei wird benoetigt:

```text
site/index.html
```

## Vorgehen im checkdomain Dateimanager

1. In checkdomain einloggen.
2. Webhosting / Dateimanager oeffnen.
3. In den Webroot wechseln: `/htdocs`.
4. Bestehende `index.html` sichern oder ersetzen.
5. Neue `site/index.html` als `index.html` hochladen.
6. Browser pruefen: `https://prompterator.de`.

## macOS Terminal-Upload per SFTP

Nur nutzen, wenn SFTP-Zugangsdaten vorliegen:

```bash
sftp BENUTZERNAME@SERVER
cd /htdocs
put site/index.html index.html
bye
```

## Nachweis

Nach Upload im Browser hart neu laden:

```text
Cmd + Shift + R
```