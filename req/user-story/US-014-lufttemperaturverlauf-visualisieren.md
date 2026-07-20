# US-014: Verlauf der Lufttemperatur visualisieren

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-004: Visuelle Darstellung der Wetterdaten

## User Story
Als **Nutzer:in der App**
möchte ich **den zeitlichen Verlauf der Lufttemperatur für den gewählten Ort und Zeitraum als Diagramm sehen**,
damit **ich Temperaturentwicklungen und Auffälligkeiten auf einen Blick erkennen kann, ohne Rohdaten manuell interpretieren zu müssen**.

## Beschreibung / Kontext
Die Lufttemperaturdaten liegen für den gewählten Ort und Zeitraum bereits lokal vor (siehe EPIC-002) bzw. wurden zuvor importiert (siehe US-002). Diese Story betrifft ausschließlich die visuelle Aufbereitung dieser Daten als Zeitreihe.

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** lokal vorliegende Lufttemperaturdaten für den gewählten Ort und Zeitraum
   **Wenn** die Visualisierung aufgerufen wird
   **Dann** wird ein Diagramm angezeigt, das die Lufttemperatur-Messwerte chronologisch über den gewählten Zeitraum darstellt

2. **Gegeben** der gewählte Zeitraum wird geändert
   **Wenn** die Visualisierung aktualisiert wird
   **Dann** zeigt das Diagramm ausschließlich Lufttemperaturdaten innerhalb des neu gewählten Zeitraums an

3. **Gegeben** für den gewählten Ort und Zeitraum liegen keine Lufttemperaturdaten vor
   **Wenn** die Visualisierung aufgerufen wird
   **Dann** wird anstelle eines Diagramms ein Hinweis angezeigt, dass keine Daten verfügbar sind

4. **Gegeben** die Lufttemperaturdaten für den gewählten Zeitraum enthalten Lücken (fehlende Messwerte)
   **Wenn** das Diagramm dargestellt wird
   **Dann** werden die Lücken im Diagramm erkennbar dargestellt, ohne fehlende Werte durch berechnete Werte zu ersetzen

## Zugehörige Functional Requirements
- [ ] FR-050: Anzeige des Lufttemperaturverlaufs als Diagramm
- [ ] FR-051: Aktualisierung des Lufttemperaturdiagramms bei geändertem Zeitraum
- [ ] FR-052: Hinweis bei fehlenden Lufttemperaturdaten für die Visualisierung
- [ ] FR-053: Erkennbare Darstellung von Datenlücken im Lufttemperaturdiagramm
- [ ] FR-054: Keine Interpolation fehlender Lufttemperaturwerte im Diagramm

## Abhängigkeiten
- Setzt lokal vorliegende Lufttemperaturdaten voraus (siehe EPIC-002, US-002)
- Nutzt Ort und Zeitraum aus der Konfiguration (siehe US-010, US-011)

## Anmerkungen
Konkreter Diagrammtyp (z. B. Liniendiagramm) ist technische Designentscheidung und in den zugehörigen Functional Requirements zu konkretisieren.
