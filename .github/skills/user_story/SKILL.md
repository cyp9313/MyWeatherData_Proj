---
name: "user_story"
description: "Erstelle oder verfeinere User Stories fuer MyWeatherData aus bestehenden Epics oder Epic Slices. Verwende diesen Skill fuer Nutzerperspektive, BDD-Akzeptanzkriterien, Edge Cases und INVEST-Pruefung."
argument-hint: "Epic-ID, Epic Slice oder Beschreibung der gewuenschten User Story"
applyTo: "doc/req/*.md"
---

# Skill: User Stories erstellen - MyWeatherData

## Aufgabe

Leite aus Epics oder Epic Slices konkrete User Stories ab. Schreibe aus Sicht einer Rolle, nicht aus Sicht der Implementierung.

Nutze als Kontext:
- `.github/copilot-instructions.md`
- `doc/req/epic_myweatherdata.md`
- `doc/req/epic_slicing_myweatherdata.md`, falls vorhanden
- Skills `bdd_format` und `invest_criteria`.

## User-Story-Template

```markdown
## USER_STORY_<NN>: <Titel>

**Epic:** <EPIC_ID>

**User Story:** Als <Rolle> moechte ich <Ziel/Aktion>, damit <Nutzen/Grund>.

**Akzeptanzkriterien:**
- Gegeben <Ausgangszustand>, wenn <Aktion/Ereignis>, dann <erwartetes Ergebnis>.
- Gegeben <Ausgangszustand>, wenn <Aktion/Ereignis>, dann <erwartetes Ergebnis>.
- Gegeben <Ausgangszustand>, wenn <Aktion/Ereignis>, dann <erwartetes Ergebnis>.

**INVEST-Pruefung:**
- Independent: <kurze Bewertung>
- Negotiable: <kurze Bewertung>
- Valuable: <kurze Bewertung>
- Estimable: <kurze Bewertung>
- Small: <kurze Bewertung>
- Testable: <kurze Bewertung>
```

## Regeln

- Vergib IDs fortlaufend als `USER_STORY_01`, `USER_STORY_02`, ...
- Jede Story referenziert genau ein bestehendes Epic.
- Formuliere: `Als <Rolle> moechte ich <Ziel>, damit <Nutzen>.`
- Erstelle mindestens drei testbare Akzeptanzkriterien im BDD-Stil.
- Fuege mindestens einen realistischen Edge Case hinzu, wenn die Story Datenabruf, Validierung, Export oder Visualisierung betrifft.
- Pruefe alle sechs INVEST-Kriterien.
- Markiere Stories als "Split empfohlen", wenn sie mehrere unabhaengige Ziele enthalten.

## Projektregeln

- Zeitraum: 01.01.2015 bis 31.12.2025.
- Standort: Koordinaten innerhalb Deutschlands.
- Stationswahl: naechstgelegene verfuegbare DWD-Wetterstation.
- Wetterdaten: Lufttemperatur, Niederschlag, Wind und Sonneneinstrahlung.

## Vermeide

- technische Implementierungsdetails als Nutzerziel
- mehrere Nutzerziele in einer Story
- Akzeptanzkriterien ohne beobachtbares Ergebnis
- unklare Rollen wie "Benutzer" ohne Kontext, wenn eine praezisere Rolle moeglich ist
