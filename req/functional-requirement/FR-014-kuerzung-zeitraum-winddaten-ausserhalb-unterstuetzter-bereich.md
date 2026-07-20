# FR-014: Kürzung des Zeitraums bei teilweiser Überschreitung des unterstützten Zeitraums (Winddaten)

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-004: Winddaten importieren

## Beschreibung
Wenn der Import der Winddaten für einen Zeitraum ausgelöst wird, der teilweise außerhalb von 01.01.2015–31.12.2025 liegt, muss der Import-Client nur die Daten innerhalb des unterstützten Zeitraums importieren und der Nutzerin/dem Nutzer einen Hinweis anzeigen, dass der Zeitraum gekürzt wurde.

## Eingabe / Vorbedingungen
- Gültige Stations-ID
- Angegebener Zeitraum liegt teilweise außerhalb von 01.01.2015–31.12.2025

## Verarbeitungslogik / Ablauf
1. Stations-ID und Zeitraum entgegennehmen.
2. Prüfen, ob der angegebene Zeitraum teilweise außerhalb von 01.01.2015–31.12.2025 liegt.
3. Den Zeitraum auf den unterstützten Bereich 01.01.2015–31.12.2025 kürzen.
4. Import der Winddaten für den gekürzten Zeitraum gemäß FR-013 durchführen.
5. Hinweis anzeigen, dass der angefragte Zeitraum gekürzt wurde.

## Ausgabe / Ergebnis
10-Minuten-Windwerte (Geschwindigkeit und Richtung) der Station für den gekürzten, unterstützten Zeitraum sowie ein Hinweis auf die Kürzung.

## Fehlerfälle / Randbedingungen
- Zeitraum liegt vollständig außerhalb von 01.01.2015–31.12.2025: nicht durch dieses FR abgedeckt, siehe Anmerkungen

## Akzeptanzkriterien
- [ ] Bei einem Zeitraum, der teilweise außerhalb von 01.01.2015–31.12.2025 liegt, werden nur die Daten innerhalb des unterstützten Zeitraums importiert
- [ ] Die Nutzerin/der Nutzer erhält einen Hinweis, dass der Zeitraum gekürzt wurde

## Abhängigkeiten
- FR-013: Import der Winddaten für gültigen Zeitraum

## Anmerkungen
Das Verhalten bei einem Zeitraum, der vollständig außerhalb von 01.01.2015–31.12.2025 liegt, ist in der User Story nicht spezifiziert und daher nicht Gegenstand dieses Functional Requirements.
