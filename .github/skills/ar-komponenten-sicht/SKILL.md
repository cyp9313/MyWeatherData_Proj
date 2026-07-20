---
name: ar-komponenten-sicht
description: 'Erstellen und Reviewen der Komponentensicht (Bausteinsicht) in der Architekturentwicklung, dargestellt mit PlantUML. Use when: eine Komponentensicht/Bausteinsicht unter arc/statische_sichten/ erstellt, ergänzt oder reviewt werden soll, oder wenn Komponenten, Teilkomponenten, Schnittstellen und deren Beziehungen eines Systems als PlantUML-Komponentendiagramm (Whitebox Ebene 1/Ebene 2) modelliert werden sollen.'
---

# Komponentensicht (Architektur)

## Zweck

Dieser Skill unterstützt bei der **Komponentensicht** (arc42-Kapitel 5 "Bausteinsicht") während der Architekturentwicklung. Er wird in zwei Situationen genutzt:

1. **Erstellen** einer neuen oder Ergänzen einer bestehenden Komponentensicht als PlantUML-Komponentendiagramm
2. **Reviewen** einer vorhandenen Komponentensicht auf Vollständigkeit, Konsistenz (insb. zur Kontextsicht) und korrekte Notation

Die Komponentensicht zerlegt das System (Blackbox aus der Kontextsicht) in seine internen Bausteine/Komponenten und zeigt deren Verantwortlichkeiten, Schnittstellen und Beziehungen zueinander sowie zu den bereits aus der Kontextsicht bekannten Nachbarn.

## Ablage

| Artefakt | Pfad |
|---|---|
| Beschreibung (Markdown) | `arc/statische_sichten/komponentensicht.md` |
| Ebene-1-Diagramm (Whitebox Gesamtsystem) | `arc/statische_sichten/komponentensicht-ebene1.puml` |
| Ebene-2-Diagramm je vertiefter Komponente | `arc/statische_sichten/komponentensicht-ebene2-<komponente>.puml` |

Die `.md`-Datei bindet die Diagramme jeweils per PlantUML-Codeblock ein (oder referenziert die `.puml`-Dateien) und beschreibt Komponenten und Schnittstellen zusätzlich in Textform/Tabelle.

## Ebenen-Konzept (Whitebox Level 1 / Level 2)

| | Ebene 1 (Whitebox Gesamtsystem) | Ebene 2 (Whitebox einer Komponente) |
|---|---|---|
| Zeigt | Das System von innen: seine Komponenten und deren Beziehungen zueinander sowie zu den Nachbarn aus der Kontextsicht | Eine einzelne Komponente aus Ebene 1 von innen: ihre Teilkomponenten und deren Beziehungen |
| Voraussetzung | Immer vorhanden | Nur für Komponenten mit relevanter interner Komplexität (nicht für jede triviale Komponente) |
| Systemgrenze/Nachbarn | Identisch zur Kontextsicht (gleiche Akteure/Nachbarsysteme, gleiche Aliase) | Externe Schnittstellen der Komponente müssen zu Ebene 1 konsistent sein |
| Detailgrad | Grobe fachlich/technisch begründete Bausteine | Feinere Zerlegung, aber weiterhin **keine** Klassen/Methoden (das ist Zielsicht/Klassendiagramm, kein Bestandteil dieser Sicht) |

Beide Ebenen bilden **denselben Baustein** ab, nur mit unterschiedlichem Detailgrad – analog zur arc42-Whitebox-Systematik. Techstack-Details stammen aus [doc/techstack/techstack-uebersicht.md](../../../doc/techstack/techstack-uebersicht.md), die Systemgrenze aus [arc/statische_sichten/kontextsicht.md](../../../arc/statische_sichten/kontextsicht.md) (sofern vorhanden).

### Kriterium für Ebene-2-Verfeinerung

Eine Komponente erhält ein Ebene-2-Diagramm, wenn **mindestens eines** der folgenden Kriterien zutrifft:

- Sie kapselt **mindestens 3** fachlich unterscheidbare Verarbeitungsschritte, die jeweils als eigene Teilkomponente sinnvoll sind (z. B. Stationssuche, Abruf, Validierung).
- Sie wird von **mehreren Epics/FRs** mit unterschiedlichen Anforderungen an ihr internes Verhalten referenziert.
- Sie behandelt eigene Fehler-/Sonderfälle (z. B. Datenlücken, fehlerhafte Datensätze), die ohne Verfeinerung nicht nachvollziehbar wären.

Trifft **keines** der Kriterien zu, bleibt die Komponente auf Ebene 1 als einzelner Baustein ohne Ebene-2-Diagramm.

## PlantUML-Notation

Es wird **reines UML** verwendet (kein C4-PlantUML-Include, keine externe Abhängigkeit):

- `component "<Name>" as <Alias>` für jede Komponente/Teilkomponente
- `interface "<Name>" as <Alias>` bzw. Lollipop-Notation (`Komponente - () "<Schnittstelle>"`) für explizit benannte Schnittstellen, wo sinnvoll
- `package "<System>" { ... }` bzw. `rectangle "<System>" as System <<System>> { ... }` als Rahmen um die Komponenten des betrachteten Systems (Ebene 1) bzw. der betrachteten Komponente (Ebene 2)
- Externe Akteure/Nachbarsysteme aus der Kontextsicht **außerhalb** des Rahmens, mit identischem Namen/Alias wie in der Kontextsicht
- Gerichtete Pfeile `A --> B : <Beschriftung>` für jede Beziehung/jeden Datenfluss, **eine Richtung pro Pfeil**
- Das betrachtete System bzw. die vertiefte Komponente optisch hervorheben, z. B. per `skinparam`
- Jedes Diagramm mit `@startuml <Name>` / `@enduml` und aussagekräftigem Diagrammnamen beginnen/beenden

Vollständige Notationsregeln, Legende und ausführliche Beispiele (Ebene 1 + Ebene 2, basierend auf dem Projekt-Techstack): siehe [plantuml-notation.md](./references/plantuml-notation.md).

## Vorgehen: Komponentensicht erstellen

1. Kontextsicht lesen ([kontextsicht.md](../../../arc/statische_sichten/kontextsicht.md), falls vorhanden): Systemgrenze, Akteure, Nachbarsysteme und deren Beziehungen zum System übernehmen.
2. Grobe Komponenten des Systems identifizieren – abgeleitet aus fachlichen Verantwortlichkeiten (Epics/User Stories) und/oder technischen Bausteinen aus dem Techstack.
3. Für jede Komponente Name und Verantwortung kurz beschreiben (eine Zeile).
4. Ebene-1-Diagramm erstellen: System als Rahmen mit den Komponenten darin, Nachbarn/Akteure identisch zur Kontextsicht außerhalb, alle Beziehungen (intern und zu den Nachbarn) als beschriftete Pfeile. Datei `komponentensicht-ebene1.puml`.
5. Prüfen, ob jede Kommunikationsbeziehung aus der Kontextsicht auf mindestens eine Komponente in Ebene 1 abgebildet ist.
6. Für Komponenten, die das [Kriterium für Ebene-2-Verfeinerung](#kriterium-für-ebene-2-verfeinerung) erfüllen: Ebene-2-Diagramm erstellen (Whitebox der Komponente mit ihren Teilkomponenten und Beziehungen). Datei `komponentensicht-ebene2-<komponente>.puml`. Externe Schnittstellen dieser Komponente müssen zu Ebene 1 passen.
7. Alle Diagramme in `komponentensicht.md` einbinden und Komponenten/Schnittstellen zusätzlich tabellarisch erläutern (Komponente, Verantwortung, eingehende/ausgehende Schnittstellen).
8. Kurz-Selbstcheck (siehe Checkliste unten) durchgehen, bevor die Komponentensicht als fertig/Review markiert wird.

## Vorgehen: Komponentensicht reviewen

1. `komponentensicht.md` sowie alle `.puml`-Dateien lesen; zusätzlich `kontextsicht.md` lesen, falls vorhanden.
2. **Konsistenz zur Kontextsicht**: Sind Akteure/Nachbarsysteme und deren Beziehungen zum System in Ebene 1 identisch zur Kontextsicht (gleiche Partner, keine widersprüchlichen oder fehlenden Beziehungen)?
3. Für **jede** Komponente in Ebene 1:
   - **Verantwortung**: Ist klar und eindeutig beschrieben, wofür die Komponente zuständig ist? Keine Überlappung mit anderen Komponenten?
   - **Notation**: Entspricht das Element der Notation oben (`component`, Rahmen, Pfeilrichtung, Beschriftung)?
   - **Schnittstellen-Konsistenz**: Falls eine Ebene-2-Verfeinerung existiert – stimmen deren externe Schnittstellen mit den in Ebene 1 gezeigten Beziehungen dieser Komponente überein?
4. Anhand des [Kriteriums für Ebene-2-Verfeinerung](#kriterium-für-ebene-2-verfeinerung) prüfen, ob eine Ebene-2-Verfeinerung an Stellen **fehlt**, wo mindestens ein Kriterium zutrifft, oder umgekehrt **unnötig** vorhanden ist, obwohl keines der Kriterien erfüllt ist.
5. Prüfen auf verbotene Detailtiefe (Klassen, Methoden, Attribute) – das gehört nicht in die Komponentensicht.
6. Ergebnis als Tabelle ausgeben (Format siehe unten).
7. Bei `⚠️`/`❌`: konkreten Korrekturvorschlag (inkl. angepasstem PlantUML-Ausschnitt) liefern, keine reine Kritik ohne Lösung.
8. Fazit: Gesamteinschätzung und Empfehlung (z. B. "Komponentensicht konsistent zur Kontextsicht" / "Komponente X um Ebene 2 ergänzen" / "Schnittstelle Y zwischen Ebene 1 und Ebene 2 widersprüchlich").

### Review-Ausgabeformat

```markdown
## Komponentensicht-Review

| # | Komponente / Beziehung | Konsistenz zur Kontextsicht ✅/⚠️/❌ | Verantwortung klar ✅/⚠️/❌ | Notation ✅/⚠️/❌ | Anmerkung / Vorschlag |
|---|---|---|---|---|---|
| 1 | System ↔ Nachbarsystem (Ebene 1) | ... | ... | ... | ... |
| 2 | Komponente A | ... | ... | ... | ... |
| 3 | Komponente A → Teilkomponenten (Ebene 2) | ... | ... | ... | ... |

**Fazit:** <Gesamteinschätzung + empfohlener nächster Schritt>
```

## Schnell-Checkliste (für Erstellung und Review gleichermaßen)

- [ ] Systemgrenze, Akteure und Nachbarsysteme sind identisch zur Kontextsicht (falls vorhanden)
- [ ] Jede Komponente hat eine eindeutige, überlappungsfreie Verantwortung
- [ ] Jede Beziehung aus der Kontextsicht ist mindestens einer Komponente in Ebene 1 zugeordnet
- [ ] Ebene-2-Diagramme existieren genau dort, wo das Kriterium für Ebene-2-Verfeinerung zutrifft (nicht mehr, nicht weniger)
- [ ] Externe Schnittstellen einer Ebene-2-Verfeinerung stimmen mit Ebene 1 überein
- [ ] Keine Klassen, Methoden oder Implementierungsdetails enthalten
- [ ] Reines UML ohne C4-Includes, gültige `@startuml`/`@enduml`-Blöcke
- [ ] Diagramme liegen unter `arc/statische_sichten/` und sind in `komponentensicht.md` eingebunden
