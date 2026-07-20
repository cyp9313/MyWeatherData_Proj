
# FR-069: Gleichzeitige Darstellung der Diagramme mehrerer ausgewählter Messgrößen

## Status
Review

## Priorität
Should have

## Zugehörige User Story
US-018: Mehrere Messgrößen gemeinsam visualisieren

## Beschreibung
Solange mehrere Messgrößen ausgewählt sind, muss die Streamlit-Oberfläche die Diagramme aller ausgewählten Messgrößen für den gleichen Ort und Zeitraum gleichzeitig darstellen.

## Eingabe / Vorbedingungen
- Mehrere Messgrößen sind über die Konfigurationsoberfläche ausgewählt (siehe US-012)
- Ort und Zeitraum sind über die Streamlit-Konfigurationsoberfläche festgelegt (siehe US-010, US-011)
- Der Aufruf der Visualisierung wird ausgelöst

## Verarbeitungslogik / Ablauf
1. Ausgewählte Messgrößen aus der Konfiguration entgegennehmen.
2. Feststellen, dass mehrere Messgrößen ausgewählt sind.
3. Für jede ausgewählte Messgröße das jeweilige Diagramm für den gewählten Ort und Zeitraum rendern.
4. Alle gerenderten Diagramme gleichzeitig in der Streamlit-Oberfläche anzeigen.

## Ausgabe / Ergebnis
Die Diagramme aller ausgewählten Messgrößen werden für den gleichen Ort und Zeitraum gleichzeitig angezeigt.

## Fehlerfälle / Randbedingungen
- Für eine der ausgewählten Messgrößen liegen keine Daten vor: siehe FR-071

## Akzeptanzkriterien
- [ ] Bei mehreren ausgewählten Messgrößen werden die Diagramme aller ausgewählten Messgrößen für den gleichen Ort und Zeitraum gleichzeitig angezeigt

## Abhängigkeiten
- Nutzt die Messgrößenauswahl aus US-012 (FR-044)
- Nutzt die Einzeldiagramme aus US-014 (FR-050), US-015 (FR-055), US-016 (FR-059), US-017 (FR-064)
- Konkretisiert durch FR-070 (Sonderfall aller vier Messgrößen) und FR-071/FR-072 (fehlende Daten einer Messgröße)

## Anmerkungen
Konkrete Anordnung (z. B. untereinander, im Raster, mit gemeinsamer Zeitachse) ist technische Designentscheidung.
