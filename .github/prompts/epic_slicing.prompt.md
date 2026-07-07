---
name: "epic_slicing"
agent: "Story_Crafter"
description: "Analysiere MyWeatherData-Epics und schlage vertikale Slices fuer testbare User Stories vor."
argument-hint: "Epic-ID oder Epic-Datei"
---

Analysiere die bestehenden MyWeatherData-Epics und erstelle einen Slicing-Vorschlag.

Nutze:
- `.github/copilot-instructions.md`
- `Modul_2.md`
- `doc/req/epic_myweatherdata.md`
- den Skill `epic_slicing`

Ziel:
- Zerlege jedes Epic in vertikale, fachlich testbare Slices.
- Beginne mit einem Happy Path.
- Ergaenze Fehlerfaelle, Edge Cases und Integrationsslices.
- Zeige Abhaengigkeiten zwischen Slices.

Schreibe das Ergebnis nach:
- `doc/req/epic_slicing_myweatherdata.md`

