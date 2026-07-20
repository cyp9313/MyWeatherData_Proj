# FR-057: Hinweis bei fehlenden Niederschlagsdaten für die Visualisierung

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-015: Verlauf des Niederschlags visualisieren

## Beschreibung
Wenn für den gewählten Ort und Zeitraum keine Niederschlagsdaten vorliegen, muss die Streamlit-Oberfläche anstelle eines Diagramms einen Hinweis anzeigen, dass keine Daten verfügbar sind.

## Eingabe / Vorbedingungen
- Für den gewählten Ort und Zeitraum sind keine Niederschlagsdaten in der SQLite-Datenbank gespeichert (siehe FR-035)
- Der Aufruf der Visualisierung wird ausgelöst

## Verarbeitungslogik / Ablauf
1. Niederschlagsdaten für den gewählten Ort und Zeitraum aus der SQLite-Datenbank abfragen.
2. Feststellen, dass die Abfrage ein leeres Ergebnis liefert.
3. Anstelle eines Diagramms einen Hinweistext anzeigen, dass keine Daten verfügbar sind.

## Ausgabe / Ergebnis
Ein Hinweis, dass keine Daten verfügbar sind, wird anstelle eines Diagramms angezeigt.

## Fehlerfälle / Randbedingungen
- Leeres Abfrageergebnis für die angefragte Kombination aus Ort, Zeitraum und Messgröße (siehe FR-035): Hinweis statt Diagramm anzeigen

## Akzeptanzkriterien
- [ ] Bei fehlenden Niederschlagsdaten für den gewählten Ort und Zeitraum wird anstelle eines Diagramms ein Hinweis angezeigt, dass keine Daten verfügbar sind

## Abhängigkeiten
- Nutzt das leere Abfrageergebnis gemäß FR-035
- Alternative zu FR-055 für den Fall fehlender Daten

## Anmerkungen
Keine.
