# Prompterator Style Registry Integration

Status: prepared, not published.

## Scope
This integration connects the PDF/Web Style Registry to the Prompterator single-file demo UI.

## Implemented UI Controls
- Style selector with styles 1-12.
- Default style: Operator.
- Send button: `Senden`.
- Clear input button: `Löschen`.
- Payload includes `selectedStyleId`.
- Explicit style names in the raw input override the UI selection.
- Matt Neon is rejected and not exposed in the active selector.

## Style IDs
1. `operator`
2. `executive_clean`
3. `industrial_logistics`
4. `ai_research_hud`
5. `tactical_black`
6. `pharma_precision`
7. `investor_minimal`
8. `cyberdeck`
9. `apple_glass`
10. `swiss_grid`
11. `brutalist_grid`
12. `cinematic_dossier`

## Manual Local Test
Open:

```bash
open demos/operator-fischer-proof-of-work-demo/site/index.html
```

Manual checks:
1. Style selector shows 1-12.
2. Operator is selected by default.
3. Matt Neon is not listed.
4. Enter text and click `Senden`.
5. Confirm payload contains `selectedStyleId`.
6. Click `Löschen` and confirm only the input field clears.
7. Enter `PDF erstellen im Brutalist Grid Format` and confirm style 11 overrides UI selection.

## Deployment Boundary
No live deploy was executed.
No FTP upload was executed.
No production publishing was executed.

## Manual Deploy Step
Only after explicit Operator Fischer approval, upload this file to the configured checkdomain webroot according to the existing deployment guide:

`demos/operator-fischer-proof-of-work-demo/deploy/checkdomain_prompterator_deploy.md`
