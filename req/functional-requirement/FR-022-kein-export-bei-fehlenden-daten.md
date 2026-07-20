# FR-022: Kein CSV-Export bei fehlenden Daten für den gewählten Zeitraum

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-006: Wetterdaten als CSV exportieren

## Beschreibung
Wenn der Export für einen Zeitraum ausgelöst wird, für den keine importierten Wetterdaten in der SQLite-Datenbank vorliegen, muss das CSV-Export-Modul keine CSV-Datei erzeugen und stattdessen einen Hinweis ausgeben, dass für den gewählten Zeitraum keine Daten vorhanden sind.

## Eingabe / Vorbedingungen
- Vom Nutzer gewählter Start- und Endzeitpunkt des Exportzeitraums
- Für den gewählten Zeitraum liegen keine importierten Wetterdaten in der SQLite-Datenbank vor

## Verarbeitungslogik / Ablauf
1. Gewählten Exportzeitraum entgegennehmen.
2. Prüfen, ob für den Zeitraum Wetterdaten in der SQLite-Datenbank vorliegen.
3. Erkennen, dass für den Zeitraum keine Datensätze vorliegen.
4. Erzeugung der CSV-Datei unterlassen.
5. Hinweis ausgeben, dass für den gewählten Zeitraum keine Daten vorhanden sind.

## Ausgabe / Ergebnis
Kein Dateiexport; stattdessen ein Hinweis, dass für den gewählten Zeitraum keine Daten vorhanden sind.

## Fehlerfälle / Randbedingungen
- Keine Wetterdaten für den gewählten Zeitraum vorhanden: keine CSV-Datei erzeugen, Hinweis ausgeben

## Akzeptanzkriterien
- [ ] Bei einem Zeitraum ohne vorhandene Daten wird keine CSV-Datei erzeugt
- [ ] Es wird ein Hinweis ausgegeben, dass für den gewählten Zeitraum keine Daten vorhanden sind

## Abhängigkeiten
- FR-021: CSV-Export bei vorhandenen Wetterdaten im gewählten Zeitraum

## Anmerkungen
Keine.
