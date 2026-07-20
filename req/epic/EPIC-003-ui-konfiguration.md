# EPIC-003: User Interface zur Konfiguration von Ort, Zeitraum und Daten

## Status
Draft

## Priorität
Must have

## Beschreibung
Nutzer benötigen eine Bedienoberfläche, über die sie einen Ort (Koordinate innerhalb Deutschlands), einen Zeitraum (innerhalb von 01.01.2015 bis 31.12.2025) sowie die darzustellenden Wetterdaten (Lufttemperatur, Niederschlag, Wind, Sonneneinstrahlung) auswählen können.

## Ziel / Business Value
Eine intuitive Konfigurationsoberfläche ermöglicht es Nutzern ohne technisches Vorwissen, gezielt die für sie relevanten historischen Wetterdaten auszuwählen und darzustellen.

## Abgrenzung / Scope
**Enthält:**
- Eingabe/Auswahl einer Koordinate bzw. eines Ortes innerhalb Deutschlands
- Auswahl eines Zeitraums innerhalb 01.01.2015–31.12.2025
- Auswahl einer oder mehrerer Messgrößen (Lufttemperatur, Niederschlag, Wind, Sonneneinstrahlung)
- Validierung der Nutzereingaben (z. B. Zeitraum innerhalb der zulässigen Grenzen, Koordinate innerhalb Deutschlands)
- Auslösen von Import (EPIC-001) bzw. Abfrage der lokalen Datenbank (EPIC-002) anhand der Konfiguration

**Enthält nicht:**
- Eigentliche Datenbeschaffung vom DWD (siehe EPIC-001)
- Grafische/tabellarische Darstellung der Ergebnisse (siehe EPIC-004)

## Zugehörige User Stories
- [ ] US-010: Ort/Koordinate für die Wetterdatenabfrage auswählen
- [ ] US-011: Zeitraum für die Wetterdatenabfrage auswählen
- [ ] US-012: Messgrößen für die Wetterdatenabfrage auswählen
- [ ] US-013: Konfiguration bestätigen und Datenabruf auslösen

## Abnahmekriterien (High-Level)
- Nutzer können eine beliebige Koordinate innerhalb Deutschlands angeben
- Nutzer können einen Zeitraum innerhalb 01.01.2015–31.12.2025 auswählen; ungültige Zeiträume werden abgelehnt
- Nutzer können eine oder mehrere der vier Messgrößen auswählen
- Nach Bestätigung der Konfiguration werden die passenden Daten geladen bzw. abgefragt

## Abhängigkeiten
- EPIC-001 (Import) und EPIC-002 (lokale Datenbank) für die Bereitstellung der angeforderten Daten
- EPIC-004 zur Anzeige der Ergebnisse basierend auf der Konfiguration

## Anmerkungen
Konkrete UI-Technologie (Web, Desktop, etc.) ist technische Designentscheidung und in den zugehörigen Functional Requirements zu konkretisieren.
