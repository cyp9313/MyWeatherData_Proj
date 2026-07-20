# FR-042: Ablehnung eines Zeitraums außerhalb des unterstützten Zeitfensters

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-011: Zeitraum für die Wetterdatenabfrage auswählen

## Beschreibung
Wenn ein Start- oder Enddatum außerhalb von 01.01.2015 bis 31.12.2025 bestätigt wird, muss die Streamlit-Konfigurationsoberfläche den Zeitraum ablehnen und einen Hinweis auf das zulässige Zeitfenster anzeigen.

## Eingabe / Vorbedingungen
- Ein Start- und ein Enddatum wurden eingegeben oder ausgewählt
- Mindestens eines der beiden Daten liegt außerhalb von 01.01.2015 bis 31.12.2025
- Die Eingabe wurde bestätigt

## Verarbeitungslogik / Ablauf
1. Start- und Enddatum entgegennehmen.
2. Prüfen, ob beide Datumswerte innerhalb von 01.01.2015 bis 31.12.2025 liegen.
3. Bei negativem Ergebnis: Zeitraum ablehnen, nicht als Teil der Konfiguration übernehmen.
4. Hinweis auf das zulässige Zeitfenster (01.01.2015–31.12.2025) anzeigen.

## Ausgabe / Ergebnis
Der Zeitraum wird abgelehnt, ein Hinweistext auf das zulässige Zeitfenster wird angezeigt.

## Fehlerfälle / Randbedingungen
- Start- oder Enddatum außerhalb von 01.01.2015 bis 31.12.2025: Ablehnung des Zeitraums und Anzeige eines Hinweises auf das zulässige Zeitfenster

## Akzeptanzkriterien
- [ ] Bei Bestätigung eines Zeitraums mit einem Start- oder Enddatum außerhalb von 01.01.2015 bis 31.12.2025 wird der Zeitraum abgelehnt
- [ ] Ein Hinweis auf das zulässige Zeitfenster wird angezeigt

## Abhängigkeiten
- Die Prüfung auf das zulässige Zeitfenster ist unabhängig von der Prüfung auf die Reihenfolge von Start- und Enddatum (FR-043)

## Anmerkungen
Keine.
