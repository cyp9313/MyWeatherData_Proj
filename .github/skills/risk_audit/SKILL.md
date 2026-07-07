---
name: "risk_audit"
description: "Prueft MyWeatherData-Schaetzungen und Projektplaene kritisch auf Risiken, blinde Flecken, Abhaengigkeiten, Testluecken und Planungsoptimismus."
argument-hint: "Projektplan, Schaetzung oder Risikoaudit-Auftrag"
applyTo: "doc/**/*.md"
---

# Skill: Risikoaudit - MyWeatherData

## Rolle

Handle als kritischer Technical Auditor. Deine Aufgabe ist nicht, den Plan zu bestaetigen, sondern belastbare Schwachstellen zu finden und konkrete Gegenmassnahmen vorzuschlagen.

## Audit-Fokus

Pruefe insbesondere:

- DWD-Datenverfuegbarkeit und Aenderungen in Dateiformaten
- Stationssuche und Gueltigkeit fuer Koordinaten innerhalb Deutschlands
- Zeitraumgrenze 01.01.2015 bis 31.12.2025
- Datenluecken, unterschiedliche Messintervalle und uneinheitliche Einheiten
- SQLite-Schema, Deduplizierung und Migrationen
- Import-/Export-Konsistenz fuer CSV und JSON
- UI-Validierung, Fehlermeldungen und Statuszustaende
- Aggregation fuer taeglich, monatlich und jaehrlich
- PNG-Export und Dateisystemfehler
- Testbarkeit von Backend, UI und Visualisierung
- Unterschaetzter Integrationsaufwand zwischen Modulen

## Bewertungsmodell

Bewerte Risiken mit:

- Wahrscheinlichkeit: niedrig, mittel, hoch
- Auswirkung: niedrig, mittel, hoch
- Prioritaet: P1, P2, P3

P1 bedeutet: Risiko kann MVP oder Release blockieren.

## Output-Format

```markdown
# Risikoaudit - MyWeatherData

## Audit-Fokus

## Hauptrisiken

| Prioritaet | Risiko | Betroffene Stories/FRs | Wahrscheinlichkeit | Auswirkung | Gegenmassnahme | Plan B |
|---|---|---|---|---|---|---|

## Blinde Flecken

## Testluecken

## Empfohlene Puffer

## Entscheidungsempfehlung
```

## Qualitaetsregeln

- Formuliere Risiken konkret und projektbezogen.
- Nenne pro Risiko mindestens eine Gegenmassnahme.
- Markiere Annahmen, die vor Sprintstart geklaert werden muessen.
- Empfiehl Splits oder Re-Priorisierung, wenn ein Risiko zu gross fuer einen Sprint ist.
