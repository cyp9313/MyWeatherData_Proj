---
name: "functional_requirement_myweatherdata"
agent: "Req_Engineer"
description: "Leite formale Functional Requirements im EARS-Format aus MyWeatherData User Stories ab."
argument-hint: "User-Story-ID, User-Story-Datei oder Requirement-Datei"
---

Leite Functional Requirements fuer MyWeatherData aus den bestehenden User Stories und Akzeptanzkriterien ab.

Nutze als Kontext:
- `.github/copilot-instructions.md`
- `Modul_2.md`
- `doc/req/epic_myweatherdata.md`
- `doc/req/user_story_myweatherdata.md`
- den Skill `func_req`
- den Skill `ears_format`

Aufgabe:
- Transformiere den Nutzerfokus der User Stories in eine Systemsicht.
- Verwende zwingend das EARS-Format.
- Verwende verbindliche Formulierungen mit "muss" oder "darf nicht".
- Vermeide "sollte", "kann", "idealerweise", "moeglichst" und "gegebenenfalls".
- Erstelle atomare, testbare und nachvollziehbare Requirements.
- Referenziere fuer jedes Requirement mindestens eine User Story.

Schreibe das Ergebnis in:
- `doc/req/functional_requirement_myweatherdata.md`

Verwende Deutsch und das im Skill `func_req` definierte Format.
