# FR-066: Hinweis bei fehlenden Sonneneinstrahlungsdaten für die Visualisierung

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-017: Verlauf der Sonneneinstrahlung visualisieren

## Beschreibung
Wenn für den gewählten Ort und Zeitraum keine Sonneneinstrahlungsdaten vorliegen, muss die Streamlit-Oberfläche anstelle eines Diagramms einen Hinweis anzeigen, dass keine Daten verfügbar sind.

## Eingabe / Vorbedingungen
- Für den gewählten Ort und Zeitraum sind keine Sonneneinstrahlungsdaten in der SQLite-Datenbank gespeichert (siehe FR-035)
- Der Aufruf der Visualisierung wird ausgelöst

## Verarbeitungslogik / Ablauf
1. Sonneneinstrahlungsdaten für den gewählten Ort und Zeitraum aus der SQLite-Datenbank abfragen.
2. Feststellen, dass die Abfrage ein leeres Ergebnis liefert.
3. Anstelle eines Diagramms einen Hinweistext anzeigen, dass keine Daten verfügbar sind.

## Ausgabe / Ergebnis
Ein Hinweis, dass keine Daten verfügbar sind, wird anstelle eines Diagramms angezeigt.

## Fehlerfälle / Randbedingungen
- Leeres Abfrageergebnis für die angefragte Kombination aus Ort, Zeitraum und Messgröße (siehe FR-035): Hinweis statt Diagramm anzeigen

## Akzeptanzkriterien
- [ ] Bei fehlenden Sonneneinstrahlungsdaten für den gewählten Ort und Zeitraum wird anstelle eines Diagramms ein Hinweis angezeigt, dass keine Daten verfügbar sind

## Abhängigkeiten
- Nutzt das leere Abfrageergebnis gemäß FR-035
- Alternative zu FR-064 für den Fall fehlender Daten

## Anmerkungen
Keine.
