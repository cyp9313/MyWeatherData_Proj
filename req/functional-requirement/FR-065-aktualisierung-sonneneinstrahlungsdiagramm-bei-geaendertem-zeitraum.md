# FR-065: Aktualisierung des Sonneneinstrahlungsdiagramms bei geändertem Zeitraum

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-017: Verlauf der Sonneneinstrahlung visualisieren

## Beschreibung
Wenn der gewählte Zeitraum geändert wird, muss das Plotly-Diagramm ausschließlich Sonneneinstrahlungs-Messwerte innerhalb des neu gewählten Zeitraums anzeigen.

## Eingabe / Vorbedingungen
- Ein Diagramm für den Sonneneinstrahlungsverlauf wird bereits angezeigt (siehe FR-064)
- Ein geänderter Zeitraum liegt über die Streamlit-Konfigurationsoberfläche vor (siehe US-011)

## Verarbeitungslogik / Ablauf
1. Änderung des gewählten Zeitraums entgegennehmen.
2. Sonneneinstrahlungsdaten für den neu gewählten Zeitraum aus der SQLite-Datenbank abfragen.
3. Zuvor dargestellte Messwerte außerhalb des neuen Zeitraums aus dem Diagramm entfernen.
4. Diagramm mit den Messwerten des neu gewählten Zeitraums neu rendern.

## Ausgabe / Ergebnis
Das Diagramm zeigt ausschließlich Sonneneinstrahlungs-Messwerte innerhalb des neu gewählten Zeitraums an.

## Fehlerfälle / Randbedingungen
- Der neu gewählte Zeitraum enthält keine Sonneneinstrahlungsdaten: siehe FR-066

## Akzeptanzkriterien
- [ ] Nach Änderung des gewählten Zeitraums zeigt das Diagramm ausschließlich Sonneneinstrahlungsdaten innerhalb des neuen Zeitraums an

## Abhängigkeiten
- Baut auf FR-064 (initiale Anzeige des Diagramms) auf
- Nutzt den geänderten Zeitraum aus der Konfiguration (siehe US-011)

## Anmerkungen
Keine.
