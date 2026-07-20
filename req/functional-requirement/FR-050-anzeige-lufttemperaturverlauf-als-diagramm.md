# FR-050: Anzeige des Lufttemperaturverlaufs als Diagramm

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-014: Verlauf der Lufttemperatur visualisieren

## Beschreibung
Wenn die Visualisierung für den gewählten Ort und Zeitraum aufgerufen wird, muss das Plotly-Diagramm die lokal vorliegenden Lufttemperatur-Messwerte chronologisch über den gewählten Zeitraum darstellen.

## Eingabe / Vorbedingungen
- Für den gewählten Ort und Zeitraum liegen Lufttemperaturdaten lokal in der SQLite-Datenbank vor (siehe FR-025)
- Ort und Zeitraum sind über die Streamlit-Konfigurationsoberfläche festgelegt (siehe US-010, US-011)
- Der Aufruf der Visualisierung wird ausgelöst

## Verarbeitungslogik / Ablauf
1. Gewählten Ort und Zeitraum entgegennehmen.
2. Lokal gespeicherte Lufttemperaturdaten für Ort und Zeitraum aus der SQLite-Datenbank abfragen.
3. Abgefragte Messwerte chronologisch nach Zeitstempel aufsteigend sortieren.
4. Sortierte Messwerte als Plotly-Diagramm rendern.
5. Diagramm in der Streamlit-Oberfläche anzeigen.

## Ausgabe / Ergebnis
Ein Diagramm zeigt die Lufttemperatur-Messwerte chronologisch über den gewählten Zeitraum an.

## Fehlerfälle / Randbedingungen
- Für den gewählten Ort und Zeitraum liegen keine Lufttemperaturdaten vor: siehe FR-052
- Die Lufttemperaturdaten enthalten Lücken: siehe FR-053, FR-054

## Akzeptanzkriterien
- [ ] Bei Aufruf der Visualisierung mit vorliegenden Lufttemperaturdaten für den gewählten Ort und Zeitraum wird ein Diagramm angezeigt, das die Messwerte chronologisch über den gewählten Zeitraum darstellt

## Abhängigkeiten
- Setzt lokal vorliegende Lufttemperaturdaten voraus (siehe FR-025)
- Nutzt Ort und Zeitraum aus der Konfiguration (siehe US-010, US-011)
- Ergänzt durch FR-051 (Aktualisierung bei geändertem Zeitraum), FR-052 (keine Daten vorhanden) sowie FR-053/FR-054 (Datenlücken)

## Anmerkungen
Als Diagrammtyp wird ein Liniendiagramm (Plotly) verwendet, um den zeitlichen Verlauf der Lufttemperatur darzustellen.
