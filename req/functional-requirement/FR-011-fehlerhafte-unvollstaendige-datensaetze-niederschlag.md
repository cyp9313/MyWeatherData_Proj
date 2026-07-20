# FR-011: Umgang mit fehlerhaften oder unvollständigen Datensätzen beim Import der Niederschlagsdaten

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-003: Niederschlagsdaten importieren

## Beschreibung
Wenn beim Import der Niederschlagsdaten fehlerhafte oder unvollständige Datensätze erkannt werden (z. B. Formatfehler, fehlende Pflichtfelder), muss der Import-Client die betroffenen Datensätze als fehlerhaft markieren bzw. überspringen und den restlichen Import fortsetzen, ohne dass die App abstürzt.

## Eingabe / Vorbedingungen
- Import der Niederschlagsdaten wurde ausgelöst
- Rohdatendatei enthält mindestens einen Datensatz mit Formatfehler oder fehlendem Pflichtfeld

## Verarbeitungslogik / Ablauf
1. Rohdaten datensatzweise parsen.
2. Jeden Datensatz auf Formatfehler und Vollständigkeit der Pflichtfelder prüfen.
3. Fehlerhafte oder unvollständige Datensätze als fehlerhaft markieren bzw. überspringen.
4. Import der übrigen, korrekten Datensätze fortsetzen.
5. Sicherstellen, dass die App bei erkannten Fehlern nicht abstürzt.

## Ausgabe / Ergebnis
Vollständiger Import der korrekten Datensätze; fehlerhafte bzw. unvollständige Datensätze sind markiert oder übersprungen und im Ergebnis nicht enthalten.

## Fehlerfälle / Randbedingungen
- Formatfehler in einem Datensatz: Datensatz als fehlerhaft markieren bzw. überspringen, restlichen Import fortsetzen
- Fehlende Pflichtfelder in einem Datensatz: Datensatz als fehlerhaft markieren bzw. überspringen, restlichen Import fortsetzen

## Akzeptanzkriterien
- [ ] Datensätze mit Formatfehlern oder fehlenden Pflichtfeldern werden erkannt und als fehlerhaft markiert bzw. übersprungen
- [ ] Der restliche Import wird trotz fehlerhafter Datensätze fortgesetzt
- [ ] Die App stürzt bei fehlerhaften Datensätzen nicht ab

## Abhängigkeiten
- FR-009: Import der Niederschlagsdaten für gültigen Zeitraum
- Format- und Feldbeschreibung: [BESCHREIBUNG_obsgermany-climate-10min-precipitation_de.md](../../doc/DWD/md/BESCHREIBUNG_obsgermany-climate-10min-precipitation_de.md)

## Anmerkungen
Keine.
