
# FR-072: Unveränderte Darstellung der übrigen Diagramme bei fehlenden Daten einer Messgröße

## Status
Review

## Priorität
Should have

## Zugehörige User Story
US-018: Mehrere Messgrößen gemeinsam visualisieren

## Beschreibung
Wenn bei mehreren ausgewählten Messgrößen für eine dieser Messgrößen im gewählten Zeitraum keine Daten vorliegen, darf die Streamlit-Oberfläche die Diagramme der übrigen ausgewählten Messgrößen nicht verändern.

## Eingabe / Vorbedingungen
- Mehrere Messgrößen sind über die Konfigurationsoberfläche ausgewählt (siehe US-012)
- Für mindestens eine der ausgewählten Messgrößen liegen im gewählten Zeitraum keine Daten vor, für mindestens eine weitere ausgewählte Messgröße liegen Daten vor
- Der Aufruf der Visualisierung wird ausgelöst

## Verarbeitungslogik / Ablauf
1. Ausgewählte Messgrößen aus der Konfiguration entgegennehmen.
2. Für jede ausgewählte Messgröße die Daten für Ort und Zeitraum aus der SQLite-Datenbank abfragen.
3. Feststellen, für welche Messgröße(n) Daten vorliegen und für welche nicht.
4. Für jede Messgröße mit vorliegenden Daten das reguläre Diagramm unverändert rendern und anzeigen, unabhängig vom Fehlen von Daten bei anderen ausgewählten Messgrößen.

## Ausgabe / Ergebnis
Die Diagramme der Messgrößen mit vorliegenden Daten werden unverändert angezeigt, unabhängig vom Hinweis auf fehlende Daten bei anderen ausgewählten Messgrößen.

## Fehlerfälle / Randbedingungen
- Keine (dieses Requirement beschreibt selbst die Randbedingung für den Umgang mit dem Fehlerfall aus FR-071)

## Akzeptanzkriterien
- [ ] Bei mehreren ausgewählten Messgrößen mit fehlenden Daten für eine davon werden die Diagramme der übrigen Messgrößen unverändert dargestellt

## Abhängigkeiten
- Ergänzt FR-071 (Hinweis auf fehlende Daten für die betroffene Messgröße)
- Nutzt die Einzeldiagramme aus US-014 (FR-050), US-015 (FR-055), US-016 (FR-059), US-017 (FR-064)

## Anmerkungen
Keine.
