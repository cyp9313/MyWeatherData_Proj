# FR-059: Anzeige des Windgeschwindigkeitsverlaufs als Diagramm

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-016: Verlauf des Winds visualisieren

## Beschreibung
Wenn die Visualisierung für den gewählten Ort und Zeitraum aufgerufen wird, muss das Plotly-Diagramm die lokal vorliegenden Windgeschwindigkeits-Messwerte chronologisch über den gewählten Zeitraum darstellen.

## Eingabe / Vorbedingungen
- Für den gewählten Ort und Zeitraum liegen Winddaten lokal in der SQLite-Datenbank vor (siehe FR-025)
- Ort und Zeitraum sind über die Streamlit-Konfigurationsoberfläche festgelegt (siehe US-010, US-011)
- Der Aufruf der Visualisierung wird ausgelöst

## Verarbeitungslogik / Ablauf
1. Gewählten Ort und Zeitraum entgegennehmen.
2. Lokal gespeicherte Windgeschwindigkeitsdaten für Ort und Zeitraum aus der SQLite-Datenbank abfragen.
3. Abgefragte Messwerte chronologisch nach Zeitstempel aufsteigend sortieren.
4. Sortierte Messwerte als Plotly-Diagramm rendern.
5. Diagramm in der Streamlit-Oberfläche anzeigen.

## Ausgabe / Ergebnis
Ein Diagramm zeigt die Windgeschwindigkeits-Messwerte chronologisch über den gewählten Zeitraum an.

## Fehlerfälle / Randbedingungen
- Für den gewählten Ort und Zeitraum liegen keine Winddaten vor: siehe FR-061
- Die Winddaten enthalten Lücken: siehe FR-062, FR-063

## Akzeptanzkriterien
- [ ] Bei Aufruf der Visualisierung mit vorliegenden Winddaten für den gewählten Ort und Zeitraum wird ein Diagramm angezeigt, das die Windgeschwindigkeits-Messwerte chronologisch über den gewählten Zeitraum darstellt

## Abhängigkeiten
- Setzt lokal vorliegende Winddaten voraus (siehe FR-025)
- Nutzt Ort und Zeitraum aus der Konfiguration (siehe US-010, US-011)
- Ergänzt durch FR-060 (Aktualisierung bei geändertem Zeitraum), FR-061 (keine Daten vorhanden) sowie FR-062/FR-063 (Datenlücken)

## Anmerkungen
Als Diagrammtyp wird ein Liniendiagramm (Plotly) verwendet, um den zeitlichen Verlauf der Windgeschwindigkeit darzustellen. Die Darstellung der Windrichtung ist nicht Teil dieses Functional Requirements (siehe US-016).
