---
name: "invest_criteria"
description: "Pruefe MyWeatherData User Stories nach INVEST: Independent, Negotiable, Valuable, Estimable, Small, Testable. Verwende diesen Skill beim Erstellen, Reviewen oder Verfeinern von User Stories."
argument-hint: "User-Story-ID oder User-Story-Text"
applyTo: "doc/req/*.md"
---

# Skill: INVEST-Pruefung

## Aufgabe

Bewerte User Stories nach INVEST und gib konkrete Verbesserungen an.

## Kriterien

| Kriterium | Prueffrage |
|---|---|
| Independent | Kann die Story weitgehend ohne andere Stories umgesetzt oder getestet werden? |
| Negotiable | Laesst die Story fachliche Details verhandelbar, ohne den Nutzen zu verlieren? |
| Valuable | Liefert die Story erkennbaren Wert fuer Nutzer, Betreiber oder Projektziel? |
| Estimable | Sind Umfang, Grenzen und Abhaengigkeiten klar genug fuer eine Schaetzung? |
| Small | Ist die Story klein genug fuer einen Sprint oder muss sie gesplittet werden? |
| Testable | Sind Akzeptanzkriterien beobachtbar und pruefbar? |

## Output

```markdown
**INVEST-Pruefung:**
- Independent: <Erfuellt | Teilweise | Nicht erfuellt> - <Begruendung>
- Negotiable: <Erfuellt | Teilweise | Nicht erfuellt> - <Begruendung>
- Valuable: <Erfuellt | Teilweise | Nicht erfuellt> - <Begruendung>
- Estimable: <Erfuellt | Teilweise | Nicht erfuellt> - <Begruendung>
- Small: <Erfuellt | Teilweise | Nicht erfuellt> - <Begruendung>
- Testable: <Erfuellt | Teilweise | Nicht erfuellt> - <Begruendung>

**Empfohlene Anpassung:**
- <konkrete Anpassung>
```

## Regeln

- Begruende jede Bewertung kurz.
- Empfiehl Splits, wenn eine Story mehrere Nutzerziele oder mehrere Komponenten ohne klares Inkrement enthaelt.
- Markiere fehlende Akzeptanzkriterien als Testbarkeitsproblem.
