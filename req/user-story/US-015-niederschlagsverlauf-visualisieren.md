# US-015: Verlauf des Niederschlags visualisieren

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-004: Visuelle Darstellung der Wetterdaten

## User Story
Als **Nutzer:in der App**
möchte ich **den zeitlichen Verlauf des Niederschlags für den gewählten Ort und Zeitraum als Diagramm sehen**,
damit **ich Niederschlagsmengen und -muster auf einen Blick erkennen kann, ohne Rohdaten manuell interpretieren zu müssen**.

## Beschreibung / Kontext
Die Niederschlagsdaten liegen für den gewählten Ort und Zeitraum bereits lokal vor (siehe EPIC-002) bzw. wurden zuvor importiert (siehe US-003). Diese Story betrifft ausschließlich die visuelle Aufbereitung dieser Daten als Zeitreihe.

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** lokal vorliegende Niederschlagsdaten für den gewählten Ort und Zeitraum
   **Wenn** die Visualisierung aufgerufen wird
   **Dann** wird ein Diagramm angezeigt, das die Niederschlagsmengen chronologisch über den gewählten Zeitraum darstellt

2. **Gegeben** der gewählte Zeitraum wird geändert
   **Wenn** die Visualisierung aktualisiert wird
   **Dann** zeigt das Diagramm ausschließlich Niederschlagsdaten innerhalb des neu gewählten Zeitraums an

3. **Gegeben** für den gewählten Ort und Zeitraum liegen keine Niederschlagsdaten vor
   **Wenn** die Visualisierung aufgerufen wird
   **Dann** wird anstelle eines Diagramms ein Hinweis angezeigt, dass keine Daten verfügbar sind

4. **Gegeben** im gewählten Zeitraum treten Perioden ohne jeglichen Niederschlag auf
   **Wenn** das Diagramm dargestellt wird
   **Dann** werden diese Perioden im Diagramm als Niederschlagsmenge von 0 dargestellt und nicht als fehlende Daten interpretiert

## Zugehörige Functional Requirements
- [ ] FR-055: Anzeige des Niederschlagsverlaufs als Diagramm
- [ ] FR-056: Aktualisierung des Niederschlagsdiagramms bei geändertem Zeitraum
- [ ] FR-057: Hinweis bei fehlenden Niederschlagsdaten für die Visualisierung
- [ ] FR-058: Darstellung niederschlagsfreier Perioden als Nullwert im Diagramm

## Abhängigkeiten
- Setzt lokal vorliegende Niederschlagsdaten voraus (siehe EPIC-002, US-003)
- Nutzt Ort und Zeitraum aus der Konfiguration (siehe US-010, US-011)

## Anmerkungen
Konkreter Diagrammtyp (z. B. Balkendiagramm für Summenwerte) ist technische Designentscheidung und in den zugehörigen Functional Requirements zu konkretisieren.
