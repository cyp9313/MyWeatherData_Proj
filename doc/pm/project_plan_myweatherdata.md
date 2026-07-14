# Projektplan - MyWeatherData

## Planungsannahmen

- **Team:** 2 Entwickler mit durchschnittlicher Produktivität
- **Sprint-Länge:** 2 Wochen (10 Arbeitstage)
- **Initiale Velocity:** 13 Story Points pro Sprint
- **Gesamtaufwand:** 39 Story Points (ggf. 40-45 SP nach USER_STORY_07 Split)
- **Releases:** MVP (Datenhaltung + Backend), Integration (UI), Release Candidate (optimiert)
- **Technische Reihenfolge:** DWD-API → Datenbank-Import → Export/Visualisierung → UI-Integration
- **Abhängigkeitsmanagement:** Epic-weise Reihenfolge: EPIC_01 → EPIC_02 → EPIC_03 + EPIC_04

---

## Work Breakdown Structure

```
MyWeatherData Project
│
├── EPIC_01: DWD-Datenanbindung (11 SP)
│   ├── USER_STORY_01: Stationssuche (3 SP)
│   └── USER_STORY_02: Datenabruf (8 SP)
│
├── EPIC_02: Lokale Datenhaltung (10 SP)
│   ├── USER_STORY_03: Duplikatfreier Import (5 SP)
│   └── USER_STORY_04: CSV/JSON-Export (5 SP)
│
├── EPIC_03: Steuerungs-UI (5 SP)
│   ├── USER_STORY_05: Parameter erfassen (3 SP)
│   └── USER_STORY_06: Status anzeigen (2 SP)
│
└── EPIC_04: Visualisierung (13 SP)
    ├── USER_STORY_07: Zeitreihen-Chart (8 SP)
    └── USER_STORY_08: PNG-Export (5 SP)
```

---

## Sprintplan

### Sprint 1: DWD-API & Datenbankgrundlagen (2 Wochen)

| Sprint | Ziel | Stories | Story Points | Lieferobjekte | Abhaengigkeiten |
|---|---|---|---:|---|---|
| **Sprint 1** | Externe Datenanbindung + lokale Persistenz etablieren | USER_STORY_01, USER_STORY_02 | **11 SP** | DWD-API-Client, SQLite-Schema, erste Messwerte in DB | DWD-API-Dokumentation verfügbar; SQLite-Umgebung aufgesetzt |

**Sprint 1 Breakdown:**
- **USER_STORY_01 (3 SP):** Stationssuche (Geo-Algorithmus, Fehlerbehandlung)
  - Deliverable: Stationssuche-Funktion mit Unit-Tests
  - Zuständigkeit: Dev 1
  - Abhängigkeit: DWD-Stationsliste verfügbar

- **USER_STORY_02 (8 SP):** Wetterdaten abrufen (API-Integration, Parsing, Error Handling)
  - Deliverable: API-Client, Datenmodell, Fehlerprotokolle
  - Zuständigkeit: Dev 2 (parallel mit Dev 1)
  - Abhängigkeit: USER_STORY_01 muss abgeschlossen sein (Stationsreferenz)
  - Integrationspunkt: USER_STORY_01 Result wird als Input genutzt

**Sprint 1 Risiken:**
- DWD-API-Dokumentation unvollständig → Zeitpuffer +3 Tage
- API-Rate-Limits nicht kommuniziert → Backoff-Logik ggf. erforderlich

**Sprint 1 Akzeptanzkriterien:**
- ✓ Stationssuche funktioniert für mind. 5 Test-Koordinaten
- ✓ API-Abruf liefert Daten für alle 4 Kategorien
- ✓ Fehler (Netzwerk, ungültige Koordinate) werden abgefangen und protokolliert

---

### Sprint 2: Persistenz, Import & Export (2 Wochen)

| Sprint | Ziel | Stories | Story Points | Lieferobjekte | Abhaengigkeiten |
|---|---|---|---:|---|---|
| **Sprint 2** | Lokale Datenspeicherung mit Duplikatschutz + Exportfunktionen | USER_STORY_03, USER_STORY_04 | **10 SP** | DB-Schema finalisiert, Import-Logik mit Tests, CSV/JSON-Exporter | Abruff-Funktionen aus Sprint 1 stabil; DB-Schema abstimmung abgeschlossen |

**Sprint 2 Breakdown:**
- **USER_STORY_03 (5 SP):** Duplikatfreier Import (Schema-Design, Batch-Import, Protokollierung)
  - Deliverable: SQL-Schema (Stationen, Messwerte), Import-Funktion, Tests
  - Zuständigkeit: Dev 1
  - Abhängigkeit: USER_STORY_02 muss abgeschlossen sein (Datenquelle)
  - Design-Review mit Tech-Lead vor Umsetzung

- **USER_STORY_04 (5 SP):** CSV/JSON-Export (Filterlogik, Formate, Fehlerbehandlung)
  - Deliverable: CSV/JSON-Exportmodule, Feldmapping-Dokument, Tests
  - Zuständigkeit: Dev 2 (parallel)
  - Abhängigkeit: USER_STORY_03 muss abgeschlossen sein (Datenbasis)

**Sprint 2 Integrationspunkte:**
- Dev 1 liefert DB-Schema → Dev 2 nutzt es für Export-Queries
- Gemeinsame Definition: Filter-Operatoren (AND, OR, Datumsgrenzen), Feldlisten

**Sprint 2 Risiken:**
- CSV-/JSON-Feldlisten nicht finalisiert → Blockade für USER_STORY_04
- Große Datenmengen (11 Jahre) könnten zu langsam sein → Indexierungs-Optimierung notwendig

**Sprint 2 Akzeptanzkriterien:**
- ✓ 1000 Messwerte können importiert werden ohne Duplikate
- ✓ CSV/JSON-Export liefert gültige, parsierbare Dateien
- ✓ Leere Ergebnismengen blocken Dateierzeugung

---

### Sprint 3: UI-Erfassung & Status-Anzeige (2 Wochen)

| Sprint | Ziel | Stories | Story Points | Lieferobjekte | Abhaengigkeiten |
|---|---|---|---:|---|---|
| **Sprint 3** | Benutzerinteraktion für Parametererfassung + Prozessüberwachung | USER_STORY_05, USER_STORY_06 | **5 SP** | UI-Komponenten (Eingabefelder, Status-Display), End-to-End-Workflow | Backend-APIs (Abruf, Import, Export) stabil; UI-Framework aufgesetzt |

**Sprint 3 Breakdown:**
- **USER_STORY_05 (3 SP):** Parametererfassung und Validierung (Koordinaten, Datum, Kategorien)
  - Deliverable: UI-Formular mit Client-seitiger Validierung, Fehlermarkierung
  - Zuständigkeit: Dev 1 (Frontend-Lead)
  - Abhängigkeit: Koordinaten-Format-Spezifikation muss vorliegen

- **USER_STORY_06 (2 SP):** Prozessstatus transparent anzeigen (State Management, Event-Handling)
  - Deliverable: Status-Komponente, Backend→Frontend Status-Updates
  - Zuständigkeit: Dev 2 (parallel, ggf. mit Dev 1-Support)
  - Abhängigkeit: Async-Execution-Model muss definiert sein (Polling vs. WebSocket)

**Sprint 3 Integrationspunkte:**
- USER_STORY_05 triggert Backend-Abruf/Speicher → USER_STORY_06 zeigt Status
- Test: User füllt Form → Start-Button wird enabled → Prozess beginnt → Status "laufend" angezeigt

**Sprint 3 Risiken:**
- Koordinaten-Input-Format zu strikt → Nutzer-Frustration → UX-Anpassung
- Async-Status-Updates verzögert → Nutzer denkt Anwendung hängt

**Sprint 3 Akzeptanzkriterien:**
- ✓ Form validiert Pflichtfelder
- ✓ Ungültige Datumsreihenfolge wird blockiert
- ✓ Status wechselt sichtbar von "laufend" → "abgeschlossen"

---

### Sprint 4: Visualisierung & Export (2-3 Wochen)

| Sprint | Ziel | Stories | Story Points | Lieferobjekte | Abhaengigkeiten |
|---|---|---|---:|---|---|
| **Sprint 4** | Zeitreihencharts + Bildexport; Integrierter Prototyp | USER_STORY_07, USER_STORY_08 (ggf. gesplittet) | **8-13 SP** | Charting-Integration, Aggregations-Logik, PNG-Export; Demo-Datensatz | Datenbank + UI-Grundlagen funktionstüchtig |

**Sprint 4 Breakdown:**
- **USER_STORY_07 (8 SP):** Zeitreihencharts pro Kategorie
  - Deliverable: Charting-Komponenten (täglich, monatlich, jährlich), Aggregations-Formeln, Datenluecken-Kennzeichnung
  - Zuständigkeit: Dev 2 (Visualisierungs-Lead)
  - Dependencies: Aggregations-Formeln müssen vor Sprint 4 geklärt sein (KRITISCH)
  - Integrationspunkt: Filterdaten von USER_STORY_05 + Datenbank aus USER_STORY_03

  ⚠ **Wenn US_07 vor Sprint 3 gesplittet wird (empfohlen):**
  - **US_07a (5 SP):** Basis-Charting + Aggregation
    - Sprint 4, Dev 2, erste Hälfte
  - **US_07b (3-5 SP):** Lückenkennzeichnung + Leerdaten-Handling
    - Sprint 4, Dev 2, zweite Hälfte oder Sprint 5

- **USER_STORY_08 (5 SP):** PNG-Export der aktuellen Visualisierung
  - Deliverable: PNG-Export-Modul, Fehlerbehandlung, Integration mit Charting-Lib
  - Zuständigkeit: Dev 1 (oder parallelisiert mit Dev 2)
  - Abhängigkeit: USER_STORY_07 muss abgeschlossen sein (Chart existiert)

**Sprint 4 Integrationspunkte:**
- User stellt Parameter ein → Chart zeigt gefilterte Daten → User klickt PNG-Export → Datei gespeichert
- End-to-End-Test: Stationssuche → Abruf → Speicher → Export → Visualisierung → PNG

**Sprint 4 Risiken:**
- Charting-Library-Performance mit 4000+ Datenpunkten unzureichend → Client-side Aggregation erforderlich
- USER_STORY_07 Aggregations-Anforderungen unklar → Design-Review vor Sprint

**Sprint 4 Akzeptanzkriterien:**
- ✓ Chart zeigt korrekte Aggregation (täglich, monatlich, jährlich)
- ✓ Datenluecken sind visuell erkennbar
- ✓ PNG-Export funktioniert ohne Fehler
- ✓ Leerdatenzustand wird unterschieden vom Fehler

---

## Meilensteine

| Meilenstein | Sprint | Datum | Zustand | Kriterium |
|---|---|---|---|---|
| **M1: MVP (Backend)** | Nach Sprint 2 | ~Woche 4 | Abgeschlossen | Abruf + Speicher + Export funktionierend; getestet mit Realdata |
| **M2: Integration (MVP + UI)** | Nach Sprint 3 | ~Woche 6 | Abgeschlossen | End-to-End-Workflow (Parameter → Abruf → Export) im UI verfügbar |
| **M3: Release Candidate** | Nach Sprint 4 | ~Woche 8 | Abgeschlossen | Visualisierung, PNG-Export; alle User Stories abgeschlossen; Performance-Tests bestanden |
| **M4: Release** | Nach Sprint 4+ | ~Woche 9-10 | Geplant | QA-Tests, Dokumentation, Go-Live-Vorbereitung |

---

## Kritischer Pfad

```
START
  ↓
USER_STORY_01 (Stationssuche) [3 SP]  ← EPICS_01 Startpunkt
  ↓ (Abhängigkeit)
USER_STORY_02 (Datenabruf) [8 SP]     ← CRITICAL: externe API-Stabilität
  ↓ (Abhängigkeit)
USER_STORY_03 (DB Import) [5 SP]      ← CRITICAL: Datenbankschema
  ↓ (Abhängigkeit)
USER_STORY_04 (Export) [5 SP]         ← parallel möglich mit USER_STORY_05/06
  ↓
USER_STORY_05 (UI-Parameter) [3 SP]   ← UI-Frontend Startpunkt
USER_STORY_06 (Status-UI) [2 SP]      ← Parallel, triggert Backend
  ↓
USER_STORY_07 (Charting) [8 SP]       ← CRITICAL: Charting-Library Performance
  ↓ (Abhängigkeit)
USER_STORY_08 (PNG-Export) [5 SP]     ← Abhängig von Chart
  ↓
END (Release Candidate)
```

**Kritische Pfad-Länge (Sequenziell):** USER_STORY_01 → 02 → 03 → 07 → 08 = 29 SP
**Parallelisierung:** USER_STORY_04, USER_STORY_05, USER_STORY_06 können teils parallel laufen, reduzieren aber nicht CP.
**Engpässe:** USER_STORY_02 (API-Stabilität), USER_STORY_07 (Charting-Performance)

---

## Parallelisierungsstrategie

### Sprint 1:
- **Dev 1:** USER_STORY_01 (Stationssuche) [3 SP]
- **Dev 2:** USER_STORY_02 (Datenabruf) [8 SP]
- **Abhängigkeit:** Dev 2 warten auf USER_STORY_01, dann Integration für 1-2 Tage
- **Ergebnis:** 11 SP in 10 Arbeitstagen → Geschätzte Velocity 11 SP ✓

### Sprint 2:
- **Dev 1:** USER_STORY_03 (DB-Import) [5 SP]
- **Dev 2:** USER_STORY_04 (CSV/JSON-Export) [5 SP]
- **Abhängigkeit:** Dev 2 warten auf Dev 1 DB-Schema (Tage 1-2), dann 3-4 Tage parallel
- **Ergebnis:** 10 SP in 10 Arbeitstagen → Velocity 10 SP ✓

### Sprint 3:
- **Dev 1:** USER_STORY_05 (UI-Parameter) [3 SP]
- **Dev 2:** USER_STORY_06 (Status-UI) [2 SP]
- **Abhängigkeit:** Keine; können vollständig parallel
- **Ergebnis:** 5 SP in 10 Arbeitstagen → Velocity 5 SP (unter-ausgelastet, aber Puffer für Integration/Testing)

### Sprint 4:
- **Dev 1:** USER_STORY_08 (PNG-Export) [5 SP]
- **Dev 2:** USER_STORY_07 (Charting) [8 SP]
- **Abhängigkeit:** Dev 1 wartet auf Dev 2 Chart (Tage 1-5), dann PNG-Export
- **Ergebnis:** 8-13 SP in 10 Arbeitstagen → Velocity 8-13 SP (je nach US_07 Split)

---

## Ressourcen & Kapazität

| Phase | Dev 1 | Dev 2 | Tech-Lead (shared) | Aufwand QA | Puffer |
|---|---|---|---|---|---|
| **Sprint 1** | USER_STORY_01 (3 SP) | USER_STORY_02 (8 SP) | API-Doku, Schema-Review | 2 Tage | 1 Tag |
| **Sprint 2** | USER_STORY_03 (5 SP) | USER_STORY_04 (5 SP) | Schema-Review, Export-Format | 2 Tage | 1 Tag |
| **Sprint 3** | USER_STORY_05 (3 SP) | USER_STORY_06 (2 SP) | Async-Model Review | 1 Tag | 2 Tage (unter-ausgelastet) |
| **Sprint 4** | USER_STORY_08 (5 SP) | USER_STORY_07 (8 SP) | Performance-Review | 2-3 Tage | 1 Tag |
| **Total** | **16 SP** | **23 SP** | ~4-5 Tage | ~7-9 Tage | 5 Tage |

**Anmerkung:** Dev 2 hat höhere Last (Backend/Charting-fokussiert). Bei Bottleneck: Dev 1 unterstützen.

---

## Meilenstein-Kriterien

### M1: MVP (Backend) – Nach Sprint 2
- ✓ USER_STORY_01, 02, 03 abgeschlossen
- ✓ DWD-API erfolgreich getestet mit echten Stationen
- ✓ Mindestens 500 Messwerte in SQLite importiert
- ✓ CSV/JSON-Export funktioniert
- ✓ Fehlerbehandlung getestet (Netzwerk, ungültige Koordinate, Duplikate)
- ✓ Projekt-Dokumentation aktualisiert

### M2: Integration (MVP + UI) – Nach Sprint 3
- ✓ USER_STORY_04, 05, 06 abgeschlossen
- ✓ End-to-End-Workflow: UI-Input → Backend-Abruf → Speicher → Export möglich
- ✓ Status-Anzeige funktioniert
- ✓ Alle Validierungen im UI aktiv
- ✓ Integration-Tests bestanden (UI + Backend zusammen)
- ✓ User-Dokumentation (Getting Started)

### M3: Release Candidate – Nach Sprint 4
- ✓ USER_STORY_07, 08 abgeschlossen
- ✓ Alle 8 User Stories abgeschlossen
- ✓ 39 Story Points vollständig umgesetzt
- ✓ Performance-Tests bestanden (4000+ Datenpunkte)
- ✓ Visualisierung + PNG-Export funktionieren
- ✓ Alle Akzeptanzkriterien erfüllt
- ✓ QA-Sign-off erhalten

---

## Risiken & Pufferstrategie

| Risiko | Sprint(s) | Puffer | Gegenmassnahme |
|---|---|---|---|
| DWD-API-Dokumentation unvollständig | Sprint 1 | +3 Tage | API-Spike vor Sprint 1; ggf. Reverse-Engineering |
| Charting-Library Performance | Sprint 4 | +2 Tage | Proof-of-Concept mit 4000+ Datenpunkten vor Sprint 4 |
| USER_STORY_07 Aggregations-Anforderungen unklar | Sprint 3 | +3 Tage | Sprint 3 Design-Review mit Fachanwender |
| Koordinaten-Eingabe-Format-Verwirrung | Sprint 3 | +1 Tag | Klare UX-Richtlinien vor Sprint 3 |
| Datenbankschema nicht abstimmungsreif | Sprint 2 | +2 Tage | Early Schema-Review vor Sprint 2 |
| Netzwerkfehler in Real-Tests nicht reproduzierbar | Sprint 1-2 | +1 Tag | Mock-Server aufsetzen |

**Total Puffer pro Projekt:** ~12 Tage → 2-3 Tage pro Sprint

---

## Dependencies & Gating

### Gating-Kriterien (vor Sprint-Start):

| Sprint | Gate | Owner | Must-Have |
|---|---|---|---|
| **Sprint 1** | API-Readiness | Tech-Lead | DWD-API-Doku verfügbar; Zugang konfiguriert |
| **Sprint 2** | Schema-Review | Tech-Lead | DB-Schema finalisiert; Feld-Mappings klar |
| **Sprint 3** | Async-Model | Tech-Lead | Execution-Modell definiert (Threading, Events); Koordinaten-Format final |
| **Sprint 4** | Charting-Spike | Dev 2 | Charting-Library getestet; Performance O.K.; Aggregations-Formeln geklärt |

---

## Kommunikations-Plan

- **Daily Standups:** 9:00 Uhr, 15 Min, beide Devs + Tech-Lead
- **Sprint Planning:** Start jedes Sprints, Montag 10:00 Uhr
- **Sprint Review:** Ende jedes Sprints, Freitag 14:00 Uhr (mit Stakeholder)
- **Sprint Retrospective:** Ende jedes Sprints, Freitag 15:00 Uhr
- **Weekly Alignment:** Donnerstag 11:00 Uhr, Tech-Lead + Product Owner (Anforderungen klären)

---

## Zusammenfassung Projektplan

| Metrik | Wert |
|---|---|
| **Gesamtaufwand** | 39 Story Points |
| **Sprints geplant** | 4 (ggf. 4,5 bei US_07 Split) |
| **Team** | 2 Entwickler |
| **Sprint-Länge** | 2 Wochen |
| **Gesamtdauer (geplant)** | 8-10 Wochen (inkl. Puffer, Meilenstein-Validierung) |
| **Geschätzter Projektstart** | Woche 1 (Sprint 1) |
| **Geschätzter Release** | Woche 9-10 (M3: Release Candidate +1 Woche Go-Live) |
| **Kritischer Pfad** | USER_STORY_01 → 02 → 03 → 07 → 08 (29 SP sequenziell) |
| **Engpässe** | DWD-API-Stabilität, Charting-Performance |
| **Risiko-Puffer** | 12 Tage (2-3 Tage/Sprint) |

