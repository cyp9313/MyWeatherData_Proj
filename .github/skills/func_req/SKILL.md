---
name: "func_req"
description: "Erstelle oder verfeinere Functional Requirements fuer MyWeatherData aus User Stories und Akzeptanzkriterien. Verwende diesen Skill fuer formale, atomare, testbare Systemanforderungen im EARS-Format."
argument-hint: "User-Story-ID, Beschreibung der Functional Requirements oder Name der Requirement-Datei"
applyTo: "doc/req/*.md"
---

# Skill: Functional Requirements erstellen - MyWeatherData

## Aufgabe

Leite aus User Stories und Akzeptanzkriterien Functional Requirements ab. Wechsle dabei vom Nutzerfokus zur Systemsicht.

Nutze als Kontext:
- `.github/copilot-instructions.md`
- `doc/req/epic_myweatherdata.md`
- `doc/req/user_story_myweatherdata.md`
- Skill `ears_format`.

## Functional-Requirement-Template

```markdown
## FR_<NN>: <Titel>

**Quelle:** <USER_STORY_ID>

**Requirement:** <Requirement im EARS-Format>

**EARS-Pattern:** <Ubiquitous | Event-Driven | State-Driven | Unwanted Behavior | Optional Feature | Complex>

**Begruendung:** <Ein kurzer Satz, warum dieses Requirement notwendig ist.>
```

## Regeln

- Vergib IDs fortlaufend als `FR_01`, `FR_02`, ...
- Jede Functional Requirement referenziert mindestens eine existierende User Story.
- Schreibe aus Sicht des MyWeatherData-Systems.
- Beschreibe genau eine Systemfunktion pro Requirement.
- Verwende verbindlich "muss" oder "darf nicht".
- Vermeide "sollte", "kann", "idealerweise", "moeglichst" und "gegebenenfalls".
- Nutze genau ein EARS-Pattern pro Requirement.
- Anforderungen muessen eindeutig, atomar, testbar und nachvollziehbar sein.

## Projektregeln

- Wenn relevant, nenne den Zeitraum 01.01.2015 bis 31.12.2025.
- Wenn relevant, beschraenke Standorte auf Koordinaten innerhalb Deutschlands.
- Wenn relevant, nenne die naechstgelegene verfuegbare DWD-Wetterstation.
- Wenn relevant, nenne die Wetterkategorien Lufttemperatur, Niederschlag, Wind und Sonneneinstrahlung.
- Wenn Fehlerfaelle relevant sind, erstelle separate Requirements fuer Fehlerbehandlung und Protokollierung.

## Qualitaetscheck

Pruefe jedes Requirement auf:
- Eindeutigkeit
- Testbarkeit
- Traceability zur User Story
- Atomaritaet
- Konsistenz mit Epics und User Stories
- Vollstaendigkeit fachlicher Randbedingungen
