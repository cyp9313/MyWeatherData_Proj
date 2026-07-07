---
name: "agile_estimation"
description: "Schaetzt User Stories fuer MyWeatherData mit Story Points, Definition-of-Ready-Pruefung und begruendeter Komplexitaetsanalyse. Verwende diesen Skill fuer Aufwandsschaetzung, Planning Poker oder Backlog-Bewertung."
argument-hint: "User-Story-ID, Backlog-Datei oder Schaetzauftrag"
applyTo: "doc/req/*.md"
---

# Skill: Agile Aufwandsschaetzung - MyWeatherData

## Aufgabe

Wenn eine User Story, ein Epic oder das gesamte Backlog geschaetzt werden soll, erstelle eine nachvollziehbare agile Aufwandsschaetzung fuer MyWeatherData.

Nutze als Kontext:
- `.github/copilot-instructions.md`
- `doc/req/epic_myweatherdata.md`
- `doc/req/user_story_myweatherdata.md`
- `doc/req/functional_requirement_myweatherdata.md`

## Schaetzmodell

Verwende Story Points aus der Fibonacci-Reihe:

| Punkte | Bedeutung |
|---:|---|
| 1 | Sehr klein, klare Aenderung, kaum Abhaengigkeiten |
| 2 | Klein, bekannte Logik, einfache Tests |
| 3 | Moderat, mehrere Bedingungen oder kleine Integration |
| 5 | Mittel, relevante Integration, Fehlerfaelle, Datenmodell oder UI-Logik |
| 8 | Gross, externe Datenquelle, komplexes Parsing, Visualisierung oder mehrere Komponenten |
| 13 | Sehr gross, muss wahrscheinlich weiter zerlegt werden |

USER_STORY_01 gilt als Referenz fuer eine kleine technische Story. Schaetze sie nur hoeher als 3, wenn zusaetzliche externe Unsicherheiten sichtbar sind.

## Definition of Ready

Pruefe jede Story gegen diese Kriterien:

- Zielgruppe und Nutzen sind klar.
- Akzeptanzkriterien sind testbar.
- Relevante Functional Requirements sind vorhanden oder eindeutig ableitbar.
- Fachliche Grenzen sind genannt: Deutschland, Zeitraum 01.01.2015 bis 31.12.2025, Wetterkategorien.
- Technische Abhaengigkeiten sind benannt.
- Offene Fragen blockieren die Umsetzung nicht oder sind explizit markiert.

## Analysepflichten

Bewerte fuer jede Story:

- Aufwandstreiber
- Abhaengigkeiten
- Edge Cases
- Testaufwand
- Datenqualitaets- oder Integrationsrisiken
- Annahmen
- Empfehlung: akzeptieren, verfeinern oder splitten

## Output-Format

```markdown
## <USER_STORY_ID>: <Titel>

**Story Points:** <1|2|3|5|8|13>

**Begruendung:** <2-4 Saetze mit konkreten Aufwandstreibern>

**Definition of Ready:** <Erfuellt | Teilweise erfuellt | Nicht erfuellt>

**Abhaengigkeiten:**
- <Abhaengigkeit 1>

**Risiken / Blind Spots:**
- <Risiko 1>

**Empfehlung:** <Akzeptieren | Verfeinern | Splitten>
```

## Qualitaetsregeln

- Keine unbegruendeten Zahlen nennen.
- Keine Scheingenauigkeit in Stunden erzeugen, sofern nicht ausdruecklich verlangt.
- Bei Unsicherheit konservativ schaetzen und die Unsicherheit benennen.
- Stories mit 13 Punkten muessen einen konkreten Split-Vorschlag erhalten.
