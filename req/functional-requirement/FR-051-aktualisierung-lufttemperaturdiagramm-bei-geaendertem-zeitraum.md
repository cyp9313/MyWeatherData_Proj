# FR-051: Aktualisierung des Lufttemperaturdiagramms bei geändertem Zeitraum

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-014: Verlauf der Lufttemperatur visualisieren

## Beschreibung
Wenn der gewählte Zeitraum geändert wird, muss das Plotly-Diagramm ausschließlich Lufttemperatur-Messwerte innerhalb des neu gewählten Zeitraums anzeigen.

## Eingabe / Vorbedingungen
- Ein Diagramm für den Lufttemperaturverlauf wird bereits angezeigt (siehe FR-050)
- Ein geänderter Zeitraum liegt über die Streamlit-Konfigurationsoberfläche vor (siehe US-011)

## Verarbeitungslogik / Ablauf
1. Änderung des gewählten Zeitraums entgegennehmen.
2. Lufttemperaturdaten für den neu gewählten Zeitraum aus der SQLite-Datenbank abfragen.
3. Zuvor dargestellte Messwerte außerhalb des neuen Zeitraums aus dem Diagramm entfernen.
4. Diagramm mit den Messwerten des neu gewählten Zeitraums neu rendern.

## Ausgabe / Ergebnis
Das Diagramm zeigt ausschließlich Lufttemperatur-Messwerte innerhalb des neu gewählten Zeitraums an.

## Fehlerfälle / Randbedingungen
- Der neu gewählte Zeitraum enthält keine Lufttemperaturdaten: siehe FR-052

## Akzeptanzkriterien
- [ ] Nach Änderung des gewählten Zeitraums zeigt das Diagramm ausschließlich Lufttemperaturdaten innerhalb des neuen Zeitraums an

## Abhängigkeiten
- Baut auf FR-050 (initiale Anzeige des Diagramms) auf
- Nutzt den geänderten Zeitraum aus der Konfiguration (siehe US-011)

## Anmerkungen
Keine.
