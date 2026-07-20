# FR-046: Auslösung des Datenabrufs bei vollständiger und gültiger Konfiguration

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-013: Konfiguration bestätigen und Datenabruf auslösen

## Beschreibung
Wenn eine vollständige und gültige Konfiguration aus Ort, Zeitraum und mindestens einer Messgröße bestätigt wird, muss die Streamlit-Konfigurationsoberfläche den Datenabruf (Import fehlender Daten oder Abfrage der lokalen Datenbank) für genau diese Konfiguration auslösen.

## Eingabe / Vorbedingungen
- Eine gültige Koordinate liegt vor (siehe FR-037)
- Ein gültiger Zeitraum liegt vor (siehe FR-041)
- Mindestens eine Messgröße ist ausgewählt (siehe FR-044)
- Die Bestätigung der Konfiguration wird ausgelöst

## Verarbeitungslogik / Ablauf
1. Bestätigung der Konfiguration entgegennehmen.
2. Prüfen, dass Ort, Zeitraum und mindestens eine Messgröße vollständig und gültig vorliegen.
3. Konfiguration aus Ort, Zeitraum und Messgrößen für den Datenabruf übernehmen.
4. Datenabruf (Import bzw. Abfrage der lokalen Datenbank) für genau diese Konfiguration auslösen.

## Ausgabe / Ergebnis
Der Datenabruf für genau die bestätigte Konfiguration aus Ort, Zeitraum und Messgrößen wird ausgelöst.

## Fehlerfälle / Randbedingungen
- Unvollständige Konfiguration bei Bestätigungsversuch: siehe FR-047
- Bereits laufender Datenabruf für dieselbe Konfiguration: siehe FR-048
- Alle Daten der Konfiguration bereits vollständig lokal vorhanden: siehe FR-049

## Akzeptanzkriterien
- [ ] Bei Bestätigung einer vollständigen und gültigen Konfiguration aus Ort, Zeitraum und mindestens einer Messgröße wird der Datenabruf für genau diese Konfiguration ausgelöst

## Abhängigkeiten
- Setzt gültige Angaben aus FR-037 (Ort), FR-041 (Zeitraum) und FR-044 (Messgrößen) voraus
- Löst je nach Datenlage den Import (EPIC-001) oder die Abfrage der lokalen Datenbank (FR-033/FR-034) aus

## Anmerkungen
Keine.
