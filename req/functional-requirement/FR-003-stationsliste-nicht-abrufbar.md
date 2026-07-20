# FR-003: Fehlerbehandlung bei nicht abrufbarer Stationsliste

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-001: Nächstgelegene Wetterstation ermitteln

## Beschreibung
Wenn die DWD-Stationsliste zum Zeitpunkt der Anfrage nicht abrufbar ist, muss der Import-Client einen Fehler mit klarem Hinweis auf die nicht verfügbare Stationsliste melden, ohne dass die App abstürzt.

## Eingabe / Vorbedingungen
- Die Ermittlung der nächstgelegenen Station wurde ausgelöst
- Die DWD-Stationsliste im „help"-Verzeichnis der CDC-OpenData-Schnittstelle ist zu diesem Zeitpunkt nicht erreichbar

## Verarbeitungslogik / Ablauf
1. Abruf der DWD-Stationsliste aus dem „help"-Verzeichnis der CDC-OpenData-Schnittstelle versuchen.
2. Fehlschlag des Abrufs erkennen (z. B. Timeout, HTTP-Fehler, Verzeichnis nicht erreichbar).
3. Fehler mit klarem Hinweis auf die nicht verfügbare Stationsliste melden.
4. Verarbeitung kontrolliert abbrechen, ohne dass die App abstürzt.

## Ausgabe / Ergebnis
Fehlermeldung mit klarem Hinweis auf die nicht verfügbare DWD-Stationsliste; die App bleibt lauffähig.

## Fehlerfälle / Randbedingungen
- DWD-Stationsliste nicht abrufbar: Fehler mit klarem Hinweis melden, App läuft stabil weiter

## Akzeptanzkriterien
- [ ] Bei nicht abrufbarer DWD-Stationsliste wird ein Fehler mit klarem Hinweis auf die nicht verfügbare Stationsliste gemeldet
- [ ] Die App stürzt in diesem Fehlerfall nicht ab

## Abhängigkeiten
- Verfügbarkeit/Erreichbarkeit der DWD-CDC-Open-Data-Schnittstelle

## Anmerkungen
Keine.
