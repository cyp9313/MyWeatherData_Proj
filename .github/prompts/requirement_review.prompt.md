---
name: "requirement_review"
agent: "Req_Reviewer"
description: "Pruefe MyWeatherData Epics, User Stories und Functional Requirements auf Qualitaet, Konsistenz und Luecken."
argument-hint: "Requirement-Datei, User-Story-Datei oder gesamter doc/req Ordner"
---

Fuehre ein Requirement Review fuer MyWeatherData durch.

Nutze:
- `.github/copilot-instructions.md`
- `Modul_2.md`
- `doc/req/epic_myweatherdata.md`
- `doc/req/user_story_myweatherdata.md`
- `doc/req/functional_requirement_myweatherdata.md`
- den Skill `req_review`
- den Skill `invest_criteria`
- den Skill `bdd_format`
- den Skill `ears_format`

Wichtig:
- Erzeuge keine neuen Requirements.
- Veraendere bestehende Requirements nur, wenn der Nutzer dies explizit verlangt.
- Pruefe stattdessen auf Widersprueche, Mehrdeutigkeit, fehlende Randbedingungen, fehlende Traceability und untestbare Aussagen.

Schreibe das Review nach:
- `doc/req/requirement_review_myweatherdata.md`

