# Risikoaudit - MyWeatherData

**Audit-Datum:** 2026-07-07  
**Auditor:** Risk_Auditor (Technical Review Mode)  
**Audit-Scope:** Aufwandsschaetzung, Projektplan, technische Machbarkeit, Integrationsrisiken  

---

## Audit-Fokus

Dieses Risikoaudit prüft den geplanten MyWeatherData-Projektplan kritisch auf:

1. **Versteckte Abhängigkeiten:** Cross-Epic-Dependencies, Integrationspunkte, Datenfluss-Risiken
2. **Unterschaetzter Aufwand:** Integrationsaufwand, Test-Aufwand, Fehlerbehandlung
3. **Datenqualitaets-Risiken:** DWD-Datenbestand-Probleme, Zeitstempel-Inconsistencies, Kategorien-Luecken
4. **Test-Luecken:** Ungetestete Szenarien, Edge Cases, Performance-Tests
5. **Planungsoptimismus:** Zu aggressive Velocity, unrealistische Parallelisierung, fehlende Puffer

---

## Hauptrisiken

| # | Risiko | Betroffene Stories | Wahrscheinlichkeit | Auswirkung | Gegenmassnahme | Plan B |
|---|---|---|---|---|---|---|
| **R1** | DWD-API dokumentation unvollstaendig oder API-Struktur aendert sich | USER_STORY_02 | **Hoch** | Sprint 1 blockiert; 5-10 Tage Verzoegerung | Spike-Task vor Sprint 1 (3-4 Tage) zur API-Dokumentation + Reverse-Engineering | Community-Forum DWD nutzen; ggf. alternative Datenquelle evaluieren |
| **R2** | DWD-API Rate-Limits oder Timeouts; unvollstaendige Datenbestaende fuer Kategorien/Stationen | USER_STORY_02 | **Hoch** | Fehlerbehandlung wird komplexer; USER_STORY_02 spaeter 5-8 SP statt 8 | Retries + Exponential-Backoff implementieren; Early Realdata-Tests (Sprint 1) mit 11-Jahres-Zeitraum | Caching-Strategie; lokale Datenbank-Fallback |
| **R3** | Charting-Bibliothek Performance unzureichend bei 4000+ Datenpunkten (11 Jahre taeglich) | USER_STORY_07, USER_STORY_08 | **Mittel** | Rendering-Lag; PNG-Export langsam; USER_STORY_07 wird groesser (8→13 SP) | Proof-of-Concept vor Sprint 4 mit echten 4000+ Points; ggf. Client-side Pre-Aggregation notwendig | Server-side Rendering; Datenpunkte auf 500er-Bins limitieren |
| **R4** | Datenbankschema nicht normalisiert; Duplikat-Detection fehleranfaellig | USER_STORY_03 | **Mittel** | Daten-Inkonsistenz; USER_STORY_04 Export liefert falsche Daten; Debugging-Aufwand +3 Tage | Early Schema-Review mit DB-Spezialist vor Sprint 2; Unit-Tests fuer Duplikat-Detection | Upsert-Logik statt UNIQUE-Constraint; manuelles Daten-Cleansing |
| **R5** | CSV/JSON-Feld-Definitionen nicht final vor USER_STORY_04 | USER_STORY_04 | **Mittel** | Rework + Re-Tests; Sprint 2 verlaengert sich um 2-3 Tage | Anforderungs-Review vor Sprint 2 mit Datenanalyst; Feldlisten in Requirement fixieren | Flexible Export-Formatierung; Custom-Feld-Selection im UI |
| **R6** | Koordinaten-Validierung zu strikt oder Eingabe-Format unklar | USER_STORY_01, USER_STORY_05 | **Mittel** | Nutzer-Frustration; UX-Aenderung in Sprint 3; +2 Tage | Koordinaten-Format vor Sprint 1 final definieren (Dezimal, Range, Separator); UX-Mock vor Sprint 3 | Flexible Input-Parser (mehrere Formate); Geocoding-Service als Alternative |
| **R7** | Async-Execution-Model nicht definiert (Threading vs. WebSocket vs. Polling) | USER_STORY_06 | **Mittel** | State-Management komplexer; USER_STORY_06 wird groesser (2→5 SP); Backend-Frontend-Coupling | Vor Sprint 3 klar definieren: Polling mit 1s-Intervall oder WebSocket? Tech-Decision-Record anfertigen | Simple Polling (kein WebSocket) als Fallback; synchrone Execution mit UI-Blockade (nicht ideal) |
| **R8** | Testaufwand unterschaetzt; Unit- + Integration-Tests vs. echte DWD-Daten | Alle Stories | **Hoch** | Test-Coverage unzureichend; Realdata-Fehler erst in QA erkannt; +5-7 Tage Nacharbeit | 20% Test-Puffer pro Sprint einplanen (2 Tage); Realdata-Tests ab Sprint 1; Integrations-Test-Suite aufbauen | Reduzierter Test-Scope; kritische Path-only getestet |
| **R9** | Netzwerkfehler, Timeout-Szenarien nicht reproduzierbar in Testumgebung | USER_STORY_02, USER_STORY_06 | **Mittel** | Fehlerbehandlung unzureichend; Produktions-Fehler treten auf; +3 Tage Debugging | Mock-DWD-Server vor Sprint 1 aufbauen; Chaos-Testing fuer Netzwerk-Fehler | Fault-Injection-Library; manuelles Network-Throttling |
| **R10** | Parallelisierung nicht realistisch; Dev-Blockaden durch Abhaengigkeiten | USER_STORY_02, USER_STORY_03, USER_STORY_07, USER_STORY_08 | **Mittel** | Warte-Zeiten; echte Velocity sinkt von 13 auf 9-10 SP/Sprint; +1-2 Sprints Erweiterung | Klare Abhaengigkeits-Sequenzialisierung; Pair-Programming bei kritischen Integrations-Punkten | Mehr Parallelisierbarkeit durch fruehe Stub-Integration; vertikale Story-Slicing |
| **R11** | Developer-Ausfallzeit (Krankheit, Turnover) | Alle Stories | **Niedrig** | Team verliert 50% Kapazitaet; Projektplan unmoeglich; +2-3 Wochen Verzoegerung | Wissenstransfer + Pair-Programming von Sprint 1 an; Dokumentation zeitnah | Externe Ressourcen reaktiviert; Prioritaeten auf MVP reduziert |
| **R12** | Stakeholder-Anforderungen aendern sich; Scope-Creep (z.B. neue Wetterkategorie) | USER_STORY_02, USER_STORY_05, USER_STORY_07 | **Mittel** | Zusaetzliche 5-13 SP; Meilensteine verschieben; +1 Sprint | Klare Scope-Fixierung in Sprint Planning; Change-Control-Prozess; Sprint-Goals nicht aendern | Prioritaets-Umgewichtung; nicht-MVP-Features in Sprint 5+ verschieben |
| **R13** | Zeitstempel-Format-Inconsistencies (UTC vs. local, Precision) zwischen DWD und DB | USER_STORY_02, USER_STORY_03 | **Mittel** | Duplikat-Detection schlaegt fehl; Visualisierung zeigt falsche Daten; +2-3 Tage Debugging | Vor Sprint 1: Zeitstempel-Standard definieren (UTC nur, Sekunden-Precision minimum); Unit-Tests fuer Konversion | Redundante Zeitstempel-Speicherung (Original + normalisiert) |
| **R14** | Visualisierung-Edge-Case: Single Datapoint oder sehr wenige Datenpunkte | USER_STORY_07 | **Niedrig** | Chart sieht verwirrend aus; User sieht nichts statt klarer "Keine Daten"-Meldung | USER_STORY_07 AC explizit auf Edge Cases (0, 1, 10 Points) testen | Simple Fallback-Meldung ("Unzureichend Daten"); keine Aggregation bei <10 Points |
| **R15** | PNG-Export fehlgeschlagen bei Dateiberechtigungen oder Speicherplatz | USER_STORY_08 | **Niedrig** | Export-Fehler; Nutzer blockiert; +1 Tag für UI-Error-Handling | Zielpfad-Validierung vor Export; Try-Catch + aussagekraeftige Fehlermeldung | Fallback auf Temp-Verzeichnis oder Clipboard-Copy |
| **R16** | Performance-Regression: Grosse Datenmengen (z.B. 500.000 Messwerte importiert) | USER_STORY_03, USER_STORY_04, USER_STORY_07 | **Niedrig** | Datenbankabfragen verlangsamen sich; Export/Visualisierung-Timeout; +2 Tage Indexierung | Fruehe Datenbankindizierung (Sprint 2); Load-Tests mit 100k+ Messwerte vor Sprint 4 | Datenbank-Partitionierung oder Archivierung alter Daten |

---

## Blinde Flecken

### B1: Integrationstest-Luecken
**Problem:** Planung deckt Unit-Tests, aber nicht ausreichend End-to-End-Integration.

**Szenario:** User waehlt Parameter im UI → Backend startet Abruf → API liefert Daten → Speicher verarbeitet → Export wird gezaehlt → Visualisierung wird aktualisiert.

**Test-Luecke:** Wie wird Status vom Abruf-Prozess (Tage 2-5 von Sprint 1) zum Frontend kommuniziert? KEINE Story deckt "Status-Channel-Aufbau" ab (z.B. Message-Queue, WebSocket-Handler).

**Gegenmassnahme:** USER_STORY_06 hat nur 2 SP; vermutlich unterschaetzt. Design-Review vor Sprint 3 erforderlich.

---

### B2: Datenqualitaets-Governance fehlt
**Problem:** DWD-Datensaetze koennen lueckenhaft sein (z.B. 2015: nur Temp+Niederschlag, aber kein Wind/Sonne).

**Szenario:** User ruft Daten 2015-01-01 bis 2015-12-31 fuer Station X, Kategorie Wind ab. DWD liefert 0 Datenpunkte. USER_STORY_02 AC sagt: "fehlende Kategorien klar ausgewiesen". Aber: Wie unterscheidet System "keine Daten vorhanden" von "Fehler beim Abruf"?

**Test-Luecke:** Realdata-Tests mit bekannten Datenluecken durchfuehren.

**Gegenmassnahme:** Integration-Test-Suite mit Mock-DWD-Responses aufbauen (vollstaendig, teilweise, leer). Vor Sprint 1 mit echten DWD-Daten validieren.

---

### B3: Exception-Handling-Strategie nicht vereinbar
**Problem:** 8 User Stories, aber keine zentrale Exception-Handling-Richtlinie dokumentiert.

**Szenario:**
- USER_STORY_02: API-Timeout → "Abruffehler" protokollieren
- USER_STORY_03: DB-Constraint-Violation → "Duplikat uebersprungen"
- USER_STORY_06: Status-Update-Fehler → "Status nicht aktualisiert"
- USER_STORY_07: Chart-Rendering-Fehler → "Leerdatenzustand"?

**Frage:** Werden diese konsistent behandelt? Wer loescht Fehler von frueheren Laufen?

**Test-Luecke:** Fehlerbehandlungs-Integrations-Tests fehlen.

**Gegenmassnahme:** Design-Review vor Sprint 1 mit Richtlinie: Exception-Kategorien (User-Fehler, Datenqualitaets-Fehler, Tech-Fehler) + Handlungslogik pro Kategorie.

---

### B4: Aggregations-Formel-Definitionen unklar fuer Wind & Sonne
**Problem:** USER_STORY_07 sagt "Aggregation taeglich, monatlich, jaehrlich" fuer 4 Kategorien, aber nicht WIE.

**Szenario:**
- Lufttemperatur: Durchschnitt (standard)
- Niederschlag: Summe (standard)
- Wind: ??? (Windgeschwindigkeit avg? oder Windrichtung avg? oder Windboeen max?)
- Sonneneinstrahlung: ??? (Summe kWh? oder durchschnitt W/m²?)

**Konsequenz:** USER_STORY_07 AC nicht testbar bis Formel-Definition. Risk: Sprint 4 blockiert.

**Gegenmassnahme:** Vor Sprint 3 Design-Review mit Fachanwender (Meteorologe/Analyst). Aggregations-Definitionen + Unit-Tests schreiben.

---

### B5: Fehler-Fallback bei DWD-API-Ausfall nicht betrachtet
**Problem:** Wenn DWD-API mehrere Stunden / Tage nicht verfuegbar ist, kann USER abrufen?

**Szenario:** User moechte Daten fuer Januar 2020 abrufen. DWD-API ist down. USER_STORY_02 gibt Fehler zurueck. USER sieht Meldung "Abruff-Fehler".

**Frage:** Kann User frueheren Export (wenn er bereits am 06.07. durchgefuehrt hat) nutzen statt Fehler zu bekommen?

**Test-Luecke:** Caching-Strategie nicht spezifiziert.

**Gegenmassnahme:** Caching-Entscheidung vor Sprint 1: Cache mit Ablauf-Datum? Nutzer-kontrolled Cache-Invalidation?

---

### B6: Skalierbarkeit begrenzt auf Single-Maschine
**Problem:** MyWeatherData benutzt SQLite (lokal). Wenn 100 Nutzer gleichzeitig Abrufe starten, kann SQLite Konkurrenz-Zugriffe nicht gut handhaben.

**Szenario:** 2 Nutzer starten parallel Abruf → beide triggern Datenbank-Insert. Locking? Write-Conflicts?

**Annahme in Plan:** 1 Nutzer, 1 Prozess. Skalierbarkeit kein Anforderung (MVP-Scope).

**Gegenmassnahme:** In Release-Notes dokumentieren "Single-Nutzer-Anwendung". Nicht relevant fuer MVP.

---

### B7: Test-Automatisierung-Infrastruktur fehlt
**Problem:** 39 SP umgesetzt, aber wer betreibt die Integrations-Test-Suite (Realdata, API-Mocks, DB-Snapshots)?

**Szenario:** Nach Sprint 1 hat Team Realdata-Tests geschrieben (z.B. Mock-DWD-Server, 5 Test-Cases). In Sprint 2 wird Test-Setup vergessen. In Sprint 3 sind Tests verwaist (neuer Code -> alte Tests failen).

**Gegenmassnahme:** Test-Infrastruktur-Task in Sprint 1 aufnehmen (ggf. 2-3 SP fuer CI/CD-Setup). Nicht separat schaetzen, sondern in USER_STORY_01 und USER_STORY_02 mitberuecksichtigen.

---

## Empfohlene Puffer

### Sprint-weise Puffer:

| Sprint | Geplant | Puffer | Grund |
|---|---|---:|---|---|
| **Sprint 1** | 11 SP | +3 Tage | DWD-API-Risiken, Spike-Aufwand |
| **Sprint 2** | 10 SP | +2 Tage | Schema-Designaufwand, Duplikat-Detection-Testing |
| **Sprint 3** | 5 SP | +2 Tage | Unter-ausgelastet; QA-Support, Dokumentation |
| **Sprint 4** | 8-13 SP | +3 Tage | Charting-Performance, PNG-Export-Edge-Cases |
| **Total Projekt-Puffer** | — | +10-12 Tage | Unvorhergesehene Probleme, Verzögerungen |

---

### Empfohlene Risikovorsichtsmassnah Men:

1. **Testing-Puffer:** +20% Aufwand fuer Tests pro Story (aktuell nicht separat geschaetzt)
   - Auswirkung: +8 SP für Testing gesamt
   - Loesung: Reduzierung auf kritische Pfad-Stories oder parallele Test-Automation

2. **Integration-Puffer:** +15% Aufwand fuer Abhaengigkeits-Aufloesung
   - Auswirkung: +6 SP
   - Loesung: Fruehe Integration zwischen Devs; tägliche Merge-Meetings

3. **Dokumentations-Puffer:** +10% Aufwand
   - Auswirkung: +4 SP
   - Loesung: Dokumentation inline mit Code (nicht separat)

**Gesamter Puffer-Empfehlung:** +15-20% auf Gesamtaufwand
- **Neue Gesamt-Schaetzung:** 39 SP + 8 SP (Tests) = **47 SP** (statt 39 SP)
- **Neue Projektdauer:** 4-5 Sprints (statt 4 Sprints)

---

## Entscheidungsempfehlung

### Status: ⚠ **BEDINGT GENEHMIGT**

**Genehmigung unter folgenden Bedingungen:**

1. **Vor Sprint 1 Start (Gating-Kriterium):**
   - [ ] DWD-API-Dokumentation final verfügbar; Zugang getestet
   - [ ] Zeitstempel-Standard definiert (UTC, Precision)
   - [ ] Exception-Handling-Richtlinie dokumentiert
   - [ ] Test-Infrastruktur-Plan erstellt (Mock-DWD, CI/CD, Test-DB)

2. **Vor Sprint 2 Start (Gating-Kriterium):**
   - [ ] Datenbankschema mit Spezialist reviewed
   - [ ] CSV/JSON-Feldlisten final
   - [ ] Duplikat-Detection-Test-Cases geschrieben

3. **Vor Sprint 3 Start (Gating-Kriterium):**
   - [ ] Async-Execution-Model definiert + Tech-Decision-Record
   - [ ] Koordinaten-Input-Format final
   - [ ] USER_STORY_07 verfeinert (Aggregations-Formeln geklärt) oder Split durchgeführt

4. **Vor Sprint 4 Start (Gating-Criteium):**
   - [ ] Charting-Library Proof-of-Concept mit 4000+ Datenpunkten durchgeführt
   - [ ] Performance-Benchmark O.K. (Render-Zeit < 2s)

### Planung ist realistisch, ABER:

- **Velocity-Annahme (13 SP/Sprint) ist optimistisch** fuer Team-Größe + Komplexität
- **Unterschaetzter Integrations- und Testaufwand** → +15-20% Puffer erforderlich
- **USER_STORY_07 kritisch** – muss vor Sprint 4 verfeinert sein
- **DWD-API-Ungewissheit** – kritisches Risiko in Sprint 1

### Empfohlene Massnahmen:

1. **Velocity realistisch halten:** Start mit 11 SP/Sprint (konservativ), auf 13+ nur mit Beweis
2. **Tägliche Integrations-Builds:** Fehler früh erkennen
3. **Realdata-Tests ab Sprint 1:** Keine "Happy Path Only"-Tests
4. **Dokumentation parallel:** Nicht am Ende
5. **Stakeholder-Alignment wöchentlich:** Scope-Creep verhindern

### Freigabe-Entscheidung:

- **FREIGEBEN für Planung** ✓ (Ist realistisch, aber mit Risiken)
- **NICHT FREIGEBEN ohne Gate-Validierung vor Sprint 1** ✗
- **Nach Sprint 1 Review:** Velocity + Risiken neu bewerten

---

## Risk-Tracking im Projekt

### Weekly Risk-Review Agenda:
- Status der Top-5-Risiken
- Neue Risiken identifizieren
- Gegenmassnahmen umsetzen
- Velocity vs. Schaetzung vergleichen

### Risiko-Eskalations-Kriterien:
- Velocity < 10 SP zwei Sprints hintereinander → Scope reduzieren oder Sprint-Laenge erhoehen
- DWD-API nicht verfügbar > 1 Tag → Fallback-Datenquelle evaluieren
- Charting-Performance Render-Zeit > 3s → Engine wechseln
- Testabdeckung < 60% → Priorität-Umgewichtung

---

## Zusammenfassung Risikoaudit

| Kategorie | Status | Bemerkung |
|---|---|---|
| **Aufwandsschaetzung** | ⚠ Optimistisch | 39 SP realistisch, aber +20% Puffer empfohlen |
| **Integrationsaufwand** | ⚠ Unterschaetzt | USER_STORY_02↔03, USER_STORY_07↔08 Integrationen komplex |
| **Datenqualitaets-Risiken** | ⚠ Hoch | DWD-API-Volatilität, Zeitstempel-Konsistenz |
| **Test-Luecken** | ⚠ Gross | Realdata-Tests, Exception-Handling-Tests fehlen |
| **Planungsoptimismus** | ⚠ Hoch | Velocity 13 SP zu optimistisch; Parallelisierung begrenzt |
| **Abhaengigkeits-Management** | ⚠ Kritisch | USER_STORY_02→03→07 sequenziell; Engpässe wahrscheinlich |

**Gesamtbewertung: REALISTISCHER PLAN MIT HOHEM RISIKO**

Freigabe empfohlen mit strikter Gate-Validierung vor Sprint-Starts.

