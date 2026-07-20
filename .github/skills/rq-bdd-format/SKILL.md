---
name: rq-bdd-format
description: 'Erstellen und Reviewen von Akzeptanzkriterien für User Stories im Behavior Driven Development (BDD) Format Gegeben/Wenn/Dann (Gherkin-Stil). Use when: Akzeptanzkriterien einer User Story unter req/user-story/ formuliert, ergänzt oder auf Qualität/Testbarkeit geprüft werden sollen, oder wenn Gegeben/Wenn/Dann-Szenarien geschrieben, geschnitten oder reviewt werden sollen.'
---

# BDD-Format (Gegeben/Wenn/Dann) für User Stories

## Zweck

Dieser Skill stellt das Behavior Driven Development (BDD) Format **Gegeben/Wenn/Dann** als Standard für Akzeptanzkriterien von User Stories bereit ([TEMPLATE-user-story.md](../../../req/user-story/TEMPLATE-user-story.md), Abschnitt "Akzeptanzkriterien"). Er wird in zwei Situationen genutzt:

1. **Erstellen** von Gegeben/Wenn/Dann-Szenarien für eine neue oder bestehende User Story
2. **Reviewen** vorhandener Akzeptanzkriterien auf Format- und Qualitätskonformität

## Gegeben/Wenn/Dann im Überblick

| Baustein | Bedeutung | Beantwortet die Frage |
|---|---|---|
| **Gegeben** | Ausgangssituation / Kontext / Vorbedingung | In welchem Zustand befindet sich das System vorher? |
| **Wenn** | Auslösende Aktion / Ereignis | Was tut der Nutzer / was passiert? |
| **Dann** | Erwartetes, prüfbares Ergebnis | Woran erkennt man objektiv, dass es funktioniert hat? |

Jedes Szenario beschreibt **genau eine** Regel/ein Verhalten. Details, Stilregeln (deklarativ statt imperativ, Umgang mit "And", Anti-Patterns) und Positiv-/Negativ-Beispiele: siehe [bdd-best-practices.md](./references/bdd-best-practices.md).

## Vorgehen: Akzeptanzkriterien erstellen

1. User-Story-Satz ("Als ... möchte ich ... damit ...") und Beschreibung lesen, um den fachlichen Kontext zu verstehen.
2. Alle relevanten **Regeln/Verhaltensweisen** der Story identifizieren (z.B. Happy Path, Validierungsfehler, Grenzfälle, Berechtigungen, leere/fehlerhafte Daten).
3. Für jede Regel ein eigenes Szenario formulieren:
   - **Gegeben**: konkreter, minimal notwendiger Ausgangszustand (keine überflüssigen Details).
   - **Wenn**: genau eine Aktion/ein Ereignis, aktiv formuliert.
   - **Dann**: objektiv, messbar prüfbares Ergebnis – keine vagen Begriffe ("schnell", "korrekt", "sinnvoll") ohne konkrete Größe.
4. Fachbegriffe konsistent zur restlichen Story/zum Glossar verwenden (ubiquitäre Sprache).
5. Neben dem Happy Path mindestens einen **Negativ-/Fehlerfall** und relevante **Randfälle** (Grenzwerte, leere Eingaben, fehlende Berechtigung) ergänzen.
6. Szenarien nummeriert im Abschnitt "Akzeptanzkriterien" der User-Story-Datei eintragen (Format siehe Template).
7. Kurz-Selbstcheck (siehe Checkliste unten) durchgehen, bevor Status auf `Review` gesetzt wird.

## Vorgehen: Akzeptanzkriterien reviewen

1. Abschnitt "Akzeptanzkriterien" der User Story lesen.
2. Für **jedes** Szenario prüfen:
   - **Format**: Sind Gegeben/Wenn/Dann vollständig, klar getrennt und korrekt benannt?
   - **Ein Verhalten pro Szenario**: Kein Szenario testet mehrere unabhängige Regeln gleichzeitig (Warnsignal: mehrere "Wenn" oder unverbundene "Und"-Ketten).
   - **Testbarkeit**: Ist das "Dann" objektiv und ohne Interpretationsspielraum prüfbar?
   - **Stil**: Deklarativ (was passiert) statt imperativ (Klick-für-Klick-UI-Beschreibung)?
   - **Konsistenz**: Fachbegriffe passen zur User Story / zum Glossar.
3. Abdeckung auf Story-Ebene prüfen: Sind Happy Path, mindestens ein Negativfall und relevante Randfälle vorhanden?
4. Ergebnis als Tabelle ausgeben (Format siehe unten).
5. Bei `⚠️`/`❌`: konkreten Formulierungsvorschlag liefern, keine reine Kritik ohne Lösung.
6. Fazit: Gesamteinschätzung und Empfehlung (z.B. "Akzeptanzkriterien vollständig" / "Negativfall ergänzen" / "Szenario X splitten").

### Review-Ausgabeformat

```markdown
## BDD-Review: US-<ID> <Titel>

| # | Szenario | Format ✅/⚠️/❌ | Ein Verhalten ✅/⚠️/❌ | Testbarkeit ✅/⚠️/❌ | Anmerkung / Vorschlag |
|---|---|---|---|---|---|
| 1 | <Kurzbezeichnung> | ... | ... | ... | ... |
| 2 | <Kurzbezeichnung> | ... | ... | ... | ... |

**Abdeckung:** Happy Path ✅/❌ · Negativfall ✅/❌ · Randfälle ✅/❌

**Fazit:** <Gesamteinschätzung + empfohlener nächster Schritt>
```

## Schnell-Checkliste (für Erstellung und Review gleichermaßen)

- [ ] Jedes Szenario hat genau ein Gegeben, ein Wenn und ein Dann (bzw. klar abgegrenzte "Und"-Ergänzungen)
- [ ] Jedes Szenario prüft genau eine Regel/ein Verhalten
- [ ] "Dann" ist objektiv messbar, keine vagen Formulierungen
- [ ] Deklarativer Stil (fachliches Verhalten), keine UI-Klickpfade
- [ ] Happy Path + mind. 1 Negativ-/Fehlerfall + relevante Randfälle vorhanden
- [ ] Konsistente Fachbegriffe (passend zu Story/Glossar)
