# Destructive QA Log — Import-Client Vertical Slice

## Geprüfter Stand

- Workspace: `MyWeatherData` (kein Git-Commit-Hash verfügbar, lokaler Arbeitsstand nach Abschluss von Phase 9 des Import-Client-Plans).
- Geprüfte Quelle: [.github/prompts/plan-importClient.prompt.md](../.github/prompts/plan-importClient.prompt.md), [tests/test_plan_import_client.md](./test_plan_import_client.md), [tests/traceability.md](./traceability.md), FR-001/004/005/006/007/008, `src/myweatherdata/domain/`, `src/myweatherdata/ports/`, `src/myweatherdata/import_client/`, alle bestehenden Unit-/Integrationstests und DWD-Fixtures unter `tests/fixtures/dwd/`.

## Formaler Requirement-Scope

FR-001, FR-004, FR-005, FR-006, FR-007, FR-008 (Vertical Slice Lufttemperatur). FR-002 (Landesgrenze) und FR-003 (Stationsliste nicht abrufbar) sind laut Plan zurückgestellt — keine Prüfung/Tests dafür in diesem Log.

## Ausgeführte Befehle

- `pytest tests\unit\test_zeitraum.py tests\unit\test_datensatz_validator.py tests\unit\test_stationsfinder.py tests\unit\test_dwd_zip_reader.py tests\unit\test_lufttemperatur_importer.py -v` (vor Fix: 6 rot, 17 grün)
- `pytest tests\unit\test_stationsfinder.py::test_stationsliste_mit_unvollstaendiger_zeile_wird_ohne_absturz_verarbeitet -v` (isolierte Nachverfolgung vor Fix)
- Nach den vier Fixes: `pytest tests\unit\test_zeitraum.py tests\unit\test_datensatz_validator.py tests\unit\test_stationsfinder.py tests\unit\test_dwd_zip_reader.py tests\unit\test_lufttemperatur_importer.py -v` → **23/23 grün**
- `pytest -v` (Gesamtsuite) → **30/30 grün**
- `mypy --strict src` → **Success: no issues found in 19 source files**
- `ruff check .` / `ruff format --check .` → **clean**
- grep `except Exception` in `src/` → kein Treffer (nur Docstring-Verweis in `http_client.py`)

## Kurzstatus der vorhandenen Suite vor dieser Session

Vollständige Suite (24 Tests) war grün, `mypy --strict`/`ruff check`/`ruff format --check` clean (Phase 9 Abschlussbericht). Diese Session ergänzte zunächst 6 neue, gezielt fehlschlagende Tests (Destructive QA), ohne bestehende Tests zu verändern oder Produktionscode anzufassen (Ergebnis: 17 bestehende Tests weiterhin grün, 6 neue Tests rot). Anschließend wurden die 4 daraus bestätigten Defekte (DQA-1 bis DQA-4) mit minimalen Produktionscode-Änderungen behoben (`sw-import-client-developer`). **Aktueller Stand: 30/30 Tests grün, Qualitätsgate vollständig clean.**

---

## DQA-1: Zeitraum vollständig außerhalb des unterstützten Bereichs stürzt ab

- Status: `✅ behoben`
- Bezug: FR-006 (Anmerkung: „vollständig außerhalb" ist laut FR-Text nicht spezifiziert, aber die Robustheitserwartung aus FR-007/FR-008 — kein Absturz der App — gilt sinngemäß für den gesamten Importpfad); Plan Phase 10, Abschnitt „Zeitraum und FR-006"
- Betroffene Dateien: `src/myweatherdata/domain/zeitraum.py`, `src/myweatherdata/import_client/lufttemperatur_importer.py`
- Szenario: `LufttemperaturImporter.importiere(station_id, zeitraum)` wird mit einem Zeitraum aufgerufen, der vollständig VOR 01.01.2015 (z. B. 2010-01-01–2010-12-31) oder vollständig NACH 31.12.2025 (z. B. 2026-01-01–2026-12-31) liegt.
- Erwartetes Verhalten: Der Import darf nicht abstürzen; ein sinnvolles `ImportErgebnis` (z. B. leere Messwerte mit Hinweis) muss zurückgegeben werden, analog zur Datenlücken-Behandlung aus FR-008.
- Tatsächliches Verhalten: `Zeitraum.gekuerzt_auf_unterstuetzten_bereich()` berechnet `neuer_start = max(start, 2015-01-01)` und `neues_ende = min(ende, 2025-12-31)` unabhängig voneinander. Liegt der ursprüngliche Zeitraum vollständig vor oder nach dem unterstützten Bereich, entsteht daraus `neuer_start > neues_ende`, wodurch der `Zeitraum`-Konstruktor eine unbehandelte `ValueError` wirft, die bis zum Aufrufer von `importiere()` durchschlägt (Absturz statt kontrolliertem Ergebnis).
- Reproduktionstest: `tests/unit/test_lufttemperatur_importer.py::test_zeitraum_vollstaendig_vor_unterstuetztem_bereich_stuerzt_nicht_ab`, `tests/unit/test_lufttemperatur_importer.py::test_zeitraum_vollstaendig_nach_unterstuetztem_bereich_stuerzt_nicht_ab`
- Testresultat (vor Fix): Beide rot — `ValueError: Zeitraum.start darf nicht nach Zeitraum.ende liegen.` propagiert unbehandelt aus `gekuerzt_auf_unterstuetzten_bereich()`.
- Fix: Neue Methode `Zeitraum.hat_ueberschneidung_mit_unterstuetztem_bereich()` ergänzt (Domain-Invariante bleibt in `Zeitraum` gekapselt). `LufttemperaturImporter.importiere()` prüft diese VOR dem Aufruf von `gekuerzt_auf_unterstuetzten_bereich()`; liegt keine Überschneidung vor, wird sofort ein leeres `ImportErgebnis` mit `_HINWEIS_DATENLUECKE` zurückgegeben, ohne die (weiterhin unveränderte) Kürzungslogik aufzurufen.
- Testresultat (nach Fix): Beide grün.
- Verantwortlicher Folge-Agent: `sw-import-client-developer`

---

## DQA-2: Ungültiges `MESS_DATUM` wird nicht als fehlerhafter Datensatz erkannt und lässt den Import abstürzen

- Status: `✅ behoben`
- Bezug: FR-007 (Akzeptanzkriterium: „Die App stürzt bei fehlerhaften Datensätzen nicht ab"); Plan Phase 10, Abschnitt „DWD ZIP und Parsing" (Szenario „ungültiges MESS_DATUM")
- Betroffene Dateien: `src/myweatherdata/import_client/datensatz_validator.py`, `src/myweatherdata/import_client/lufttemperatur_importer.py`
- Szenario: Ein roher Datensatz enthält alle Pflichtfelder (`STATIONS_ID`, `MESS_DATUM`, `TT_10`) und einen gültigen `TT_10`-Wert, aber `MESS_DATUM` ist kein gültiges Datum im Format `%Y%m%d%H%M` (z. B. `"ABCDEFGHIJKL"`).
- Erwartetes Verhalten: `DatensatzValidator.validiere(...)` muss `False` liefern (Formatfehler gemäß FR-007), der Datensatz wird übersprungen, der restliche Import läuft fehlerfrei weiter.
- Tatsächliches Verhalten: `DatensatzValidator.validiere()` prüft nur, ob `MESS_DATUM` als Schlüssel vorhanden ist — der Wert selbst wird nie gegen das Zeitstempelformat geprüft. Der Datensatz besteht die Validierung fälschlich (`True`). Erst in `LufttemperaturImporter._zu_messwerten()` wird `datetime.strptime(rohdatensatz["MESS_DATUM"], _ZEITSTEMPEL_FORMAT)` aufgerufen, was eine unbehandelte `ValueError` wirft und den gesamten Import abbrechen lässt — direkter Verstoß gegen das FR-007-Akzeptanzkriterium „App stürzt nicht ab".
- Reproduktionstest: `tests/unit/test_datensatz_validator.py::test_rohdatensatz_mit_defektem_mess_datum_besteht_validierung_nicht`, `tests/unit/test_lufttemperatur_importer.py::test_datensatz_mit_defektem_mess_datum_wird_uebersprungen_statt_absturz` (nutzt neue Fixture `tests/fixtures/dwd/10minutenwerte_TU_00099_defekt_mess_datum_hist.zip`)
- Testresultat (vor Fix): Beide rot — Validator liefert `True` statt `False`; Importer wirft `ValueError: time data 'ABCDEFGHIJKL' does not match format '%Y%m%d%H%M'` unbehandelt.
- Fix: `DatensatzValidator.validiere()` versucht zusätzlich `datetime.strptime(rohdatensatz["MESS_DATUM"], _ZEITSTEMPEL_FORMAT)`; bei `ValueError` liefert die Methode `False`. Dadurch wird der Datensatz bereits in der Validierung verworfen, bevor `LufttemperaturImporter._zu_messwerten()` den Zeitstempel erneut parst.
- Testresultat (nach Fix): Beide grün.
- Verantwortlicher Folge-Agent: `sw-import-client-developer`

---

## DQA-3: Unvollständige/zu kurze Stationszeile lässt die Stationssuche abstürzen

- Status: `✅ behoben`
- Bezug: FR-001 (Robustheit, sinngemäß analog FR-007 „kein Absturz der App"); Plan Phase 10, Abschnitt „Stationssuche und Distanz" (Szenario „fehlerhafte oder unvollständige Stationszeilen")
- Betroffene Dateien: `src/myweatherdata/import_client/dwd_stationsliste_parser.py`
- Szenario: Die DWD-Stationsliste enthält eine Zeile, die kürzer ist als die aus der Trennzeile abgeleiteten Spaltenbreiten (z. B. eine Zeile, die nach `Stationshoehe` abbricht und `geoBreite`/`geoLaenge`/`Stationsname`/`Bundesland` nicht mehr enthält).
- Erwartetes Verhalten: Die fehlerhafte Zeile sollte übersprungen werden (analog zur Fehlerbehandlungs-Philosophie aus FR-007 für Messdatensätze), die übrigen, korrekten Stationszeilen bleiben nutzbar.
- Tatsächliches Verhalten: `_zeile_in_spalten_zerlegen()` schneidet Substrings anhand fester Positionen ohne Längenprüfung; bei einer zu kurzen Zeile liefern `geoBreite`/`geoLaenge` leere Strings. `float("".strip())` wirft eine unbehandelte `ValueError`, die aus `parse_stationsliste()` bis zu `StationsFinder.finde_naechste()` durchschlägt und die gesamte Stationssuche abstürzen lässt — auch wenn andere Stationszeilen der Liste vollständig gültig wären.
- Reproduktionstest: `tests/unit/test_stationsfinder.py::test_stationsliste_mit_unvollstaendiger_zeile_wird_ohne_absturz_verarbeitet` (neue Fixture `tests/fixtures/dwd/stationsliste_defekte_zeile.txt`)
- Testresultat (vor Fix): Rot — `ValueError: could not convert string to float: ''` in `dwd_stationsliste_parser.py`, Zeile mit `float(felder["geobreite"].strip())`.
- Fix: Die Konstruktion der `Koordinate` (inkl. der beiden `float(...)`-Aufrufe) ist pro Zeile in einen gezielten `try/except ValueError` eingebettet; schlägt die Konvertierung fehl, wird die Zeile übersprungen (`continue`) statt die Exception zu propagieren. Kein `except Exception`.
- Testresultat (nach Fix): Grün.
- Verantwortlicher Folge-Agent: `sw-import-client-developer`

---

## DQA-4: ZIP mit mehreren `produkt_*`-Dateien wird stillschweigend mehrdeutig verarbeitet

- Status: `✅ behoben`
- Bezug: Architekturhygiene / dokumentierte Modul-Annahme in `src/myweatherdata/import_client/dwd_zip_reader.py` (Docstring: „die ZIP-Datei enthält... genau eine Datei mit Präfix `produkt_`"); Plan Phase 10, Abschnitt „DWD ZIP und Parsing" (Szenario „ZIP mit mehreren möglichen Produktdateien")
- Betroffene Dateien: `src/myweatherdata/import_client/dwd_zip_reader.py`
- Szenario: Ein ZIP-Archiv enthält zwei unterschiedliche Dateien mit Präfix `produkt_` (z. B. unterschiedliche Zeiträume/Inhalte).
- Erwartetes Verhalten: Da die dokumentierte Kernannahme des Moduls „genau eine Produktdatei" lautet, muss ein Verstoß dagegen als Formatfehler (`DwdZipFormatError`) erkannt werden — analog zum bereits behandelten Fall „keine Produktdatei gefunden".
- Tatsächliches Verhalten: `_finde_produkt_datei()` gibt den ERSTEN Treffer aus `archiv.namelist()` zurück und bricht die Suche sofort ab; eine zweite passende Datei wird nie geprüft. Bei mehreren Produktdateien wird also stillschweigend und von der (nicht garantiert stabilen) ZIP-internen Reihenfolge abhängig eine beliebige der beiden Dateien verwendet, ohne dass dies erkennbar oder deterministisch nachvollziehbar wäre.
- Reproduktionstest: `tests/unit/test_dwd_zip_reader.py::test_zip_mit_mehreren_produkt_dateien_wirft_dwd_zip_format_error`
- Testresultat (vor Fix): Rot — `Failed: DID NOT RAISE DwdZipFormatError` (aktuelle Implementierung liest kommentarlos eine der beiden Dateien ein).
- Fix: `_finde_produkt_datei()` sammelt jetzt ALLE Namen mit Präfix `produkt_`; bei keinem Treffer wie bisher `DwdZipFormatError` (kein Produktfile), bei mehr als einem Treffer NEU ebenfalls `DwdZipFormatError` (Mehrdeutigkeit), nur bei genau einem Treffer wird dieser zurückgegeben.
- Testresultat (nach Fix): Grün.
- Verantwortlicher Folge-Agent: `sw-import-client-developer`

---

## ⚠️ Offene Risiken (nicht als bestätigter Defekt automatisiert reproduzierbar)

### DQA-R1: Keine Validierung der mathematisch zulässigen Koordinaten-Grenzwerte

- Status: `⚠️ Risiko`
- Bezug: Architekturregel/Domain-Invariante (kein konkretes FR im aktuellen Scope, da FR-002 — Landesgrenze — zurückgestellt ist und ausdrücklich NICHT geprüft werden soll)
- Betroffene Dateien: `src/myweatherdata/domain/koordinate.py`, `src/myweatherdata/import_client/distanz.py`
- Szenario: `Koordinate(breitengrad=200.0, laengengrad=500.0)` — Werte weit außerhalb der mathematisch zulässigen Bereiche `-90/90` bzw. `-180/180`.
- Begründung, warum nicht als bestätigter Defekt dokumentiert: Die Haversine-Formel in `distanz_km()` ist mathematisch so aufgebaut (`a = sin²(Δlat/2) + cos(lat1)·cos(lat2)·sin²(Δlon/2)`), dass der Term unter der Wurzel für JEDEN reellen Winkel im Intervall `[0, 1]` bleibt (trigonometrische Identität, äquivalent zum sphärischen Kosinussatz) — ein Absturz (`math domain error`) konnte für keine getestete Kombination reproduziert werden. Das Modul `Koordinate` validiert die Grenzwerte dennoch nicht, wodurch rein numerisch plausible, aber geografisch unsinnige Distanzen berechnet werden könnten.
- Empfohlene Prüfung: Klären, ob `Koordinate.__post_init__` eine Bereichsprüfung (`-90 <= breitengrad <= 90`, `-180 <= laengengrad <= 180`) erhalten soll, unabhängig von der (zurückgestellten) Landesgrenzprüfung aus FR-002. Kein automatischer Testfall ergänzt, da kein reproduzierbarer Absturz und keine FR-Vorgabe im aktuellen Scope vorliegt.

### DQA-R2: Keine Behandlung doppelter oder unsortierter Zeitstempel im Lufttemperatur-Import

- Status: `⚠️ Risiko`
- Bezug: Kein explizites FR im aktuellen Scope (FR-005/006/007/008 spezifizieren weder Deduplizierung noch Sortierung)
- Betroffene Dateien: `src/myweatherdata/import_client/lufttemperatur_importer.py`
- Szenario: Die DWD-ZIP-Rohdaten enthalten zwei Zeilen mit identischem `MESS_DATUM` oder Zeilen in nicht-chronologischer Reihenfolge.
- Begründung, warum nicht als bestätigter Defekt dokumentiert: `_zu_messwerten()` übernimmt Datensätze unverändert in Eingabereihenfolge; es gibt keinen Crash, nur ein potenziell aus Sicht der Visualisierung unerwartetes Ergebnis (Duplikate/unsortierte Liste). Da keines der FR-005/006/007/008-Akzeptanzkriterien Deduplizierung oder Sortierung fordert, ist unklar, ob dies überhaupt fachlich unerwünscht ist.
- Empfohlene Prüfung: Mit PO/Datenhaltung-Verantwortlichem klären, ob Deduplizierung/Sortierung Aufgabe des Import-Client oder der nachgelagerten Datenhaltung ist, bevor ein Testfall ergänzt wird.

### DQA-R3: `parse_stationsliste` reagiert empfindlich auf abweichende Leerzeichen-Konventionen in der Trennzeile

- Status: `⚠️ Risiko`
- Bezug: Weitere Confirmation-Punkte Nr. 4 im Plan (unverifizierte DWD-Format-Spike-Annahme)
- Betroffene Dateien: `src/myweatherdata/import_client/dwd_stationsliste_parser.py`
- Szenario: Enthält die reale DWD-Trennzeile z. B. doppelte Leerzeichen zwischen Spaltengruppen (abweichend von der Fixture-Annahme), würde `zeilen[1].split(" ")` leere Zwischenelemente erzeugen und die abgeleiteten Spaltenbreiten verfälschen.
- Begründung, warum nicht als bestätigter Defekt dokumentiert: Ohne eine echte, verifizierte DWD-Beispieldatei (offener Spike-Punkt laut Plan) lässt sich nicht zuverlässig reproduzieren, ob dieses Szenario in der Praxis auftritt; ein synthetischer Test würde nur die bereits bekannte Fragilität der Spike-Annahme wiederholen, nicht einen eigenständigen neuen Fehler nachweisen.
- Empfohlene Prüfung: Nach Abschluss des in Confirmation-Punkt 4 geforderten DWD-Format-Spikes mit einer echten Stationsliste erneut prüfen.
- **Addendum (Phase 10R, diese Session):** Dieses Risiko ist inzwischen **überholt/gegenstandslos**. Seit Phase 6R (`pjm/import-client-implementation-plan.md`) leitet `dwd_stationsliste_parser.py` die Spaltenbreiten nicht mehr aus der Trennzeile ab, sondern verwendet feste, gegen `doc/DWD/dwd-import-contract-baseline.md` verifizierte Byte-Offsets. Die hier beschriebene Fragilität (`zeilen[1].split(" ")`) existiert im aktuellen Code nicht mehr. Dieser Eintrag bleibt gemäß Vorgabe unverändert erhalten und wird nicht gelöscht; er ist nur noch als historischer Kontext relevant.

---

## Zusammenfassung

- **Bestätigte Defekte:** 4 (DQA-1 bis DQA-4) — **alle 4 behoben** (`sw-import-client-developer`, minimale Fixes, siehe jeweiliger Abschnitt)
- **Offene Risiken:** 3 (DQA-R1 bis DQA-R3) — unverändert offen, keine PO-Entscheidung in dieser Session
- **Neu erstellte/geänderte Test-/Fixture-Dateien (Destructive-QA-Phase):**
  - `tests/unit/test_lufttemperatur_importer.py` (3 neue Tests ergänzt)
  - `tests/unit/test_datensatz_validator.py` (1 neuer Test ergänzt)
  - `tests/unit/test_stationsfinder.py` (1 neuer Test ergänzt)
  - `tests/unit/test_dwd_zip_reader.py` (1 neuer Test ergänzt)
  - `tests/fixtures/dwd/10minutenwerte_TU_00099_defekt_mess_datum_hist.zip` (neue Defekt-Fixture)
  - `tests/fixtures/dwd/stationsliste_defekte_zeile.txt` (neue Defekt-Fixture)
  - `tests/destructive-qa-log.md` (dieses Dokument)
- **Geänderte Produktionsdateien (Fix-Phase, `sw-import-client-developer`):**
  - `src/myweatherdata/domain/zeitraum.py` (neue Methode `hat_ueberschneidung_mit_unterstuetztem_bereich()`)
  - `src/myweatherdata/import_client/lufttemperatur_importer.py` (Kurzschluss für Zeitraum ohne Überschneidung vor der Kürzung)
  - `src/myweatherdata/import_client/datensatz_validator.py` (MESS_DATUM-Formatprüfung ergänzt)
  - `src/myweatherdata/import_client/dwd_stationsliste_parser.py` (defekte Zeilen werden übersprungen statt zu crashen)
  - `src/myweatherdata/import_client/dwd_zip_reader.py` (Mehrdeutigkeit bei mehreren Produktdateien erkannt)
- Keine bestehenden Tests wurden abgeschwächt, gelöscht oder inhaltlich verändert; lediglich Docstring-/Kommentar-Zeilenlängen in den neuen Tests wurden für `ruff format`/`ruff check` angepasst (keine Assertion-Änderungen).
- **Vollständige Qualitätsgate-Verifikation nach den Fixes:** `pytest -v` 30/30 grün, `mypy --strict src` clean, `ruff check`/`ruff format --check` clean, kein `except Exception` in `src/`.
- **Scope-Check:** Keine Tests für FR-002/FR-003 ergänzt; keine Prüfung von Niederschlag/Wind/Sonne/CSV/SQLite/Streamlit/Plotly; Landesgrenzprüfung explizit ausgeklammert (DQA-R1 prüft nur mathematische Grenzwerte, nicht deutsche Landesgrenzen).

---

# Phase 10R — Unabhängiges Destructive Re-Review (Real-DWD-Kontrakt)

## Geprüfter Stand

- Workspace: `MyWeatherData`, lokaler Arbeitsstand nach Abschluss von Plan-Phasen 5.5/5.6/6R/7R/8R/9R (`pjm/import-client-implementation-plan.md`, v1.1). Zu diesem Zeitpunkt: `pytest -v` 39/39 grün + 2 deselektiert (`live`-Marker), `mypy --strict src` clean, `ruff check .`/`ruff format --check .` clean, Live-Smoke-Test (`tests/integration/test_live_dwd_smoke.py`) manuell 2/2 grün (2026-07-20).
- Geprüfte Quelle: `pjm/import-client-implementation-plan.md` (v1.1, autoritativ), `pjm/vertical-slice-prototyp.md`, FR-001/004/005/006/007/008, `tests/test_plan_import_client.md`, `tests/traceability.md`, [python-guidelines](../.github/skills/python-guidelines/SKILL.md), `arc/statische_sichten/klassensicht-import-client.puml`/`klassensicht.md`, vollständiger Produktionscode unter `src/myweatherdata/import_client/` und `src/myweatherdata/domain/`/`src/myweatherdata/ports/`, alle Unit-/Integrationstests, `tests/fixtures/dwd/` inkl. `README.md`, `doc/DWD/dwd-import-contract-baseline.md`, `.github/workflows/ci.yml`.

## Formaler Requirement-Scope

FR-001, FR-004, FR-005, FR-006, FR-007, FR-008. FR-002/FR-003 weiterhin zurückgestellt, keine Tests dafür ergänzt. Zusätzlich (laut Plan Phase 10R): Übereinstimmung von realem DWD-Kontrakt (Baseline-Dokument) mit tatsächlichem Parser-/Reader-/Download-Verhalten.

## Ausgeführte Befehle

- Verifikationsskript (temporär, außerhalb des erlaubten Schreibbereichs erzeugt und sofort wieder gelöscht) zur Bestätigung der STATIONS_ID-Feld-Hypothese gegen die reale Spaltenformatierung.
- `pytest -m live tests/integration/test_live_dwd_smoke.py -v` — bereits vor dieser Session grün (nicht erneut gegen das Live-Netzwerk ausgeführt, um wiederholte externe Zugriffe zu vermeiden; Ergebnis unverändert aus dem letzten Entwickler-Lauf übernommen).
- `pytest tests/unit/test_dwd_zip_reader.py tests/unit/test_lufttemperatur_importer.py -v` → 3 neue Tests rot, 11 bestehende Tests weiterhin grün.
- `pytest -v` (Gesamtsuite) → **3 neu rot, 39 bestehende weiterhin grün, 2 deselektiert (`live`)**.
- `ruff format --check tests/unit/test_dwd_zip_reader.py tests/unit/test_lufttemperatur_importer.py` / `ruff check` → clean nach kleiner Zeilenlängen-Korrektur in den neuen Tests.
- `git ls-files | Select-String -Pattern '\.venv'` → kein Treffer (bestätigt: `.venv/` nicht getrackt).

## Kurzstatus der vorhandenen Suite vor dieser Session

39 Tests grün, 2 `live`-Tests deselektiert im Standardlauf, Qualitätsgate (`mypy --strict`, `ruff check`, `ruff format --check`) clean, Live-Smoke-Test manuell 2/2 grün. Diese Session ergänzt 3 neue, gezielt fehlschlagende Tests (DQA-5 bis DQA-7), ohne bestehende Tests oder Produktionscode zu verändern. **Aktueller Stand: 39 bestehende Tests weiterhin grün, 3 neue Tests rot.**

---

## DQA-5: `Messwert.station_id` verliert bei realer DWD-Spaltenformatierung die führenden Nullen und weicht von der angefragten Station ab

- Status: `✅ behoben`
- Bezug: FR-005 (Akzeptanzkriterium: „Die geladenen Werte werden in einem einheitlichen internen Format bereitgestellt"); Architekturregel Datenkonsistenz zwischen `ImportErgebnis.station.station_id` (vom `LufttemperaturImportKoordinator` gesetzt) und `ImportErgebnis.messwerte[i].station_id`
- Betroffene Dateien: `src/myweatherdata/import_client/lufttemperatur_importer.py` (`_zu_messwerten`), `src/myweatherdata/import_client/dwd_zip_reader.py` (Ursache: `.strip()` auf rechtsbündigem `STATIONS_ID`-Feld)
- Szenario: Die reale DWD-ZIP-Produktdatei enthält die `STATIONS_ID`-Spalte rechtsbündig ohne führende Nullen (bestätigt in `doc/DWD/dwd-import-contract-baseline.md`, Abschnitt 2, und bereits in `tests/unit/test_dwd_zip_reader.py::test_realer_auszug_wird_korrekt_eingelesen_und_validiert` als Kontraktbefund dokumentiert: Feld `"          3"` wird nach `.strip()` zu `"3"`). `LufttemperaturImporter._zu_messwerten()` übernimmt diesen Rohwert unverändert als `Messwert.station_id`, statt die im Methodenaufruf bereits bekannte, mit führenden Nullen versehene angefragte `station_id` zu verwenden.
- Erwartetes Verhalten: `Messwert.station_id` sollte konsistent mit `ImportErgebnis.station.station_id` (z. B. `"00003"`) sein, da beide dieselbe Station referenzieren und die App laut FR-005 ein „einheitliches internes Format" liefern soll. Eine nachgelagerte Datenhaltung (SQLite, künftige Komponente), die `Station`/`Messwert` über `station_id` verknüpft, würde bei realen Daten sonst niemals einen Treffer finden (`"00003"` vs. `"3"`).
- Tatsächliches Verhalten: Bei realen ZIP-Daten liefert `Messwert.station_id == "3"`, während `ImportErgebnis.station.station_id == "00003"` bleibt (durch `StationsFinder`/`LufttemperaturImportKoordinator` bereits korrekt mit führenden Nullen). Bei synthetischen Fixtures (`STATIONS_ID` bereits als `"00003"` ohne führende Leerzeichen im Feld hinterlegt) tritt der Defekt NICHT auf — daher blieb er bisher unentdeckt.
- Reproduktionstest: `tests/unit/test_lufttemperatur_importer.py::test_messwert_station_id_entspricht_angefragter_stations_id_trotz_realer_formatierung`
- Testresultat (vor Fix): Rot — `AssertionError: assert '3' == '00003'`.
- Fix: `LufttemperaturImporter._zu_messwerten()` erhält jetzt zusätzlich die angefragte `station_id` als Parameter und verwendet diese für `Messwert.station_id` statt `rohdatensatz["STATIONS_ID"]`, analog zur bereits bestehenden Praxis in `ImportErgebnis.station=StationsTreffer(station_id=station_id, ...)` in derselben Methode.
- Testresultat (nach Fix): Grün.
- Verantwortlicher Folge-Agent: `sw-import-client-developer` (behoben)

---

## DQA-6: CSV-Zeile mit weniger Feldern als die Kopfzeile lässt `lese_rohdatensaetze()` abstürzen

- Status: `✅ behoben`
- Bezug: FR-007 (Akzeptanzkriterium: „Die App stürzt bei fehlerhaften Datensätzen nicht ab"); Plan Phase 10R / Plan-Abschnitt „DWD ZIP und Parsing" (Szenario „fehlende Pflichtspalten" / „gemischte gültige und fehlerhafte Zeilen")
- Betroffene Dateien: `src/myweatherdata/import_client/dwd_zip_reader.py`
- Szenario: Eine Datenzeile der Produktdatei enthält weniger `;`-getrennte Felder als die Kopfzeile (z. B. durch eine abgeschnittene/unvollständig geschriebene Zeile am Ende einer realen Datei).
- Erwartetes Verhalten: Der unvollständige Datensatz darf den Lesevorgang nicht abstürzen lassen — analog zur bestehenden Fehlerbehandlungs-Philosophie aus FR-007 (fehlerhafte Datensätze werden übersprungen/als ungültig markiert, der restliche Import läuft weiter).
- Tatsächliches Verhalten: `csv.DictReader` befüllt bei einer zu kurzen Zeile die fehlenden Schlüssel mit `None` (Standard-`restval`). Die anschließende Dict-Comprehension `{schluessel.strip(): wert.strip() for schluessel, wert in zeile.items()}` ruft `.strip()` auf diesem `None`-Wert auf und wirft eine unbehandelte `AttributeError: 'NoneType' object has no attribute 'strip'`, die aus `lese_rohdatensaetze()` bis zum Aufrufer (`LufttemperaturImporter.importiere()`) durchschlägt und den gesamten Import abbrechen lässt — auch wenn andere Zeilen der Datei vollständig gültig wären.
- Reproduktionstest: `tests/unit/test_dwd_zip_reader.py::test_zeile_mit_weniger_spalten_als_kopfzeile_wird_ohne_absturz_verarbeitet`
- Testresultat (vor Fix): Rot — `AttributeError: 'NoneType' object has no attribute 'strip'` in `dwd_zip_reader.py`, Zeile mit `{schluessel.strip(): wert.strip() for ...}`.
- Fix: Die Dict-Comprehension in `lese_rohdatensaetze()` behandelt fehlende Werte jetzt explizit (`wert.strip() if wert is not None else ""`), sodass fehlende Felder als leerer String statt `None` erscheinen. Der bestehende `DatensatzValidator`-Vertrag (prüft Schlüssel-Anwesenheit und Formatgültigkeit der Werte) verwirft den dadurch weiterhin unvollständigen Datensatz regulär, sobald ein Pflichtfeld betroffen ist.
- Testresultat (nach Fix): Grün.
- Verantwortlicher Folge-Agent: `sw-import-client-developer` (behoben)

---

## DQA-7: CSV-Zeile mit zusätzlicher unbekannter Spalte lässt `lese_rohdatensaetze()` abstürzen

- Status: `✅ behoben`
- Bezug: FR-007 (Akzeptanzkriterium: „Die App stürzt bei fehlerhaften Datensätzen nicht ab"); Plan Phase 10R / Plan-Abschnitt „DWD ZIP und Parsing" (Szenario „zusätzliche unbekannte Spalten")
- Betroffene Dateien: `src/myweatherdata/import_client/dwd_zip_reader.py`
- Szenario: Eine Datenzeile enthält mehr `;`-getrennte Felder als die Kopfzeile Spaltennamen definiert (z. B. eine zusätzliche, im aktuellen Format nicht dokumentierte Spalte einer künftigen DWD-Formatversion).
- Erwartetes Verhalten: Die zusätzliche, unbekannte Spalte darf den Lesevorgang nicht abstürzen lassen; die bekannten Spalten des Datensatzes sollten regulär nutzbar bleiben (analog zur Fehlertoleranz-Philosophie aus FR-007).
- Tatsächliches Verhalten: `csv.DictReader` sammelt Werte ohne passenden Spaltennamen unter dem Schlüssel `None` (Standard-`restkey`) in einer Liste. Die Dict-Comprehension ruft `schluessel.strip()` auf diesem `None`-Schlüssel auf und wirft dieselbe unbehandelte `AttributeError` wie bei DQA-6, wodurch der gesamte Import abbricht.
- Reproduktionstest: `tests/unit/test_dwd_zip_reader.py::test_zeile_mit_zusaetzlicher_unbekannter_spalte_wird_ohne_absturz_verarbeitet`
- Testresultat (vor Fix): Rot — `AttributeError: 'NoneType' object has no attribute 'strip'` in `dwd_zip_reader.py`, identische Ursache wie DQA-6, aber ausgelöst durch den `restkey=None`-Mechanismus statt `restval=None`.
- Fix: Dieselbe Dict-Comprehension in `lese_rohdatensaetze()` überspringt jetzt Einträge mit `schluessel is None` (den `restkey`-Eintrag) explizit, bevor `.strip()` aufgerufen wird — die bekannten, benannten Spalten bleiben davon unberührt.
- Testresultat (nach Fix): Grün.
- Verantwortlicher Folge-Agent: `sw-import-client-developer` (behoben)

---

## ⚠️ Statischer Befund (nicht automatisiert reproduzierbar, keine Produktionscode-Datei)

### DQA-R4: CI-Workflow prüft nicht, dass `.venv/` nicht getrackt ist

- Status: `⚠️ Risiko`
- Bezug: `pjm/import-client-implementation-plan.md`, Phase 9R.b (verbindliche CI-Anforderung: „einen Check, dass `.venv/` nicht getrackt ist (z. B. `git ls-files | grep -q '^\.venv/' && exit 1 || exit 0`)")
- Betroffene Datei: `.github/workflows/ci.yml`
- Befund: Der Workflow führt `pytest`, `mypy --strict src`, `ruff check .` und `ruff format --check .` aus, enthält aber KEINEN Schritt, der überprüft, dass `.venv/` nicht im Git-Index getrackt ist. Diese Prüfung ist im Plan als expliziter Bestandteil von Phase 9R.b gefordert.
- Begründung, warum nicht als Test reproduzierbar: Es handelt sich um eine fehlende CI-Konfigurationszeile, kein Python-Verhalten — nicht durch einen `pytest`-Test abbildbar. Lokal ist `.venv/` nachweislich nicht getrackt (`git ls-files | Select-String -Pattern '\.venv'` liefert keinen Treffer), das Risiko besteht ausschließlich darin, dass ein künftiger Regressions-Fall (`.venv/` wird versehentlich committet) von der aktuellen CI nicht erkannt würde.
- Empfohlene Prüfung/Korrektur: `.github/workflows/ci.yml` um einen zusätzlichen Schritt ergänzen, der den Plan-Wortlaut umsetzt (liegt außerhalb des Schreibbereichs dieses Reviews, da `.github/` für `sw-destructive-reviewer` gesperrt ist).
- Verantwortlicher Folge-Agent: `sw-import-client-developer`

---

## Zusammenfassung Phase 10R

- **Bestätigte Defekte:** 3 (DQA-5, DQA-6, DQA-7) — alle mit fehlschlagendem Reproduktionstest belegt und anschließend (`sw-import-client-developer`) mit minimalem Fix behoben.
- **Offene Risiken:** 1 neu (DQA-R4, CI-Konfigurationslücke, weiterhin offen — außerhalb des Schreibbereichs von `sw-destructive-reviewer`, kein reproduzierender Test möglich); die bestehenden DQA-R1 bis DQA-R3 aus der vorherigen Session bleiben unverändert offen (siehe oben) und wurden in dieser Session erneut überprüft, aber nicht neu bewertet, da sich an ihrer Grundlage nichts geändert hat.
- **Neu erstellte/geänderte Test-Dateien:**
  - `tests/unit/test_dwd_zip_reader.py` (2 neue Tests ergänzt: DQA-6, DQA-7)
  - `tests/unit/test_lufttemperatur_importer.py` (1 neuer Test ergänzt: DQA-5, zusätzliche Imports `io`/`zipfile`)
  - `tests/destructive-qa-log.md` (dieser Abschnitt)
- **Keine Fixture-Dateien unter `tests/fixtures/dwd/` ergänzt** — alle drei neuen Tests konstruieren ihre ZIP-Bytes inline über `io.BytesIO`/`zipfile.ZipFile` (analog zu bestehenden Tests wie `test_zip_mit_mehreren_produkt_dateien_wirft_dwd_zip_format_error`), eine zusätzliche Fixture-Datei war nicht erforderlich.
- **Fix-Phase (`sw-import-client-developer`, im Anschluss an diesen Review):**
  - `src/myweatherdata/import_client/dwd_zip_reader.py`: Dict-Comprehension in `lese_rohdatensaetze()` behandelt fehlende Werte (`restval=None`) als leeren String und ignoriert den `restkey=None`-Eintrag bei zusätzlichen unbekannten Spalten (behebt DQA-6, DQA-7).
  - `src/myweatherdata/import_client/lufttemperatur_importer.py`: `_zu_messwerten()` erhält zusätzlich die angefragte `station_id` als Parameter und verwendet diese für `Messwert.station_id` statt des rohen CSV-Feldes `rohdatensatz["STATIONS_ID"]` (behebt DQA-5).
  - Keine bestehenden Tests wurden verändert; die 3 zuvor roten Reproduktionstests sind jetzt grün.
- **Regressionsstatus (nach Fix):** `pytest -v` → **42 Tests grün, 2 deselektiert** (`live`-Marker unverändert), keine Regression. `mypy --strict src` clean, `ruff check .`/`ruff format --check .` clean, kein `except Exception` in `src/` (grep-Check, nur Docstring-Erwähnung in `http_client.py`).
- **Real-DWD-Kontrakt-Abgleich (Phase 10R-Checkliste):** `doc/DWD/dwd-import-contract-baseline.md` existiert mit Abrufdatum, verifizierten URLs und Rohformat-Auszügen (kein reiner Annahme-Text). Stationslisten-Format und Parser-Verhalten stimmen überein (reale Byte-Offsets, verifiziert durch `test_dwd_stationsliste_parser.py`). ZIP-Namensregel und Download-Verhalten stimmen überein (`dwd_archiv_verzeichnis.py`, verifiziert durch `test_dwd_archiv_verzeichnis.py`). Produktdatei-Namensregel und ZIP-Reader-Verhalten stimmen nach den Fixes für DQA-5/6/7 nun auch bei der Feldbehandlung (`STATIONS_ID`-Spalte, CSV-Spaltenanzahl-Abweichungen) überein. Fixtures kennzeichnen ihre Herkunft (synthetisch/real-basiert) in `tests/fixtures/dwd/README.md`. Mindestens ein Offline-Fixture ist auf eine echte DWD-Datei zurückführbar (`stationsliste_real_auszug.txt`, `10minutenwerte_TU_00003_real_auszug_hist.zip`). Live-Smoke-Test ist über den `live`-Marker eindeutig vom Standardlauf getrennt; Standardlauf greift nachweislich nicht auf das Netzwerk zu (ausschließlich `FakeHttpClient` in Unit-/Integrationstests). Kein TODO/Docstring stellt eine unverifizierte Annahme mehr als „implementierte Wahrheit" dar. CI verifiziert `pytest`, `mypy --strict` und `ruff`, ABER NICHT den `.venv`-Tracking-Status (DQA-R4, weiterhin offen).
- **Scope-Check:** Keine Tests für FR-002/FR-003 ergänzt; keine Prüfung von Niederschlag/Wind/Sonne/CSV/SQLite/Streamlit/Plotly.
