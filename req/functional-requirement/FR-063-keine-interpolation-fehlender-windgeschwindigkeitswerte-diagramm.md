# FR-063: Keine Interpolation fehlender Windgeschwindigkeitswerte im Diagramm

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-016: Verlauf des Winds visualisieren

## Beschreibung
Solange die Winddaten für den gewählten Zeitraum Lücken aufweisen, darf das Plotly-Diagramm die fehlenden Messwerte nicht durch berechnete Werte ersetzen.

## Eingabe / Vorbedingungen
- Die abgefragten Winddaten für den gewählten Zeitraum enthalten fehlende Zeitpunkte (Datenlücken, siehe FR-016)

## Verarbeitungslogik / Ablauf
1. Abgefragte Windgeschwindigkeits-Messwerte auf fehlende Zeitpunkte prüfen.
2. Für fehlende Zeitpunkte keine berechneten bzw. interpolierten Werte erzeugen.
3. Ausschließlich tatsächlich vorliegende Messwerte in das Diagramm übernehmen.

## Ausgabe / Ergebnis
Das Diagramm enthält ausschließlich tatsächlich gemessene Windgeschwindigkeitswerte, keine berechneten Ersatzwerte für fehlende Zeitpunkte.

## Fehlerfälle / Randbedingungen
- Keine.

## Akzeptanzkriterien
- [ ] Für Datenlücken innerhalb des gewählten Zeitraums werden keine berechneten Ersatzwerte im Diagramm angezeigt

## Abhängigkeiten
- Ergänzt FR-062 (erkennbare Darstellung von Datenlücken); beide FRs zusammen erfüllen das zugehörige Akzeptanzkriterium der US-016

## Anmerkungen
Keine.
