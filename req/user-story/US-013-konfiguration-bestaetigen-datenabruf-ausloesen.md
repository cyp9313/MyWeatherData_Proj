# US-013: Konfiguration bestätigen und Datenabruf auslösen

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-003: User Interface zur Konfiguration von Ort, Zeitraum und Daten

## User Story
Als **Nutzer:in der App**
möchte ich **meine vollständige Konfiguration aus Ort, Zeitraum und Messgrößen bestätigen können**,
damit **die dazu passenden Wetterdaten geladen bzw. abgefragt werden, ohne dass ich weitere Schritte manuell anstoßen muss**.

## Beschreibung / Kontext
Diese Story bündelt die in US-010 (Ort), US-011 (Zeitraum) und US-012 (Messgrößen) erfassten Konfigurationsteile und löst darauf basierend entweder den Import fehlender Daten (EPIC-001) oder die Abfrage bereits lokal vorhandener Daten (US-009) aus.

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** eine vollständige und gültige Konfiguration aus Ort, Zeitraum und mindestens einer Messgröße
   **Wenn** die Konfiguration bestätigt wird
   **Dann** wird der Datenabruf (Import bzw. Abfrage der lokalen Datenbank) für genau diese Konfiguration ausgelöst

2. **Gegeben** eine unvollständige Konfiguration (z. B. fehlender Ort, fehlender Zeitraum oder keine Messgröße)
   **Wenn** versucht wird, die Konfiguration zu bestätigen
   **Dann** wird die Bestätigung verhindert und es werden alle fehlenden Angaben benannt

3. **Gegeben** ein Datenabruf für eine zuvor bestätigte Konfiguration läuft noch
   **Wenn** die Konfiguration erneut bestätigt wird
   **Dann** wird kein zweiter, paralleler Datenabruf ausgelöst, sondern ein Hinweis auf den laufenden Vorgang angezeigt

4. **Gegeben** für die gesamte bestätigte Konfiguration liegen bereits alle Daten lokal vor
   **Wenn** die Konfiguration bestätigt wird
   **Dann** werden die Daten aus der lokalen Datenbank abgefragt, ohne einen erneuten Import beim DWD auszulösen

## Zugehörige Functional Requirements
- [ ] FR-046: Auslösung des Datenabrufs bei vollständiger und gültiger Konfiguration
- [ ] FR-047: Verhinderung der Bestätigung bei unvollständiger Konfiguration
- [ ] FR-048: Verhinderung eines zweiten, parallelen Datenabrufs bei laufendem Vorgang
- [ ] FR-049: Lokale Abfrage statt erneutem Import bei vollständig vorhandenem Datenbestand

## Abhängigkeiten
- Setzt vollständige Angaben aus US-010 (Ort/Koordinate), US-011 (Zeitraum) und US-012 (Messgrößen) voraus
- Löst je nach Datenlage EPIC-001 (Import) oder US-009 (Abfrage der lokalen Datenbank) aus

## Anmerkungen
Keine.
