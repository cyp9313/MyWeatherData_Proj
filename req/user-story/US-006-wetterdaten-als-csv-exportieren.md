# US-006: Wetterdaten als CSV exportieren

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-001: Datenimport/-export vom DWD Climate Data Center

## User Story
Als **Nutzer:in der App**
möchte ich **die importierten Wetterdaten für einen von mir gewählten Zeitraum als CSV-Datei exportieren**,
damit **ich die Daten in anderen Tools (z. B. Tabellenkalkulation) außerhalb der App weiterverwenden kann**.

## Beschreibung / Kontext
Der Export bezieht sich auf bereits importierte/aufbereitete Daten (siehe US-002 bis US-005), unabhängig von der jeweiligen Messgröße. Die persistente Speicherung der Daten selbst ist nicht Teil dieser Story (siehe EPIC-002).

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** importierte Wetterdaten liegen für den gewählten Zeitraum vor
   **Wenn** der Export ausgelöst wird
   **Dann** wird eine CSV-Datei erzeugt, die je Zeitstempel die zugehörigen Messwerte des Zeitraums in getrennten Spalten enthält

2. **Gegeben** für den gewählten Zeitraum liegen keine importierten Daten vor
   **Wenn** der Export ausgelöst wird
   **Dann** wird keine Datei erzeugt, sondern ein Hinweis ausgegeben, dass für den Zeitraum keine Daten vorhanden sind

3. **Gegeben** ein gewählter Zeitraum, der den gesamten unterstützten Bereich (01.01.2015–31.12.2025) umfasst
   **Wenn** der Export ausgelöst wird
   **Dann** enthält die erzeugte CSV-Datei genau einen Datensatz je vorhandenem Zeitstempel des gesamten Zeitraums

4. **Gegeben** ein gewählter Start- oder Enddatum liegt außerhalb des unterstützten Bereichs (01.01.2015–31.12.2025)
   **Wenn** der Export ausgelöst wird
   **Dann** wird der Zeitraum auf den unterstützten Bereich begrenzt und der Nutzer erhält einen entsprechenden Hinweis

## Zugehörige Functional Requirements
- [ ] FR-021: CSV-Export bei vorhandenen Wetterdaten im gewählten Zeitraum
- [ ] FR-022: Kein CSV-Export bei fehlenden Daten für den gewählten Zeitraum
- [ ] FR-023: Vollständigkeit der CSV-Datei beim Export des gesamten unterstützten Bereichs
- [ ] FR-024: Kürzung des Exportzeitraums bei Überschreitung des unterstützten Bereichs

## Abhängigkeiten
- Setzt importierte Daten aus US-002 (Lufttemperatur), US-003 (Niederschlag), US-004 (Wind) und/oder US-005 (Sonneneinstrahlung) voraus

## Anmerkungen
Performance-Aspekte bei sehr großen Exportzeiträumen sind bei Bedarf in einem separaten Functional Requirement zu konkretisieren.
