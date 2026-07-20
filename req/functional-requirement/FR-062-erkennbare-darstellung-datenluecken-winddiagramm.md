# FR-062: Erkennbare Darstellung von Datenlücken im Winddiagramm

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-016: Verlauf des Winds visualisieren

## Beschreibung
Solange die Winddaten für den gewählten Zeitraum Lücken aufweisen, muss das Plotly-Diagramm diese Lücken im dargestellten Verlauf erkennbar machen.

## Eingabe / Vorbedingungen
- Die abgefragten Winddaten für den gewählten Zeitraum enthalten fehlende Zeitpunkte (Datenlücken, siehe FR-016)

## Verarbeitungslogik / Ablauf
1. Abgefragte Windgeschwindigkeits-Messwerte auf fehlende Zeitpunkte im erwarteten Messintervall prüfen.
2. Fehlende Zeitpunkte als Lücke im Diagrammverlauf kennzeichnen (z. B. Unterbrechung der Linie).
3. Diagramm mit den erkennbar gekennzeichneten Lücken rendern.

## Ausgabe / Ergebnis
Das Diagramm stellt Datenlücken im gewählten Zeitraum erkennbar dar.

## Fehlerfälle / Randbedingungen
- Fehlende Werte dürfen dabei nicht durch berechnete Werte ersetzt werden: siehe FR-063

## Akzeptanzkriterien
- [ ] Bei Datenlücken innerhalb des gewählten Zeitraums werden diese im Diagramm erkennbar dargestellt

## Abhängigkeiten
- Ergänzt FR-059 (Anzeige des Diagramms)
- Direkt verknüpft mit FR-063 (keine Interpolation fehlender Werte)

## Anmerkungen
Keine.
