# US-010: Ort/Koordinate für die Wetterdatenabfrage auswählen

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-003: User Interface zur Konfiguration von Ort, Zeitraum und Daten

## User Story
Als **Nutzer:in der App**
möchte ich **einen Ort bzw. eine Koordinate innerhalb Deutschlands in der Konfigurationsoberfläche eingeben oder auswählen können**,
damit **ich festlegen kann, für welchen Standort ich Wetterdaten sehen möchte**.

## Beschreibung / Kontext
Die ausgewählte Koordinate ist die Eingangsgröße für die Ermittlung der nächstgelegenen DWD-Station (siehe US-001) und damit für den weiteren Datenabruf. Die Oberfläche muss die Eingabe entgegennehmen und auf Gültigkeit prüfen, bevor sie als Teil der Konfiguration übernommen wird.

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** eine gültige Koordinate innerhalb Deutschlands wird eingegeben
   **Wenn** die Eingabe bestätigt wird
   **Dann** wird die Koordinate als Ort für die Konfiguration übernommen und dem Nutzer zur Kontrolle angezeigt

2. **Gegeben** eine Koordinate außerhalb Deutschlands wird eingegeben
   **Wenn** die Eingabe bestätigt wird
   **Dann** wird die Koordinate abgelehnt und ein Hinweis angezeigt, dass der Ort außerhalb des unterstützten Gebiets liegt

3. **Gegeben** ein ungültiges Eingabeformat (z. B. Text statt Zahlenwert) für die Koordinate
   **Wenn** die Eingabe bestätigt wird
   **Dann** wird die Eingabe abgelehnt und ein Hinweis auf das erwartete Format angezeigt

4. **Gegeben** keine Koordinate wurde eingegeben oder ausgewählt
   **Wenn** die Konfiguration ohne Ortsangabe bestätigt werden soll
   **Dann** wird die Bestätigung verhindert und ein Hinweis angezeigt, dass ein Ort erforderlich ist

## Zugehörige Functional Requirements
- [ ] FR-037: Übernahme einer gültigen Koordinate innerhalb Deutschlands
- [ ] FR-038: Ablehnung einer Koordinate außerhalb Deutschlands in der Konfigurationsoberfläche
- [ ] FR-039: Ablehnung eines ungültigen Eingabeformats für die Koordinate
- [ ] FR-040: Verhinderung der Bestätigung ohne Ortsangabe

## Abhängigkeiten
- Liefert die Koordinate als Eingangsgröße für US-001 (nächstgelegene Wetterstation ermitteln) und für US-013 (Konfiguration bestätigen und Datenabruf auslösen)

## Anmerkungen
Konkrete Eingabemethode (Texteingabe von Koordinaten, Kartenauswahl, Adresssuche) ist technische Designentscheidung und in den zugehörigen Functional Requirements zu konkretisieren.
