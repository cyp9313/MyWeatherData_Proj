# US-018: Mehrere Messgrößen gemeinsam visualisieren

## Status
Review

## Priorität
Should have

## Zugehöriges Epic
EPIC-004: Visuelle Darstellung der Wetterdaten

## User Story
Als **Nutzer:in der App**
möchte ich **die Diagramme mehrerer ausgewählter Messgrößen für denselben Ort und Zeitraum gleichzeitig bzw. übersichtlich nebeneinander sehen**,
damit **ich Zusammenhänge und Unterschiede zwischen den Messgrößen im gleichen Zeitraum vergleichen kann**.

## Beschreibung / Kontext
Diese Story baut auf den einzelnen Messgrößen-Diagrammen (US-014 bis US-017) auf und regelt deren gemeinsame, übersichtliche Anordnung, wenn der Nutzer mehr als eine Messgröße ausgewählt hat (siehe US-012).

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** genau eine Messgröße ist ausgewählt
   **Wenn** die Visualisierung angezeigt wird
   **Dann** wird nur das Diagramm dieser einen Messgröße dargestellt

2. **Gegeben** mehrere Messgrößen sind ausgewählt
   **Wenn** die Visualisierung angezeigt wird
   **Dann** werden die Diagramme aller ausgewählten Messgrößen für den gleichen Ort und Zeitraum gleichzeitig angezeigt

3. **Gegeben** alle vier verfügbaren Messgrößen sind ausgewählt
   **Wenn** die Visualisierung angezeigt wird
   **Dann** werden alle vier Diagramme ohne gegenseitige Überschneidung oder Überlappung dargestellt

4. **Gegeben** mehrere Messgrößen sind ausgewählt und für eine davon liegen im gewählten Zeitraum keine Daten vor
   **Wenn** die Visualisierung angezeigt wird
   **Dann** wird für die betroffene Messgröße ein Hinweis auf fehlende Daten angezeigt, während die Diagramme der übrigen Messgrößen unverändert dargestellt werden

## Zugehörige Functional Requirements
- [ ] FR-068: Einzeldarstellung bei genau einer ausgewählten Messgröße
- [ ] FR-069: Gleichzeitige Darstellung der Diagramme mehrerer ausgewählter Messgrößen
- [ ] FR-070: Überschneidungsfreie Darstellung aller vier Messgrößen-Diagramme
- [ ] FR-071: Hinweis auf fehlende Daten bei gemeinsamer Darstellung mehrerer Messgrößen
- [ ] FR-072: Unveränderte Darstellung der übrigen Diagramme bei fehlenden Daten einer Messgröße

## Abhängigkeiten
- Setzt die Einzeldarstellungen aus US-014 (Lufttemperatur), US-015 (Niederschlag), US-016 (Wind) und US-017 (Sonneneinstrahlung) voraus
- Nutzt die Messgrößenauswahl aus US-012

## Anmerkungen
Konkrete Anordnung (z. B. untereinander, im Raster, mit gemeinsamer Zeitachse) ist technische Designentscheidung und in den zugehörigen Functional Requirements zu konkretisieren.
