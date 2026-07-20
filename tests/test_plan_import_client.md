# Testplan: Import-Client Vertical Slice (FR-001, FR-004, FR-005, FR-006, FR-007, FR-008)

Dieser Testplan ist die Checkliste für die TDD-Implementierung (Phasen 4–8) und wird nach Abschluss gegen [tests/traceability.md](./traceability.md) abgeglichen (keine Zeile ohne zugehörigen Test). Testfälle für FR-002/FR-003 sind bewusst nicht enthalten (siehe Abschnitt „Zurückgestellt").

## Domäne (Phase 4)

| # | Szenario | FR-ID | Erwartetes Ergebnis | Testdatei |
|---|---|---|---|---|
| D1 | `Zeitraum` vollständig innerhalb 01.01.2015–31.12.2025 | FR-005 | `liegt_vollstaendig_im_unterstuetzten_bereich() == True` | `tests/unit/test_zeitraum.py` |
| D2 | `Zeitraum` teilweise außerhalb des unterstützten Bereichs | FR-006 | `liegt_vollstaendig_im_unterstuetzten_bereich() == False`; `gekuerzt_auf_unterstuetzten_bereich()` liefert auf 01.01.2015–31.12.2025 begrenzten Zeitraum | `tests/unit/test_zeitraum.py` |
| D3 | `Zeitraum.start > Zeitraum.ende` (Edge Case) | – (Robustheit, kein FR) | Definiertes Verhalten (Validierung bei Konstruktion oder dokumentierte Annahme) | `tests/unit/test_zeitraum.py` |

## Bausteine (Phase 5)

| # | Szenario | FR-ID | Erwartetes Ergebnis | Testdatei |
|---|---|---|---|---|
| B1 | Distanzberechnung zwischen zwei bekannten Koordinaten (Haversine) | FR-001 | Ergebnis entspricht bekanntem Referenzwert (Toleranz) | `tests/unit/test_distanz.py` |
| B2 | Distanz zwischen identischer Koordinate | FR-001 (Edge Case) | Distanz = 0 | `tests/unit/test_distanz.py` |
| B3 | Gültiger Rohdatensatz besteht Validierung | FR-007 | `validiere(...) == True` | `tests/unit/test_datensatz_validator.py` |
| B4 | Rohdatensatz mit Fehlwert (`-999`) besteht Validierung nicht | FR-007 | `validiere(...) == False` | `tests/unit/test_datensatz_validator.py` |
| B5 | Unvollständiger Rohdatensatz (fehlende Spalte) besteht Validierung nicht | FR-007 | `validiere(...) == False` | `tests/unit/test_datensatz_validator.py` |

## HTTP & Stationssuche (Phase 6)

| # | Szenario | FR-ID | Erwartetes Ergebnis | Testdatei |
|---|---|---|---|---|
| H1 | `RequestsHttpClient` fängt `requests.RequestException` und wirft `HttpClientError` | – (Architektur, Port-Grenze) | `HttpClientError` statt `requests`-spezifischer Exception | `tests/unit/test_http_client.py` |
| S1 | Eindeutig nächstgelegene Station für Koordinate innerhalb Deutschlands | FR-001 | Korrekter `StationsTreffer` (Stations-ID, Name, Distanz) | `tests/unit/test_stationsfinder.py` |
| S2 | Zwei Stationen mit identischer Minimaldistanz | FR-004 | Station mit numerisch niedrigerer Stations-ID gewählt; Ausgabe behält führende Nullen bei (z. B. `"00003"`) | `tests/unit/test_stationsfinder.py` |
| S3 | Drei oder mehr Stationen mit identischer Minimaldistanz (Edge Case) | FR-004 | Weiterhin genau eine Station, niedrigste Stations-ID | `tests/unit/test_stationsfinder.py` |
| S4 | Leere Stationsliste (Edge Case) | – (Robustheit, kein FR) | Definiertes Verhalten (dokumentierte Annahme, kein Absturz) | `tests/unit/test_stationsfinder.py` |

## Lufttemperatur-Import (Phase 7)

| # | Szenario | FR-ID | Erwartetes Ergebnis | Testdatei |
|---|---|---|---|---|
| L1 | Import für vollständig unterstützten Zeitraum, ausschließlich gültige Datensätze | FR-005 | Messwerte entsprechen Fixture-Daten, `verwendeter_zeitraum` == angefragter Zeitraum, `hinweise == []` | `tests/unit/test_lufttemperatur_importer.py` |
| L2 | Import für Zeitraum, der teilweise außerhalb 01.01.2015–31.12.2025 liegt | FR-006 | Nur Daten im unterstützten Bereich importiert; `verwendeter_zeitraum` == gekürzter Zeitraum; Hinweis auf Kürzung in `hinweise` | `tests/unit/test_lufttemperatur_importer.py` |
| L3 | ZIP enthält fehlerhafte/unvollständige Zeilen neben gültigen | FR-007 | Fehlerhafte Zeilen fehlen im Ergebnis, gültige sind enthalten | `tests/unit/test_lufttemperatur_importer.py` |
| L4 | Angefragter Zeitraum liegt innerhalb einer bekannten Datenlücke der Station | FR-008 | `messwerte == []`, Hinweis auf Datenlücke in `hinweise` | `tests/unit/test_lufttemperatur_importer.py` |
| Z1 | `dwd_zip_reader` liest gültiges ZIP-Fixture korrekt ein | FR-005 | Rohdatensätze entsprechen Fixture-Inhalt | `tests/unit/test_dwd_zip_reader.py` |
| Z2 | `dwd_zip_reader` bei defektem/unerwartetem ZIP-Inhalt (Edge Case) | – (Robustheit, kein FR) | Definiertes Verhalten (dokumentierte Annahme, kein Absturz) | `tests/unit/test_dwd_zip_reader.py` |

## Fassade & Integration (Phase 8)

| # | Szenario | FR-ID | Erwartetes Ergebnis | Testdatei |
|---|---|---|---|---|
| K1 | `LufttemperaturImportKoordinator.importiere_lufttemperatur(...)` Happy Path | FR-001, FR-005 | `ImportErgebnis.station` == von `StationsFinder` ermittelte `StationsTreffer` (unverändert übernommen) | `tests/unit/test_import_koordinator.py` |
| K2 | Koordinator bei FR-006-Kürzung | FR-006 | `ImportErgebnis.verwendeter_zeitraum` == tatsächlich importierter, gekürzter Zeitraum | `tests/unit/test_import_koordinator.py` |
| E1 | End-to-End: Koordinate → Station → Messwerte, echte Fixture-Bytes, kein Netzwerkzugriff | FR-001, FR-004, FR-005, FR-006, FR-007, FR-008 | Vollständiges, korrektes `ImportErgebnis` über die gesamte Kette | `tests/integration/test_import_lufttemperatur_end_to_end.py` |

## Zurückgestellt (Folge-Slice, nicht Teil dieses Testplans)

| FR-ID | Grund |
|---|---|
| FR-002 | Koordinate außerhalb Deutschlands – Landesgrenzprüfung deferred, siehe [pjm/vertical-slice-prototyp.md](../pjm/vertical-slice-prototyp.md) und `arc/statische_sichten/klassensicht.md` |
| FR-003 | DWD-Stationsliste nicht abrufbar – FR-003-spezifische typisierte Exception deferred, siehe `arc/statische_sichten/klassensicht.md` |
