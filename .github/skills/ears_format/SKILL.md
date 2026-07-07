---
name: "ears_format"
description: "Formuliere und pruefe Functional Requirements im EARS-Format fuer MyWeatherData. Verwende diesen Skill fuer eindeutige, atomare, testbare Systemanforderungen mit muss/darf-nicht-Formulierungen."
argument-hint: "Functional Requirement oder User Story"
applyTo: "doc/req/*.md"
---

# Skill: EARS-Format

## Aufgabe

Formuliere Functional Requirements im EARS-Format, um Mehrdeutigkeit zu reduzieren.

## EARS-Pattern

| Pattern | Syntax |
|---|---|
| Ubiquitous | Das MyWeatherData-System muss <Systemantwort>. |
| Event-Driven | Wenn <Trigger>, muss das MyWeatherData-System <Systemantwort>. |
| State-Driven | Solange <Zustand>, muss/darf das MyWeatherData-System <Systemantwort>. |
| Unwanted Behavior | Wenn <unerwuenschtes Ereignis>, dann muss/darf das MyWeatherData-System <Systemantwort>. |
| Optional Feature | Wo <Feature vorhanden ist>, muss das MyWeatherData-System <Systemantwort>. |
| Complex | Solange <Zustand>, wenn <Trigger>, dann muss das MyWeatherData-System <Systemantwort>. |

## Regeln

- Verwende genau ein Pattern pro Requirement.
- Schreibe aus Systemsicht, nicht aus Nutzersicht.
- Verwende "muss" oder "darf nicht".
- Beschreibe genau eine Systemantwort.
- Vermeide weiche Woerter: "sollte", "kann", "idealerweise", "moeglichst", "gegebenenfalls".
- Mache Trigger, Zustand und Ergebnis konkret.

## Auswahlhilfe

- Immer geltende Systemregel: Ubiquitous.
- Reaktion auf Nutzeraktion, Downloadende oder Exportstart: Event-Driven.
- Verhalten waehrend eines laufenden Zustands: State-Driven.
- Fehler, Ausfall oder ungueltige Eingabe: Unwanted Behavior.
- Konfigurierbares Zusatzfeature: Optional Feature.
- Kombination aus Zustand und Ereignis: Complex.

## Qualitaetscheck

Ein gutes EARS Requirement ist:
- eindeutig
- testbar
- atomar
- nachvollziehbar zu einer User Story
- konsistent mit Projektgrenzen und Akzeptanzkriterien
