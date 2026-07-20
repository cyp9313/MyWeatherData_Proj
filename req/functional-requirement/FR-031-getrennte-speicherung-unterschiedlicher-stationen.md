# FR-031: Getrennte Speicherung unterschiedlicher Stationen bei gleichem Zeitraum und gleicher Messgröße

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-008: Duplikate bei wiederholtem Import vermeiden

## Beschreibung
Wenn Wetterdaten für eine Station importiert werden und in der SQLite-Datenbank bereits Datensätze einer anderen Station für denselben Zeitraum und dieselbe Messgröße existieren, muss der Import-Client die importierten Daten als eigenständige, neue Datensätze speichern.

## Eingabe / Vorbedingungen
- Für Station A sind für einen Zeitraum und eine Messgröße bereits Datensätze in der SQLite-Datenbank gespeichert
- Ein Import liefert Datensätze für Station B im selben Zeitraum und derselben Messgröße

## Verarbeitungslogik / Ablauf
1. Prüfen, ob für den importierten Datensatz von Station B bereits ein Datensatz mit identischer Kombination aus Station, Messgröße und Zeitstempel existiert (siehe FR-029).
2. Da die Stations-ID von der bereits gespeicherten Station A abweicht, den vorhandenen Datensatz nicht als Duplikat werten.
3. Datensätze von Station B unabhängig von den Datensätzen der Station A als neue Datensätze in der SQLite-Datenbank speichern.

## Ausgabe / Ergebnis
Datensätze der Station B sind zusätzlich zu den bereits gespeicherten Datensätzen der Station A in der SQLite-Datenbank vorhanden; beide Stationen sind unabhängig voneinander abrufbar.

## Fehlerfälle / Randbedingungen
- Keine (strukturelle Anforderung an den Umfang der Eindeutigkeitsprüfung; Schreibfehler siehe FR-028)

## Akzeptanzkriterien
- [ ] Beim Import von Daten einer Station für einen Zeitraum und eine Messgröße, für die bereits Daten einer anderen Station gespeichert sind, werden die Daten der neuen Station zusätzlich gespeichert
- [ ] Datensätze unterschiedlicher Stationen für denselben Zeitraum und dieselbe Messgröße existieren unabhängig voneinander in der SQLite-Datenbank

## Abhängigkeiten
- Baut auf FR-029 (Duplikatvermeidung bei identischer Kombination) und FR-026 (eindeutige Speicherung je Messgröße) auf

## Anmerkungen
Keine.
