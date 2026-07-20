---
name: ar-kontext-sicht
description: 'Erstellen und Reviewen der Kontextsicht (Kontextabgrenzung) in der Architekturentwicklung, dargestellt mit PlantUML. Use when: eine fachliche oder technische Kontextsicht/Kontextabgrenzung unter arc/statische_sichten/ erstellt, ergänzt oder reviewt werden soll, oder wenn Systemgrenzen, Nachbarsysteme, Akteure und Schnittstellen eines Systems als PlantUML-Diagramm modelliert werden sollen.'
---

# Kontextsicht (Architektur)

## Zweck

Dieser Skill unterstützt bei der **Kontextsicht** (arc42-Kapitel 3 "Kontextabgrenzung") während der Architekturentwicklung. Er wird in zwei Situationen genutzt:

1. **Erstellen** einer neuen oder Ergänzen einer bestehenden Kontextsicht (fachlich und/oder technisch) als PlantUML-Diagramm
2. **Reviewen** einer vorhandenen Kontextsicht auf Vollständigkeit, Konsistenz und korrekte Notation

Die Kontextsicht grenzt das System von seiner Umwelt ab: Wer/was kommuniziert mit dem System, welche Informationen bzw. welche technischen Schnittstellen werden dabei ausgetauscht.

## Ablage

| Artefakt | Pfad |
|---|---|
| Beschreibung (Markdown) | `arc/statische_sichten/kontextsicht.md` |
| Fachliches Kontextdiagramm | `arc/statische_sichten/kontextsicht-fachlich.puml` |
| Technisches Kontextdiagramm | `arc/statische_sichten/kontextsicht-technisch.puml` |

Die `.md`-Datei bindet die Diagramme jeweils per PlantUML-Codeblock ein (oder referenziert die `.puml`-Dateien) und beschreibt die Kommunikationsbeziehungen zusätzlich in Textform/Tabelle.

## Fachlicher vs. technischer Kontext

| | Fachlicher Kontext | Technischer Kontext |
|---|---|---|
| Zeigt | Fachliche Kommunikationsbeziehungen zwischen System und Nachbarn (Akteure, Nachbarsysteme) | Technische Schnittstellen, Kanäle, Protokolle, Datenformate |
| Elemente | System als Ganzes (Blackbox), Akteure, Nachbarsysteme | System (ggf. mit technischen Teilkomponenten an der Grenze), technische Adapter, Protokolle |
| Beschriftung der Beziehungen | Ausgetauschte fachliche Information (z. B. "Ort, Zeitraum, Messgrößen konfigurieren") | Technisches Protokoll/Format (z. B. "HTTP GET, CSV-Payload") |
| Enthält keine | Technologienamen, Protokolle | – |

Beide Sichten bilden **dieselbe Systemgrenze** ab, nur mit unterschiedlichem Detailgrad. Techstack-Details für den technischen Kontext stammen aus [doc/techstack/techstack-uebersicht.md](../../../doc/techstack/techstack-uebersicht.md).

## PlantUML-Notation

Es wird **reines UML** verwendet (kein C4-PlantUML-Include, keine externe Abhängigkeit):

- `actor "<Name>" as <Alias>` für menschliche Akteure (z. B. Nutzer:in)
- `rectangle "<Name>" as <Alias>` für das betrachtete System und fachliche Nachbarsysteme (fachlicher Kontext)
- `component "<Name>"` bzw. `database "<Name>"` für technische Elemente (technischer Kontext), wo sinnvoll
- Gerichtete Pfeile `A --> B : <Beschriftung>` für jede Kommunikationsbeziehung, **eine Richtung pro Pfeil** (bei Antwort/Rückgabe einen eigenen Pfeil in Gegenrichtung)
- Das betrachtete System optisch hervorheben, z. B. per `skinparam` oder `<<System>>`-Stereotyp
- Jedes Diagramm mit `@startuml <Name>` / `@enduml` und aussagekräftigem Diagrammnamen beginnen/beenden

Vollständige Notationsregeln, Legende und ausführliche Beispiele (fachlich + technisch, basierend auf dem Projekt-Techstack): siehe [plantuml-notation.md](./references/plantuml-notation.md).

## Vorgehen: Kontextsicht erstellen

1. System und dessen Grenze eindeutig benennen (was gehört zum System, was ist Umwelt).
2. Alle Kommunikationspartner sammeln: Akteure (Nutzer:innen, Rollen) und Nachbarsysteme (z. B. externe APIs, Dateisysteme, andere Anwendungen).
3. Für jeden Kommunikationspartner die **fachlichen** Beziehungen erfassen: Welche Information fließt in welche Richtung? Diagramm gemäß Notation oben als `kontextsicht-fachlich.puml` erstellen.
4. Für jede fachliche Beziehung die **technische** Realisierung ergänzen (Protokoll, Schnittstelle, Datenformat, ggf. konkrete Bibliothek/Technologie aus dem Techstack). Diagramm als `kontextsicht-technisch.puml` erstellen.
5. Beide Diagramme in `kontextsicht.md` einbinden und pro Kommunikationsbeziehung kurz in Textform/Tabelle erläutern (Partner, ausgetauschte Daten, Richtung, Trigger).
6. Kurz-Selbstcheck (siehe Checkliste unten) durchgehen, bevor die Kontextsicht als fertig/Review markiert wird.

## Vorgehen: Kontextsicht reviewen

1. `kontextsicht.md` sowie beide `.puml`-Dateien lesen.
2. Prüfen, ob die Systemgrenze in beiden Diagrammen **identisch** ist (gleiche Kommunikationspartner, keine widersprüchliche Abgrenzung).
3. Für **jede** Kommunikationsbeziehung:
   - **Vollständigkeit**: Ist die Beziehung sowohl fachlich als auch technisch dargestellt?
   - **Notation**: Entspricht das Element der Notation oben (Akteur vs. Rechteck/Komponente, Pfeilrichtung, Beschriftung)?
   - **Trennschärfe**: Enthält der fachliche Kontext keine Technologienamen/Protokolle? Enthält der technische Kontext eine konkrete, aus dem Techstack ableitbare Realisierung?
   - **Richtung**: Ist die Pfeilrichtung korrekt (wer initiiert, wer antwortet)?
4. Prüfen, ob es Nachbarsysteme/Akteure gibt, die in der Anforderungslage (Epics/User Stories/FRs) vorkommen, aber in der Kontextsicht fehlen.
5. Ergebnis als Tabelle ausgeben (Format siehe unten).
6. Bei `⚠️`/`❌`: konkreten Korrekturvorschlag (inkl. angepasstem PlantUML-Ausschnitt) liefern, keine reine Kritik ohne Lösung.
7. Fazit: Gesamteinschätzung und Empfehlung (z. B. "Kontextsicht vollständig" / "Nachbarsystem X ergänzen" / "Technischen Kontext um Protokoll für Beziehung Y ergänzen").

### Review-Ausgabeformat

```markdown
## Kontextsicht-Review

| # | Kommunikationsbeziehung | Fachlich ✅/⚠️/❌ | Technisch ✅/⚠️/❌ | Notation ✅/⚠️/❌ | Anmerkung / Vorschlag |
|---|---|---|---|---|---|
| 1 | Nutzer:in ↔ System | ... | ... | ... | ... |
| 2 | System ↔ Nachbarsystem | ... | ... | ... | ... |

**Fazit:** <Gesamteinschätzung + empfohlener nächster Schritt>
```

## Schnell-Checkliste (für Erstellung und Review gleichermaßen)

- [ ] Systemgrenze ist in fachlichem und technischem Diagramm identisch
- [ ] Alle Akteure und Nachbarsysteme aus Epics/User Stories/FRs sind berücksichtigt
- [ ] Fachlicher Kontext enthält keine Technologienamen/Protokolle
- [ ] Technischer Kontext benennt konkrete Protokolle/Formate passend zum Techstack
- [ ] Jede Kommunikationsbeziehung hat eine eindeutige Pfeilrichtung und aussagekräftige Beschriftung
- [ ] Reines UML ohne C4-Includes, gültige `@startuml`/`@enduml`-Blöcke
- [ ] Diagramme liegen unter `arc/statische_sichten/` und sind in `kontextsicht.md` eingebunden
