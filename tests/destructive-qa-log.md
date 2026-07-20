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
