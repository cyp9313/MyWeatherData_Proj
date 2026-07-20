---
name: rq-invest-criteria
description: 'Anwendung des INVEST-Prinzips (Independent, Negotiable, Valuable, Estimable, Small, Testable) beim Erstellen und Reviewen von User Stories. Use when: eine User Story unter req/user-story/ erstellt, formuliert, geschätzt, geschnitten (Story Splitting) oder reviewt werden soll, oder wenn die Qualität von Akzeptanzkriterien geprüft werden soll.'
---

# INVEST-Kriterien für User Stories

## Zweck

Dieser Skill stellt das INVEST-Prinzip als Qualitätsmaßstab für User Stories bereit. Er wird in zwei Situationen genutzt:

1. **Erstellen** einer neuen User Story (Datei unter `req/user-story/`, Basis: [TEMPLATE-user-story.md](../../../req/user-story/TEMPLATE-user-story.md))
2. **Reviewen** einer bestehenden User Story auf INVEST-Konformität

## Die 6 INVEST-Kriterien im Überblick

| Buchstabe | Kriterium | Kurzbeschreibung |
|---|---|---|
| **I** | Independent (unabhängig) | Story steht für sich, ist ohne Blockade durch andere Stories planbar/umsetzbar |
| **N** | Negotiable (verhandelbar) | Kein starres Pflichtenheft, sondern Diskussionsgrundlage zwischen PO/Kunde und Team |
| **V** | Valuable (wertvoll) | Erkennbarer, messbarer Mehrwert für Nutzer, Kunde oder Business |
| **E** | Estimable (schätzbar) | Team kann Aufwand/Komplexität/Risiko grob einschätzen (z.B. Story Points) |
| **S** | Small (klein) | Umsetzbar, testbar und auslieferbar innerhalb eines Sprints (typ. 2–3 Wochen) |
| **T** | Testable (testbar) | Klar und objektiv prüfbar über konkrete Akzeptanzkriterien |

Für das **T-Kriterium** (Formulierung und Review von Gegeben/Wenn/Dann-Akzeptanzkriterien im Detail) siehe den Skill [rq-bdd-format](../rq-bdd-format/SKILL.md).

Detaillierte Prüffragen, Red Flags und Positiv-/Negativ-Beispiele je Kriterium: siehe [invest-kriterien-details.md](./references/invest-kriterien-details.md).

## Vorgehen: User Story erstellen

1. Template kopieren: `req/user-story/TEMPLATE-user-story.md` → neue Datei `US-<ID>-<kurztitel>.md` gemäß Namenskonvention aus [req/README.md](../../../req/README.md).
2. "Als ... möchte ich ... damit ..."-Satz formulieren und dabei **V (Valuable)** und **N (Negotiable)** im Blick behalten: der Nutzen muss klar erkennbar sein, die Formulierung darf keine technische Lösung vorschreiben.
3. Zuschnitt der Story anhand **I (Independent)** und **S (Small)** prüfen: Lässt sie sich unabhängig von anderen offenen Stories umsetzen? Passt sie in einen Sprint? Falls nicht: Story splitten (z.B. nach Workflow-Schritten, Datenvarianten, CRUD-Operationen oder Business-Regeln).
4. Akzeptanzkriterien im Gegeben/Wenn/Dann-Format ergänzen – das ist die Grundlage für **T (Testable)**. Jedes Kriterium muss objektiv verifizierbar sein (keine vagen Begriffe wie "schnell", "benutzerfreundlich" ohne Messgröße). Details zu Formulierung und Struktur: siehe [rq-bdd-format](../rq-bdd-format/SKILL.md).
5. Grobe Schätzbarkeit gegenchecken (**E**): Sind Kontext, Abhängigkeiten und Umfang so klar beschrieben, dass das Team Aufwand/Risiko einschätzen könnte? Falls offene Fragen bestehen, unter "Anmerkungen" festhalten.
6. Abschließend alle 6 Kriterien als Kurz-Selbstcheck durchgehen (siehe Checkliste unten) und Status setzen (`Draft` → `Review`).

## Vorgehen: User Story reviewen

1. Story vollständig lesen (User-Story-Satz, Beschreibung, Akzeptanzkriterien, Abhängigkeiten, verknüpfte FRs).
2. Für **jedes** der 6 INVEST-Kriterien bewerten: `✅ erfüllt` / `⚠️ teilweise` / `❌ nicht erfüllt`, jeweils mit kurzer Begründung anhand der Prüffragen aus [invest-kriterien-details.md](./references/invest-kriterien-details.md).
3. Ergebnis als Tabelle ausgeben (Format siehe unten).
4. Bei `⚠️`/`❌`: konkreten, umsetzbaren Verbesserungsvorschlag geben (z.B. Formulierungsvorschlag, Splitting-Vorschlag, fehlendes Akzeptanzkriterium ergänzen) – keine reine Kritik ohne Lösungsvorschlag.
5. Fazit: Gesamteinschätzung (INVEST-konform / mit Überarbeitung konform / grundlegend zu überarbeiten) und Empfehlung für nächsten Status.

### Review-Ausgabeformat

```markdown
## INVEST-Review: US-<ID> <Titel>

| Kriterium | Bewertung | Begründung | Empfehlung |
|---|---|---|---|
| I – Independent | ✅/⚠️/❌ | ... | ... |
| N – Negotiable | ✅/⚠️/❌ | ... | ... |
| V – Valuable | ✅/⚠️/❌ | ... | ... |
| E – Estimable | ✅/⚠️/❌ | ... | ... |
| S – Small | ✅/⚠️/❌ | ... | ... |
| T – Testable | ✅/⚠️/❌ | ... | ... |

**Fazit:** <Gesamteinschätzung + empfohlener nächster Schritt>
```

## Schnell-Checkliste (für Erstellung und Review gleichermaßen)

- [ ] Story ist ohne Abhängigkeit zu offenen/blockierenden Stories umsetzbar (I)
- [ ] Formulierung schreibt keine Lösung vor, lässt Raum für Gespräch (N)
- [ ] Nutzen für Rolle/Kunde/Business ist explizit erkennbar (V)
- [ ] Umfang ist klar genug für eine grobe Aufwandsschätzung (E)
- [ ] Story passt in einen Sprint; sonst splitten (S)
- [ ] Mind. 1 objektiv prüfbares Gegeben/Wenn/Dann-Akzeptanzkriterium vorhanden (T)
