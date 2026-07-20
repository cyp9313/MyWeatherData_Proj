# FR-023: Vollständigkeit der CSV-Datei beim Export des gesamten unterstützten Bereichs

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-006: Wetterdaten als CSV exportieren

## Beschreibung
Wenn der Export für einen Zeitraum ausgelöst wird, der den gesamten unterstützten Bereich (01.01.2015–31.12.2025) umfasst, muss das CSV-Export-Modul die erzeugte CSV-Datei mit genau einem Datensatz je vorhandenem Zeitstempel des gesamten Zeitraums befüllen.

## Eingabe / Vorbedingungen
- Vom Nutzer gewählter Exportzeitraum entspricht genau dem gesamten unterstützten Bereich 01.01.2015–31.12.2025
- Für diesen Zeitraum liegen importierte Wetterdaten in der SQLite-Datenbank vor

## Verarbeitungslogik / Ablauf
1. Gewählten Exportzeitraum entgegennehmen.
2. Prüfen, dass der Zeitraum genau dem gesamten unterstützten Bereich 01.01.2015–31.12.2025 entspricht.
3. Alle für den gesamten Zeitraum vorhandenen Zeitstempel aus der SQLite-Datenbank lesen.
4. Für jeden vorhandenen Zeitstempel genau einen Datensatz in die CSV-Datei aufnehmen.

## Ausgabe / Ergebnis
Eine CSV-Datei, die für den gesamten unterstützten Bereich (01.01.2015–31.12.2025) genau einen Datensatz je vorhandenem Zeitstempel enthält.

## Fehlerfälle / Randbedingungen
- Keine (Sonderfall des Exports ohne abweichendes Fehlerverhalten gegenüber FR-021)

## Akzeptanzkriterien
- [ ] Bei einem Export über den gesamten unterstützten Bereich (01.01.2015–31.12.2025) enthält die CSV-Datei genau einen Datensatz je vorhandenem Zeitstempel
- [ ] Es entstehen keine doppelten oder fehlenden Datensätze für vorhandene Zeitstempel innerhalb des Bereichs

## Abhängigkeiten
- FR-021: CSV-Export bei vorhandenen Wetterdaten im gewählten Zeitraum

## Anmerkungen
Keine.
