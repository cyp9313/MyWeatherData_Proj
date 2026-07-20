# US-004: Winddaten importieren

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-001: Datenimport/-export vom DWD Climate Data Center

## User Story
Als **Nutzer:in der App**
möchte ich **historische 10-Minuten-Winddaten einer DWD-Station für einen selbst gewählten Zeitraum zwischen 01.01.2015 und 31.12.2025 importieren**,
damit **die Winddaten für Speicherung, Auswertung und Visualisierung innerhalb der App zur Verfügung stehen**.

## Beschreibung / Kontext
Die Rohdaten liegen im DWD-Format gemäß [BESCHREIBUNG_obsgermany-climate-10min-wind_de.md](../../doc/DWD/md/BESCHREIBUNG_obsgermany-climate-10min-wind_de.md) vor und müssen für die angegebene Station und den angegebenen Zeitraum abgerufen, geparst und validiert werden. Die Stations-ID wird als Eingangsparameter übergeben (siehe US-001).

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** eine gültige Stations-ID und ein Zeitraum vollständig innerhalb 01.01.2015–31.12.2025
   **Wenn** der Import der Winddaten ausgelöst wird
   **Dann** werden alle für diesen Zeitraum verfügbaren 10-Minuten-Windwerte (Geschwindigkeit und Richtung) der Station geladen und in einem einheitlichen internen Format bereitgestellt

2. **Gegeben** ein Zeitraum, der teilweise außerhalb von 01.01.2015–31.12.2025 liegt
   **Wenn** der Import ausgelöst wird
   **Dann** werden nur die Daten innerhalb des unterstützten Zeitraums importiert und der Nutzer erhält einen Hinweis, dass der Zeitraum gekürzt wurde

3. **Gegeben** eine Rohdatendatei mit fehlerhaften oder unvollständigen Datensätzen (z. B. Formatfehler, fehlende Pflichtfelder)
   **Wenn** der Import ausgelöst wird
   **Dann** werden die betroffenen Datensätze erkannt und als fehlerhaft markiert bzw. übersprungen, der restliche Import wird fortgesetzt und die App stürzt nicht ab

4. **Gegeben** ein gültiger Zeitraum, für den die Station keine Messwerte aufgezeichnet hat (Datenlücke)
   **Wenn** der Import ausgelöst wird
   **Dann** wird ein leeres Ergebnis mit dem Hinweis auf die fehlenden Daten zurückgegeben, statt eines Fehlers

## Zugehörige Functional Requirements
- [ ] FR-013: Import der Winddaten für gültigen Zeitraum
- [ ] FR-014: Kürzung des Zeitraums bei teilweiser Überschreitung des unterstützten Zeitraums (Winddaten)
- [ ] FR-015: Umgang mit fehlerhaften oder unvollständigen Datensätzen beim Import der Winddaten
- [ ] FR-016: Rückgabe eines leeren Ergebnisses bei Datenlücke der Winddaten

## Abhängigkeiten
- Benötigt eine Stations-ID als Eingangsparameter (siehe US-001)
- Format- und Feldbeschreibung: [BESCHREIBUNG_obsgermany-climate-10min-wind_de.md](../../doc/DWD/md/BESCHREIBUNG_obsgermany-climate-10min-wind_de.md)

## Anmerkungen
Keine.
