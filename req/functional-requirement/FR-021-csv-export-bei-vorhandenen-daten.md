# FR-021: CSV-Export bei vorhandenen Wetterdaten im gewählten Zeitraum

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-006: Wetterdaten als CSV exportieren

## Beschreibung
Wenn der Export für einen Zeitraum ausgelöst wird, für den importierte Wetterdaten in der SQLite-Datenbank vorliegen, muss das CSV-Export-Modul eine CSV-Datei erzeugen, die je Zeitstempel die zugehörigen Messwerte des Zeitraums in getrennten Spalten enthält.

## Eingabe / Vorbedingungen
- Vom Nutzer gewählter Start- und Endzeitpunkt des Exportzeitraums
- Für den gewählten Zeitraum liegen importierte/aufbereitete Wetterdaten (Lufttemperatur, Niederschlag, Wind und/oder Sonneneinstrahlung) in der SQLite-Datenbank vor

## Verarbeitungslogik / Ablauf
1. Gewählten Exportzeitraum entgegennehmen.
2. Für den Zeitraum vorhandene Wetterdaten aus der SQLite-Datenbank lesen.
3. Prüfen, dass für den Zeitraum mindestens ein Datensatz vorliegt.
4. Messwerte je Zeitstempel zusammenführen, sodass jede Messgröße in einer eigenen Spalte steht.
5. CSV-Datei aus den zusammengeführten Daten erzeugen.

## Ausgabe / Ergebnis
Eine CSV-Datei, die je Zeitstempel des gewählten Zeitraums einen Datensatz mit den zugehörigen Messwerten in getrennten Spalten enthält.

## Fehlerfälle / Randbedingungen
- Für den gewählten Zeitraum liegen keine Daten vor: siehe FR-022
- Zeitraum umfasst den gesamten unterstützten Bereich: siehe FR-023
- Start- oder Enddatum außerhalb des unterstützten Bereichs: siehe FR-024

## Akzeptanzkriterien
- [ ] Für einen Zeitraum mit vorhandenen Wetterdaten wird beim Auslösen des Exports eine CSV-Datei erzeugt
- [ ] Die CSV-Datei enthält je Zeitstempel genau einen Datensatz
- [ ] Die Messwerte je Zeitstempel stehen in getrennten Spalten

## Abhängigkeiten
- Setzt voraus, dass Wetterdaten gemäß US-007 (Wetterdaten lokal speichern) in der SQLite-Datenbank gespeichert sind
- FR-005, FR-009, FR-013, FR-017: Import der jeweiligen Messgrößen als Datenquelle für den Export

## Anmerkungen
Performance-Aspekte bei sehr großen Exportzeiträumen sind bei Bedarf in einem separaten Functional Requirement zu konkretisieren.
