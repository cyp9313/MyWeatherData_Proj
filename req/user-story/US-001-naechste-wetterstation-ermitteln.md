# US-001: Nächstgelegene Wetterstation ermitteln

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-001: Datenimport/-export vom DWD Climate Data Center

## User Story
Als **Nutzer:in der App**
möchte ich **zu einer von mir angegebenen Koordinate in Deutschland die nächstgelegene DWD-Wetterstation ermitteln lassen**,
damit **ich weiß, von welcher Station die für mich relevanten Wetterdaten stammen, ohne die DWD-Stationsliste manuell durchsuchen zu müssen**.

## Beschreibung / Kontext
Grundlage für den Import ist stets eine konkrete DWD-Station. Die Zuordnung Koordinate → Station erfolgt anhand der geografischen Distanz zwischen der angegebenen Koordinate und den in den DWD-Stationslisten (Verzeichnis „help") geführten Stationsstandorten. Das Ergebnis dieser Story (Stations-ID) ist die Eingangsgröße für die Import-Stories (US-002 bis US-005), kann für deren Umsetzung und Tests aber auch unabhängig als fester Parameter vorgegeben werden.

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** eine gültige Koordinate innerhalb Deutschlands
   **Wenn** die Ermittlung der nächstgelegenen Station ausgelöst wird
   **Dann** wird die Station mit der geringsten Entfernung zur Koordinate zurückgegeben, inklusive Stations-ID, Stationsname und Entfernung in km

2. **Gegeben** eine Koordinate außerhalb Deutschlands
   **Wenn** die Ermittlung der nächstgelegenen Station ausgelöst wird
   **Dann** wird kein Stationsergebnis geliefert, sondern ein Hinweis, dass die Koordinate außerhalb des unterstützten Gebiets liegt

3. **Gegeben** zwei oder mehr Stationen mit identischer, minimaler Entfernung zur angegebenen Koordinate
   **Wenn** die Ermittlung der nächstgelegenen Station ausgelöst wird
   **Dann** wird nach einer festen, nachvollziehbaren Regel (aufsteigend nach Stations-ID) genau eine Station als Ergebnis ausgewählt

4. **Gegeben** die DWD-Stationsliste ist zum Zeitpunkt der Anfrage nicht abrufbar
   **Wenn** die Ermittlung der nächstgelegenen Station ausgelöst wird
   **Dann** wird ein Fehler mit klarem Hinweis auf die nicht verfügbare Stationsliste gemeldet, ohne dass die App abstürzt

## Zugehörige Functional Requirements
- [ ] FR-001: Nächstgelegene Station für Koordinate innerhalb Deutschlands ermitteln
- [ ] FR-002: Hinweis bei Koordinate außerhalb Deutschlands
- [ ] FR-003: Fehlerbehandlung bei nicht abrufbarer Stationsliste
- [ ] FR-004: Zuordnungsregel bei Distanz-Gleichstand mehrerer Stationen

## Abhängigkeiten
- Verfügbarkeit der DWD-Stationslisten im „help"-Verzeichnis der CDC-OpenData-Schnittstelle
- Liefert die Stations-ID als Eingangsgröße für US-002 (Lufttemperatur), US-003 (Niederschlag), US-004 (Wind) und US-005 (Sonneneinstrahlung)

## Anmerkungen
Die konkrete Zuordnungsregel bei Distanz-Gleichstand (Kriterium 3) ist mit dem Team/PO final abzustimmen; „aufsteigend nach Stations-ID" ist ein Vorschlag, kein bindendes Detail.
