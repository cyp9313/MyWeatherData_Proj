# US-007: Wetterdaten dauerhaft lokal speichern

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-002: Speichern und Verwalten der Wetterdaten in einer lokalen Datenbank

## User Story
Als **Nutzer:in der App**
möchte ich **dass importierte Wetterdaten (Lufttemperatur, Niederschlag, Wind, Sonneneinstrahlung) dauerhaft in einer lokalen Datenbank gespeichert werden**,
damit **ich nach einem Neustart der App weiterhin auf die Daten zugreifen kann, ohne sie erneut vom DWD abrufen zu müssen**.

## Beschreibung / Kontext
Die aus EPIC-001 importierten Rohdaten (siehe US-002 bis US-005) liegen zunächst nur im Arbeitsspeicher der App vor. Damit sie über einen Neustart hinaus verfügbar bleiben und als Grundlage für Abfragen (siehe US-009), Konfiguration (EPIC-003) und Visualisierung (EPIC-004) dienen können, müssen sie in einer lokalen Datenbank persistiert werden. Das Datenmodell muss Wetterstationen sowie Messwerte aller vier Messgrößen so abbilden, dass jede Messgröße eindeutig einer Station und einem Zeitpunkt zugeordnet ist. Die konkrete Datenbanktechnologie und das genaue Schema sind technische Designentscheidungen und werden in den zugehörigen Functional Requirements festgelegt.

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** ein erfolgreicher Import von Wetterdaten einer Messgröße für eine Station und einen Zeitraum
   **Wenn** der Import abgeschlossen ist
   **Dann** sind alle importierten Datensätze inkl. Stations-ID, Zeitstempel und Messwert in der lokalen Datenbank gespeichert

2. **Gegeben** importierte Daten mehrerer Messgrößen (Temperatur, Niederschlag, Wind, Sonneneinstrahlung) für dieselbe Station
   **Wenn** die Daten gespeichert werden
   **Dann** bleibt jede Messgröße eindeutig unterscheidbar und einzeln abrufbar

3. **Gegeben** zuvor gespeicherte Wetterdaten
   **Wenn** die App neu gestartet wird
   **Dann** stehen die Daten unverändert zur Verfügung, ohne dass ein erneuter Import ausgelöst werden muss

4. **Gegeben** ein Fehler beim Schreiben in die lokale Datenbank (z. B. Datenbank nicht erreichbar oder Schreibvorgang schlägt fehl)
   **Wenn** importierte Daten gespeichert werden sollen
   **Dann** wird der Fehler erkannt, der betroffene Speichervorgang als fehlgeschlagen markiert und die App stürzt nicht ab

## Zugehörige Functional Requirements
- [ ] FR-025: Speicherung importierter Wetterdaten nach Abschluss des Imports
- [ ] FR-026: Eindeutige Speicherung mehrerer Messgrößen pro Station
- [ ] FR-027: Dauerhafte Verfügbarkeit gespeicherter Wetterdaten über App-Neustarts hinweg
- [ ] FR-028: Fehlerbehandlung bei fehlgeschlagenem Schreibvorgang in die lokale Datenbank

## Abhängigkeiten
- Benötigt importierte Rohdaten aus EPIC-001 (US-002 bis US-005) als Eingangsdaten
- Grundlage für US-008 (Duplikatvermeidung) und US-009 (Abfrage gespeicherter Daten)

## Anmerkungen
Konkretes Datenmodell/Schema und Wahl der Datenbanktechnologie (z. B. SQLite) werden in den zugehörigen Functional Requirements konkretisiert.
