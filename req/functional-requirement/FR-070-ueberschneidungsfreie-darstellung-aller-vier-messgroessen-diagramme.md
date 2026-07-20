
# FR-070: Überschneidungsfreie Darstellung aller vier Messgrößen-Diagramme

## Status
Review

## Priorität
Should have

## Zugehörige User Story
US-018: Mehrere Messgrößen gemeinsam visualisieren

## Beschreibung
Solange alle vier verfügbaren Messgrößen ausgewählt sind, muss die Streamlit-Oberfläche alle vier Diagramme ohne gegenseitige Überschneidung oder Überlappung darstellen.

## Eingabe / Vorbedingungen
- Alle vier verfügbaren Messgrößen (Lufttemperatur, Niederschlag, Wind, Sonneneinstrahlung) sind über die Konfigurationsoberfläche ausgewählt (siehe US-012)
- Ort und Zeitraum sind über die Streamlit-Konfigurationsoberfläche festgelegt (siehe US-010, US-011)
- Der Aufruf der Visualisierung wird ausgelöst

## Verarbeitungslogik / Ablauf
1. Ausgewählte Messgrößen aus der Konfiguration entgegennehmen.
2. Feststellen, dass alle vier verfügbaren Messgrößen ausgewählt sind.
3. Für jede der vier Messgrößen das jeweilige Diagramm rendern.
4. Alle vier Diagramme in einem Layout anordnen, das keine gegenseitige Überschneidung oder Überlappung der Diagrammflächen zulässt.

## Ausgabe / Ergebnis
Alle vier Diagramme werden gleichzeitig und ohne gegenseitige Überschneidung oder Überlappung angezeigt.

## Fehlerfälle / Randbedingungen
- Für eine der vier Messgrößen liegen keine Daten vor: siehe FR-071

## Akzeptanzkriterien
- [ ] Bei Auswahl aller vier verfügbaren Messgrößen werden alle vier Diagramme ohne gegenseitige Überschneidung oder Überlappung dargestellt

## Abhängigkeiten
- Konkretisiert FR-069 für den Sonderfall aller vier ausgewählten Messgrößen
- Nutzt die Einzeldiagramme aus US-014 (FR-050), US-015 (FR-055), US-016 (FR-059), US-017 (FR-064)

## Anmerkungen
Konkrete Anordnung (z. B. Raster-Layout) ist technische Designentscheidung.
