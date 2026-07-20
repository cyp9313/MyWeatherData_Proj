# FR-055: Anzeige des Niederschlagsverlaufs als Diagramm

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-015: Verlauf des Niederschlags visualisieren

## Beschreibung
Wenn die Visualisierung für den gewählten Ort und Zeitraum aufgerufen wird, muss das Plotly-Diagramm die lokal vorliegenden Niederschlags-Messwerte chronologisch über den gewählten Zeitraum darstellen.

## Eingabe / Vorbedingungen
- Für den gewählten Ort und Zeitraum liegen Niederschlagsdaten lokal in der SQLite-Datenbank vor (siehe FR-025)
- Ort und Zeitraum sind über die Streamlit-Konfigurationsoberfläche festgelegt (siehe US-010, US-011)
- Der Aufruf der Visualisierung wird ausgelöst

## Verarbeitungslogik / Ablauf
1. Gewählten Ort und Zeitraum entgegennehmen.
2. Lokal gespeicherte Niederschlagsdaten für Ort und Zeitraum aus der SQLite-Datenbank abfragen.
3. Abgefragte Messwerte chronologisch nach Zeitstempel aufsteigend sortieren.
4. Sortierte Messwerte als Plotly-Diagramm rendern.
5. Diagramm in der Streamlit-Oberfläche anzeigen.

## Ausgabe / Ergebnis
Ein Diagramm zeigt die Niederschlags-Messwerte chronologisch über den gewählten Zeitraum an.

## Fehlerfälle / Randbedingungen
- Für den gewählten Ort und Zeitraum liegen keine Niederschlagsdaten vor: siehe FR-057
- Der gewählte Zeitraum enthält Perioden ohne Niederschlag: siehe FR-058

## Akzeptanzkriterien
- [ ] Bei Aufruf der Visualisierung mit vorliegenden Niederschlagsdaten für den gewählten Ort und Zeitraum wird ein Diagramm angezeigt, das die Messwerte chronologisch über den gewählten Zeitraum darstellt

## Abhängigkeiten
- Setzt lokal vorliegende Niederschlagsdaten voraus (siehe FR-025)
- Nutzt Ort und Zeitraum aus der Konfiguration (siehe US-010, US-011)
- Ergänzt durch FR-056 (Aktualisierung bei geändertem Zeitraum), FR-057 (keine Daten vorhanden) sowie FR-058 (Darstellung niederschlagsfreier Perioden)

## Anmerkungen
Als Diagrammtyp wird ein Balkendiagramm (Plotly) verwendet, um die Niederschlagsmengen je Zeitpunkt darzustellen; die konkrete Umsetzung bleibt technische Designentscheidung.
