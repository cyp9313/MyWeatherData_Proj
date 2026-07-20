# US-009: Gespeicherte Wetterdaten nach Station, Zeitraum und Messgröße abfragen

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-002: Speichern und Verwalten der Wetterdaten in einer lokalen Datenbank

## User Story
Als **Nutzer:in der App**
möchte ich **in der lokalen Datenbank gespeicherte Wetterdaten nach Station, Zeitraum und Messgröße abfragen können**,
damit **ich gezielt die für Auswertung, Visualisierung oder Export relevanten Daten erhalte**.

## Beschreibung / Kontext
Damit die UI-Konfiguration (EPIC-003) und die Visualisierung (EPIC-004) auf die zuvor importierten und gespeicherten Wetterdaten (siehe US-007) zugreifen können, muss die lokale Datenhaltung eine Abfrageschnittstelle bereitstellen. Die Abfrage erfolgt anhand von Stations-ID, Zeitraum und optional einer oder mehrerer Messgrößen (Temperatur, Niederschlag, Wind, Sonneneinstrahlung).

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** gespeicherte Wetterdaten mehrerer Messgrößen und Zeiträume für eine Station
   **Wenn** eine Abfrage mit Stations-ID, Zeitraum und einer konkreten Messgröße ausgeführt wird
   **Dann** werden genau die Datensätze zurückgegeben, die zu dieser Station, diesem Zeitraum und dieser Messgröße gehören

2. **Gegeben** gespeicherte Wetterdaten mehrerer Messgrößen für eine Station und einen Zeitraum
   **Wenn** eine Abfrage mit Stations-ID und Zeitraum ohne Angabe einer Messgröße ausgeführt wird
   **Dann** werden die Datensätze aller gespeicherten Messgrößen für diese Station und diesen Zeitraum zurückgegeben

3. **Gegeben** keine gespeicherten Daten für die angefragte Kombination aus Station, Zeitraum und Messgröße
   **Wenn** die Abfrage ausgeführt wird
   **Dann** wird ein leeres Ergebnis zurückgegeben, ohne dass ein Fehler ausgelöst wird

4. **Gegeben** eine Abfrage mit einer Stations-ID, die in der lokalen Datenbank nicht existiert
   **Wenn** die Abfrage ausgeführt wird
   **Dann** wird ein entsprechender Hinweis zurückgegeben, statt fehlerhafter Daten oder eines Absturzes

## Zugehörige Functional Requirements
- [ ] FR-033: Abfrage gespeicherter Wetterdaten nach Station, Zeitraum und Messgröße
- [ ] FR-034: Abfrage gespeicherter Wetterdaten ohne Angabe einer Messgröße
- [ ] FR-035: Leeres Ergebnis bei fehlenden Daten für die angefragte Kombination
- [ ] FR-036: Hinweis bei Abfrage mit unbekannter Stations-ID

## Abhängigkeiten
- Setzt US-007 (Speichern importierter Daten in der lokalen Datenbank) voraus
- Wird von EPIC-003 (UI-Konfiguration) und EPIC-004 (Visualisierung) zum Datenzugriff genutzt

## Anmerkungen
Keine.
