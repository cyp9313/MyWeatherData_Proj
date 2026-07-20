---
name: ar-klassen-sicht
description: 'Erstellen und Reviewen der Klassensicht (Klassendiagramm) in der Architekturentwicklung, dargestellt mit PlantUML. Use when: eine Klassensicht/Klassendiagramm unter arc/statische_sichten/ erstellt, ergänzt oder reviewt werden soll, oder wenn Klassen, Attribute, Methoden, Vererbung, Assoziation, Aggregation, Komposition oder Schnittstellen einer Komponente als PlantUML-Klassendiagramm modelliert werden sollen.'
---

# Klassensicht (Architektur)

## Zweck

Dieser Skill unterstützt bei der **Klassensicht** während der Architekturentwicklung. Sie verfeinert einzelne Komponenten/Teilkomponenten aus der [Komponentensicht](../ar-komponenten-sicht/SKILL.md) auf Ebene der Klassen und wird in zwei Situationen genutzt:

1. **Erstellen** einer neuen oder Ergänzen einer bestehenden Klassensicht als PlantUML-Klassendiagramm
2. **Reviewen** einer vorhandenen Klassensicht auf Vollständigkeit, Konsistenz (insb. zur Komponentensicht) und korrekte Notation

Die Klassensicht zeigt für eine Komponente/Teilkomponente die relevanten Klassen, Schnittstellen und Aufzählungstypen mit ihren wichtigsten Attributen und Methoden sowie deren Beziehungen zueinander (Vererbung, Assoziation, Aggregation, Komposition, Realisierung).

## Ablage

| Artefakt | Pfad |
|---|---|
| Beschreibung (Markdown) | `arc/statische_sichten/klassensicht.md` |
| Klassendiagramm je vertiefter Komponente | `arc/statische_sichten/klassensicht-<komponente>.puml` |

Die `.md`-Datei bindet die Diagramme jeweils per PlantUML-Codeblock ein (oder referenziert die `.puml`-Dateien) und beschreibt Klassen und Beziehungen zusätzlich in Textform/Tabelle.

## Verhältnis zur Komponentensicht

| | Komponentensicht (Ebene 1/2) | Klassensicht |
|---|---|---|
| Zeigt | Komponenten/Teilkomponenten und deren Beziehungen | Klassen/Schnittstellen/Enums **einer** Komponente/Teilkomponente und deren Beziehungen |
| Detailgrad | Fachliche/technische Bausteine, keine Implementierungsdetails | Attribute (mit Typ), Methoden (mit Signatur), Vererbung/Assoziation/Aggregation/Komposition |
| Voraussetzung | Immer vorhanden | Nur für Komponenten/Teilkomponenten mit relevantem eigenen Datenmodell oder Verhalten (siehe Kriterium unten) |
| Konsistenz | – | Jede Klasse ist eindeutig einer Komponente/Teilkomponente aus der Komponentensicht zugeordnet; externe Beziehungen der Komponente bleiben erhalten |

Die Klassensicht ersetzt **nicht** die Komponentensicht, sondern vertieft einzelne Bausteine. Techstack-Details (insb. Python) stammen aus [doc/techstack/techstack-uebersicht.md](../../../doc/techstack/techstack-uebersicht.md), die zu verfeinernden Bausteine aus [arc/statische_sichten/komponentensicht.md](../../../arc/statische_sichten/komponentensicht.md) (sofern vorhanden).

### Schnittstellen nach außen (Pflicht)

Jede eingehende externe Beziehung einer Komponente/Teilkomponente aus der Komponentensicht (d. h. jeder Aufruf, den eine andere Komponente oder ein Akteur an die verfeinerte Komponente richtet) **muss** in der Klassensicht als explizites `interface`-Element modelliert werden – nicht nur in Prosa/Tabelle beschrieben werden. Die Klasse, die den Aufruf tatsächlich entgegennimmt, realisiert diese Schnittstelle (`..|>`). Damit ist die nach außen sichtbare, öffentliche Schnittstelle der Komponente unmittelbar im Diagramm erkennbar, ohne dass die Komponentensicht erneut gelesen werden muss.

- Ausgangspunkt sind die eingehenden Pfeile auf die Komponente in der Komponentensicht (Ebene 1 bzw. Ebene 2), z. B. `UI --> Core` oder `Core --> Import-Client`.
- Pro eingehender externer Beziehung (bzw. pro fachlich zusammengehöriger Gruppe von Beziehungen) ein `interface "<Name>Schnittstelle" as <Alias>` mit den Methoden, die von außen aufrufbar sind.
- Ausgehende externe Beziehungen (die verfeinerte Komponente ruft eine andere Komponente auf) werden weiterhin **nicht** erneut modelliert, sondern bleiben – wie bisher – Bestandteil der Komponentensicht.
- Interne Klassen, die nur innerhalb der Komponente verwendet werden, benötigen kein Interface.

### Kriterium für Klassenverfeinerung

Eine Komponente/Teilkomponente erhält ein Klassendiagramm, wenn **mindestens eines** der folgenden Kriterien zutrifft:

- Sie verwaltet ein eigenes, dauerhaftes **Datenmodell** (z. B. Datenbank-Entitäten wie Station, Messwert), das von mehreren Komponenten/FRs referenziert wird.
- Sie kapselt **mindestens 2** Klassen mit eigenständiger Verantwortung, deren Zusammenspiel (Vererbung, Aggregation, Assoziation) sonst nicht nachvollziehbar wäre.
- Sie definiert eine oder mehrere **Schnittstellen** (z. B. Repository-Interface), die von anderen Komponenten genutzt oder von mehreren Klassen implementiert werden.

Trifft **keines** der Kriterien zu, bleibt die Komponente/Teilkomponente ohne eigenes Klassendiagramm.

## PlantUML-Notation

Es wird **reines UML** verwendet (kein C4-PlantUML-Include, keine externe Abhängigkeit):

- `class "<Name>" as <Alias> { ... }` für jede Klasse, mit Attributen (`<Sichtbarkeit><name>: <Typ>`) und Methoden (`<Sichtbarkeit><name>(<param>: <Typ>): <Rückgabetyp>`) im Klassenkörper
- `interface "<Name>" as <Alias>` für Schnittstellen
- `enum "<Name>" as <Alias> { WERT1 WERT2 ... }` für Aufzählungstypen
- Sichtbarkeit passend zur Python-Konvention: `+` öffentlich (kein führender Unterstrich), `-` privat/geschützt (führender Unterstrich `_`/`__`)
- `Sub --|> Super` für Vererbung (Generalisierung)
- `Klasse ..|> Interface` für Realisierung/Implementierung einer Schnittstelle
- `A "1" --> "0..*" B : <Rolle/Beschriftung>` für Assoziation mit Multiplizität, **eine Richtung pro Pfeil**
- `A o-- B` für Aggregation, `A *-- B` für Komposition
- `A ..> B : <benutzt>` für lose Abhängigkeit (z. B. Aufruf ohne dauerhafte Referenz)
- Nur die für die Architektur relevanten Attribute/Methoden zeigen (öffentliche Schnittstelle, keine vollständige Implementierung)
- **Stereotypen sind verpflichtend**, wenn eine Klasse einem der folgenden Python-Konstrukte entspricht: `<<dataclass>>` für reine Datenklassen (Python `@dataclass`), `<<Protocol>>` für strukturelle Schnittstellen (Python `Protocol` statt `ABC`), `<<Repository>>` für Klassen, die dem Repository-Pattern für den Datenbankzugriff folgen. Aufzählungstypen werden über das native PlantUML-Schlüsselwort `enum` abgebildet (kein zusätzlicher Stereotyp nötig).
- Jedes Diagramm mit `@startuml <Name>` / `@enduml` und aussagekräftigem Diagrammnamen beginnen/beenden

Vollständige Notationsregeln, Legende und ausführliches Beispiel (basierend auf dem Projekt-Techstack): siehe [plantuml-notation.md](./references/plantuml-notation.md).

## Vorgehen: Klassensicht erstellen

1. Komponentensicht lesen ([komponentensicht.md](../../../arc/statische_sichten/komponentensicht.md), falls vorhanden): zu verfeinernde Komponente/Teilkomponente und deren externe Beziehungen übernehmen, insbesondere alle **eingehenden** externen Beziehungen (Aufrufe anderer Komponenten/Akteure auf die verfeinerte Komponente).
2. Anhand des [Kriteriums für Klassenverfeinerung](#kriterium-für-klassenverfeinerung) prüfen, ob die Komponente/Teilkomponente überhaupt ein Klassendiagramm benötigt.
3. Fachliche Entitäten und technische Bausteine der Komponente aus Epics/User Stories/FRs und Techstack identifizieren (z. B. Station, Messwert, Messgröße, Repository).
4. Für jede eingehende externe Beziehung aus Schritt 1 ein `interface` gemäß [Schnittstellen nach außen](#schnittstellen-nach-außen-pflicht) modellieren; die intern zuständige Klasse realisiert dieses Interface.
5. Für jede Klasse/Schnittstelle/Enum Name, relevante Attribute (mit Typ) und relevante Methoden (mit Signatur) knapp ergänzen – nur die für die Architektur wichtige öffentliche Schnittstelle, keine vollständige Implementierung.
6. Beziehungen zwischen den Klassen bestimmen (Vererbung, Realisierung, Assoziation mit Multiplizität, Aggregation, Komposition) gemäß Notation oben.
7. Diagramm erstellen: Datei `klassensicht-<komponente>.puml`.
8. Prüfen, dass jede Klasse eindeutig dieser einen Komponente/Teilkomponente zugeordnet ist, jede eingehende externe Beziehung als Interface abgebildet ist und keine externe Beziehung der Komponente aus der Komponentensicht verloren geht.
9. Diagramm in `klassensicht.md` einbinden und Klassen zusätzlich tabellarisch erläutern (Klasse, Verantwortung, wichtigste Attribute/Methoden).
10. Kurz-Selbstcheck (siehe Checkliste unten) durchgehen, bevor die Klassensicht als fertig/Review markiert wird.

## Vorgehen: Klassensicht reviewen

1. `klassensicht.md` sowie alle `.puml`-Dateien lesen; zusätzlich `komponentensicht.md` lesen, falls vorhanden.
2. **Konsistenz zur Komponentensicht**: Ist jede Klasse eindeutig einer Komponente/Teilkomponente zugeordnet? Bleiben externe Beziehungen der Komponente erhalten?
3. **Schnittstellen nach außen**: Ist für jede eingehende externe Beziehung aus der Komponentensicht ein explizites `interface`-Element vorhanden ([siehe Regel](#schnittstellen-nach-außen-pflicht)), das von der zuständigen Klasse realisiert wird? Fehlt eine solche Schnittstelle, ist das ein `❌`.
4. Für **jede** Klasse/Schnittstelle/Enum:
   - **Verantwortung**: Ist klar, wofür die Klasse zuständig ist? Keine Überlappung mit anderen Klassen?
   - **Attribute/Methoden**: Sind nur architektur-relevante, öffentliche Elemente gezeigt (keine vollständige Implementierung, keine überflüssigen Hilfsmethoden)?
   - **Notation**: Entspricht das Element der Notation oben (`class`/`interface`/`enum`, Sichtbarkeit, Typangaben)?
4. Für **jede** Beziehung: Ist der Beziehungstyp (Vererbung/Realisierung/Assoziation/Aggregation/Komposition/Abhängigkeit) fachlich korrekt gewählt und mit passender Multiplizität/Beschriftung versehen?
5. Anhand des [Kriteriums für Klassenverfeinerung](#kriterium-für-klassenverfeinerung) prüfen, ob eine Verfeinerung an Stellen **fehlt** oder umgekehrt **unnötig** vorhanden ist.
6. Ergebnis als Tabelle ausgeben (Format siehe unten).
7. Bei `⚠️`/`❌`: konkreten Korrekturvorschlag (inkl. angepasstem PlantUML-Ausschnitt) liefern, keine reine Kritik ohne Lösung.
8. Fazit: Gesamteinschätzung und Empfehlung (z. B. "Klassensicht konsistent zur Komponentensicht" / "Beziehung X zu Y falsch typisiert" / "Klasse Z fehlt Attribut aus FR-026").

### Review-Ausgabeformat

```markdown
## Klassensicht-Review

| # | Klasse / Beziehung | Konsistenz zur Komponentensicht ✅/⚠️/❌ | Verantwortung klar ✅/⚠️/❌ | Notation ✅/⚠️/❌ | Anmerkung / Vorschlag |
|---|---|---|---|---|---|
| 1 | Station | ... | ... | ... | ... |
| 2 | Station "1" --> "0..*" Messwert | ... | ... | ... | ... |

**Fazit:** <Gesamteinschätzung + empfohlener nächster Schritt>
```

## Schnell-Checkliste (für Erstellung und Review gleichermaßen)

- [ ] Jede Klasse ist eindeutig einer Komponente/Teilkomponente aus der Komponentensicht zugeordnet
- [ ] Jede eingehende externe Beziehung aus der Komponentensicht ist als explizites `interface`-Element modelliert und wird von der zuständigen Klasse realisiert (`..|>`)
- [ ] Klassendiagramme existieren genau dort, wo das Kriterium für Klassenverfeinerung zutrifft (nicht mehr, nicht weniger)
- [ ] Jede Klasse hat eine eindeutige, überlappungsfreie Verantwortung
- [ ] Nur architektur-relevante Attribute/Methoden gezeigt (keine vollständige Implementierung)
- [ ] Stereotypen (`<<dataclass>>`, `<<Protocol>>`, `<<Repository>>`) sind bei zutreffenden Python-Konstrukten gesetzt
- [ ] Beziehungstyp (Vererbung/Realisierung/Assoziation/Aggregation/Komposition/Abhängigkeit) ist jeweils fachlich korrekt gewählt
- [ ] Multiplizitäten und Beschriftungen an Assoziationen sind vorhanden und sinnvoll
- [ ] Externe Beziehungen der verfeinerten Komponente stimmen mit der Komponentensicht überein
- [ ] Reines UML ohne C4-Includes, gültige `@startuml`/`@enduml`-Blöcke
- [ ] Diagramme liegen unter `arc/statische_sichten/` und sind in `klassensicht.md` eingebunden
