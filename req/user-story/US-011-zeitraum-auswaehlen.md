# US-011: Zeitraum für die Wetterdatenabfrage auswählen

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-003: User Interface zur Konfiguration von Ort, Zeitraum und Daten

## User Story
Als **Nutzer:in der App**
möchte ich **einen Zeitraum innerhalb von 01.01.2015 bis 31.12.2025 in der Konfigurationsoberfläche auswählen können**,
damit **ich festlege, für welchen Zeitraum ich historische Wetterdaten sehen möchte**.

## Beschreibung / Kontext
Der ausgewählte Zeitraum ist Teil der Konfiguration und wird für den Datenabruf (Import bzw. Abfrage der lokalen Datenbank) verwendet. Er muss vollständig innerhalb des unterstützten Zeitfensters 01.01.2015–31.12.2025 liegen und ein gültiges Intervall (Start vor oder gleich Ende) bilden.

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** ein Start- und Enddatum innerhalb von 01.01.2015 bis 31.12.2025 mit Start vor oder gleich Ende
   **Wenn** die Eingabe bestätigt wird
   **Dann** wird der Zeitraum als Teil der Konfiguration übernommen

2. **Gegeben** ein Start- oder Enddatum außerhalb von 01.01.2015 bis 31.12.2025
   **Wenn** die Eingabe bestätigt wird
   **Dann** wird der Zeitraum abgelehnt und ein Hinweis auf das zulässige Zeitfenster angezeigt

3. **Gegeben** ein Startdatum, das nach dem Enddatum liegt
   **Wenn** die Eingabe bestätigt wird
   **Dann** wird der Zeitraum abgelehnt und ein Hinweis angezeigt, dass das Startdatum nicht nach dem Enddatum liegen darf

4. **Gegeben** Start- und Enddatum entsprechen exakt den Grenzwerten 01.01.2015 bzw. 31.12.2025
   **Wenn** die Eingabe bestätigt wird
   **Dann** wird der Zeitraum als gültig übernommen

## Zugehörige Functional Requirements
- [ ] FR-041: Übernahme eines gültigen Zeitraums innerhalb des unterstützten Zeitfensters
- [ ] FR-042: Ablehnung eines Zeitraums außerhalb des unterstützten Zeitfensters
- [ ] FR-043: Ablehnung eines Zeitraums mit Startdatum nach Enddatum

## Abhängigkeiten
- Liefert den Zeitraum als Eingangsgröße für US-013 (Konfiguration bestätigen und Datenabruf auslösen)

## Anmerkungen
Konkrete Eingabemethode (Kalenderauswahl, Textfelder) ist technische Designentscheidung und in den zugehörigen Functional Requirements zu konkretisieren.
