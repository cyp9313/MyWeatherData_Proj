# FR-030: Ergänzung fehlender Zeitpunkte bei teilweiser Überschneidung mit bereits gespeicherten Daten

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-008: Duplikate bei wiederholtem Import vermeiden

## Beschreibung
Wenn ein Import für einen Zeitraum ausgeführt wird, der sich für dieselbe Station und Messgröße teilweise mit bereits in der SQLite-Datenbank gespeicherten Zeitpunkten überschneidet, muss der Import-Client ausschließlich die in der SQLite-Datenbank fehlenden Zeitpunkte als neue Datensätze speichern.

## Eingabe / Vorbedingungen
- Für eine Station und Messgröße sind Datensätze für einen Teil eines angeforderten Zeitraums bereits in der SQLite-Datenbank gespeichert
- Ein Import wird für einen Zeitraum ausgelöst, der sich teilweise mit den bereits gespeicherten Zeitpunkten überschneidet

## Verarbeitungslogik / Ablauf
1. Für jeden Zeitpunkt im angeforderten Zeitraum prüfen, ob für die Kombination aus Station und Messgröße bereits ein Datensatz in der SQLite-Datenbank existiert (siehe FR-029).
2. Datensätze zu bereits vorhandenen Zeitpunkten unverändert lassen und nicht erneut schreiben.
3. Datensätze zu den in der SQLite-Datenbank fehlenden Zeitpunkten als neue Datensätze speichern.

## Ausgabe / Ergebnis
Nach dem Import sind alle Zeitpunkte des angeforderten Zeitraums für die Station und Messgröße in der SQLite-Datenbank vorhanden; zuvor bereits gespeicherte Datensätze innerhalb des überschneidenden Zeitraums bleiben unverändert.

## Fehlerfälle / Randbedingungen
- Bereits gespeicherte Datensätze innerhalb des überschneidenden Zeitraums dürfen durch den Import nicht überschrieben oder verändert werden (siehe FR-029)

## Akzeptanzkriterien
- [ ] Bei teilweiser Überschneidung eines importierten Zeitraums mit bereits gespeicherten Daten werden ausschließlich die zuvor fehlenden Zeitpunkte als neue Datensätze ergänzt
- [ ] Bereits gespeicherte Datensätze innerhalb des überschneidenden Zeitraums bleiben nach dem Import unverändert

## Abhängigkeiten
- Setzt FR-029 (Duplikatvermeidung bei identischer Kombination aus Station, Messgröße und Zeitstempel) voraus
- Baut auf FR-025 (Speicherung importierter Wetterdaten) auf

## Anmerkungen
Keine.
