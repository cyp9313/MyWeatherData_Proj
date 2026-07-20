# US-008: Duplikate bei wiederholtem Import vermeiden

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-002: Speichern und Verwalten der Wetterdaten in einer lokalen Datenbank

## User Story
Als **Nutzer:in der App**
möchte ich **dass beim erneuten Import bereits vorhandener Stationen/Zeiträume keine doppelten Datensätze in der lokalen Datenbank entstehen**,
damit **meine Datenbasis konsistent bleibt und kein unnötiger Speicherplatz durch Mehrfachimporte verbraucht wird**.

## Beschreibung / Kontext
Nutzer:innen können einen Import (siehe US-002 bis US-005) für Stationen und Zeiträume mehrfach auslösen, z. B. weil sie sich überschneidende Zeiträume abrufen oder einen Import versehentlich wiederholen. Beim Speichern (siehe US-007) muss daher erkannt werden, ob für eine Kombination aus Station, Messgröße und Zeitpunkt bereits ein Datensatz existiert, um doppelte Einträge zu vermeiden.

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** Wetterdaten einer Station sind für einen Zeitraum bereits gespeichert
   **Wenn** derselbe Zeitraum für dieselbe Station und Messgröße erneut importiert wird
   **Dann** bleibt die Anzahl der gespeicherten Datensätze für diese Kombination unverändert

2. **Gegeben** ein bereits gespeicherter Zeitraum überschneidet sich teilweise mit einem neu angeforderten Import
   **Wenn** der Import ausgeführt wird
   **Dann** werden nur die bisher fehlenden Zeitpunkte innerhalb des Zeitraums ergänzt und bereits vorhandene Datensätze bleiben unverändert

3. **Gegeben** Wetterdaten für Station A sind für einen Zeitraum bereits gespeichert
   **Wenn** Wetterdaten für Station B im selben Zeitraum und derselben Messgröße importiert werden
   **Dann** werden die Daten von Station B als eigenständige, neue Datensätze gespeichert

4. **Gegeben** zwei Importvorgänge für dieselbe Station, denselben Zeitraum und dieselbe Messgröße werden nacheinander ausgelöst
   **Wenn** beide Importvorgänge abgeschlossen sind
   **Dann** existieren die Datensätze dieses Zeitraums danach weiterhin nur einmal in der Datenbank

## Zugehörige Functional Requirements
- [ ] FR-029: Keine Duplikate bei wiederholtem Import derselben Kombination aus Station, Messgröße und Zeitstempel
- [ ] FR-030: Ergänzung fehlender Zeitpunkte bei teilweiser Überschneidung mit bereits gespeicherten Daten
- [ ] FR-031: Getrennte Speicherung unterschiedlicher Stationen bei gleichem Zeitraum und gleicher Messgröße
- [ ] FR-032: Aktualisierung des gespeicherten Werts bei inhaltlich abweichendem, zeitlich neuerem Import für identische Kombination

## Abhängigkeiten
- Setzt US-007 (Speichern importierter Daten in der lokalen Datenbank) voraus

## Anmerkungen
Bei inhaltlich abweichenden Werten für denselben Zeitpunkt (z. B. nachträglich korrigierte DWD-Daten) wird stets der zeitlich zuletzt importierte (neueste) Wert übernommen (siehe FR-032).
