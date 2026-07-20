# FR-053: Erkennbare Darstellung von Datenlücken im Lufttemperaturdiagramm

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-014: Verlauf der Lufttemperatur visualisieren

## Beschreibung
Solange die Lufttemperaturdaten für den gewählten Zeitraum Lücken aufweisen, muss das Plotly-Diagramm diese Lücken im dargestellten Verlauf erkennbar machen.

## Eingabe / Vorbedingungen
- Die abgefragten Lufttemperaturdaten für den gewählten Zeitraum enthalten fehlende Zeitpunkte (Datenlücken, siehe FR-008)

## Verarbeitungslogik / Ablauf
1. Abgefragte Lufttemperatur-Messwerte auf fehlende Zeitpunkte im erwarteten Messintervall prüfen.
2. Fehlende Zeitpunkte als Lücke im Diagrammverlauf kennzeichnen (z. B. Unterbrechung der Linie).
3. Diagramm mit den erkennbar gekennzeichneten Lücken rendern.

## Ausgabe / Ergebnis
Das Diagramm stellt Datenlücken im gewählten Zeitraum erkennbar dar.

## Fehlerfälle / Randbedingungen
- Fehlende Werte dürfen dabei nicht durch berechnete Werte ersetzt werden: siehe FR-054

## Akzeptanzkriterien
- [ ] Bei Datenlücken innerhalb des gewählten Zeitraums werden diese im Diagramm erkennbar dargestellt

## Abhängigkeiten
- Ergänzt FR-050 (Anzeige des Diagramms)
- Direkt verknüpft mit FR-054 (keine Interpolation fehlender Werte)

## Anmerkungen
Keine.
