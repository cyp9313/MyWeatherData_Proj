# Aufwandsschätzung MyWeatherData

**Projekt:** Wetterdatenbank und Visualisierung (MyWeatherData)

**Quelle:** `doc/req/user_story_myweatherdata.md`, `doc/req/functional_requirement_myweatherdata.md`

**Methode:** Agile Schätzung mit Story Points (Fibonacci: 1, 2, 3, 5, 8, 13)

**Datum:** 2026-07-07

**Schätzer:** Agile_Estimator

---

## Zusammenfassung

| User Story | Punkte | Status | Empfehlung |
|---|---:|---|---|
| USER_STORY_01 | 3 | ✓ Ready | Akzeptieren |
| USER_STORY_02 | 5 | ✓ Ready | Akzeptieren |
| USER_STORY_03 | 3 | ✓ Ready | Akzeptieren |
| USER_STORY_04 | 5 | ✓ Ready | Akzeptieren |
| USER_STORY_05 | 3 | ✓ Ready | Akzeptieren |
| USER_STORY_06 | 5 | ✓ Ready | Akzeptieren |
| USER_STORY_07 | 8 | ⚠ Teilweise Ready | Verfeinern |
| USER_STORY_08 | 5 | ✓ Ready | Akzeptieren |
| **Gesamt** | **37** | — | — |

---

## Detaillierte Schätzungen

---

## USER_STORY_01: Naechstgelegene DWD-Station fuer Koordinaten bestimmen

**Quelle Epics & FRs:** EPIC_01 • FR_01, FR_02, FR_03

### Story Points: 3

### Begruendung

Moderate Komplexität mit drei klaren Aufwandstreibern:
1. **Geografische Validierung** (FR_01): Koordinate prüfen, ob innerhalb Deutschlands. Klare Regel, aber geodätische Genauigkeit erforderlich.
2. **Distanzberechnung** (FR_02): Haversine- oder ähnliche Formel zur nächsten Station. Bekannte Algorithmen, aber erfordert Test mit Edge Cases (Grenzkoordinaten, äquatornahe Berechnung).
3. **Fehlerbehandlung** (FR_03): Fehlerzustände bei ungültiger Koordinate und fehlender Station. Klare Negativ-Cases testbar.

Annahmen:
- DWD-Stationenverzeichnis ist vorhanden oder leicht abrufbar.
- Geometrie-Bibliothek (z.B. Geopy) ist verfügbar.

### Definition of Ready

✓ **Erfüllt:**
- Zielgruppe (Fachanwender) ist klar.
- Akzeptanzkriterien sind testbar (positive: gültige Koordinate → Station; negative: außerhalb Deutschlands → Fehler).
- Functional Requirements (FR_01-03) sind vollständig zugeordnet.
- Fachliche Grenzen klar (Deutschland, nächste Station).
- Keine blockierenden Abhängigkeiten.

### Abhängigkeiten

- **Technisch:** DWD-Stationenverzeichnis muss vorhanden sein.
- **Funktional:** Keine vorgelagerten Stories; Basis für USER_STORY_02.

### Aufwandstreiber & Edge Cases

| Treiber | Komplexität | Testfall |
|---|---|---|
| Koordinatenvalidierung | Niedrig | (48.5, 13.4) = München ✓; (90, 180) = Außerhalb ✗ |
| Distanzberechnung | Moderat | Mehrere Stationen ähnlicher Distanz; Grenzkoordinaten |
| Fehlerberichte | Niedrig | Klare Meldung pro Fehlertyp |

### Risiken / Blind Spots

- **Datenqualität DWD-Stationen:** Wenn Stationenverzeichnis unvollständig oder fehlerhaft, können gültige Koordinaten als „keine Station" bewertet werden.
- **Geodätische Genauigkeit:** Distanzformel muss tatsächlich nächste Station liefern (z.B. keine Verwechslung Luftlinie vs. Landmasse).

### Testaufwand

- Unit-Tests: 3-4 Test-Cases (valide Koordinaten, Grenzfälle, außerhalb).
- Integrations-Tests: Stationsverzeichnis-Abfrage validieren.
- Geschätzter Test-Aufwand: 1-2 Tage.

### Empfehlung

**Akzeptieren** – Story ist klar, unabhängig, mit wenigen Annahmen.

---

## USER_STORY_02: Wetterdaten fuer gueltigen Zeitraum abrufen

**Quelle Epics & FRs:** EPIC_01 • FR_04, FR_05, FR_06, FR_07

### Story Points: 5

### Begruendung

Höhere Komplexität durch vier signifikante Aufwandstreiber:
1. **Externe Datenquelle (DWD):** API-Integration mit unbekannter Struktur/Schnittstelle erfordert Dokumentationsstudium und möglicherweise Adapter-Code.
2. **Zeitraumvalidierung (FR_04):** Begrenzung auf 01.01.2015–31.12.2025; einfache Regel, aber muss im Request durchgesetzt werden.
3. **Multi-Kategorie-Parsing (FR_05):** Vier verschiedene Wetterkategorien (Lufttemperatur, Niederschlag, Wind, Sonneneinstrahlung) bedeuten möglicherweise unterschiedliche Datenformate/Endpoints.
4. **Fehlerbehandlung & Protokollierung (FR_06, FR_07):** Netzwerkfehler, Datenlücken, teilweise fehlende Kategorien müssen unterschieden und protokolliert werden.

Annahmen:
- DWD-API hat stabile, dokumentierte Schnittstelle.
- Datenformat ist strukturiert (z.B. JSON oder CSV).
- Netzwerk-Timeouts sind vorhersehbar.

### Definition of Ready

✓ **Erfüllt:**
- User Story ist Value-fokussiert: Nutzer erhält historische Wetterdaten.
- Akzeptanzkriterien sind testbar (erfolgreicher Abruf, Zeitraum-Validierung, Fehlerfall Netzwerk, Teilverfügbarkeit).
- FRs sind vollständig zugeordnet (FR_04-07).
- Fachliche Grenzen klar (Zeitraum, vier Kategorien).

⚠ **Teilweise Lücken:**
- DWD-API-Details nicht dokumentiert. Abhängigkeit unklar, wer API-Dokumente bereitstellt.

### Abhängigkeiten

- **Technisch:** DWD CDC API-Zugriff, ggf. API-Key/-Authentifizierung.
- **Funktional:** USER_STORY_01 sollte vor oder parallel (Station muss vorhanden sein).

### Aufwandstreiber & Edge Cases

| Treiber | Komplexität | Testfall |
|---|---|---|
| API-Anbindung | Hoch | Happy Path: validste Station, Zeitraum 01.01.2020–31.12.2020, alle 4 Kategorien ✓ |
| Zeitraum-Validierung | Niedrig | Start vor 2015 ✗; Ende nach 2025 ✗; gütiger Bereich ✓ |
| Multi-Kategorie-Parsing | Moderat | Alle 4 verfügbar ✓; 3 verfügbar, 1 fehlend ⚠; keine verfügbar ✗ |
| Netzwerkfehler | Moderat | Timeout, 5xx Error, DNS-Fehler → Fehler protokollieren |

### Risiken / Blind Spots

- **API-Änderungen:** DWD könnte Datenformat/Struktur ändern. Response-Parsing könnte fragil sein.
- **Datenqualität:** Nicht alle Kategorien sind für alle Stationen/Zeiträume verfügbar. Fehlerbehandlung muss robust sein.
- **Performance:** Großer Zeitraum (11 Jahre) mit vielen Stationen könnte zu großen Payloads führen. Pagination unklar.

### Testaufwand

- Unit-Tests: Zeitraum-Validierung (3-4 Cases).
- Integrations-Tests: API-Mock für verschiedene Erfolgs-/Fehlerfälle (5-6 Cases).
- End-to-End-Test: Echter DWD-API-Aufruf mit validem Zeitraum (1-2 Cases).
- Geschätzter Test-Aufwand: 2-3 Tage.

### Empfehlung

**Akzeptieren** – Story ist unabhängig, aber erfordert API-Dokumentation. Vor Sprint sollte API-Struktur geklärt sein.

---

## USER_STORY_03: Importierte Messwerte ohne Duplikate speichern

**Quelle Epics & FRs:** EPIC_02 • FR_08, FR_09, FR_10

### Story Points: 3

### Begruendung

Moderate Komplexität, aber bekannte Muster:
1. **Datenbankschema:** Eindeutiger Key aus (Station, Zeitstempel, Kategorie). Standard-Normalisierung.
2. **Duplikat-Detection (FR_08, FR_09):** UNIQUE-Constraint oder Upsert-Logik. Klare Regel, einfach zu implementieren.
3. **Formatvalidierung (FR_10):** Eingehende Daten müssen auf strukturelle Gültigkeit geprüft werden. Standard-Validierung.
4. **Protokollierung:** Fehlerhafte/übersprungene Records zählen und loggen.

Annahmen:
- SQLite (oder andere lokale DB) ist ausgewählt.
- Datenmodell (Station, Messwert, Zeitstempel, Kategorie) ist klar.

### Definition of Ready

✓ **Erfüllt:**
- User Story fokussiert auf Persistenz ohne Duplikate.
- Akzeptanzkriterien sind testbar (neue Werte speichern, Duplikate verhindern, Format-Fehler verwerfen).
- FRs sind vollständig (FR_08-10).

### Abhängigkeiten

- **Technisch:** Datenbankverbindung, SQLite-Setup.
- **Funktional:** Daten von USER_STORY_02 (Abruf), liefert Basis für USER_STORY_04, USER_STORY_07.

### Aufwandstreiber & Edge Cases

| Treiber | Komplexität | Testfall |
|---|---|---|
| Datenbank-Schema | Niedrig | UNIQUE (station_id, timestamp, category) |
| Duplikat-Erkennung | Niedrig | 2x gleicher Record → 1x gespeichert, 1x übersprungen |
| Formatvalidierung | Niedrig | Gütiger Record ✓; NULL-Werte ✗; falsche Typen ✗ |
| Protokollierung | Sehr niedrig | Counts der übersprungenen Records loggen |

### Risiken / Blind Spots

- **Zeitstempel-Genauigkeit:** Wenn Zeitstempel-Format zwischen Quell- und Zieldatenbank unterschiedlich, könnte Duplikat-Detection fehlerhafte Ergebnisse liefern (z.B. 2020-01-01T00:00:00Z vs. 2020-01-01 00:00:00).
- **Keine Konflikt-Auflösung:** Wenn Wert für identische (Station, Timestamp, Category) unterschiedlich ist, wird einfach übersprungen. Update-Szenario nicht adressiert.

### Testaufwand

- Unit-Tests: 4-5 Cases (neue Daten, Duplikate, Format-Fehler, Timestamps).
- Integrations-Tests: Datenbank-Operationen validieren.
- Geschätzter Test-Aufwand: 1-2 Tage.

### Empfehlung

**Akzeptieren** – Story ist klar, mit bekannten Mustern. Keine blockierenden Abhängigkeiten.

---

## USER_STORY_04: Gefilterte Wetterdaten als CSV oder JSON exportieren

**Quelle Epics & FRs:** EPIC_02 • FR_11, FR_12, FR_13, FR_14

### Story Points: 5

### Begruendung

Mittlere bis höhere Komplexität durch:
1. **Gefilterte Abfrage (FR_11):** SQL-Query nach Standort (Station), Zeitraum (Start/End) und Kategorie. Klare Filterlogik, aber mehrere Bedingungen.
2. **CSV-Format (FR_12):** Comma-Separated Values mit dokumentierten Pflichtfeldern. Quoting, Escaping, Datum-Formate müssen korrekt sein.
3. **JSON-Format (FR_13):** Strukturierte JSON-Ausgabe. Ebenfalls dokumentiert, aber unterschiedliche Fehlerfall-Behandlung als CSV.
4. **Leerdaten-Handling (FR_14):** Bei 0 Zeilen keine Datei erzeugen, nur Meldung. Zusätzliche Bedingung.

Annahmen:
- Filterparameter werden vom UI/Aufrufer validiert (siehe USER_STORY_05).
- CSV-/JSON-Struktur ist in Anforderungen dokumentiert.

### Definition of Ready

✓ **Erfüllt:**
- User Story ist Value-fokussiert: Nutzer kann Daten extern nutzen.
- Akzeptanzkriterien sind testbar (CSV/JSON-Format, Filter-Treue, Leer-Fall).
- FRs sind vollständig (FR_11-14).

⚠ **Teilweise Lücken:**
- CSV- und JSON-Feld-Dokumentation nicht in Story. Annahme: existiert woanders oder ist abstimmbar (Story sagt „dokumentierte Pflichtfelder").

### Abhängigkeiten

- **Technisch:** Datenbank-Zugriff, CSV-/JSON-Serialisierung.
- **Funktional:** Daten von USER_STORY_03 (Persistenz), Input von USER_STORY_05 (Filterparameter).

### Aufwandstreiber & Edge Cases

| Treiber | Komplexität | Testfall |
|---|---|---|
| SQL-Filter | Moderat | Station + Zeitraum + Kategorie; nur 1 Filter; keine Filter (alle Daten) |
| CSV-Export | Moderat | Quoting/Escaping bei Komma/Zeilenumbruch in Daten; Datum-Format konsistent |
| JSON-Export | Moderat | Nested-Struktur (Array von Objects); Unicode-Escaping; große Payloads |
| Leer-Handling | Niedrig | Wenn 0 Rows → keine Datei, nur Meldung |

### Risiken / Blind Spots

- **Dateischreibrechte:** FR_14 und allgemein nicht adressiert: Was wenn Zielordner nicht beschreibbar? (Siehe USER_STORY_08 für PNG, aber hier auch relevant.)
- **Große Datenmengen:** 11-Jahres-Zeitraum mit hoher Auflösung könnte Gigabyte erzeugen. Memory-Handling bei Streaming vs. buffering unklar.
- **Character-Encoding:** CSV-Dateien können UTF-8 oder andere Codierungen haben. Muss konsistent sein.

### Testaufwand

- Unit-Tests: 6-7 Cases (Filter-Kombinationen, CSV-Format, JSON-Format, Leer).
- Integrations-Tests: Datenbank-Abfrage + Datei-Erzeugung.
- End-to-End-Test: Exportierte Datei in extern nutzbarem Tool validieren.
- Geschätzter Test-Aufwand: 2-3 Tage.

### Empfehlung

**Akzeptieren** – Story ist unabhängig, aber erfordert Klarheit auf CSV-/JSON-Struktur vor Sprint.

---

## USER_STORY_05: Suchparameter im UI erfassen und validieren

**Quelle Epics & FRs:** EPIC_03 • FR_15, FR_16

### Story Points: 3

### Begruendung

Moderate Komplexität, fokussiert auf UI-Eingabelogik:
1. **Koordinaten-Eingabefeld:** Formatierung (Dezimal-Koordinaten?), Validierung gegen Deutschland (mit USER_STORY_01 koordinieren).
2. **Datums-Eingabefelder:** Start/End-Datum, innerhalb 01.01.2015–31.12.2025. Kalender-Widget oder Text-Eingabe.
3. **Kategorien-Checkboxen:** Mindestens 1 von 4 auswählen. UI-State-Verwaltung.
4. **Pflichtfeld-Markierung (FR_15):** Fehlende Felder visuell markieren.
5. **Datumsreihenfolge-Validierung (FR_16):** Enddatum >= Startdatum.

Annahmen:
- UI-Framework ist ausgewählt (z.B. React, Svelte, Vue).
- Validierungslogik kann auch Backend-seitig erfolgen (Client + Server).

### Definition of Ready

✓ **Erfüllt:**
- User Story ist klar: Nutzer erfasst Parameter, validiert zu bekommen.
- Akzeptanzkriterien sind testbar (Koordinate akzeptiert, Datum im Bereich, Enddatum >= Startdatum, Fehlende Felder blockieren).
- FRs sind zugeordnet (FR_15, FR_16).

### Abhängigkeiten

- **Technisch:** UI-Framework-Setup, ggf. Koordinaten-Parsing-Bibliothek.
- **Funktional:** Keine direkten Abhängigkeiten. INPUT zu USER_STORY_06.

### Aufwandstreiber & Edge Cases

| Treiber | Komplexität | Testfall |
|---|---|---|
| Koordinaten-Eingabe | Moderat | "48.5, 13.4" (München) ✓; "91, 0" (außerhalb) → Fehler |
| Datums-Eingabe | Niedrig | 01.01.2015 ✓; 31.12.2025 ✓; 01.01.2014 ✗; 01.01.2026 ✗ |
| Kategorien-Auswahl | Niedrig | Min. 1 Kategorie ✓; 0 Kategorien → Blockieren |
| Datumsreihenfolge | Niedrig | Start: 01.01.2020, End: 31.12.2020 ✓; Start: 31.12.2020, End: 01.01.2020 ✗ |

### Risiken / Blind Spots

- **Koordinaten-Format-Varianzen:** Nutzer könnte eingeben: "48.5 13.4", "48° 30' N, 13° 24' E", "EPSG:4326", etc. Nur Dezimal-Format dokumentiert?
- **Zeitzone-Verwechslungen:** Wenn Nutzer Uhrzeit eingibt (z.B. "01.01.2020 12:00 CET"), wird es verkompliziert.
- **UX-Detail:** Wenn Nutzer nur Enddatum ändert und es vor Startdatum liegt, sollte Fehler in Echtzeit oder erst bei Submit?

### Testaufwand

- Component-Tests: 6-8 Cases (gültige/ungültige Eingaben).
- Integration-Tests: Form-Submit mit vollständigen/unvollständigen Daten.
- E2E-Tests: User-Szenarien (gültige Eingabe → enabled Submit-Button; ungültige → disabled).
- Geschätzter Test-Aufwand: 1-2 Tage.

### Empfehlung

**Akzeptieren** – Story ist UI-fokussiert, unabhängig, mit klarem Scope. Koordinaten-Format sollte vor Sprint geklärt sein.

---

## USER_STORY_06: Prozessstatus im UI transparent anzeigen

**Quelle Epics & FRs:** EPIC_03 • FR_17, FR_18

### Story Points: 5

### Begruendung

Mittlere Komplexität durch:
1. **Asynchrone Ausführung:** Abruf + Speicherung läuft im Hintergrund oder Worker. UI muss Status-Updates erhalten (via Polling, WebSocket, Callbacks).
2. **Statusverwaltung:** Mehrere Zustände (laufend, abgeschlossen, Fehler) mit unterschiedlichen Rueckmeldungen (FR_17, FR_18).
3. **Fehlerzuordnung (FR_18):** Welcher Schritt ist fehlgeschlagen? (Abruf vs. Speicherung). Meldung muss aussagekräftig sein.
4. **State-Lifecycle:** Nach neuem Start müssen alte Fehler gelöscht werden.

Annahmen:
- Async-Execution (z.B. Backend-Job, Web Worker) ist vorhanden.
- Status-Updates sind durch Aufrufer an UI übermittelbar (z.B. Event-Listeners, State-Management).

### Definition of Ready

✓ **Erfüllt:**
- User Story ist klar: Nutzer sieht Fortschritt.
- Akzeptanzkriterien sind testbar (Status laufend/abgeschlossen/Fehler, Fehlerzuordnung, State-Cleanup).
- FRs sind zugeordnet (FR_17, FR_18).

⚠ **Teilweise Lücken:**
- Wie wird async-Status vom Abruf/Speicher-Prozess zum UI kommuniziert? Nicht spezifiziert.
- Wie granular sollte Fehlerzuordnung sein? („Abruffehler" vs. „DWD-API-Timeout" vs. „Netzwerkfehler")?

### Abhängigkeiten

- **Technisch:** Async-Execution-Model (Backend-Job, Thread, Worker), Status-Update-Mechanismus.
- **Funktional:** INPUT von USER_STORY_05 (Start triggert Abruf+Speicher), OUTPUT zu USER_STORY_07 (Visualisierung auf Datenspeicherung warten).

### Aufwandstreiber & Edge Cases

| Treiber | Komplexität | Testfall |
|---|---|---|
| Async-Status-Tracking | Moderat | Start → "laufend" angezeigt; nach 5 Sekunden → "abgeschlossen" |
| Fehlerzuordnung | Moderat | Abruff-Fehler → "Abruff: DWD-API timeout"; Speicher-Fehler → "Speicher: Datenbankfehler" |
| State-Cleanup | Niedrig | Neuer Start → alter Fehler gelöscht; "laufend" ersetzt "abgeschlossen" |
| UI-Updates | Moderat | Status-Anzeige re-rendered; keine veralteten Meldungen |

### Risiken / Blind Spots

- **Race Conditions:** Wenn Nutzer mehrfach Start klickt, könnten Prozesse sich überlappen. Nur 1 gleichzeitiger Prozess?
- **Timeout/Stalled:** Wenn Status „laufend" für zu lange bleibt, denkt Nutzer Anwendung hängt. Timeout + Auto-Fehler?
- **Fehler-Details-Balance:** Zu viele technische Details verwirren, zu wenige helfen nicht bei Debugging.

### Testaufwand

- Unit-Tests: Status-Zustandsübergänge (4-5 Cases).
- Integrations-Tests: Async-Ausführung mit Status-Updates (3-4 Cases).
- E2E-Tests: User-Sicht (Start → Laufend → Abgeschlossen; Start → Laufend → Fehler).
- Geschätzter Test-Aufwand: 2-3 Tage.

### Empfehlung

**Akzeptieren** – Story ist wichtig für UX. Vor Sprint sollte Async-Execution-Model geklärt sein (Threading, WebSocket vs. Polling?).

---

## USER_STORY_07: Zeitreihen pro Wetterkategorie analysieren

**Quelle Epics & FRs:** EPIC_04 • FR_19, FR_20, FR_21

### Story Points: 8

### Begruendung

**Höchste Komplexität** mit vier signifikanten Aufwandstreibern:

1. **Visualisierungs-Bibliothek:** Zeitreihenchart (z.B. Chart.js, D3.js, Plotly). Integration, API-Nutzung, Custom-Styling.
2. **Aggregations-Logik (FR_19):** Täglich, monatlich, jährlich. Unterschiedliche Aggregationen (Durchschnitt für Temp, Summe für Niederschlag, Min/Max für Wind). Kategorieabhängig, nicht einheitlich.
3. **Datenluecken-Kennzeichnung (FR_20):** Visuelle Darstellung fehlender Werte (z.B. Lücken im Chart, Hatch-Muster). Muss für alle 3 Aggregationen konsistent sein.
4. **Leerdaten-Handling (FR_21):** Wenn keine Daten, statt Chart eine Meldung anzeigen.
5. **Interaktivität:** Auflösungs-Wechsel triggert Re-Aggregation + Re-Rendering.

Annahmen:
- Visualisierungs-Framework ist ausgewählt.
- Aggregations-Formeln pro Kategorie sind dokumentiert (z.B. Temp = Average, Niederschlag = Sum).
- Chart-Library hat Performance für 11-Jahres-Daten.

### Definition of Ready

⚠ **Teilweise erfüllt:**

✓:
- User Story ist Value-fokussiert: Analyst sieht Trends.
- Akzeptanzkriterien sind testbar (Diagramm angezeigt, Auflösung aggregiert korrekt, Lücken markiert, Leerdaten-Meldung).
- FRs sind zugeordnet (FR_19-21).

✗ **Lücken:**
- **Aggregations-Formeln fehlen:** FR_19 sagt „aggregieren", aber nicht WIE pro Kategorie. USER_STORY_07 AC sagt nicht explizit, welche Aggregation für welche Kategorie.
  - Temperatur: Durchschnitt? Min/Max-Range? Tagsüber-Mittel?
  - Niederschlag: Summe? Durchschnitt?
  - Wind: Durchschnitt? Böen (Max)?
  - Sonneneinstrahlung: Summe? Durchschnitt?
- **Performance-Anforderung:** Wie viele Datenpunkte? Wenn 11 Jahre täglich = ~4000 Points. Akzeptabel für Chart. Aber nicht genannt.
- **Chart-Typ pro Kategorie:** FR_19 sagt nicht explizit, welche Chart-Form. Annahme: Linien-Chart. Aber Niederschlag könnte Balken sein?

### Abhängigkeiten

- **Technisch:** Visualisierungs-Framework, Aggregations-Utilities.
- **Funktional:** Datenbasis von USER_STORY_03 (Persistenz) + USER_STORY_04 (gefilterte Abfrage). INPUT von USER_STORY_05/06 (Parameter, Status).

### Aufwandstreiber & Edge Cases

| Treiber | Komplexität | Testfall |
|---|---|---|
| Visualisierungs-Integration | Hoch | Chart-Library init, data-binding, re-render |
| Aggregation: Kategorie-abhängig | Hoch | Temp täglich = avg(Temp); Niederschlag täglich = sum(mm); korrekte Aggregation pro Kat |
| Lückenkennzeichnung | Moderat | Wenn 01.01–31.01 Daten, aber 01.02 fehlt, dann Gap in Chart |
| Auflösungs-Wechsel | Moderat | User wechselt täglich → monatlich → jährlich; Aggregation + Re-render schnell |
| Leerdaten-Meldung | Niedrig | Wenn 0 Zeilen aus DB → "Keine Daten für Auswahl" statt leerer Chart |

### Risiken / Blind Spots

- **Aggregations-Ambiguität (CRITICAL):** Wind hat unterschiedliche Bedeutungen. Ist es Windgeschwindigkeit (km/h)? Dann: Durchschnitt sinnvoll. Oder Windrichtung (Grad)? Dann: Average unsinnig. **Muss vor Sprint geklärt sein.**
- **Chart-Performance:** Mit 4000+ Datenpunkten kann chart.js langsam werden. Rendering, Hover-Tooltips könnten laggen.
- **Datum-Alignment:** Bei monatlicher Aggregation: ist Januar = alle Tage 01.01–31.01? Oder Wochen? Konsistenz wichtig.
- **Leerdaten vs. Technik-Fehler:** FR_21 unterscheidet Leerdaten von Fehler. Aber Implementierung? Beide werden als Fehler zurückkommen, nur Zahl der Rows ist Unterschied.

### Testaufwand

- Unit-Tests: Aggregations-Formeln (6-8 Cases pro Kategorie, 4 Kategorien = 24-32 Cases).
- Integrations-Tests: Datenbank-Abfrage → Aggregation → Chart-Rendering (4 Cases, 1 pro Kategorie).
- Visual-Tests: Chart-Darstellung, Lückenkennzeichnung (4-5 Cases).
- E2E-Tests: User-Szenario (Auflösung wechseln, Lücken sichtbar, Leerdaten-Meldung).
- Performance-Tests: 4000+ Points in Chart, Responsive?
- Geschätzter Test-Aufwand: 4-5 Tage (wegen Komplexität + Aggregations-Ambiguität).

### Empfehlung

**Verfeinern** – Story hat 3 kritische Lücken:
1. Aggregations-Formeln pro Kategorie explizit in AC oder FR dokumentieren.
2. Performance-Anforderungen klären (max Punkte pro Chart, Responsiveness-Ziel).
3. Chart-Typ pro Kategorie entscheiden (Linie, Balken, etc.).

**Nach Verfeinerung: Wahrscheinlich Split in 2 Stories:**
- US_07a: Basis-Aggregation + Chart-Integration (5-8 SP).
- US_07b: Lückenkennzeichnung + Leerdaten-Handling + Performance (3-5 SP).

---

## USER_STORY_08: Aktuelle Visualisierung als PNG exportieren

**Quelle Epics & FRs:** EPIC_04 • FR_22, FR_23, FR_24

### Story Points: 5

### Begruendung

Mittlere Komplexität mit 3 Aufwandstreibern:
1. **Chart→PNG-Rendering:** Visualisierungs-Library muss PNG-Export unterstützen (z.B. Chart.js mit Plugin, D3 mit canvas-export, Plotly built-in).
2. **Ansichtsbezug (FR_22):** PNG muss aktuelle Darstellung (Kategorie, Auflösung, Filter) exportieren. Nicht neue Abfrage. Snapshot-Logik.
3. **Fehlerbehandlung (FR_23, FR_24):** Zielpfad-Validierung, technische Fehler abfangen, aussagekräftige Meldung.

Annahmen:
- Visualisierungs-Framework hat PNG-Export-Kapabilität.
- Nutzer-Filesystem-Zugriff erlaubt (z.B. Download-Dialog oder API).

### Definition of Ready

✓ **Erfüllt:**
- User Story ist klar: Nutzer exportiert aktuelle Darstellung.
- Akzeptanzkriterien sind testbar (PNG erzeugt, Pfad-Fehler → keine Datei + Meldung, Fehler-Resilienz).
- FRs sind zugeordnet (FR_22-24).

⚠ **Teilweise Lücken:**
- FR_23 spricht von „nicht beschreibbarem Zielpfad". Aber wie wird Zielpfad angegeben? UI-Dateiauswahl? Hard-coded? Nicht spezifiziert.

### Abhängigkeiten

- **Technisch:** Chart-Library PNG-Export, ggf. Server-side Rendering falls Client-Export nicht möglich.
- **Funktional:** Darstellung von USER_STORY_07 (Chart muss existieren).

### Aufwandstreiber & Edge Cases

| Treiber | Komplexität | Testfall |
|---|---|---|
| PNG-Export-API | Moderat | Chart.js.toImage() oder äquivalent; Größe OK; Qualität OK |
| Ansichtsbezug | Niedrig | Wenn Nutzer Auflösung ändert, PNG zeigt neue Aggregation |
| Zielpfad-Fehler | Niedrig | Read-only-Ordner, kein Speicherplatz → Error ohne PNG-Erzeugung |
| Fehler-Resilienz | Niedrig | Technischer Fehler → Meldung, App bleibt nutzbar (nicht abgestürzt) |

### Risiken / Blind Spots

- **Zielpfad-Angabe:** Auf Web/Browser: Download-Dialog auto-generiert. Auf Desktop: Nutzer wählt Ordner? API unklar.
- **Dateiname-Konvention:** Wer bestimmt Dateiname? System (z.B. "weather_export_20260707.png")? Nutzer-Input? FR sagt nichts.
- **Bildqualität:** PNG-Export mit vielen Datenpunkten könnte groß oder verschwommen sein. Kompression-Tradeoff?

### Testaufwand

- Unit-Tests: PNG-Export-Logic isoliert (2-3 Cases).
- Integrations-Tests: Chart-Export + Fehlerfall (4-5 Cases).
- E2E-Tests: User-Szenario (Chart anzeigen → Export-Button → PNG heruntergeladen).
- Geschätzter Test-Aufwand: 1-2 Tage.

### Empfehlung

**Akzeptieren** – Story ist unabhängig, mit bekannten Mustern. Vor Sprint sollte Zielpfad-Angabe-Mechanismus geklärt sein (Dialog, API, etc.).

---

## Zusammenfassung Empfehlungen

### Sofort Akzeptieren (Ready):
1. **USER_STORY_01** (3 SP) – Stationssuche, klare Logik.
2. **USER_STORY_02** (5 SP) – API-Abruf, mit Hinweis auf API-Dokumentation.
3. **USER_STORY_03** (3 SP) – Datenhaltung, Standard-Muster.
4. **USER_STORY_04** (5 SP) – Datenexport, mit Hinweis auf CSV-/JSON-Struktur.
5. **USER_STORY_05** (3 SP) – UI-Erfassung, mit Hinweis auf Koordinaten-Format.
6. **USER_STORY_06** (5 SP) – Status-Anzeige, mit Hinweis auf Async-Execution-Model.
7. **USER_STORY_08** (5 SP) – PNG-Export, mit Hinweis auf Zielpfad-Mechanismus.

### Verfeinern Vor Akzeptanz:
- **USER_STORY_07** (aktuell 8 SP, wird zu 2 Stories nach Split):
  - **Kritische Lücken:** Aggregations-Formeln pro Kategorie, Performance-Anforderungen, Chart-Typ-Festlegung.
  - **Empfehlung:** In Sprint-Planung mit Analysten klären. Danach möglicherweise in 2 Stories splitten.

---

## Gesamtaufwand

| Kategorie | Punkte |
|---|---:|
| Sofort Akzeptiert (7 Stories) | 29 SP |
| Zu Verfeinern (USER_STORY_07 ungesplittet) | 8 SP |
| **Gesamt aktuell** | **37 SP** |
| **Nach Split US_07** (voraussichtlich) | **~40-45 SP** (mit 2 Slices à 5-8 SP) |

---

## Definition of Ready - Checkliste

Vor Sprint-Start **alle** dieser Punkte validieren:

- [ ] **USER_STORY_02:** DWD-API-Struktur und Datenformat dokumentiert.
- [ ] **USER_STORY_04:** CSV- und JSON-Ausgabe-Schema dokumentiert.
- [ ] **USER_STORY_05:** Koordinaten-Eingabe-Format festgelegt (Dezimal, Range, Separator).
- [ ] **USER_STORY_06:** Async-Execution-Model definiert (Threading, WebSocket, Polling?). Fehler-Zuordnungs-Granularität geklärt.
- [ ] **USER_STORY_07:** ⚠ **KRITISCH:** 
  - Aggregations-Formeln pro Kategorie (z.B. Temp=avg, Niederschlag=sum).
  - Performance-Ziele (max Datenpunkte, Responsiveness).
  - Chart-Typ pro Kategorie.
- [ ] **USER_STORY_08:** Zielpfad-Angabe-Mechanismus (Dialog, API, File-Picker).

---

## Qualitätssicherung & Risiken

### Übergreifende Risiken (Projekt-Ebene):

1. **DWD-API-Stabilität:** Wenn DWD-API ändert sich, USER_STORY_02 könnte brechen. → Monitoring + Fallback-Plan.
2. **Datenqualität DWD:** Nicht alle Stationen haben Daten für alle 4 Kategorien im gesamten 11-Jahres-Zeitraum. → Error-Handling robust machen.
3. **Performance:** Aggregation + Rendering von 11 Jahren täglich (~4000 Punkte). Akzeptabel, aber Grenze. → Testing mit Realdata.
4. **Koordinaten-Parsing:** Viele Varianten möglich (Dezimal, Grad, etc.). Nur eine unterstützen? → Dokumentieren, User-Fehler minimieren.

### Test-Strategie:

- **Unit-Tests:** ~30-40 Test-Cases (Validierung, Aggregation, Serialisierung).
- **Integrations-Tests:** ~20-25 Test-Cases (DB + API + Dateisystem).
- **E2E-Tests:** ~8-10 User-Szenarien.
- **Realdata-Tests:** Mindestens 1 echter Abruf von DWD mit 11 Jahren Daten.

---

## Nächste Schritte

1. **Vor Sprint-Planung:**
   - Definition-of-Ready-Checkliste durchgehen mit Produkt-Owner.
   - USER_STORY_07 mit Fachanwendern klären (Aggregations-Details).
   - Datenschema (CSV/JSON, Datenbank) finalisieren.

2. **Im Sprint-Planning:**
   - 7 Ready Stories in Sprint einplanen (29 SP als Basis).
   - USER_STORY_07 entweder verfeinern + splittens oder als 8-SP-Story akzeptieren (mit Risiko).
   - Sprint-Kapazität berücksichtigen (z.B. wenn Team 25 SP/Sprint schafft, ist Sprint 2 erforderlich).

3. **Im Sprint:**
   - Täglich Fokus auf Integration (USER_STORY_02 ↔ USER_STORY_03 ↔ USER_STORY_04).
   - USER_STORY_07 mit Visualisierungs-Spike evaluieren.
   - Realdata-Tests durchführen.

---

**Geschätzt von:** GitHub Copilot (Agile_Estimator Mode)

**Datum:** 2026-07-07
