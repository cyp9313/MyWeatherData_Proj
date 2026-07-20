# Plan: Import-Client (Vertical Slice FR-001 + FR-004 + FR-005 + FR-006 + FR-007 + FR-008)

**Version:** 1.1
**Status:** Freigegeben (autoritative Implementierungsbaseline)
**Vorgänger:** [.github/prompts/plan-importClient.prompt.md](../.github/prompts/plan-importClient.prompt.md) (v1.0 – bleibt als wiederverwendbarer Prompt bestehen, ist aber NICHT mehr die maßgebliche Planquelle)
**Autoritative Quelle ab sofort:** Dieses Dokument, `pjm/import-client-implementation-plan.md`. Beide Agents (`sw-import-client-developer`, `sw-destructive-reviewer`) lesen ab v1.1 dieses Dokument statt des ursprünglichen Prompts.

## Anlass für v1.1

Phase 9 (Qualitätsgate) und Phase 10 (Destructive QA) von v1.0 wurden erfolgreich abgeschlossen — aber ausschließlich auf Basis **synthetischer, nie gegen einen echten DWD-Abruf verifizierter Fixtures und Annahmen**. Mehrere Produktionsmodule dokumentieren dies bereits selbst als offenen Punkt:

- `src/myweatherdata/import_client/dwd_stationsliste_parser.py`: Docstring nennt das Spaltenformat ausdrücklich als "technischer Spike... noch nicht gegen eine live heruntergeladene DWD-Datei verifiziert".
- `src/myweatherdata/import_client/stationsfinder.py`: `STATIONSLISTE_URL` als "Spike-Annahme... noch nicht gegen einen Live-Abruf verifiziert" markiert.
- `src/myweatherdata/import_client/lufttemperatur_importer.py`: `ZIP_URL_TEMPLATE` als "vereinfacht ohne den realen Datumsbereich im Dateinamen, noch nicht gegen einen Live-Abruf verifiziert" markiert.
- `src/myweatherdata/import_client/dwd_zip_reader.py`: Produktdatei-Präfix/CSV-Trennzeichen als Spike-Annahme markiert.
- `tests/fixtures/dwd/README.md` widerspricht sogar dem tatsächlichen Zustand: Er beschreibt beide Fixture-Dateien als "werden erst angelegt, sobald der DWD-Format-Spike... bestätigt hat" — die Dateien existieren aber bereits, ohne dass dieser Spike je stattgefunden hat.
- Ein Abgleich mit `doc/DWD/md/BESCHREIBUNG_obsgermany-climate-10min-air_temperature_de.md` zeigt bereits jetzt (ohne Live-Zugriff) eine wahrscheinliche Kontraktabweichung: Das offiziell dokumentierte ZIP-Namensschema ist `*_{product_code}_{station_id}_{begin_date}_{end_date}_hist.zip` (inkl. Datumsbereich), während `ZIP_URL_TEMPLATE` im Code nur `10minutenwerte_TU_{station_id}_hist.zip` (ohne Datumsbereich) annimmt.

v1.1 macht die Verifikation gegen die echten offiziellen DWD-Ressourcen zu einem **verbindlichen Gate**, bevor irgendeine Aussage über "reale DWD-Integration abgeschlossen" zulässig ist. v1.1 ist **kein Neustart**: Bestehende Architektur, Domänencode, Adaptercode, Tests, Fixtures, Traceability und das Destructive-QA-Log bleiben erhalten und werden nur dort geändert, wo der Spike eine nachgewiesene Kontraktabweichung aufdeckt.

---

## Phasenübersicht (Status v1.1)

| Phase | Titel | Status v1.1 | Bemerkung |
|---|---|---|---|
| 0 | Python-Guidelines-Skill | ✅ Abgeschlossen | Regression: Skill unverändert gültig |
| 1 | SW-Design-Abgleich | ✅ Abgeschlossen | Regression: Diagramme bleiben gültig, ggf. Delta in 5.6 |
| 2 | Testplan-Dokument | ✅ Abgeschlossen | Bleibt Referenz, wird durch 5.6 ggf. ergänzt |
| 3 | Python-Scaffolding | ✅ Abgeschlossen | Regression: Struktur unverändert gültig |
| 4 | Domäne & Ports | ✅ Abgeschlossen | Regression: bestehende Tests bleiben grün |
| 5 | Bausteine (Distanz, Validator) | ✅ Abgeschlossen | Regression: bestehende Tests bleiben grün |
| **5.5** | **Real-DWD Contract Spike** | 🆕 **Neu, PFLICHT-GATE** | Blockiert jede Aussage "reale Integration fertig" |
| **5.6** | **Contract Delta Analysis** | 🆕 Neu | Nur nach 5.5 |
| 6 | HTTP & Stationssuche (fixture-basiert) | ✅ Abgeschlossen, ⚠️ wiedereröffnet für reale Verifikation | Fixture-Implementierung bleibt als Regressionsbasis; reale Korrektheit ungeklärt bis 5.5/6R |
| **6R** | **Stationsliste Remediation** | 🆕 Neu | Nur bei nachgewiesenem Delta |
| 7 | Lufttemperatur-Import (fixture-basiert) | ✅ Abgeschlossen, ⚠️ wiedereröffnet für reale Verifikation | Wie Phase 6 |
| **7R** | **ZIP- und Temperatur-Import Remediation** | 🆕 Neu | Nur bei nachgewiesenem Delta |
| 8 | Fassade & Integration | ✅ Abgeschlossen | Regression: bestehende Tests bleiben grün |
| 9 | Qualitätssicherung & Abschluss | ✅ Abgeschlossen (fixture-Basis) | ⚠️ Aussage "abgeschlossen" gilt NUR für fixture-basierte Korrektheit, nicht für reale DWD-Konformität |
| **8R** | **Regression- und Live-Smoke-Verifikation** | 🆕 Neu | Nach 6R/7R |
| **9R** | **CI- und Repository-Qualitätsgate** | 🆕 Neu | Enthält Repo-Hygiene + GitHub Actions |
| 10 | Destructive QA (fixture-Scope) | ✅ Abgeschlossen (fixture-Basis) | DQA-1..4 behoben, DQA-R1..R3 offen; gilt weiterhin nur für fixture-basierten Scope |
| **10R** | **Unabhängiges Destructive Re-Review** | 🆕 Neu | Nach 9R, prüft zusätzlich reale Kontraktkonformität |

Legende: ✅ abgeschlossen (Regressionsstatus) · ⚠️ teilweise/wiedereröffnet · 🆕 neu · Nummern ohne Suffix = Original aus v1.0, Suffix `R` = Remediation, `.5`/`.6` = eingeschobene Zwischenphasen.

---

## Bindende Grundsätze für v1.1 (gelten für alle Phasen ab 5.5)

1. **Kein Neustart.** Bestehende Architekturdokumente, Domänenverträge, Adaptercode, Unit-/Integrationstests, Fixtures, `tests/traceability.md` und `tests/destructive-qa-log.md` bleiben erhalten und werden referenziert, nicht neu erfunden.
2. **Bestehende grüne Tests sind Regressionstests.** Sie werden vor und nach jeder Remediation-Phase erneut ausgeführt und müssen grün bleiben, sofern sie nicht nachweislich ein falsches (weil auf einer widerlegten Annahme beruhendes) Verhalten prüfen.
3. **Produktionscode wird nur geändert, wenn der Real-DWD-Contract-Spike (Phase 5.5) eine Annahme nachweislich widerlegt**, oder um eine daraus resultierende, zuerst rot geschriebene Regressionstest grün zu machen.
4. **Kein bestehender Test wird gelöscht oder abgeschwächt**, nur weil das reale Format vom synthetischen Fixture abweicht. Bei einer nachgewiesenen Abweichung wird der betroffene Test ergänzt bzw. präzisiert (z. B. Fixture ausgetauscht/ergänzt), niemals ersatzlos entfernt.
5. **Synthetische Fixtures dürfen bestehen bleiben**, aber ausschließlich für gezielte Randfall-Tests (z. B. defekte Zeile, `-999`-Fehlwert, mehrdeutige ZIP-Produktdatei). Ihr synthetischer Ursprung muss dokumentiert sein (siehe `tests/fixtures/dwd/README.md`, Phase 5.5).
6. **Kein Erfinden von URLs, Dateinamen, Encodings, Spaltenbreiten oder Archivstrukturen.** Jede Aussage über das reale DWD-Format muss auf einem tatsächlichen, dokumentierten Abruf beruhen. Ist kein Netzwerk-/DWD-Zugriff möglich, wird die Phase als `❌ blockiert` gemeldet, nicht durch Annahmen ersetzt.
7. **Der Live-Check läuft niemals automatisch im Standard-`pytest`-Lauf.** Er wird durch einen dedizierten `live`-Marker (oder ein separates Skript) isoliert.

---

## Phase 5.5 – Real-DWD Contract Spike (NEU, PFLICHT-GATE)

**Zweck:** Verifikation der bisher nur angenommenen DWD-Formate gegen die tatsächlichen, offiziellen Live-Ressourcen des DWD Climate Data Center (CDC), BEVOR eine reale Integration als abgeschlossen gilt.

**Trigger:** Muss durchlaufen werden, bevor Phase 6R, 7R, 8R, 9R oder 10R beginnen, und bevor irgendein Abschlussbericht behauptet, die "reale DWD-Integration" sei fertig.

**Durchführung:** Ausschließlich durch `sw-import-client-developer`, mit explizitem Netzwerkzugriff auf offizielle DWD-CDC-Ressourcen (`opendata.dwd.de`). Kein Rückgriff auf erfundene oder aus Dokumentations-Fragmenten geratene Werte.

### Zu verifizierende Punkte — Stationsliste

- Tatsächliche offizielle Stationsliste-URL (Ausgangspunkt: die im Code hinterlegte Annahme `.../climate/10_minutes/air_temperature/historical/zehn_min_tu_Beschreibung_Stationen.txt`, siehe `doc/DWD/md/BESCHREIBUNG_obsgermany-climate-10min-air_temperature_de.md`, Abschnitt „Verzeichnisstruktur").
- HTTP-Status und Redirects beim Abruf.
- Encoding der Datei.
- Kopfzeilenformat (Spaltennamen, evtl. mehrzeilig).
- Trennzeichen- oder Fixed-Width-Struktur (aktuelle Codeannahme: Trennzeile aus Bindestrichen definiert Spaltenbreiten — zu verifizieren).
- Tatsächliche Spaltenpositionen und -namen.
- Repräsentation der Stations-ID (führende Nullen? numerisch? String?).
- Datumsspalten (`von_datum`/`bis_datum`: Format, Typ).
- Koordinatenspalten (Dezimaltrennzeichen, Vorzeichen, Anzahl Nachkommastellen).
- Umgang mit Stationsname und Bundesland (Spaltenbreite, Sonderzeichen, Umlaute).
- Leerzeilen, Zeilenenden (`\n` vs. `\r\n`) und Whitespace-Konventionen.

### Zu verifizierende Punkte — Historisches Lufttemperatur-Archiv

- Tatsächliche offizielle Verzeichnisstruktur unterhalb `climate/10_minutes/air_temperature/historical/`.
- Tatsächliches ZIP-Dateinamensschema (laut `doc/DWD/md/BESCHREIBUNG_obsgermany-climate-10min-air_temperature_de.md` bereits als `*_{product_code}_{station_id}_{begin_date}_{end_date}_hist.zip` dokumentiert — durch echten Verzeichnis-Listing-Abruf zu bestätigen).
- Ob der Dateiname tatsächlich einen Datumsbereich enthält (Doku sagt ja — aktueller Code (`ZIP_URL_TEMPLATE`) nimmt das Gegenteil an; **wahrscheinlicher bestätigter Konflikt**, siehe Phase 5.6).
- Wie das korrekte ZIP für eine gegebene Station ermittelt wird (Verzeichnis-Listing + Pattern-Match auf Stations-ID, da der Datumsbereich vorab nicht bekannt ist).
- ZIP-Inhalts-Namensgebung und Groß-/Kleinschreibung (`produkt_*` vs. `Produkt_*` u. Ä.).
- Anzahl und Muster der Produktdateien (genau eine? mehrere Metadaten-Dateien zusätzlich, siehe Doku: `Metadaten_Parameter*`, `Metadaten_Geraete*`, `Metadaten_Stationsname*`, `Metadaten_Geographie*`).
- CSV-Trennzeichen (Doku nennt `;`).
- Encoding (Code nimmt aktuell `latin-1` an — zu verifizieren).
- Pflichtspalten (Doku nennt u. a. `MESS_DATUM`, `QN`, `PP_10`, `TT_10`, `TM5_10`, `RF_10`, `TD_10`).
- `MESS_DATUM`-Format (Doku: `YYYYMMDDHH24`; Code nimmt `%Y%m%d%H%M` an — Konsistenz zu prüfen, insbesondere ob Sekunden/Minutenauflösung exakt passt).
- `TT_10`-Repräsentation (Dezimalformat, Vorzeichen).
- Fehlwert-Repräsentation (Doku: `-999`, Format `990.0` — zu bestätigen, ob exakt `-999` oder `-999.0`).
- Relevante Metadatendateien (siehe oben) und ob sie das Parsing der Produktdatei beeinflussen (z. B. Auswahl bei mehreren Dateien im Archiv).

### Pflicht-Outputs der Phase 5.5

1. `doc/DWD/dwd-import-contract-baseline.md` mit mindestens:
   - Abrufdatum (`Retrieval-Datum`),
   - den verifizierten offiziellen Quell-Locations (vollständige URLs),
   - einem kurzen Rohformat-Auszug, soweit rechtlich (CC BY 4.0, siehe DWD-Doku „Copyright") und technisch angemessen (keine vollständigen Dumps, nur repräsentative Kopf-/Beispielzeilen),
   - einer dokumentierten Zuordnung externer DWD-Felder zu internen Domänenfeldern (`MESS_DATUM` → `Messwert.zeitstempel`, `TT_10` → `Messwert.wert`, `Stations_id` → `StationsTreffer.station_id`, usw.),
   - einer vollständigen Liste jeder bisherigen Implementierungsannahme, klassifiziert als `bestätigt`, `korrigiert` oder `weiterhin unklar` (Basisliste: Stationsliste-URL, Stationsliste-Spaltenformat, ZIP-URL-Schema inkl. Datumsbereich, ZIP-Produktdatei-Präfix/-Eindeutigkeit, CSV-Trennzeichen, Encoding, `MESS_DATUM`-Format, Fehlwert-Repräsentation).
2. Kleine lokale Fixtures, die aus echten DWD-Daten abgeleitet sind (nicht die vollständigen Dateien, sondern reduzierte, aber real-basierte Auszüge), mit dokumentierter Herkunft in `tests/fixtures/dwd/README.md` (Real-DWD-Herkunft klar von den bestehenden synthetischen Fixtures unterschieden).
3. Ein separates, manuell auszuführendes Live-Smoke-Skript bzw. ein pytest-Test mit dediziertem `live`-Marker, das NICHT Teil des Standard-`pytest`-Laufs ist (z. B. `pytest -m live` explizit, während `pytest`/`pytest -v` diesen Marker per `pyproject.toml`/`pytest.ini` (`addopts = "-m 'not live'"` oder gleichwertig) automatisch ausschließt).

Standard-Unit- und Integrationstests bleiben durchgehend offline und deterministisch; sie werden durch die Spike-Ergebnisse nicht auf Netzwerkzugriff umgestellt.

### Blockierende Bedingung für „reale DWD-Integration abgeschlossen"

Die Aussage „Phase 6/7 reale DWD-Integration abgeschlossen" ist erst zulässig, wenn ALLE folgenden Punkte erfüllt sind:

- eine echte Stationsliste wurde heruntergeladen und erfolgreich geparst,
- ein echtes historisches Lufttemperatur-ZIP wurde lokalisiert und erfolgreich gelesen,
- mindestens ein echter Messwert wurde erfolgreich in die interne `Messwert`-Repräsentation überführt,
- die verifizierten URL- und Dateinamensregeln sind dokumentiert (`doc/DWD/dwd-import-contract-baseline.md`),
- die lokalen Baseline-Fixtures haben eine nachvollziehbare, dokumentierte Real-DWD-Herkunft.

**Ist kein Netzwerk-/DWD-Zugriff verfügbar:** Der Agent STOPPT Phase 5.5, meldet den Status `❌ blockiert`, und erfindet NICHT ersatzweise URLs, Dateinamen, Encodings, Spaltenbreiten oder Archivstrukturen. Phasen 6R/7R/8R/9R/10R bleiben in diesem Fall ebenfalls blockiert; Phase 6–10 (fixture-basiert) gelten weiterhin als abgeschlossen, aber ausdrücklich nur für den fixture-basierten Scope.

---

## Phase 5.6 – Contract Delta Analysis (NEU)

**Voraussetzung:** Phase 5.5 abgeschlossen (nicht blockiert).

Vergleicht den verifizierten externen Kontrakt (`doc/DWD/dwd-import-contract-baseline.md`) systematisch gegen:

- `src/myweatherdata/import_client/dwd_stationsliste_parser.py`,
- `src/myweatherdata/import_client/stationsfinder.py` (insbesondere `STATIONSLISTE_URL`),
- `src/myweatherdata/import_client/dwd_zip_reader.py`,
- `src/myweatherdata/import_client/lufttemperatur_importer.py` (insbesondere `ZIP_URL_TEMPLATE`, `_ZEITSTEMPEL_FORMAT`),
- alle URL- und Dateinamens-Vorlagen im Code,
- bestehende Fixtures unter `tests/fixtures/dwd/`,
- Architekturdokumentation (`arc/statische_sichten/klassensicht-import-client.puml`, `klassensicht.md`, Sequenzsicht),
- `tests/test_plan_import_client.md` und `tests/traceability.md`.

**Ergebnis:** Eine Delta-Liste (bestätigt/korrigiert/unklar aus Phase 5.5, hier auf konkrete Dateien/Zeilen gemappt). Nur Dateien mit einer nachgewiesenen Kontraktabweichung werden in den Remediation-Phasen 6R/7R geändert. Dateien ohne nachgewiesenes Delta bleiben unverändert (Regressionsschutz).

Bekannter, bereits vor Live-Abruf plausibler Kandidat (durch Doku-Abgleich, noch nicht live verifiziert): `ZIP_URL_TEMPLATE` in `lufttemperatur_importer.py` ignoriert den laut Doku vorhandenen Datumsbereich im Dateinamen — muss in Phase 5.5 live bestätigt und danach in Phase 5.6/7R behandelt werden.

---

## Phase 6R – Stationsliste Remediation (NEU, bedingt)

Nur falls Phase 5.6 ein Delta bei Stationsliste-URL, -Encoding, -Spaltenformat oder -Parsing-Logik bestätigt.

- Betrifft potenziell: `dwd_stationsliste_parser.py`, `stationsfinder.py`, `tests/unit/test_stationsfinder.py`, `tests/fixtures/dwd/stationsliste_beispiel.txt` (ergänzt um real-basierte Fixture, nicht ersetzt).
- Vorgehen: Rot-Grün-Refactor. Zuerst ein neuer, aus der realen Baseline abgeleiteter Test schreiben (rot, da er das bisher falsche/unvollständige Verhalten aufdeckt), dann minimale Korrektur, dann grün.
- Bestehende, weiterhin gültige Tests (z. B. Tie-Break FR-004, leere Stationsliste) bleiben unverändert bestehen.

## Phase 7R – ZIP- und Temperatur-Import Remediation (NEU, bedingt)

Nur falls Phase 5.6 ein Delta bei ZIP-URL/-Namensschema, Produktdatei-Erkennung, CSV-Format, Encoding, `MESS_DATUM`-Format oder Fehlwert-Repräsentation bestätigt.

- Betrifft potenziell: `dwd_zip_reader.py`, `lufttemperatur_importer.py`, zugehörige Unit-/Integrationstests, `tests/fixtures/dwd/10minutenwerte_TU_00003_beispiel_hist.zip` (ergänzt, nicht ersetzt).
- Besonders zu behandeln: Falls bestätigt, dass das ZIP-Namensschema einen Datumsbereich enthält, muss die Stationssuche/der Import das korrekte ZIP über ein Verzeichnis-Listing (nicht über ein statisches Template) ermitteln — Design-Konsequenz dokumentieren, bevor Code geändert wird.
- Rot-Grün-Refactor wie in 6R.

## Phase 8R – Regression- und Live-Smoke-Verifikation (NEU)

Nach 6R/7R (oder direkt nach 5.5/5.6, falls kein Delta bestätigt wurde):

1. Vollständige bestehende Suite erneut ausführen (`pytest -v`) — muss weiterhin grün sein (Regression).
2. Den dedizierten Live-Smoke-Test/Spike-Skript manuell ausführen (NICHT Teil des Standardlaufs) und Ergebnis dokumentieren.
3. `mypy --strict src`, `ruff check .`, `ruff format --check .` erneut ausführen.

## Phase 9R – CI- und Repository-Qualitätsgate (NEU)

Zwei Teilaufgaben:

### a) Repository-Hygiene (früh im Ablauf durchführbar, unabhängig vom Spike-Ergebnis)

- `.gitignore` prüfen/ergänzen (bereits vorhanden, aktueller Stand: `.venv/`, `__pycache__/`, `*.py[cod]`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`, `.coverage`, `htmlcov/`, `dist/`, `build/`, `*.egg-info/` — Ist-Zustand bereits ausreichend, aber die Datei selbst ist laut `git status` aktuell noch **nicht committet** (`??`-Status) und zahlreiche `__pycache__/*.pyc`-Dateien sind laut `git ls-files` bereits **im Index getrackt**, obwohl sie ignoriert werden sollten).
- `.venv/` ist laut `git ls-files`-Prüfung dieser Planrevision **nicht** getrackt — hier ist NUR eine Bestätigung/Dokumentation nötig, KEINE Aktion erforderlich.
- Bereits getrackte `__pycache__/*.pyc`-Dateien mit `git rm -r --cached <pfad>` aus dem Index entfernen (Datei bleibt lokal erhalten, nur der Git-Tracking-Zustand ändert sich) und `.gitignore` committen.
- **Ausdrücklich NICHT tun:** das lokale `.venv/`-Verzeichnis des Entwicklers löschen. Es wird ausschließlich das GIT-TRACKING entfernt (`git rm --cached`), niemals das Dateisystem-Verzeichnis selbst, außer der Nutzer fordert dies ausdrücklich an.
- `.github/copilot-instructions.md` aktualisieren: Der Abschnitt „Projektphase" behauptet aktuell fälschlich, es existiere „noch kein Anwendungscode (kein `src/`-Verzeichnis)" und das Projekt befinde sich „aktuell in der Requirements- und Architekturphase" — beides ist überholt, da `src/myweatherdata/` mit vollständiger Hexagonal-Struktur und `tests/` mit 30 grünen Tests existieren. Text ist auf den tatsächlichen Stand (Requirements/Architektur UND laufende Implementierung des Import-Client-Vertical-Slice) zu aktualisieren.

### b) CI als unabhängiger Qualitätsnachweis

Neuer GitHub-Actions-Workflow (`.github/workflows/`), der bei `push` und `pull_request` ausführt:

- Installation aus `pyproject.toml` (inkl. `dev`-Extra),
- den Standard-Testlauf OFFLINE (Live-Marker automatisch ausgeschlossen),
- `mypy --strict src`,
- `ruff check .`,
- `ruff format --check .`,
- einen Check, dass `.venv/` nicht getrackt ist (z. B. `git ls-files | grep -q '^\.venv/' && exit 1 || exit 0`).

Der Live-DWD-Smoke-Test läuft NICHT automatisch in dieser CI. Falls gewünscht, wird er als separater, ausdrücklich optionaler/manueller Workflow (`workflow_dispatch`) ergänzt, niemals in `push`/`pull_request` ausgelöst.

## Phase 10R – Unabhängiges Destructive Re-Review (NEU)

Durch `sw-destructive-reviewer`, nach 9R. Prüft zusätzlich zum bisherigen Scope (siehe v1.0 Phase 10) ausdrücklich:

- Existenz und Evidenzqualität von `doc/DWD/dwd-import-contract-baseline.md`,
- Übereinstimmung von realem Stationslisten-Format und Parser-Verhalten,
- Übereinstimmung von realer ZIP-Namensregel und Download-Verhalten,
- Übereinstimmung von realer Produktdatei-Namensregel und ZIP-Reader-Verhalten,
- dass Fixtures ihre Herkunft (synthetisch vs. real-basiert) kennzeichnen,
- dass mindestens ein Offline-Fixture nachweisbar auf einer echten DWD-Datei basiert,
- dass der Live-Smoke-Test vom deterministischen Suite-Lauf getrennt ist,
- dass der Standard-Testlauf keinen Netzwerkzugriff durchführt,
- dass kein TODO/Docstring eine unverifizierte URL/einen unverifizierten Dateinamen mehr als „implementierte Wahrheit" darstellt,
- dass CI `pytest`, `mypy --strict` und `Ruff` verifiziert,
- dass `.venv/` nicht getrackt ist.

Der Reviewer ändert weiterhin KEINEN Produktionscode. Er darf statische Kontraktbefunde dokumentieren und Offline-Regressionstests ergänzen, wo ein verifizierter Real-DWD-Kontraktverstoß reproduzierbar ist.

---

## Übernommene, unveränderte Inhalte aus v1.0

Die folgenden Abschnitte aus `.github/prompts/plan-importClient.prompt.md` gelten unverändert weiter und werden hier nicht dupliziert, sondern per Referenz übernommen:

- Kernbefund Architektur-Lücke und dessen Lösung (`LufttemperaturImportKoordinator`, `ImportSchnittstelle` als Core-Port).
- Phasenbeschreibungen 0–5 und 8–10 (Wortlaut, Dateien, Testfälle) — siehe Originaldokument, Abschnitt „Steps".
- Relevante Fixtures (bestehende, synthetische Dateien; Herkunft wird in Phase 5.5 zusätzlich dokumentiert, nicht ersetzt).
- Abschnitt „Decisions" (Scope-Begrenzung FR-002/003 deferred, `pandas`-Bedingung, Domänen-Modulaufteilung, Tie-Break-Regel usw.) — bleibt gültig.
- Abschnitt „Weitere Confirmation-Punkte" — Punkt 4 („Exaktes Spalten-/Dateiformat... technischer Spike anhand einer echten DWD-Beispieldatei vor Phase 6/7") gilt durch Phase 5.5 nun als in Bearbeitung/verbindlich eingelöst statt weiterhin offen.

## Verification (ergänzt um v1.1-Gates)

1. Wie v1.0 (TDD rot/grün je Schritt, Gesamtsuite, PlantUML-Review, Testplan/Traceability-Abgleich, Destructive-QA-Review).
2. Zusätzlich: Phase 5.5 darf nicht übersprungen oder durch Annahmen ersetzt werden, bevor Phase 6R/7R/8R/9R/10R beginnen.
3. Zusätzlich: `doc/DWD/dwd-import-contract-baseline.md` muss vor jedem Abschlussbericht existieren, der reale DWD-Integration als fertig behauptet.
4. Zusätzlich: CI-Workflow muss lokal nachvollziehbar dieselben Befehle ausführen wie das lokale Qualitätsgate.

## Decisions (v1.1, zusätzlich zu v1.0)

- `pjm/import-client-implementation-plan.md` ersetzt `.github/prompts/plan-importClient.prompt.md` als autoritative Planquelle ab sofort; der Prompt bleibt als wiederverwendbare Vorlage erhalten.
- Reale DWD-Kontraktverifikation ist ein hartes Gate (Phase 5.5), keine optionale Nacharbeit.
- Repository-Hygiene (Phase 9R.a) ist unabhängig vom Spike-Ergebnis und kann früh parallel erledigt werden.
- CI (Phase 9R.b) prüft ausschließlich den Offline-Pfad; Live-Smoke bleibt manuell/optional.
