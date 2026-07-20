# US-016: Verlauf des Winds visualisieren

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-004: Visuelle Darstellung der Wetterdaten

## User Story
Als **Nutzer:in der App**
möchte ich **den zeitlichen Verlauf der Windgeschwindigkeit für den gewählten Ort und Zeitraum als Diagramm sehen**,
damit **ich Windverhältnisse und Auffälligkeiten auf einen Blick erkennen kann, ohne Rohdaten manuell interpretieren zu müssen**.

## Beschreibung / Kontext
Die Winddaten liegen für den gewählten Ort und Zeitraum bereits lokal vor (siehe EPIC-002) bzw. wurden zuvor importiert (siehe US-004). Diese Story betrifft ausschließlich die visuelle Aufbereitung der Windgeschwindigkeit als Zeitreihe; die Darstellung der Windrichtung ist nicht Teil dieser Story.

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** lokal vorliegende Winddaten für den gewählten Ort und Zeitraum
   **Wenn** die Visualisierung aufgerufen wird
   **Dann** wird ein Diagramm angezeigt, das die Windgeschwindigkeits-Messwerte chronologisch über den gewählten Zeitraum darstellt

2. **Gegeben** der gewählte Zeitraum wird geändert
   **Wenn** die Visualisierung aktualisiert wird
   **Dann** zeigt das Diagramm ausschließlich Winddaten innerhalb des neu gewählten Zeitraums an

3. **Gegeben** für den gewählten Ort und Zeitraum liegen keine Winddaten vor
   **Wenn** die Visualisierung aufgerufen wird
   **Dann** wird anstelle eines Diagramms ein Hinweis angezeigt, dass keine Daten verfügbar sind

4. **Gegeben** die Winddaten für den gewählten Zeitraum enthalten Lücken (fehlende Messwerte)
   **Wenn** das Diagramm dargestellt wird
   **Dann** werden die Lücken im Diagramm erkennbar dargestellt, ohne fehlende Werte durch berechnete Werte zu ersetzen

## Zugehörige Functional Requirements
- [ ] FR-059: Anzeige des Windgeschwindigkeitsverlaufs als Diagramm
- [ ] FR-060: Aktualisierung des Winddiagramms bei geändertem Zeitraum
- [ ] FR-061: Hinweis bei fehlenden Winddaten für die Visualisierung
- [ ] FR-062: Erkennbare Darstellung von Datenlücken im Winddiagramm
- [ ] FR-063: Keine Interpolation fehlender Windgeschwindigkeitswerte im Diagramm

## Abhängigkeiten
- Setzt lokal vorliegende Winddaten voraus (siehe EPIC-002, US-004)
- Nutzt Ort und Zeitraum aus der Konfiguration (siehe US-010, US-011)

## Anmerkungen
Ob und wie zusätzlich die Windrichtung dargestellt wird, ist in den zugehörigen Functional Requirements zu klären; diese Story deckt nur die Windgeschwindigkeit ab.
