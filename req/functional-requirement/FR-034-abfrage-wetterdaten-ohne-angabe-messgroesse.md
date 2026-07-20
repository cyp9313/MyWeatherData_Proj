# FR-034: Abfrage gespeicherter Wetterdaten ohne Angabe einer Messgröße

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-009: Gespeicherte Wetterdaten nach Station, Zeitraum und Messgröße abfragen

## Beschreibung
Wenn eine Abfrage mit Stations-ID und Zeitraum ohne Angabe einer Messgröße ausgeführt wird, muss die SQLite-Datenbank die Datensätze aller gespeicherten Messgrößen für diese Station und diesen Zeitraum zurückgeben.

## Eingabe / Vorbedingungen
- Für die angefragte Station sind Wetterdaten mehrerer Messgrößen für den angefragten Zeitraum in der SQLite-Datenbank gespeichert (siehe FR-025)
- Eine Abfrage mit Stations-ID und Zeitraum (Start-/Enddatum) ohne Angabe einer Messgröße liegt vor

## Verarbeitungslogik / Ablauf
1. Abfrageparameter Stations-ID und Zeitraum entgegennehmen.
2. Feststellen, dass keine Messgröße angegeben wurde.
3. Gespeicherte Datensätze der SQLite-Datenbank anhand der Stations-ID filtern.
4. Ergebnis zusätzlich auf den angefragten Zeitraum einschränken, ohne nach Messgröße zu filtern.
5. Gefilterte Datensätze aller gespeicherten Messgrößen zurückgeben.

## Ausgabe / Ergebnis
Es werden die Datensätze aller gespeicherten Messgrößen für die angefragte Station und den angefragten Zeitraum zurückgegeben.

## Fehlerfälle / Randbedingungen
- Keine Daten für die angefragte Kombination vorhanden: siehe FR-035
- Angefragte Stations-ID existiert nicht in der lokalen Datenbank: siehe FR-036

## Akzeptanzkriterien
- [ ] Bei einer Abfrage mit Stations-ID und Zeitraum ohne Angabe einer Messgröße werden die Datensätze aller gespeicherten Messgrößen für diese Station und diesen Zeitraum zurückgegeben

## Abhängigkeiten
- Setzt gespeicherte Wetterdaten gemäß FR-025 voraus
- Ergänzt FR-033 (Abfrage mit konkreter Messgröße)

## Anmerkungen
Keine.
