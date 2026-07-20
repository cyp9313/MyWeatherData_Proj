# FR-002: Hinweis bei Koordinate außerhalb Deutschlands

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-001: Nächstgelegene Wetterstation ermitteln

## Beschreibung
Wenn die angegebene Koordinate außerhalb Deutschlands liegt, muss der Import-Client anstelle eines Stationsergebnisses einen Hinweis liefern, dass die Koordinate außerhalb des unterstützten Gebiets liegt.

## Eingabe / Vorbedingungen
- Die Ermittlung der nächstgelegenen Station wurde für eine Koordinate ausgelöst, die außerhalb der Landesgrenzen Deutschlands liegt

## Verarbeitungslogik / Ablauf
1. Koordinate entgegennehmen.
2. Prüfen, ob die Koordinate innerhalb der Landesgrenzen Deutschlands liegt.
3. Bei negativem Ergebnis: Ermittlung der nächstgelegenen Station nicht durchführen.
4. Hinweis zurückgeben, dass die Koordinate außerhalb des unterstützten Gebiets liegt.

## Ausgabe / Ergebnis
Hinweis, dass die Koordinate außerhalb des unterstützten Gebiets liegt; kein Stationsergebnis.

## Fehlerfälle / Randbedingungen
- Koordinate außerhalb Deutschlands: kein Stationsergebnis, stattdessen Hinweis auf nicht unterstütztes Gebiet

## Akzeptanzkriterien
- [ ] Bei einer Koordinate außerhalb Deutschlands wird kein Stationsergebnis geliefert
- [ ] Stattdessen wird ein Hinweis angezeigt, dass die Koordinate außerhalb des unterstützten Gebiets liegt

## Abhängigkeiten
- Definition der Landesgrenzen Deutschlands als Prüfgrundlage

## Anmerkungen
Keine.
