# FR-043: Ablehnung eines Zeitraums mit Startdatum nach Enddatum

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-011: Zeitraum für die Wetterdatenabfrage auswählen

## Beschreibung
Wenn ein Startdatum bestätigt wird, das nach dem Enddatum liegt, muss die Streamlit-Konfigurationsoberfläche den Zeitraum ablehnen und einen Hinweis anzeigen, dass das Startdatum nicht nach dem Enddatum liegen darf.

## Eingabe / Vorbedingungen
- Ein Start- und ein Enddatum wurden eingegeben oder ausgewählt
- Das Startdatum liegt nach dem Enddatum
- Die Eingabe wurde bestätigt

## Verarbeitungslogik / Ablauf
1. Start- und Enddatum entgegennehmen.
2. Prüfen, ob das Startdatum nach dem Enddatum liegt.
3. Bei positivem Ergebnis: Zeitraum ablehnen, nicht als Teil der Konfiguration übernehmen.
4. Hinweis anzeigen, dass das Startdatum nicht nach dem Enddatum liegen darf.

## Ausgabe / Ergebnis
Der Zeitraum wird abgelehnt, ein Hinweistext zur ungültigen Reihenfolge von Start- und Enddatum wird angezeigt.

## Fehlerfälle / Randbedingungen
- Startdatum liegt nach dem Enddatum: Ablehnung des Zeitraums und Anzeige eines Hinweises, dass das Startdatum nicht nach dem Enddatum liegen darf

## Akzeptanzkriterien
- [ ] Bei Bestätigung eines Zeitraums mit einem Startdatum nach dem Enddatum wird der Zeitraum abgelehnt
- [ ] Ein Hinweis wird angezeigt, dass das Startdatum nicht nach dem Enddatum liegen darf

## Abhängigkeiten
- Die Prüfung auf die Reihenfolge von Start- und Enddatum ist unabhängig von der Prüfung auf das zulässige Zeitfenster (FR-042)

## Anmerkungen
Ein Zeitraum mit identischem Start- und Enddatum gilt nicht als "Startdatum nach Enddatum" und wird gemäß FR-041 übernommen.
