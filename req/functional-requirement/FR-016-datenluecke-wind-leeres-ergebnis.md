# FR-016: Rückgabe eines leeren Ergebnisses bei Datenlücke der Winddaten

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-004: Winddaten importieren

## Beschreibung
Wenn für einen gültigen Zeitraum keine Wind-Messwerte der Station vorliegen (Datenlücke), muss der Import-Client ein leeres Ergebnis mit einem Hinweis auf die fehlenden Daten zurückgeben, statt einen Fehler zu melden.

## Eingabe / Vorbedingungen
- Gültige Stations-ID
- Zeitraum vollständig innerhalb 01.01.2015–31.12.2025
- Für den angegebenen Zeitraum sind keine Messwerte der Station aufgezeichnet (Datenlücke)

## Verarbeitungslogik / Ablauf
1. Stations-ID und Zeitraum entgegennehmen.
2. Import der Rohdaten für den angegebenen Zeitraum versuchen.
3. Erkennen, dass für den Zeitraum keine Messwerte der Station vorliegen.
4. Leeres Ergebnis zurückgeben.
5. Hinweis auf die fehlenden Daten für den angefragten Zeitraum ausgeben.

## Ausgabe / Ergebnis
Leeres Ergebnis für den angefragten Zeitraum, zusammen mit einem Hinweis auf die fehlenden Daten.

## Fehlerfälle / Randbedingungen
- Keine Messwerte der Station im gültigen Zeitraum vorhanden (Datenlücke): leeres Ergebnis mit Hinweis zurückgeben, kein Fehler

## Akzeptanzkriterien
- [ ] Bei einer Datenlücke im gültigen Zeitraum wird kein Fehler ausgelöst
- [ ] Es wird ein leeres Ergebnis mit einem Hinweis auf die fehlenden Daten zurückgegeben

## Abhängigkeiten
- FR-013: Import der Winddaten für gültigen Zeitraum

## Anmerkungen
Keine.
