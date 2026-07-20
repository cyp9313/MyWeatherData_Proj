# US-017: Verlauf der Sonneneinstrahlung visualisieren

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-004: Visuelle Darstellung der Wetterdaten

## User Story
Als **Nutzer:in der App**
möchte ich **den zeitlichen Verlauf der Sonneneinstrahlung für den gewählten Ort und Zeitraum als Diagramm sehen**,
damit **ich Sonneneinstrahlungsverläufe und Auffälligkeiten auf einen Blick erkennen kann, ohne Rohdaten manuell interpretieren zu müssen**.

## Beschreibung / Kontext
Die Sonneneinstrahlungsdaten liegen für den gewählten Ort und Zeitraum bereits lokal vor (siehe EPIC-002) bzw. wurden zuvor importiert (siehe US-005). Diese Story betrifft ausschließlich die visuelle Aufbereitung dieser Daten als Zeitreihe.

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** lokal vorliegende Sonneneinstrahlungsdaten für den gewählten Ort und Zeitraum
   **Wenn** die Visualisierung aufgerufen wird
   **Dann** wird ein Diagramm angezeigt, das die Sonneneinstrahlungs-Messwerte chronologisch über den gewählten Zeitraum darstellt

2. **Gegeben** der gewählte Zeitraum wird geändert
   **Wenn** die Visualisierung aktualisiert wird
   **Dann** zeigt das Diagramm ausschließlich Sonneneinstrahlungsdaten innerhalb des neu gewählten Zeitraums an

3. **Gegeben** für den gewählten Ort und Zeitraum liegen keine Sonneneinstrahlungsdaten vor
   **Wenn** die Visualisierung aufgerufen wird
   **Dann** wird anstelle eines Diagramms ein Hinweis angezeigt, dass keine Daten verfügbar sind

4. **Gegeben** im gewählten Zeitraum treten Nachtstunden ohne Sonneneinstrahlung auf
   **Wenn** das Diagramm dargestellt wird
   **Dann** werden diese Zeitpunkte als Sonneneinstrahlung von 0 dargestellt und nicht als fehlende Daten interpretiert

## Zugehörige Functional Requirements
- [ ] FR-064: Anzeige des Sonneneinstrahlungsverlaufs als Diagramm
- [ ] FR-065: Aktualisierung des Sonneneinstrahlungsdiagramms bei geändertem Zeitraum
- [ ] FR-066: Hinweis bei fehlenden Sonneneinstrahlungsdaten für die Visualisierung
- [ ] FR-067: Darstellung von Nachtstunden als Nullwert im Sonneneinstrahlungsdiagramm

## Abhängigkeiten
- Setzt lokal vorliegende Sonneneinstrahlungsdaten voraus (siehe EPIC-002, US-005)
- Nutzt Ort und Zeitraum aus der Konfiguration (siehe US-010, US-011)

## Anmerkungen
Konkreter Diagrammtyp ist technische Designentscheidung und in den zugehörigen Functional Requirements zu konkretisieren.
