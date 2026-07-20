# FR-060: Aktualisierung des Winddiagramms bei geändertem Zeitraum

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-016: Verlauf des Winds visualisieren

## Beschreibung
Wenn der gewählte Zeitraum geändert wird, muss das Plotly-Diagramm ausschließlich Windgeschwindigkeits-Messwerte innerhalb des neu gewählten Zeitraums anzeigen.

## Eingabe / Vorbedingungen
- Ein Diagramm für den Windgeschwindigkeitsverlauf wird bereits angezeigt (siehe FR-059)
- Ein geänderter Zeitraum liegt über die Streamlit-Konfigurationsoberfläche vor (siehe US-011)

## Verarbeitungslogik / Ablauf
1. Änderung des gewählten Zeitraums entgegennehmen.
2. Winddaten für den neu gewählten Zeitraum aus der SQLite-Datenbank abfragen.
3. Zuvor dargestellte Messwerte außerhalb des neuen Zeitraums aus dem Diagramm entfernen.
4. Diagramm mit den Messwerten des neu gewählten Zeitraums neu rendern.

## Ausgabe / Ergebnis
Das Diagramm zeigt ausschließlich Windgeschwindigkeits-Messwerte innerhalb des neu gewählten Zeitraums an.

## Fehlerfälle / Randbedingungen
- Der neu gewählte Zeitraum enthält keine Winddaten: siehe FR-061

## Akzeptanzkriterien
- [ ] Nach Änderung des gewählten Zeitraums zeigt das Diagramm ausschließlich Winddaten innerhalb des neuen Zeitraums an

## Abhängigkeiten
- Baut auf FR-059 (initiale Anzeige des Diagramms) auf
- Nutzt den geänderten Zeitraum aus der Konfiguration (siehe US-011)

## Anmerkungen
Keine.
