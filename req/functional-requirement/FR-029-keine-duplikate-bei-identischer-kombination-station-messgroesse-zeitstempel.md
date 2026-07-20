# FR-029: Keine Duplikate bei wiederholtem Import derselben Kombination aus Station, Messgröße und Zeitstempel

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-008: Duplikate bei wiederholtem Import vermeiden

## Beschreibung
Wenn der Import-Client einen Datensatz importiert, für dessen Kombination aus Station, Messgröße und Zeitstempel in der SQLite-Datenbank bereits ein Datensatz existiert, darf der Import-Client keinen zusätzlichen Datensatz für diese Kombination speichern.

## Eingabe / Vorbedingungen
- In der SQLite-Datenbank ist bereits ein Datensatz für eine bestimmte Kombination aus Station, Messgröße und Zeitstempel gespeichert (siehe FR-025, FR-026)
- Der Import-Client importiert einen Datensatz mit identischer Kombination aus Station, Messgröße und Zeitstempel

## Verarbeitungslogik / Ablauf
1. Vor dem Speichern jedes importierten Datensatzes prüfen, ob in der SQLite-Datenbank bereits ein Datensatz mit derselben Kombination aus Station, Messgröße und Zeitstempel existiert.
2. Falls ein solcher Datensatz bereits existiert, den importierten Datensatz verwerfen und keinen neuen Datensatz anlegen.
3. Diese Prüfung für jeden importierten Datensatz unabhängig davon anwenden, wie oft oder wie häufig hintereinander der Import für dieselbe Kombination ausgelöst wurde.

## Ausgabe / Ergebnis
Für jede Kombination aus Station, Messgröße und Zeitstempel existiert nach beliebig vielen wiederholten Importen genau ein Datensatz in der SQLite-Datenbank.

## Fehlerfälle / Randbedingungen
- Keine (Regel gilt unabhängig von Fehlerfällen beim Schreibvorgang; Schreibfehler siehe FR-028)

## Akzeptanzkriterien
- [ ] Nach erneutem Import eines bereits vollständig gespeicherten Zeitraums für dieselbe Station und Messgröße bleibt die Anzahl der gespeicherten Datensätze für diese Kombination unverändert
- [ ] Nach zwei nacheinander ausgelösten Importvorgängen für dieselbe Station, denselben Zeitraum und dieselbe Messgröße existieren die Datensätze dieses Zeitraums danach nur einmal in der SQLite-Datenbank

## Abhängigkeiten
- Baut auf FR-025 (Speicherung importierter Wetterdaten) und FR-026 (eindeutige Speicherung je Messgröße) auf
- Grundlage für FR-030 (Ergänzung fehlender Zeitpunkte), FR-031 (getrennte Speicherung unterschiedlicher Stationen) und FR-032 (Aktualisierung bei abweichendem Wert)

## Anmerkungen
Der Umgang mit inhaltlich abweichenden Werten für denselben Zeitpunkt (z. B. nachträglich korrigierte DWD-Daten) ist nicht Gegenstand dieses Functional Requirements, siehe FR-032 (Aktualisierung bei abweichendem, zeitlich neuerem Wert).
