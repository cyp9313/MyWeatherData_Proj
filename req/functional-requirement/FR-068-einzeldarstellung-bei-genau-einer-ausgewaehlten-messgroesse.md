
# FR-068: Einzeldarstellung bei genau einer ausgewählten Messgröße

## Status
Review

## Priorität
Should have

## Zugehörige User Story
US-018: Mehrere Messgrößen gemeinsam visualisieren

## Beschreibung
Solange genau eine Messgröße ausgewählt ist, muss die Streamlit-Oberfläche nur das Diagramm dieser einen Messgröße darstellen.

## Eingabe / Vorbedingungen
- Genau eine Messgröße ist über die Konfigurationsoberfläche ausgewählt (siehe US-012)
- Ort und Zeitraum sind über die Streamlit-Konfigurationsoberfläche festgelegt (siehe US-010, US-011)
- Der Aufruf der Visualisierung wird ausgelöst

## Verarbeitungslogik / Ablauf
1. Ausgewählte Messgröße(n) aus der Konfiguration entgegennehmen.
2. Feststellen, dass genau eine Messgröße ausgewählt ist.
3. Nur das Diagramm der ausgewählten Messgröße rendern.
4. Kein weiteres Diagramm in der Streamlit-Oberfläche anzeigen.

## Ausgabe / Ergebnis
Es wird ausschließlich das Diagramm der einen ausgewählten Messgröße angezeigt.

## Fehlerfälle / Randbedingungen
- Keine.

## Akzeptanzkriterien
- [ ] Bei genau einer ausgewählten Messgröße wird nur das Diagramm dieser einen Messgröße dargestellt

## Abhängigkeiten
- Nutzt die Messgrößenauswahl aus US-012 (FR-044)
- Nutzt die Einzeldiagramme aus US-014 (FR-050), US-015 (FR-055), US-016 (FR-059), US-017 (FR-064)

## Anmerkungen
Keine.
