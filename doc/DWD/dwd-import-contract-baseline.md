# Real-DWD Contract Baseline (Phase 5.5)

**Zweck:** Verifikation der bisher nur angenommenen DWD-Formate (Stationsliste, historisches
10-Minuten-Lufttemperatur-Archiv) gegen die tatsächlichen, offiziellen Live-Ressourcen des
DWD Climate Data Center (CDC), gemäß `pjm/import-client-implementation-plan.md`, Phase 5.5.

**Retrieval-Datum:** 2026-07-20

**Quelle / Lizenz:** DWD Climate Data Center (CDC), `opendata.dwd.de`. Daten stehen unter
CC BY 4.0 (siehe `doc/DWD/md/BESCHREIBUNG_obsgermany-climate-10min-air_temperature_de.md`,
Abschnitt „Copyright"). Nachfolgend werden nur kurze, repräsentative Auszüge zitiert, keine
vollständigen Dumps.

---

## 1. Stationsliste

**Verifizierte URL:**
`https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/10_minutes/air_temperature/historical/zehn_min_tu_Beschreibung_Stationen.txt`

- HTTP-Status: `200 OK` (kein Redirect beobachtet, `Invoke-WebRequest -OutFile` erfolgreich,
  Dateigröße 543.309 Bytes).
- Encoding: `latin-1` (Datei enthält Umlaute/Sonderzeichen in Stationsnamen; Dekodierung mit
  `latin-1` erfolgreich ohne `UnicodeDecodeError`).
- Zeilenzahl gesamt: 544 (1 Kopfzeile + 1 Trennzeile + 542 Datenzeilen).
- Zeilenlänge jeder Datenzeile: konstant **1000 Zeichen** (rechtsseitig mit Leerzeichen
  aufgefüllt).

### Kopfzeile und Trennzeile (Auszug)

```
Stations_id von_datum bis_datum Stationshoehe geoBreite geoLaenge Stationsname Bundesland Abgabe
----------- --------- --------- ------------- --------- --------- ----------------------------------------- ---------- ------
```

### Beispielzeile (Station Aachen, gekürzt auf die relevanten ersten ~130 Zeichen)

```
00003 19930428 20120403            202     50.7827    6.0941 Aachen                                   Nordrhein-Westfalen                      Frei
```

### Tatsächliche Spaltenpositionen (0-basiert, `[start, ende)`, byteweise nach `latin-1`-Dekodierung)

**Wichtiger Befund:** Die Trennzeile (Bindestriche) gibt NICHT die tatsächlichen Spaltenbreiten
der Datenzeilen wieder. Sie stimmt nur zufällig für das Feld `Stationsname` (41 Zeichen) überein,
ist aber für alle anderen Felder falsch. Die realen Spaltenpositionen wurden durch
Cross-Validierung über 7 Beispielzeilen mit unterschiedlichen Ziffernlängen (Stationshöhe:
2–4 Ziffern) ermittelt, indem stabile rechtsbündige End-Offsets (numerische Felder) bzw.
linksbündige Start-Offsets (Textfelder) gesucht wurden:

| Feld | Byte-Bereich | Ausrichtung | Bemerkung |
|---|---|---|---|
| `Stations_id` | `[0, 5)` | linksbündig | 5-stellig, führende Nullen erhalten |
| (Leerzeichen) | `[5, 6)` | — | |
| `von_datum` | `[6, 14)` | — | Format `YYYYMMDD` |
| (Leerzeichen) | `[14, 15)` | — | |
| `bis_datum` | `[15, 23)` | — | Format `YYYYMMDD` |
| `Stationshoehe` | `[23, 38)` | rechtsbündig | ganzzahlig, Ende immer bei Spalte 38 (bestätigt für 2–4-stellige Werte) |
| `geoBreite` | `[38, 50)` | rechtsbündig | Dezimalpunkt, 4 Nachkommastellen, Ende immer bei Spalte 50 |
| `geoLaenge` | `[50, 60)` | rechtsbündig | Dezimalpunkt, 4 Nachkommastellen, Ende immer bei Spalte 60 |
| (Leerzeichen) | `[60, 61)` | — | |
| `Stationsname` | `[61, 102)` | linksbündig | fester 41-Zeichen-Slot (Rest mit Leerzeichen aufgefüllt), Bundesland beginnt immer bei 102 |
| `Bundesland` | `[102, 143)` | linksbündig | fester 41-Zeichen-Slot, „Abgabe"-Feld beginnt immer bei 143 |
| `Abgabe` | `[143, …)` | linksbündig | z. B. `Frei`; Zeile insgesamt auf 1000 Zeichen mit Leerzeichen aufgefüllt |

- **Stations-ID-Repräsentation:** String, genau 5 Stellen, führende Nullen erhalten
  (z. B. `"00003"`) — **bestätigt**, wie von der aktuellen Domäne (`station_id: str`) erwartet.
- **Datumsspalten:** `von_datum`/`bis_datum` als reine Ziffernfolge `YYYYMMDD`, kein Trennzeichen.
- **Koordinaten:** Dezimalpunkt (kein Komma), bis zu 4 Nachkommastellen, kein Vorzeichen bei den
  Beispielen in Deutschland (positive Werte).
- **Umlaute/Sonderzeichen:** In Stationsnamen und Bundesland vorhanden (z. B. „Großenkneten",
  „Baden-Württemberg"), korrekt dekodierbar mit `latin-1`.
- **Zeilenenden:** Datei verwendet Standard-Zeilenumbrüche, kompatibel mit `str.splitlines()`.
- **Leerzeilen:** Keine Leerzeilen zwischen Kopf-, Trenn- und Datenzeilen beobachtet.

---

## 2. Historisches 10-Minuten-Lufttemperatur-Archiv

**Verifizierte Verzeichnis-URL:**
`https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/10_minutes/air_temperature/historical/`

- Verzeichnis-Listing (HTML) erfolgreich abgerufen (HTTP 200, 258.003 Bytes).
- Enthält **1630 ZIP-Dateien** und genau **1 Textdatei** (`zehn_min_tu_Beschreibung_Stationen.txt`).
  Keine separaten `Metadaten_*`-Dateien auf dieser Verzeichnisebene gefunden (diese liegen laut
  Doku ggf. in anderen Unterordnern, sind für den aktuellen Scope FR-005/006/007/008 nicht
  relevant).

### ZIP-Namensschema — **bestätigter Kontraktkonflikt gegenüber `ZIP_URL_TEMPLATE`**

Tatsächliches Schema (verifiziert per Verzeichnis-Listing):

```
10minutenwerte_TU_{station_id}_{begin_date}_{end_date}_hist.zip
```

Beispiel — Station `00003` hat **drei** ZIP-Dateien für unterschiedliche, nicht überlappende
Zeiträume:

```
10minutenwerte_TU_00003_19930428_19991231_hist.zip
10minutenwerte_TU_00003_20000101_20091231_hist.zip
10minutenwerte_TU_00003_20100101_20110331_hist.zip
```

**Aktueller Code-Stand (`ZIP_URL_TEMPLATE` in `lufttemperatur_importer.py`):**
`10minutenwerte_TU_{station_id}_hist.zip` (ohne Datumsbereich) — **dieses Template existiert als
reale Ressource nicht**. Ein Abruf mit diesem Muster würde einen `404` liefern. Zusätzlich kann es
**mehrere ZIP-Dateien pro Station** geben (unterschiedliche, nicht überlappende Zeiträume), sodass
das korrekte ZIP für einen angefragten Zeitraum nur über das Verzeichnis-Listing (Pattern-Match
auf `station_id`, dann Auswahl nach Zeitraumüberschneidung) ermittelt werden kann, nicht über ein
statisches Template.

### ZIP-Inhalt (Beispiel: `10minutenwerte_TU_00003_20100101_20110331_hist.zip`, 657.685 Bytes)

- Enthält genau **eine** Datei: `produkt_zehn_min_tu_20100101_20110331_00003.txt`
  (4.717.504 Bytes) — Präfix `produkt_` **bestätigt**, genau eine Produktdatei **bestätigt**.
- Encoding: `latin-1` **bestätigt** (Dekodierung erfolgreich, keine Fehler).
- Zeilenenden: `\r\n` (CRLF) **bestätigt**, `\r\n` im Rohbyte-Inhalt nachgewiesen.
- CSV-Trennzeichen: `;` **bestätigt**.
- Zeilenanzahl: 65.521 (1 Kopfzeile + 65.520 Datenzeilen).

### Kopfzeile und Beispielzeilen (Auszug)

```
STATIONS_ID;MESS_DATUM;  QN;PP_10;TT_10;TM5_10;RF_10;TD_10;eor
          3;201001010000;    3;  970.2;  -1.2;  -1.0;  97.2;  -1.6;eor
          3;201001010010;    3;  970.3;  -1.3;  -1.1;  97.2;  -1.7;eor
```

- **Zusätzliche, nicht in `doc/DWD/md/BESCHREIBUNG_obsgermany-climate-10min-air_temperature_de.md`
  dokumentierte Spalte:** `eor` (End-Of-Record-Marker, letzte Spalte jeder Zeile, Wert immer
  `eor`). Kein funktionaler Einfluss auf das Parsing der benötigten Felder (`STATIONS_ID`,
  `MESS_DATUM`, `TT_10`), da `csv.DictReader` diese als zusätzliche Spalte einliest, die aktuell
  nicht ausgewertet wird.
- **`STATIONS_ID`-Repräsentation in der CSV-Datenzeile:** rechtsbündige Ganzzahl-Darstellung ohne
  führende Nullen (z. B. `"          3"` für Station `00003`). Nach dem in
  `dwd_zip_reader.lese_rohdatensaetze()` durchgeführten `.strip()` wird daraus `"3"`
  (**korrigiert/neuer Befund** gegenüber der Annahme, dass `STATIONS_ID` in der CSV wie die
  extern übergebene, 5-stellige Stations-ID aussieht). Siehe Abschnitt 4 (Delta-Klassifikation)
  zur Einordnung, ob dies für das aktuelle Verhalten überhaupt relevant ist.
- **`MESS_DATUM`-Format:** `YYYYMMDDHHMM`, also 12 Ziffern inkl. Minutenauflösung (Beispiel
  `201001010000`). Der Code-Wert `_ZEITSTEMPEL_FORMAT = "%Y%m%d%H%M"` ist damit **bestätigt**
  korrekt (die zusammenfassende Doku-Kurzformel „YYYYMMDDHH24" war ungenau/verkürzt, meint aber
  dasselbe Format inkl. Minuten).
- **`TT_10`-Repräsentation:** Dezimalzahl mit Punkt als Trennzeichen, Vorzeichen möglich
  (z. B. `-1.2`), führende Leerzeichen vor dem Wert (durch `.strip()` im Code entfernt) —
  **bestätigt**, `float()`-Konvertierung im bestehenden Code funktioniert unverändert.
- **Fehlwert-Repräsentation (`-999`):** In der geprüften Stichprobe (Station `00003`, Zeitraum
  2010-01-01 bis 2011-03-31, 65.520 Datenzeilen) trat **kein** `-999`-Wert in `TT_10` oder einer
  anderen Spalte auf — **weiterhin unklar / nicht live reproduziert**, aber durch die offizielle
  DWD-Doku (`doc/DWD/md/BESCHREIBUNG_obsgermany-climate-10min-air_temperature_de.md`) als
  Fehlwertkonvention `-999` dokumentiert. Der bestehende Code
  (`datensatz_validator.py`, `_FEHLWERT = -999.0`) setzt exakt diese dokumentierte Konvention um.
  Ohne einen live beobachteten `-999`-Datensatz gilt dieser Punkt als **dokumentiert, aber nicht
  unabhängig live reproduziert**; es besteht kein Anlass für eine Code-Änderung, da Code und
  offizielle Doku übereinstimmen.

### Externe Feld → interne Domäne — Mapping

| Externes DWD-Feld | Internes Domänenfeld | Bemerkung |
|---|---|---|
| `Stations_id` (Stationsliste) | `StationsTreffer.station_id` | String, 5-stellig, führende Nullen erhalten |
| `geoBreite` / `geoLaenge` (Stationsliste) | Koordinaten für Distanzberechnung (`stationsfinder.py`) | Dezimalgrad |
| `Stationsname` (Stationsliste) | `StationsTreffer.name` | |
| `MESS_DATUM` (Produktdatei) | `Messwert.zeitstempel` | Format `%Y%m%d%H%M`, bestätigt |
| `TT_10` (Produktdatei) | `Messwert.wert` | °C, `-999.0` = Fehlwert |
| `STATIONS_ID` (Produktdatei) | `Messwert.station_id` | Siehe Delta-Befund oben (führende Nullen nach `.strip()` verloren) |

---

## 3. Klassifikation bisheriger Implementierungsannahmen

| Annahme | Status | Beleg |
|---|---|---|
| Stationsliste-URL | **bestätigt** | HTTP 200, Datei erfolgreich geladen und dekodiert |
| Stationsliste-Spaltenformat (Trennzeile definiert Breiten) | **korrigiert** | Trennzeile stimmt nur für `Stationsname` zufällig; reale Breiten siehe Tabelle Abschnitt 1 |
| ZIP-URL-Schema (`ZIP_URL_TEMPLATE` ohne Datumsbereich) | **korrigiert** | Reale Dateien enthalten immer `{begin_date}_{end_date}`; mehrere ZIPs pro Station möglich |
| ZIP-Produktdatei-Präfix (`produkt_`) / genau eine Datei | **bestätigt** | Verifiziert am realen Archiv für Station 00003 |
| CSV-Trennzeichen (`;`) | **bestätigt** | Verifiziert an realer Produktdatei |
| Encoding (`latin-1`) | **bestätigt** | Beide Dateien (Stationsliste, Produktdatei) fehlerfrei dekodiert |
| `MESS_DATUM`-Format (`%Y%m%d%H%M`) | **bestätigt** | Exakter Abgleich mit realen Werten (`201001010000` usw.) |
| Fehlwert-Repräsentation (`-999`) | **weiterhin unklar (dokumentiert, nicht live reproduziert)** | Keine `-999`-Zeile in der geprüften Stichprobe; Code stimmt mit offizieller Doku überein |
| `STATIONS_ID` in Produktdatei = extern übergebene, 5-stellige Stations-ID | **korrigiert (neuer Befund)** | Reale Werte sind rechtsbündige Ganzzahlen ohne führende Nullen, werden durch `.strip()` zu z. B. `"3"` |
| Zusätzliche Spalte `eor` in Produktdatei | **neuer Befund, unkritisch** | Nicht in Kurzdoku erwähnt, aber ohne Funktionsauswirkung |

---

## 4. Blockierende Bedingung — Status

- ✅ Eine echte Stationsliste wurde heruntergeladen und erfolgreich geparst — **inzwischen auch
  durch den produktiven `StationsFinder`/`parse_stationsliste()`-Code selbst** (nach Phase 6R),
  verifiziert über den Live-Smoke-Test `tests/integration/test_live_dwd_smoke.py::test_live_stationsliste_wird_real_geladen_und_geparst`
  (manuell ausgeführt am 2026-07-20, `PASSED`).
- ✅ Ein echtes historisches Lufttemperatur-ZIP wurde lokalisiert (über das reale
  Verzeichnis-Listing, `dwd_archiv_verzeichnis`, Phase 7R) und erfolgreich gelesen, verifiziert
  über `tests/integration/test_live_dwd_smoke.py::test_live_zip_wird_lokalisiert_gelesen_und_zu_messwert_konvertiert`
  (manuell ausgeführt am 2026-07-20, `PASSED`).
- ✅ Reale Rohdatensätze wurden erfolgreich validiert (`DatensatzValidator`) und sind mit der
  internen `Messwert`-Repräsentation kompatibel (Feldkonvertierung nachvollzogen und live
  bestätigt).
- ✅ URL- und Dateinamensregeln sind hier dokumentiert.
- ✅ Lokale Baseline-Fixtures mit dokumentierter Real-DWD-Herkunft: `stationsliste_real_auszug.txt`,
  `10minutenwerte_TU_00003_real_auszug_hist.zip` (siehe `tests/fixtures/dwd/README.md`).

**Ergebnis:** Alle Punkte der blockierenden Bedingung aus Phase 5.5 sind erfüllt. Die reale
DWD-Integration gilt für den Scope FR-001/004/005/006/007/008 (Stationssuche, ZIP-Ermittlung,
ZIP-Lesen, Validierung) als **abgeschlossen** — bestätigt durch produktiven Code (Phase 6R/7R)
UND einen erfolgreichen, manuell ausgeführten Live-Smoke-Test (Phase 8R).

---

## 5. Phase 5.6 — Contract Delta Analysis

Systematischer Abgleich der obigen Baseline gegen den bestehenden Produktionscode, die
Fixtures, die Architekturdokumentation und die Testplan-/Traceability-Dokumente. Nur Dateien
mit einer **nachgewiesenen** Kontraktabweichung werden in Phase 6R/7R geändert.

| Datei | Betroffene Stelle | Delta-Status | Konsequenz |
|---|---|---|---|
| `src/myweatherdata/import_client/dwd_stationsliste_parser.py` | Docstring (Format-Annahme), `_SPALTEN_REIHENFOLGE`, `parse_stationsliste()` (Trennzeilen-basierte Spaltenbreiten), `_zeile_in_spalten_zerlegen()` | **korrigiert** — Algorithmus liefert gegen die reale Datei 0 statt ~542 Einträge | **Phase 6R**: Neuimplementierung anhand der festen Byte-Offsets aus Abschnitt 1, TDD mit `stationsliste_real_auszug.txt` |
| `src/myweatherdata/import_client/stationsfinder.py` | `STATIONSLISTE_URL` (Konstante) | **bestätigt** — URL korrekt, kein Logik-Delta | Nur Docstring-Aktualisierung (Spike-Hinweis → bestätigt) im Rahmen von 6R, keine Verhaltensänderung |
| `src/myweatherdata/import_client/stationsfinder.py` | `finde_naechste()` (Aufrufer von `parse_stationsliste`) | **abhängig** — funktioniert erst korrekt, sobald 6R den Parser korrigiert | Kein eigenständiger Delta, aber Regressionstest nach 6R erneut ausführen |
| `src/myweatherdata/import_client/dwd_zip_reader.py` | Docstring (Format-Annahme), `_PRODUKT_DATEI_PRAEFIX`, CSV-Parsing (`;`, `latin-1`) | **bestätigt** — Präfix, Eindeutigkeit, Trennzeichen, Encoding korrekt | Nur Docstring-Aktualisierung (Spike-Hinweis → bestätigt), keine Logikänderung |
| `src/myweatherdata/import_client/dwd_zip_reader.py` | `.strip()` auf CSV-Werten → `STATIONS_ID` verliert führende Nullen (z. B. `"3"` statt eines 5-stelligen Werts) | **neuer Befund, unklar** — kein aktuell existierender Test oder Verhaltenspfad vergleicht `Messwert.station_id` mit der 5-stelligen Abfrage-Stations-ID; keine nachgewiesene Verhaltensauswirkung im aktuellen Scope | **Keine Änderung** in 7R (Grundsatz „nur nachgewiesene Deltas"); als offenes Risiko in Abschnitt 6 dokumentiert |
| `src/myweatherdata/import_client/lufttemperatur_importer.py` | `ZIP_URL_TEMPLATE` (Konstante, ohne Datumsbereich) | **korrigiert** — reale Dateinamen enthalten immer `{begin_date}_{end_date}`; ein statisches Template kann das korrekte ZIP nicht ermitteln, insbesondere bei mehreren ZIPs pro Station | **Phase 7R**: Verzeichnis-Listing-basierte ZIP-Ermittlung (Design-Konsequenz vor Code-Änderung dokumentieren), TDD mit `10minutenwerte_TU_00003_real_auszug_hist.zip` |
| `src/myweatherdata/import_client/lufttemperatur_importer.py` | `_ZEITSTEMPEL_FORMAT = "%Y%m%d%H%M"` | **bestätigt** — exakt passend zu realen `MESS_DATUM`-Werten | Keine Änderung |
| `tests/fixtures/dwd/stationsliste_beispiel.txt`, `10minutenwerte_TU_00003_beispiel_hist.zip`, `10minutenwerte_TU_00099_defekt_mess_datum_hist.zip`, `stationsliste_defekte_zeile.txt` | Synthetische Fixtures | **bleiben bestehen** (Grundsatz 5) | Nur Herkunft in `tests/fixtures/dwd/README.md` dokumentiert (bereits erledigt), keine inhaltliche Änderung |
| `arc/statische_sichten/klassensicht-import-client.puml`, `arc/statische_sichten/klassensicht.md` | Abschnitt „Weitere Confirmation-Punkte", Nr. 4 | **eingelöst durch Phase 5.5** | Statusaktualisierung in Doku-Schritt (nach 6R/7R), kein Diagramm-Strukturdelta |
| `tests/test_plan_import_client.md`, `tests/traceability.md` | Fehlende Einträge für real-basierte Regressionstests | **Ergänzungsbedarf** | Wird nach 6R/7R im Dokumentations-Schritt nachgezogen |

**Zusammenfassung:** Zwei Dateien mit nachgewiesenem, code-relevantem Delta:
`dwd_stationsliste_parser.py` (Phase 6R) und `lufttemperatur_importer.py` (Phase 7R, `ZIP_URL_TEMPLATE`).
Alle anderen geprüften Annahmen sind bestätigt oder betreffen ausschließlich Docstrings bzw.
noch unklare, aktuell nicht verhaltensrelevante Randfragen.
