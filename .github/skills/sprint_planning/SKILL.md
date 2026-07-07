---
name: "sprint_planning"
description: "Erstellt fuer MyWeatherData einen Sprint- und Meilensteinplan aus Epics, User Stories, Story Points und Abhaengigkeiten."
argument-hint: "Backlog-Datei, Schaetzdatei oder Planungsauftrag"
applyTo: "doc/**/*.md"
---

# Skill: Sprint Planning - MyWeatherData

## Aufgabe

Wenn aus dem Backlog ein Projektplan erstellt werden soll, ordne Epics und User Stories in eine sinnvolle zeitliche Reihenfolge. Plane inkrementell, sodass frueh ein testbarer MVP entsteht.

## Standardannahmen

Wenn der Nutzer nichts anderes vorgibt, verwende:

- Sprintlaenge: 2 Wochen
- Team: 2 Entwickler
- Initiale Velocity: 13 Story Points pro Sprint
- Puffer: mindestens 15 Prozent fuer Integration, Datenprobleme und Nacharbeit
- Ziel: lokales Python-basiertes System mit DWD-Daten, SQLite, UI und Visualisierung

## Abhaengigkeitsregeln

Beruecksichtige diese technische Reihenfolge:

1. Stationssuche und DWD-Datenabruf vor Datenbankimport.
2. Datenbankschema und Deduplizierung vor gefiltertem Export.
3. Stabile Backend-Schnittstellen vor finaler UI-Integration.
4. Gespeicherte Daten und Aggregation vor Visualisierung.
5. Gerenderte Visualisierung vor PNG-Export.

## Planungsschritte

1. Erstelle eine Work Breakdown Structure nach Epics.
2. Identifiziere den kritischen Pfad.
3. Ordne User Stories Sprints zu.
4. Halte Velocity-Grenzen ein oder begruende Ausnahmen.
5. Definiere Meilensteine.
6. Markiere Abhaengigkeiten und Integrationspunkte.

## Output-Format

```markdown
# Projektplan - MyWeatherData

## Planungsannahmen

## Work Breakdown Structure

## Sprintplan

| Sprint | Ziel | Stories | Story Points | Lieferobjekte | Abhaengigkeiten |
|---|---|---|---:|---|---|

## Meilensteine

| Meilenstein | Zielzustand | Enthaltene Stories | Nachweis |
|---|---|---|---|

## Kritischer Pfad

## Integrationspunkte

## Offene Planungsfragen
```

## Qualitaetsregeln

- Kein Sprint darf ohne Begruendung deutlich ueber der Velocity liegen.
- Plane keine Visualisierung ohne verfuegbare Datenquelle.
- Plane keine UI-Abnahme ohne Fehlermeldungen und Statuszustaende.
- Mache Abhaengigkeiten sichtbar, statt sie in Lieferobjekten zu verstecken.
