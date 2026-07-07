---
name: "module_2_requirement_pipeline"
agent: "Req_Engineer"
description: "Fuehre den Modul-2-Requirement-Engineering-Workflow fuer MyWeatherData aus: Epics, Stories, FRs und Review-Hinweise."
argument-hint: "vollstaendiger Requirement-Engineering-Lauf"
---

Fuehre fuer MyWeatherData den Requirement-Engineering-Workflow aus Modul 2 aus.

Nutze als verbindlichen Kontext:
- `.github/copilot-instructions.md`
- `Modul_2.md`
- vorhandene Dateien in `doc/req/`

Arbeite in vier Phasen:

1. Epics pruefen oder erstellen
   - Nutze `epic` und `epic_slicing`.
   - Schreibe nach `doc/req/epic_myweatherdata.md`.

2. User Stories ableiten
   - Nutze `user_story`, `bdd_format` und `invest_criteria`.
   - Schreibe nach `doc/req/user_story_myweatherdata.md`.

3. Functional Requirements ableiten
   - Nutze `func_req` und `ears_format`.
   - Schreibe nach `doc/req/functional_requirement_myweatherdata.md`.

4. Review vorbereiten
   - Nutze `req_review`.
   - Schreibe Review-Hinweise nach `doc/req/requirement_review_myweatherdata.md`.

Regeln:
- Verwende Deutsch.
- Halte bestehende IDs stabil, wenn Inhalte bereits existieren.
- Vergib neue IDs fortlaufend.
- Loesche keine bestehenden Anforderungen ohne ausdruecklichen Auftrag.
- Markiere Annahmen und offene Fragen explizit.
