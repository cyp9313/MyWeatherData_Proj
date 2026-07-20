---
name: rq-ears-syntax
description: 'Erstellen und Reviewen von Functional Requirements im EARS-Format (Easy Approach to Requirements Syntax: Ubiquitous, Event-Driven, State-Driven, Unwanted Behavior, Optional Feature, Complex). Use when: ein Functional Requirement unter req/functional-requirement/ formuliert, ergänzt oder auf Eindeutigkeit/Testbarkeit geprüft werden soll, oder wenn Anforderungssätze nach EARS-Mustern geschrieben, klassifiziert oder reviewt werden sollen.'
---

# EARS-Syntax für Functional Requirements

## Zweck

Dieser Skill stellt **EARS (Easy Approach to Requirements Syntax)** als Standard für die Formulierung von Functional Requirements bereit ([TEMPLATE-functional-requirement.md](../../../req/functional-requirement/TEMPLATE-functional-requirement.md), primär Abschnitt "Beschreibung", ergänzend "Fehlerfälle / Randbedingungen"). Er wird in zwei Situationen genutzt:

1. **Erstellen** eines neuen oder Ergänzen eines bestehenden Functional Requirements im passenden EARS-Pattern
2. **Reviewen** vorhandener Anforderungssätze auf Format-, Eindeutigkeits- und Testbarkeitskonformität

## Die 6 EARS-Pattern im Überblick

| # | Pattern | Wann nutzen | Syntax | Beispiel |
|---|---|---|---|---|
| 1 | **Ubiquitous** (Allgegenwärtig) | Fundamentale Eigenschaft, die immer gilt, ohne Trigger/Zustand | Das [System] muss [Systemantwort] | "Das Kameramodul muss einen Bildwinkel von 120 Grad abdecken." |
| 2 | **Event-Driven** (Ereignisgesteuert) | System reagiert nur bei Eintreten eines Ereignisses (Trigger) | Wenn [Trigger], muss [System] [Systemantwort] | "Wenn der Mute-Button gedrückt wird, muss das Infotainment-System alle Audioausgaben stummschalten." |
| 3 | **State-Driven** (Zustandsgesteuert) | Verhalten gilt, solange ein Zustand andauert | Solange [Zustand], muss/darf [System] [Systemantwort] | "Solange sich das Fahrzeug im Wartungsmodus befindet, darf das Motorsteuergerät keine OTA-Updates installieren." |
| 4 | **Unwanted Behavior** (Unerwünschtes Verhalten) | Fehlerfälle, Ausfälle, Störungen, Grenzüberschreitungen abfangen | Wenn [Unerwünschtes Ereignis], dann muss [System] [Systemantwort] | "Wenn die errechnete Fluggeschwindigkeit nicht verfügbar ist, muss das Kontrollsystem die modellierte Fluggeschwindigkeit nutzen." |
| 5 | **Optional Feature** (Optionale Funktion) | Verhalten gilt nur bei bestimmter Ausbaustufe/vorhandenem Feature | Wo [Feature vorhanden], muss das [System] [Systemantwort] | "Wo ein Radarsensor verbaut ist, muss die Software den adaptiven Tempomaten aktivieren." |
| 6 | **Complex** (Kombination) | Vorbedingungen, Zustände und Ereignisse kommen zusammen | Wo [Feature], solange [Zustand], wenn [Trigger], dann muss das [System] [Systemantwort] (Reihenfolge immer: Wo → Solange → Wenn → Dann; nicht benötigte Teile entfallen) | "Solange das Flugzeug am Boden ist, wenn Umkehrschub befohlen wird, dann muss das Kontrollsystem den Einsatz der Schubumkehr ermöglichen." |

Detaillierte Erläuterungen je Pattern, weitere Beispiele und Anti-Patterns: siehe [ears-best-practices.md](./references/ears-best-practices.md).

## Entscheidungshilfe: Welches Pattern passt?

1. Gilt die Anforderung **immer**, ohne speziellen Auslöser, Zustand oder optionales Feature? → **Ubiquitous**
2. Soll das System **einmalig auf ein Ereignis reagieren**? → **Event-Driven**
3. Gilt das Verhalten **nur solange** ein bestimmter Zustand andauert? → **State-Driven**
4. Behandelt die Anforderung einen **Fehler, Ausfall oder eine Grenzüberschreitung**? → **Unwanted Behavior**
5. Gilt die Anforderung **nur bei einer bestimmten Ausbaustufe/einem optionalen Feature**? → **Optional Feature**
6. Kommen **mehrere** der obigen Bedingungen (Feature, Zustand, Trigger) gleichzeitig vor? → **Complex** (Teile in korrekter Reihenfolge kombinieren)

## Vorgehen: Functional Requirement erstellen

1. Systemname festlegen und im gesamten FR konsistent verwenden (konkrete Komponente statt pauschal "das System", z.B. "das Importmodul", "die Konfigurationsoberfläche").
2. Für jede fachliche Regel prüfen, ob ein Trigger, ein Zustand, ein Fehlerfall oder ein optionales Feature vorliegt (siehe Entscheidungshilfe oben).
3. Passendes EARS-Pattern wählen und Anforderungssatz exakt nach dessen Syntax formulieren.
4. Systemantwort aktiv formulieren, mit "muss" (Pflicht) bzw. "darf"/"darf nicht" (Erlaubnis/Verbot) – keine vagen Begriffe ("schnell", "sinnvoll", "korrekt") ohne konkrete Größe.
5. Genau **eine** Anforderung pro Satz. Mehrere unabhängige Regeln nicht mit "und" verketten, sondern als separate FRs/Sätze führen.
6. Ergebnis in den Abschnitt "Beschreibung" der FR-Datei eintragen. Fehlerfälle (Unwanted Behavior) zusätzlich unter "Fehlerfälle / Randbedingungen" auflisten, damit sie an beiden Stellen konsistent sind.
7. Kurz-Selbstcheck (siehe Checkliste unten) durchgehen, bevor Status auf `Review` gesetzt wird.

## Vorgehen: Functional Requirement reviewen

1. Abschnitte "Beschreibung", "Verarbeitungslogik / Ablauf" und "Fehlerfälle / Randbedingungen" der FR-Datei lesen.
2. Für **jeden** Anforderungssatz:
   - **Pattern erkennen**: Welches der 6 EARS-Pattern liegt vor (oder sollte vorliegen)?
   - **Format**: Entspricht der Satz exakt der Syntax des erkannten Patterns (richtige Reihenfolge, keine fehlenden Bausteine)?
   - **Eindeutigkeit**: Genau eine Anforderung pro Satz, kein Vermischen mehrerer Regeln?
   - **Testbarkeit**: Ist die Systemantwort objektiv und messbar prüfbar?
   - **Konsistenz**: Systemname konkret und einheitlich verwendet?
3. Ergebnis als Tabelle ausgeben (Format siehe unten).
4. Bei `⚠️`/`❌`: konkreten Formulierungsvorschlag im korrekten EARS-Pattern liefern, keine reine Kritik ohne Lösung.
5. Fazit: Gesamteinschätzung und Empfehlung (z.B. "EARS-konform" / "Fehlerfall als Unwanted Behavior ergänzen" / "Satz X in zwei Anforderungen splitten").

### Review-Ausgabeformat

```markdown
## EARS-Review: FR-<ID> <Titel>

| # | Anforderungssatz (Ist) | Erkanntes Pattern | Format ✅/⚠️/❌ | Testbarkeit ✅/⚠️/❌ | Vorschlag (Soll) |
|---|---|---|---|---|---|
| 1 | <Satz> | ... | ... | ... | ... |
| 2 | <Satz> | ... | ... | ... | ... |

**Fazit:** <Gesamteinschätzung + empfohlener nächster Schritt>
```

## Schnell-Checkliste (für Erstellung und Review gleichermaßen)

- [ ] Jeder Satz folgt exakt einem EARS-Pattern (Ubiquitous, Event-Driven, State-Driven, Unwanted Behavior, Optional Feature oder Complex)
- [ ] Bei Complex-Sätzen: Reihenfolge Wo → Solange → Wenn → Dann eingehalten
- [ ] Systemname ist konkret und konsistent (keine pauschale "das System"-Formulierung, wenn eine Komponente gemeint ist)
- [ ] Systemantwort ist mit "muss"/"darf"/"darf nicht" formuliert und objektiv messbar
- [ ] Genau eine Anforderung pro Satz, keine Verkettung unabhängiger Regeln mit "und"
- [ ] Fehlerfälle nutzen das Unwanted-Behavior-Pattern und sind auch unter "Fehlerfälle / Randbedingungen" gelistet
