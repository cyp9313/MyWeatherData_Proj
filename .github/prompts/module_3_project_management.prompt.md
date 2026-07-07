---
agent: "agent"
description: "Erstelle die Modul-3-Projektmanagement-Artefakte fuer MyWeatherData: Aufwandsschaetzung, Sprintplan und Risikoaudit."
---

Erstelle fuer das Projekt MyWeatherData die Projektmanagement-Artefakte aus Modul 3.

Nutze als verbindlichen Kontext:
- `.github/copilot-instructions.md`
- `doc/req/epic_myweatherdata.md`
- `doc/req/user_story_myweatherdata.md`
- `doc/req/functional_requirement_myweatherdata.md`

Arbeite in drei Phasen:

1. Aufwandsschaetzung
   - Schaetze jede User Story mit Story Points aus der Fibonacci-Reihe: 1, 2, 3, 5, 8, 13.
   - Nutze USER_STORY_01 als kleine technische Referenzstory.
   - Begruende jede Schaetzung mit konkreten Aufwandstreibern, Abhaengigkeiten, Edge Cases und offenen Annahmen.
   - Pruefe fuer jede Story die Definition of Ready.

2. Projektplan
   - Erstelle aus Epics, User Stories und Schaetzungen einen logischen Sprintplan.
   - Plane mit 2-Wochen-Sprints, einem kleinen Team von 2 Entwicklern und einer initialen Velocity von 13 Story Points pro Sprint.
   - Beruecksichtige technische Reihenfolge: DWD-API vor Datenbankimport, Datenbank vor Export und Visualisierung, UI-Integration nach stabilen Backend-Schnittstellen.
   - Definiere Meilensteine fuer MVP, integrierten Prototyp und Release Candidate.

3. Risikoaudit
   - Pruefe den Plan kritisch als Technical Auditor.
   - Suche nach versteckten Abhaengigkeiten, unterschaetztem Integrationsaufwand, Datenqualitaetsrisiken, Testluecken und Planungsoptimismus.
   - Schlage konkrete Gegenmassnahmen, Puffer und Plan-B-Optionen vor.

Schreibe die Ergebnisse in folgende Dateien:
- `doc/pm/effort_estimation_myweatherdata.md`
- `doc/pm/project_plan_myweatherdata.md`
- `doc/pm/risk_audit_myweatherdata.md`

Falls `doc/pm/` nicht existiert, lege den Ordner an.

Verwende Deutsch. Schreibe sachlich, pruefbar und tabellarisch, wo es die Lesbarkeit verbessert.

Die Dateien muessen diese Mindeststruktur haben:

`effort_estimation_myweatherdata.md`

```markdown
# Aufwandsschaetzung - MyWeatherData

## Annahmen

## Schaetzmodell

## Story-Point-Schaetzung

| Story | Epic | Titel | Story Points | Aufwandstreiber | Abhaengigkeiten | Definition of Ready | Annahmen |
|---|---|---|---:|---|---|---|---|

## Zusammenfassung nach Epic

## Offene Punkte
```

`project_plan_myweatherdata.md`

```markdown
# Projektplan - MyWeatherData

## Planungsannahmen

## Work Breakdown Structure

## Sprintplan

| Sprint | Ziel | Stories | Story Points | Lieferobjekte | Abhaengigkeiten |
|---|---|---|---:|---|---|

## Meilensteine

## Kritischer Pfad
```

`risk_audit_myweatherdata.md`

```markdown
# Risikoaudit - MyWeatherData

## Audit-Fokus

## Hauptrisiken

| Risiko | Betroffene Stories | Wahrscheinlichkeit | Auswirkung | Gegenmassnahme | Plan B |
|---|---|---|---|---|---|

## Blinde Flecken

## Empfohlene Puffer

## Entscheidungsempfehlung
```
