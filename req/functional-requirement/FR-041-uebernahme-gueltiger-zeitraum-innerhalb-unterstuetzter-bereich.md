# FR-041: Übernahme eines gültigen Zeitraums innerhalb des unterstützten Zeitfensters

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-011: Zeitraum für die Wetterdatenabfrage auswählen

## Beschreibung
Wenn ein Zeitraum mit Start- und Enddatum innerhalb von 01.01.2015 bis 31.12.2025 und Startdatum vor oder gleich Enddatum bestätigt wird, muss die Streamlit-Konfigurationsoberfläche den Zeitraum als Teil der Konfiguration übernehmen.

## Eingabe / Vorbedingungen
- Ein Start- und ein Enddatum wurden eingegeben oder ausgewählt, beide liegen innerhalb von 01.01.2015 bis 31.12.2025 (Grenzwerte eingeschlossen)
- Das Startdatum liegt vor oder ist identisch mit dem Enddatum
- Die Eingabe wurde bestätigt

## Verarbeitungslogik / Ablauf
1. Start- und Enddatum entgegennehmen.
2. Prüfen, ob beide Datumswerte innerhalb von 01.01.2015 bis 31.12.2025 liegen (Grenzwerte eingeschlossen).
3. Prüfen, ob das Startdatum vor oder gleich dem Enddatum liegt.
4. Bei positivem Ergebnis beider Prüfungen: Zeitraum als Teil der Konfiguration übernehmen.

## Ausgabe / Ergebnis
Der bestätigte Zeitraum ist als Teil der Konfiguration übernommen.

## Fehlerfälle / Randbedingungen
- Ablehnungsfälle (Zeitraum außerhalb des unterstützten Zeitfensters, Startdatum nach Enddatum) sind in FR-042 und FR-043 geregelt.

## Akzeptanzkriterien
- [ ] Bei Bestätigung eines Zeitraums mit Start- und Enddatum innerhalb von 01.01.2015 bis 31.12.2025 und Start vor oder gleich Ende wird der Zeitraum als Teil der Konfiguration übernommen
- [ ] Ein Zeitraum, dessen Start- und Enddatum exakt den Grenzwerten 01.01.2015 bzw. 31.12.2025 entsprechen, wird als gültig übernommen
- [ ] Ein Zeitraum mit identischem Start- und Enddatum wird als gültiger Einzeltag-Zeitraum übernommen

## Abhängigkeiten
- Liefert den Zeitraum als Eingangsgröße für US-013 (Konfiguration bestätigen und Datenabruf auslösen)

## Anmerkungen
Konkrete Eingabemethode (Kalenderauswahl, Textfelder) ist technische Designentscheidung und nicht Gegenstand dieses Functional Requirements.
