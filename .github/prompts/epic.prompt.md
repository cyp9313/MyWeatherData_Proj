---
name: "epic_myweatherdata"
agent: "Req_Engineer"
description: "Erstelle oder ueberarbeite Epics fuer MyWeatherData anhand des Modul-2-Requirement-Engineering-Workflows."
argument-hint: "Epic-Ziel, Feature-Idee oder Name der Epic-Datei"
---

Erstelle oder ueberarbeite Epics fuer das Projekt MyWeatherData.

Nutze als Kontext:
- `.github/copilot-instructions.md`
- `Modul_2.md`
- `doc/req/epic_myweatherdata.md`, falls vorhanden
- den Skill `epic`
- den Skill `epic_slicing`

Aufgabe:
- Formuliere Epics auf strategischer Ebene.
- Pruefe die Systemgrenzen: DWD Climate Data Center, lokale Datenbank, UI, Visualisierung, Export.
- Beruecksichtige den Zeitraum 01.01.2015 bis 31.12.2025.
- Beruecksichtige Koordinaten innerhalb Deutschlands und die naechstgelegene DWD-Wetterstation.
- Beruecksichtige Lufttemperatur, Niederschlag, Wind und Sonneneinstrahlung.
- Identifiziere Abhaengigkeiten zwischen Epics.
- Schlage sinnvolle vertikale Slices vor, damit spaeter testbare User Stories entstehen.

Schreibe das Ergebnis in:
- `doc/req/epic_myweatherdata.md`

Verwende Deutsch und das im Skill `epic` definierte Format.
