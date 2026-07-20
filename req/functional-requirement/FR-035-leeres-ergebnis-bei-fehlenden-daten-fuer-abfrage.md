# FR-035: Leeres Ergebnis bei fehlenden Daten für die angefragte Kombination

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-009: Gespeicherte Wetterdaten nach Station, Zeitraum und Messgröße abfragen

## Beschreibung
Wenn für die angefragte Kombination aus Station, Zeitraum und Messgröße keine gespeicherten Daten vorhanden sind, muss die SQLite-Datenbank ein leeres Ergebnis zurückgeben, ohne dass ein Fehler ausgelöst wird.

## Eingabe / Vorbedingungen
- Eine Abfrage mit Stations-ID, Zeitraum und optional einer Messgröße liegt vor
- Für die angefragte Kombination aus Station, Zeitraum und Messgröße sind keine Datensätze in der SQLite-Datenbank gespeichert

## Verarbeitungslogik / Ablauf
1. Abfrage anhand von Stations-ID, Zeitraum und optionaler Messgröße ausführen.
2. Feststellen, dass kein Datensatz die Abfragekriterien erfüllt.
3. Leeres Ergebnis zurückgeben.
4. Keine Fehlermeldung oder Ausnahme auslösen.

## Ausgabe / Ergebnis
Ein leeres Ergebnis wird zurückgegeben; kein Fehler wird ausgelöst.

## Fehlerfälle / Randbedingungen
- Keine gespeicherten Daten für die angefragte Kombination aus Station, Zeitraum und Messgröße: leeres Ergebnis zurückgeben statt Fehler

## Akzeptanzkriterien
- [ ] Bei einer Abfrage ohne passende gespeicherte Daten wird ein leeres Ergebnis zurückgegeben
- [ ] Es wird in diesem Fall kein Fehler ausgelöst

## Abhängigkeiten
- Ergänzt FR-033 und FR-034 um den Fall fehlender Daten

## Anmerkungen
Keine.
