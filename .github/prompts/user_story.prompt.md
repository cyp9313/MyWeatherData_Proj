---
name: "user_story_myweatherdata"
agent: "Story_Crafter"
description: "Leite User Stories mit BDD-Akzeptanzkriterien und INVEST-Pruefung aus MyWeatherData-Epics ab."
argument-hint: "Epic-ID, Epic-Datei oder Beschreibung der gewuenschten User Stories"
---

Erstelle User Stories fuer das Projekt MyWeatherData basierend auf den bestehenden Epics.

Nutze als Kontext:
- `.github/copilot-instructions.md`
- `Modul_2.md`
- `doc/req/epic_myweatherdata.md`
- den Skill `user_story`
- den Skill `bdd_format`
- den Skill `invest_criteria`

Aufgabe:
- Erstelle pro Epic mindestens zwei User Stories.
- Formuliere jede Story im Format: Als <Rolle> moechte ich <Ziel>, damit <Nutzen>.
- Formuliere Akzeptanzkriterien im BDD-Stil mit Gegeben/Wenn/Dann.
- Denke als Advocatus Diaboli ueber realistische Edge Cases nach.
- Fuehre fuer jede Story eine INVEST-Pruefung durch.
- Markiere Stories, die zu gross, zu technisch oder nicht testbar sind.

Schreibe das Ergebnis in:
- `doc/req/user_story_myweatherdata.md`

Verwende Deutsch und das im Skill `user_story` definierte Format.
