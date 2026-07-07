---
name: "epic"
description: "Erstelle, pruefe oder verfeinere Epics fuer das MyWeatherData-Projekt. Verwende diesen Skill fuer Requirement Engineering auf strategischer Ebene, Epic-Brainstorming, Systemgrenzen, Abhaengigkeiten und Vorbereitung von Epic Slicing."
argument-hint: "Epic-Ziel, Feature-Idee oder Name der Epic-Datei"
applyTo: "doc/req/*.md"
---

# Skill: Epics erstellen - MyWeatherData

## Aufgabe

Erstelle oder verfeinere Epics fuer MyWeatherData in Deutsch. Ein Epic beschreibt eine groessere fachliche Initiative auf strategischer Ebene und bereitet spaetere User Stories vor.

Nutze als Kontext:
- `.github/copilot-instructions.md`
- `doc/req/epic_myweatherdata.md`, falls vorhanden
- Projektgrenzen aus MyWeatherData: DWD Climate Data Center, lokale SQLite-Datenbank, User Interface, Visualisierung und Export.

## Epic-Template

```markdown
## EPIC_<NN>: <Titel>

**Ziel:** <Ein Satz, der Nutzen und Zweck des Epics beschreibt.>

**Beschreibung:**
<Zwei bis vier Saetze, die beschreiben, was implementiert wird, welche Komponenten betroffen sind und wie das Epic in das Gesamtsystem passt.>

**Akzeptanzkriterien:**
- <Messbares und testbares Kriterium 1>
- <Messbares und testbares Kriterium 2>
- <Messbares und testbares Kriterium 3>
- <Messbares und testbares Kriterium 4>

**Umfang:**
- <Lieferobjekt oder Aktivitaet 1>
- <Lieferobjekt oder Aktivitaet 2>
- <Lieferobjekt oder Aktivitaet 3>
- <Lieferobjekt oder Aktivitaet 4>
```

## Regeln

- Vergib IDs fortlaufend als `EPIC_01`, `EPIC_02`, ...
- Halte bestehende IDs stabil.
- Formuliere Akzeptanzkriterien messbar und testbar.
- Beruecksichtige den Zeitraum 01.01.2015 bis 31.12.2025, wenn Datenabruf oder Anzeige betroffen sind.
- Beruecksichtige Koordinaten innerhalb Deutschlands und die naechstgelegene DWD-Wetterstation.
- Beruecksichtige Lufttemperatur, Niederschlag, Wind und Sonneneinstrahlung.
- Nenne konkrete Lieferobjekte im Umfang.
- Vermeide vage Formulierungen wie "einfach", "flexibel", "benutzerfreundlich" ohne pruefbares Kriterium.

## Qualitaetscheck

Pruefe jedes Epic auf:
- fachlichen Nutzen
- klare Systemgrenze
- erkennbare Abhaengigkeiten
- spaetere Zerlegbarkeit in User Stories
- keine Vermischung mehrerer unabhaengiger Initiativen

Wenn ein Epic zu gross ist, nutze oder empfehle den Skill `epic_slicing`.
