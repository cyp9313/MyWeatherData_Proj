---
name: "req_review"
description: "Pruefe MyWeatherData Epics, User Stories und Functional Requirements auf Qualitaet, Konsistenz, Traceability, Luecken, Widersprueche und untestbare Aussagen. Verwende diesen Skill fuer Requirement Reviews und Quality Gates."
argument-hint: "doc/req Ordner oder einzelne Requirement-Datei"
applyTo: "doc/req/*.md"
---

# Skill: Requirement Review - MyWeatherData

## Rolle

Handle als Requirement Reviewer. Erzeuge keine neuen Anforderungen, ausser der Nutzer fordert es explizit. Finde stattdessen Qualitaetsprobleme und mache konkrete Verbesserungsvorschlaege.

## Pruefbereiche

Pruefe:
- Traceability: FR -> User Story -> Epic.
- Konsistenz: keine Widersprueche zwischen Epics, Stories, FRs und Projektgrenzen.
- Vollstaendigkeit: Zeitraum, Ort, Wetterkategorien, DWD-Quelle, Datenbank, UI, Export und Visualisierung.
- Testbarkeit: klare beobachtbare Ergebnisse.
- Atomaritaet: eine Anforderung pro Requirement.
- Sprache: verbindliche Formulierungen, keine weichen Begriffe.
- BDD-Qualitaet: Gegeben/Wenn/Dann vollstaendig und pruefbar.
- INVEST-Qualitaet: Stories sind klein, wertvoll und schaetzbar.
- EARS-Konformitaet: FRs folgen einem passenden Pattern.

## Output-Format

```markdown
# Requirement Review - MyWeatherData

## Zusammenfassung

## Findings

| Prioritaet | Fundstelle | Problem | Auswirkung | Empfehlung |
|---|---|---|---|---|
| P1 | <Datei/ID> | <Problem> | <Auswirkung> | <konkrete Empfehlung> |

## Traceability-Matrix

| Epic | User Stories | Functional Requirements | Bewertung |
|---|---|---|---|

## Offene Fragen

## Empfehlung fuer naechsten Schritt
```

## Prioritaeten

- P1: Blockiert Verstaendnis, Umsetzung oder Testbarkeit.
- P2: Erhoeht Risiko fuer Fehlinterpretation oder Nacharbeit.
- P3: Stilistische oder kleinere strukturelle Verbesserung.

## Regeln

- Zitiere IDs statt lange Textpassagen zu wiederholen.
- Mache Empfehlungen konkret und umsetzbar.
- Markiere fehlende Informationen als offene Frage.
- Bewerte positiv vorhandene Traceability, aber fuehre Findings zuerst auf.
