# FR-058: Darstellung niederschlagsfreier Perioden als Nullwert im Diagramm

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-015: Verlauf des Niederschlags visualisieren

## Beschreibung
Solange im gewählten Zeitraum Perioden ohne jeglichen Niederschlag vorliegen, muss das Plotly-Diagramm diese Perioden als Niederschlagsmenge von 0 darstellen.

Solange im gewählten Zeitraum Perioden ohne jeglichen Niederschlag vorliegen, darf das Plotly-Diagramm diese Perioden nicht als fehlende Daten (Datenlücke) interpretieren.

## Eingabe / Vorbedingungen
- Für den gewählten Ort und Zeitraum liegen Niederschlagsdaten lokal in der SQLite-Datenbank vor (siehe FR-025)
- Die abgefragten Niederschlagsdaten enthalten für einzelne Zeitpunkte den gemessenen Wert 0 (kein Niederschlag)

## Verarbeitungslogik / Ablauf
1. Abgefragte Niederschlags-Messwerte auf Zeitpunkte mit gemessenem Wert 0 prüfen.
2. Zeitpunkte mit gemessenem Wert 0 als regulären Messwert (Niederschlagsmenge 0) in das Diagramm übernehmen.
3. Zeitpunkte mit gemessenem Wert 0 von tatsächlich fehlenden Zeitpunkten (Datenlücken) unterscheiden.
4. Diagramm mit den Niederschlagsmengen inkl. der Nullwerte rendern.

## Ausgabe / Ergebnis
Das Diagramm stellt Perioden ohne Niederschlag durchgängig als Niederschlagsmenge von 0 dar, ohne diese als fehlende Daten zu kennzeichnen.

## Fehlerfälle / Randbedingungen
- Keine.

## Akzeptanzkriterien
- [ ] Perioden ohne Niederschlag im gewählten Zeitraum werden im Diagramm als Niederschlagsmenge von 0 dargestellt
- [ ] Perioden ohne Niederschlag werden dabei nicht als fehlende Daten interpretiert

## Abhängigkeiten
- Ergänzt FR-055 (Anzeige des Diagramms)
- Abzugrenzen von tatsächlichen Datenlücken gemäß FR-012 (keine gemessenen Werte vorhanden)

## Anmerkungen
Keine.
