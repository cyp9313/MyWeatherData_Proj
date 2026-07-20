# FR-067: Darstellung von Nachtstunden als Nullwert im Sonneneinstrahlungsdiagramm

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-017: Verlauf der Sonneneinstrahlung visualisieren

## Beschreibung
Solange im gewählten Zeitraum Nachtstunden ohne Sonneneinstrahlung vorliegen, muss das Plotly-Diagramm diese Zeitpunkte als Sonneneinstrahlung von 0 darstellen.

Solange im gewählten Zeitraum Nachtstunden ohne Sonneneinstrahlung vorliegen, darf das Plotly-Diagramm diese Zeitpunkte nicht als fehlende Daten (Datenlücke) interpretieren.

## Eingabe / Vorbedingungen
- Für den gewählten Ort und Zeitraum liegen Sonneneinstrahlungsdaten lokal in der SQLite-Datenbank vor (siehe FR-025)
- Die abgefragten Sonneneinstrahlungsdaten enthalten für Nachtstunden den gemessenen Wert 0 (keine Sonneneinstrahlung)

## Verarbeitungslogik / Ablauf
1. Abgefragte Sonneneinstrahlungs-Messwerte auf Zeitpunkte mit gemessenem Wert 0 prüfen.
2. Zeitpunkte mit gemessenem Wert 0 als regulären Messwert (Sonneneinstrahlung 0) in das Diagramm übernehmen.
3. Zeitpunkte mit gemessenem Wert 0 von tatsächlich fehlenden Zeitpunkten (Datenlücken) unterscheiden.
4. Diagramm mit den Sonneneinstrahlungswerten inkl. der Nullwerte für Nachtstunden rendern.

## Ausgabe / Ergebnis
Das Diagramm stellt Nachtstunden ohne Sonneneinstrahlung durchgängig als Sonneneinstrahlung von 0 dar, ohne diese als fehlende Daten zu kennzeichnen.

## Fehlerfälle / Randbedingungen
- Keine.

## Akzeptanzkriterien
- [ ] Nachtstunden ohne Sonneneinstrahlung im gewählten Zeitraum werden im Diagramm als Sonneneinstrahlung von 0 dargestellt
- [ ] Nachtstunden ohne Sonneneinstrahlung werden dabei nicht als fehlende Daten interpretiert

## Abhängigkeiten
- Ergänzt FR-064 (Anzeige des Diagramms)
- Abzugrenzen von tatsächlichen Datenlücken gemäß FR-020 (keine gemessenen Werte vorhanden)

## Anmerkungen
Keine.
