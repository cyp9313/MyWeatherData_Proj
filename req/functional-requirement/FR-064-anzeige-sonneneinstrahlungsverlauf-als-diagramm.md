# FR-064: Anzeige des Sonneneinstrahlungsverlaufs als Diagramm

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-017: Verlauf der Sonneneinstrahlung visualisieren

## Beschreibung
Wenn die Visualisierung für den gewählten Ort und Zeitraum aufgerufen wird, muss das Plotly-Diagramm die lokal vorliegenden Sonneneinstrahlungs-Messwerte chronologisch über den gewählten Zeitraum darstellen.

## Eingabe / Vorbedingungen
- Für den gewählten Ort und Zeitraum liegen Sonneneinstrahlungsdaten lokal in der SQLite-Datenbank vor (siehe FR-025)
- Ort und Zeitraum sind über die Streamlit-Konfigurationsoberfläche festgelegt (siehe US-010, US-011)
- Der Aufruf der Visualisierung wird ausgelöst

## Verarbeitungslogik / Ablauf
1. Gewählten Ort und Zeitraum entgegennehmen.
2. Lokal gespeicherte Sonneneinstrahlungsdaten für Ort und Zeitraum aus der SQLite-Datenbank abfragen.
3. Abgefragte Messwerte chronologisch nach Zeitstempel aufsteigend sortieren.
4. Sortierte Messwerte als Plotly-Diagramm rendern.
5. Diagramm in der Streamlit-Oberfläche anzeigen.

## Ausgabe / Ergebnis
Ein Diagramm zeigt die Sonneneinstrahlungs-Messwerte chronologisch über den gewählten Zeitraum an.

## Fehlerfälle / Randbedingungen
- Für den gewählten Ort und Zeitraum liegen keine Sonneneinstrahlungsdaten vor: siehe FR-066
- Der gewählte Zeitraum enthält Nachtstunden ohne Sonneneinstrahlung: siehe FR-067

## Akzeptanzkriterien
- [ ] Bei Aufruf der Visualisierung mit vorliegenden Sonneneinstrahlungsdaten für den gewählten Ort und Zeitraum wird ein Diagramm angezeigt, das die Messwerte chronologisch über den gewählten Zeitraum darstellt

## Abhängigkeiten
- Setzt lokal vorliegende Sonneneinstrahlungsdaten voraus (siehe FR-025)
- Nutzt Ort und Zeitraum aus der Konfiguration (siehe US-010, US-011)
- Ergänzt durch FR-065 (Aktualisierung bei geändertem Zeitraum), FR-066 (keine Daten vorhanden) sowie FR-067 (Darstellung der Nachtstunden)

## Anmerkungen
Als Diagrammtyp wird ein Liniendiagramm (Plotly) verwendet, um den zeitlichen Verlauf der Sonneneinstrahlung darzustellen.
