# EPIC-002: Speichern und Verwalten der Wetterdaten in einer lokalen Datenbank

## Status
Draft

## Priorität
Must have

## Beschreibung
Importierte Wetterdaten müssen dauerhaft und effizient in einer lokalen Datenbank gespeichert werden, damit sie ohne erneuten Abruf beim DWD wiederverwendet, gefiltert und für die Visualisierung sowie den Export bereitgestellt werden können.

## Ziel / Business Value
Eine lokale Datenhaltung reduziert wiederholte externe API-Aufrufe, ermöglicht schnellen Zugriff auf bereits geladene Zeiträume/Stationen und bildet die Grundlage für Auswertung und Visualisierung.

## Abgrenzung / Scope
**Enthält:**
- Datenmodell für Wetterstationen und Messwerte (Lufttemperatur, Niederschlag, Wind, Sonneneinstrahlung)
- Speichern importierter Daten aus EPIC-001 in der lokalen Datenbank
- Vermeidung von Duplikaten bei wiederholtem Import gleicher Zeiträume/Stationen
- Abfragen der gespeicherten Daten nach Station, Zeitraum und Messgröße für UI und Visualisierung

**Enthält nicht:**
- Abruf der Rohdaten vom DWD (siehe EPIC-001)
- Darstellung der Daten in Diagrammen/Tabellen (siehe EPIC-004)

## Zugehörige User Stories
- [ ] US-007: Wetterdaten dauerhaft lokal speichern
- [ ] US-008: Duplikate bei wiederholtem Import vermeiden
- [ ] US-009: Gespeicherte Wetterdaten nach Station, Zeitraum und Messgröße abfragen

## Abnahmekriterien (High-Level)
- Wetterdaten werden nach dem Import dauerhaft lokal gespeichert und stehen nach Neustart der App weiterhin zur Verfügung
- Ein erneuter Import bereits vorhandener Zeiträume/Stationen erzeugt keine doppelten Datensätze
- Gespeicherte Daten können performant nach Station, Zeitraum und Messgröße abgefragt werden

## Abhängigkeiten
- EPIC-001 liefert die zu speichernden Rohdaten
- EPIC-003 und EPIC-004 lesen Daten aus der lokalen Datenbank

## Anmerkungen
Wahl der konkreten Datenbanktechnologie (z. B. SQLite) ist technische Designentscheidung und in den zugehörigen Functional Requirements zu konkretisieren.
