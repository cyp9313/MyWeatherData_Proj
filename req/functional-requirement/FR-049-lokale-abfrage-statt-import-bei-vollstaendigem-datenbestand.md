# FR-049: Lokale Abfrage statt erneutem Import bei vollständig vorhandenem Datenbestand

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-013: Konfiguration bestätigen und Datenabruf auslösen

## Beschreibung
Solange für die gesamte bestätigte Konfiguration bereits alle Daten in der SQLite-Datenbank vorliegen, wenn die Konfiguration bestätigt wird, muss die Streamlit-Konfigurationsoberfläche die Daten aus der SQLite-Datenbank abfragen, ohne einen erneuten Import beim DWD auszulösen.

## Eingabe / Vorbedingungen
- Für die gesamte bestätigte Konfiguration (Ort, Zeitraum, alle ausgewählten Messgrößen) liegen bereits alle Daten in der SQLite-Datenbank vor (siehe FR-025)
- Die Konfiguration wird bestätigt

## Verarbeitungslogik / Ablauf
1. Bestätigte Konfiguration entgegennehmen.
2. Prüfen, ob für die gesamte Konfiguration bereits alle Daten in der SQLite-Datenbank vorliegen (siehe FR-033/FR-034).
3. Bei positivem Ergebnis: Abfrage der SQLite-Datenbank für die Konfiguration auslösen.
4. Keinen Import beim DWD auslösen.

## Ausgabe / Ergebnis
Die Daten werden ausschließlich aus der SQLite-Datenbank abgefragt, es wird kein Import beim DWD ausgelöst.

## Fehlerfälle / Randbedingungen
- Für Teile der Konfiguration liegen noch keine Daten lokal vor: kein Anwendungsfall dieses Requirements, stattdessen Import gemäß FR-046/EPIC-001

## Akzeptanzkriterien
- [ ] Wenn für die gesamte bestätigte Konfiguration bereits alle Daten lokal vorliegen, werden bei Bestätigung die Daten aus der SQLite-Datenbank abgefragt
- [ ] In diesem Fall wird kein erneuter Import beim DWD ausgelöst

## Abhängigkeiten
- Setzt gespeicherte Daten gemäß FR-025 voraus und nutzt die Abfrage gemäß FR-033/FR-034
- Ergänzt FR-046 um den Sonderfall eines vollständig vorhandenen lokalen Datenbestands

## Anmerkungen
Keine.
