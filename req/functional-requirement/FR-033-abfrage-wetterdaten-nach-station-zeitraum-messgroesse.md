# FR-033: Abfrage gespeicherter Wetterdaten nach Station, Zeitraum und Messgröße

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-009: Gespeicherte Wetterdaten nach Station, Zeitraum und Messgröße abfragen

## Beschreibung
Wenn eine Abfrage mit Stations-ID, Zeitraum und einer konkreten Messgröße ausgeführt wird, muss die SQLite-Datenbank genau die Datensätze zurückgeben, die zu dieser Station, diesem Zeitraum und dieser Messgröße gehören.

## Eingabe / Vorbedingungen
- Für die angefragte Station sind Wetterdaten mehrerer Messgrößen und Zeiträume in der SQLite-Datenbank gespeichert (siehe FR-025)
- Eine Abfrage mit Stations-ID, Zeitraum (Start-/Enddatum) und genau einer Messgröße (Lufttemperatur, Niederschlag, Wind oder Sonneneinstrahlung) liegt vor

## Verarbeitungslogik / Ablauf
1. Abfrageparameter Stations-ID, Zeitraum und Messgröße entgegennehmen.
2. Gespeicherte Datensätze der SQLite-Datenbank anhand der Stations-ID filtern.
3. Ergebnis zusätzlich auf den angefragten Zeitraum einschränken.
4. Ergebnis zusätzlich auf die angefragte Messgröße einschränken.
5. Gefilterte Datensätze zurückgeben.

## Ausgabe / Ergebnis
Es werden genau die Datensätze zurückgegeben, die zur angefragten Station, zum angefragten Zeitraum und zur angefragten Messgröße gehören.

## Fehlerfälle / Randbedingungen
- Keine Daten für die angefragte Kombination vorhanden: siehe FR-035
- Angefragte Stations-ID existiert nicht in der lokalen Datenbank: siehe FR-036

## Akzeptanzkriterien
- [ ] Bei einer Abfrage mit Stations-ID, Zeitraum und einer konkreten Messgröße werden ausschließlich die Datensätze zurückgegeben, die zu dieser Station, diesem Zeitraum und dieser Messgröße gehören

## Abhängigkeiten
- Setzt gespeicherte Wetterdaten gemäß FR-025 voraus
- Ergänzt durch FR-034 (Abfrage ohne Messgrößenangabe), FR-035 (leeres Ergebnis) und FR-036 (unbekannte Stations-ID)

## Anmerkungen
Keine.
