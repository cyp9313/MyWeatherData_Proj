---
name: "epic_slicing"
description: "Zerlege MyWeatherData-Epics in vertikale, fachlich testbare Slices. Verwende diesen Skill fuer Epic Slicing, Happy Path, Edge Cases, Integrationsslices und Vorbereitung kleiner User Stories."
argument-hint: "Epic-ID oder Epic-Datei"
applyTo: "doc/req/*.md"
---

# Skill: Epic Slicing - MyWeatherData

## Aufgabe

Zerlege ein Epic in vertikale Slices, die fachlichen Nutzen liefern und spaeter als User Stories umgesetzt werden koennen.

## Slicing-Prinzipien

- Schneide nach Nutzerwert, nicht nach technischen Schichten.
- Starte mit dem Happy Path.
- Ergaenze Validierungs-, Fehler- und Edge-Case-Slices.
- Markiere Integrationsslices, wenn mehrere Module verbunden werden muessen.
- Halte Slices klein genug, damit daraus schaetzbare User Stories entstehen.

## MyWeatherData-Slice-Typen

Nutze diese Slice-Typen, wenn passend:

- Happy Path: gueltige Eingaben, verfuegbare DWD-Daten, erfolgreiche Speicherung oder Anzeige.
- Validierung: Zeitraum, Koordinaten, Pflichtfelder, Kategorieauswahl.
- Fehlerfall: Netzwerkfehler, fehlende DWD-Dateien, leerer Export, nicht beschreibbarer Zielpfad.
- Datenqualitaet: Datenluecken, unterschiedliche Messintervalle, fehlende Werte.
- Integration: API zu Datenbank, Datenbank zu UI, Datenbank zu Visualisierung, Visualisierung zu PNG-Export.

## Output-Format

```markdown
## <EPIC_ID>: <Epic-Titel>

| Slice | Typ | Nutzerwert | Betroffene Komponenten | Moegliche User Story | Abhaengigkeiten |
|---|---|---|---|---|---|
| S1 | Happy Path | <Nutzen> | <Komponenten> | <Story-Idee> | <Abhaengigkeiten> |

**Empfohlene Reihenfolge:**
1. <Slice>
2. <Slice>

**Offene Fragen:**
- <Frage>
```

## Qualitaetsregeln

- Jeder Slice muss ein pruefbares Ergebnis haben.
- Jeder Slice muss einem Epic zuordenbar sein.
- Keine reinen Schichten-Slices wie "Datenbank bauen" ohne Nutzerwert, ausser als klar markierter Integrations- oder Infrastruktur-Slice.
