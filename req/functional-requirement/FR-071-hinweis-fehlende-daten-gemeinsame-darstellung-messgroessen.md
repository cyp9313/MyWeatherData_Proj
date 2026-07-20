
# FR-071: Hinweis auf fehlende Daten bei gemeinsamer Darstellung mehrerer Messgrößen

## Status
Review

## Priorität
Should have

## Zugehörige User Story
US-018: Mehrere Messgrößen gemeinsam visualisieren

## Beschreibung
Wenn bei mehreren ausgewählten Messgrößen für eine dieser Messgrößen im gewählten Zeitraum keine Daten vorliegen, muss die Streamlit-Oberfläche für die betroffene Messgröße anstelle eines Diagramms einen Hinweis auf fehlende Daten anzeigen.

## Eingabe / Vorbedingungen
- Mehrere Messgrößen sind über die Konfigurationsoberfläche ausgewählt (siehe US-012)
- Für mindestens eine der ausgewählten Messgrößen liegen im gewählten Zeitraum keine Daten in der SQLite-Datenbank vor
- Der Aufruf der Visualisierung wird ausgelöst

## Verarbeitungslogik / Ablauf
1. Ausgewählte Messgrößen aus der Konfiguration entgegennehmen.
2. Für jede ausgewählte Messgröße die Daten für Ort und Zeitraum aus der SQLite-Datenbank abfragen.
3. Feststellen, für welche Messgröße(n) die Abfrage ein leeres Ergebnis liefert.
4. Für jede betroffene Messgröße anstelle eines Diagramms einen Hinweis anzeigen, dass keine Daten verfügbar sind.

## Ausgabe / Ergebnis
Für jede Messgröße ohne Daten wird ein Hinweis auf fehlende Daten anstelle eines Diagramms angezeigt.

## Fehlerfälle / Randbedingungen
- Leeres Abfrageergebnis für eine einzelne der mehreren ausgewählten Messgrößen: Hinweis statt Diagramm für diese Messgröße anzeigen

## Akzeptanzkriterien
- [ ] Bei mehreren ausgewählten Messgrößen und fehlenden Daten für eine davon wird für die betroffene Messgröße ein Hinweis auf fehlende Daten angezeigt

## Abhängigkeiten
- Nutzt das leere Abfrageergebnis gemäß FR-035
- Analog zu den messgrößenspezifischen Hinweisen aus FR-052, FR-057, FR-061, FR-066
- Ergänzt durch FR-072 (unveränderte Darstellung der übrigen Diagramme)

## Anmerkungen
Keine.
