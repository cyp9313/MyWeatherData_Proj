# DWD-Test-Fixtures

Referenzierte Beispieldateien für die Unit-/Integrationstests, siehe
[Testplan](../../test_plan_import_client.md). Seit Phase 5.5 (Real-DWD Contract Spike,
siehe `doc/DWD/dwd-import-contract-baseline.md`) wird jede Fixture-Datei mit ihrer Herkunft
klassifiziert: **synthetisch** (frei erfunden, ausschließlich für gezielte Randfall-Tests),
**real-basiert** (reduzierter, aber unveränderter Auszug aus einer echten, live abgerufenen
DWD-Datei) oder **destructive-QA-only** (ausschließlich vom Destructive Reviewer für
Regressionstests genutzt).

## Stationsliste

- `stationsliste_beispiel.txt` — **synthetisch**. Frei erfundene, kleine Stationsliste inkl.
  Tie-Break-Paar (FR-004). Verwendet ein Spaltenlayout, das auf der (durch Phase 5.5 als falsch
  erkannten) Trennzeilen-Breiten-Annahme beruht. Bleibt als gezielter Test für die Tie-Break-Logik
  (FR-004) und die generelle Parser-API bestehen, ist aber **kein** Nachweis für reale
  DWD-Konformität.
- `stationsliste_defekte_zeile.txt` — **synthetisch**. Enthält eine absichtlich fehlerhafte
  Zeile zum Testen der Fehlerbehandlung defekter Datensätze. Gleiche Einschränkung wie oben.
- `stationsliste_real_auszug.txt` — **real-basiert**. Kopf- und Trennzeile sowie 6 reale
  Datenzeilen (Stationen `00003` Aachen, `00044` Großenkneten, `00071` Albstadt-Badkap, `00073`
  Aldersbach-Kramersepp, `00460` Berus, `20098` Seebach), unverändert übernommen aus der am
  2026-07-20 live abgerufenen offiziellen Datei
  `https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/10_minutes/air_temperature/historical/zehn_min_tu_Beschreibung_Stationen.txt`
  (siehe `doc/DWD/dwd-import-contract-baseline.md`, Abschnitt 1). Bewusst gewählt mit
  unterschiedlicher Ziffernlänge bei `Stationshoehe` (2–4 Ziffern), um die feste
  Byte-Offset-Parsing-Logik gegen reale Varianz abzusichern.

## Historisches Lufttemperatur-Archiv

- `10minutenwerte_TU_00003_beispiel_hist.zip` — **synthetisch**. Enthält gültige, fehlerhafte
  und `-999`-Fehlwert-Zeilen sowie einen Datenlücke-Zeitraum, gezielt für Randfall-Tests
  (FR-007, FR-008) konstruiert.
- `10minutenwerte_TU_00099_defekt_mess_datum_hist.zip` — **synthetisch**. Enthält einen Datensatz
  mit ungültigem `MESS_DATUM`-Format zum Testen der Validierung (FR-007).
- `10minutenwerte_TU_00003_real_auszug_hist.zip` — **real-basiert**. Enthält die reale
  Produktdatei `produkt_zehn_min_tu_20100101_20110331_00003.txt`, reduziert auf Kopfzeile plus
  die ersten 20 realen Datenzeilen (unveränderter Inhalt, nur gekürzt), unverändert übernommen
  aus dem am 2026-07-20 live abgerufenen offiziellen Archiv
  `https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/10_minutes/air_temperature/historical/10minutenwerte_TU_00003_20100101_20110331_hist.zip`
  (siehe `doc/DWD/dwd-import-contract-baseline.md`, Abschnitt 2).

Alle real-basierten Fixtures stammen vom DWD Climate Data Center (CDC), lizenziert unter
CC BY 4.0 (siehe `doc/DWD/md/BESCHREIBUNG_obsgermany-climate-10min-air_temperature_de.md`,
Abschnitt „Copyright").
