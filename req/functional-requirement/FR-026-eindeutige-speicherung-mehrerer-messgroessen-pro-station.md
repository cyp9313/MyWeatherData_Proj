# FR-026: Eindeutige Speicherung mehrerer Messgrößen pro Station

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-007: Wetterdaten dauerhaft lokal speichern

## Beschreibung
Die SQLite-Datenbank muss Messwerte unterschiedlicher Messgrößen (Lufttemperatur, Niederschlag, Wind, Sonneneinstrahlung) derselben Station eindeutig unterscheidbar und einzeln abrufbar speichern.

## Eingabe / Vorbedingungen
- Importierte Datensätze mehrerer Messgrößen für dieselbe Station liegen vor (siehe FR-025)

## Verarbeitungslogik / Ablauf
1. Jeden Datensatz eindeutig einer Messgröße, einer Station und einem Zeitstempel zuordnen.
2. Zuordnung so speichern, dass jede Messgröße unabhängig von den anderen identifiziert werden kann.
3. Abruf einzelner Messgrößen ermöglichen, ohne Daten anderer Messgrößen einzubeziehen.

## Ausgabe / Ergebnis
Für dieselbe Station gespeicherte Daten je Messgröße sind eindeutig unterscheidbar und können einzeln abgerufen werden.

## Fehlerfälle / Randbedingungen
- Keine (strukturelle Anforderung an das Datenmodell der SQLite-Datenbank)

## Akzeptanzkriterien
- [ ] Für eine Station mit gespeicherten Daten mehrerer Messgrößen kann jede Messgröße einzeln und eindeutig abgerufen werden
- [ ] Daten unterschiedlicher Messgrößen derselben Station werden nicht vermischt

## Abhängigkeiten
- Baut auf FR-025 (Speicherung importierter Wetterdaten) auf
- Grundlage für US-009 (Abfrage gespeicherter Daten nach Messgröße)

## Anmerkungen
Konkretes Schema (z. B. gemeinsame Messwerttabelle mit Messgrößen-Spalte oder separate Tabellen je Messgröße) ist technische Designentscheidung und nicht Gegenstand dieses Functional Requirements.
