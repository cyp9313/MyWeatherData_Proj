# FR-024: Kürzung des Exportzeitraums bei Überschreitung des unterstützten Bereichs

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-006: Wetterdaten als CSV exportieren

## Beschreibung
Wenn ein für den Export gewähltes Start- oder Enddatum außerhalb des unterstützten Bereichs (01.01.2015–31.12.2025) liegt, muss das CSV-Export-Modul den Exportzeitraum auf den unterstützten Bereich begrenzen und der Nutzerin/dem Nutzer einen Hinweis anzeigen, dass der Zeitraum gekürzt wurde.

## Eingabe / Vorbedingungen
- Vom Nutzer gewählter Start- und/oder Endzeitpunkt des Exportzeitraums liegt außerhalb von 01.01.2015–31.12.2025

## Verarbeitungslogik / Ablauf
1. Gewählten Exportzeitraum entgegennehmen.
2. Prüfen, ob Start- und/oder Enddatum außerhalb von 01.01.2015–31.12.2025 liegen.
3. Zeitraum auf den unterstützten Bereich begrenzen.
4. Export mit dem begrenzten Zeitraum gemäß FR-021 durchführen.
5. Hinweis ausgeben, dass der Zeitraum gekürzt wurde.

## Ausgabe / Ergebnis
CSV-Datei auf Basis des auf den unterstützten Bereich begrenzten Zeitraums, zusammen mit einem Hinweis auf die vorgenommene Kürzung.

## Fehlerfälle / Randbedingungen
- Start- oder Enddatum außerhalb 01.01.2015–31.12.2025: Zeitraum kürzen, Hinweis ausgeben, kein Fehler

## Akzeptanzkriterien
- [ ] Bei einem Start- oder Enddatum außerhalb 01.01.2015–31.12.2025 wird der Exportzeitraum auf den unterstützten Bereich begrenzt
- [ ] Der Nutzer erhält einen Hinweis, dass der Zeitraum gekürzt wurde

## Abhängigkeiten
- FR-021: CSV-Export bei vorhandenen Wetterdaten im gewählten Zeitraum

## Anmerkungen
Keine.
