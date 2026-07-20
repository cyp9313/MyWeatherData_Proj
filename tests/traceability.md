# Traceability-Matrix: Import-Client Vertical Slice

Abgleich von [tests/test_plan_import_client.md](./test_plan_import_client.md) gegen die tatsächlich
implementierten Tests (Stand: Phase 9, Qualitätsgate). Jede Zeile des Testplans ist hier mit einem
konkreten, grün laufenden Test hinterlegt.

## Domäne (Phase 4)

| # | FR-ID | Testfunktion | Datei |
|---|---|---|---|
| D1 | FR-005 | `test_zeitraum_vollstaendig_im_unterstuetzten_bereich_liefert_true` | `tests/unit/test_zeitraum.py` |
| D2 | FR-006 | `test_zeitraum_teilweise_ausserhalb_liefert_false`, `test_zeitraum_teilweise_ausserhalb_wird_auf_unterstuetzten_bereich_gekuerzt` | `tests/unit/test_zeitraum.py` |
| D3 | – (Robustheit) | `test_zeitraum_start_nach_ende_wirft_value_error` | `tests/unit/test_zeitraum.py` |

## Bausteine (Phase 5)

| # | FR-ID | Testfunktion | Datei |
|---|---|---|---|
| B1 | FR-001 | `test_distanz_zwischen_bekannten_koordinaten_entspricht_referenzwert` | `tests/unit/test_distanz.py` |
| B2 | FR-001 | `test_distanz_zwischen_identischer_koordinate_ist_null` | `tests/unit/test_distanz.py` |
| B3 | FR-007 | `test_gueltiger_rohdatensatz_besteht_validierung` | `tests/unit/test_datensatz_validator.py` |
| B4 | FR-007 | `test_rohdatensatz_mit_fehlwert_besteht_validierung_nicht` | `tests/unit/test_datensatz_validator.py` |
| B5 | FR-007 | `test_unvollstaendiger_rohdatensatz_besteht_validierung_nicht` | `tests/unit/test_datensatz_validator.py` |

## HTTP & Stationssuche (Phase 6)

| # | FR-ID | Testfunktion | Datei |
|---|---|---|---|
| H1 | – (Architektur) | `test_get_bytes_liefert_response_inhalt_bei_erfolg`, `test_get_bytes_wandelt_request_exception_in_http_client_error_um` | `tests/unit/test_http_client.py` |
| S1 | FR-001 | `test_eindeutig_naechstgelegene_station_wird_ermittelt` | `tests/unit/test_stationsfinder.py` |
| S2 | FR-004 | `test_distanz_gleichstand_waehlt_niedrigere_stations_id` | `tests/unit/test_stationsfinder.py` |
| S3 | FR-004 | `test_drei_stationen_mit_identischer_distanz_waehlt_niedrigste_id` | `tests/unit/test_stationsfinder.py` |
| S4 | – (Robustheit) | `test_leere_stationsliste_wirft_value_error` | `tests/unit/test_stationsfinder.py` |

## Lufttemperatur-Import (Phase 7)

| # | FR-ID | Testfunktion | Datei |
|---|---|---|---|
| L1 | FR-005 | `test_happy_path_liefert_gueltige_messwerte_ohne_hinweise` | `tests/unit/test_lufttemperatur_importer.py` |
| L2 | FR-006 | `test_zeitraum_teilweise_ausserhalb_wird_gekuerzt_und_hinweis_gesetzt` | `tests/unit/test_lufttemperatur_importer.py` |
| L3 | FR-007 | `test_fehlerhafte_datensaetze_werden_verworfen_gueltige_bleiben` | `tests/unit/test_lufttemperatur_importer.py` |
| L4 | FR-008 | `test_datenluecke_liefert_leeres_ergebnis_mit_hinweis` | `tests/unit/test_lufttemperatur_importer.py` |
| Z1 | FR-005 | `test_gueltiges_zip_fixture_wird_korrekt_eingelesen` | `tests/unit/test_dwd_zip_reader.py` |
| Z2 | – (Robustheit) | `test_zip_ohne_produkt_datei_wirft_dwd_zip_format_error` | `tests/unit/test_dwd_zip_reader.py` |

## Fassade & Integration (Phase 8)

| # | FR-ID | Testfunktion | Datei |
|---|---|---|---|
| K1 | FR-001, FR-005 | `test_ergebnis_station_entspricht_treffer_des_stationsfinder_unveraendert` | `tests/unit/test_import_koordinator.py` |
| K2 | FR-006 | `test_verwendeter_zeitraum_entspricht_dem_vom_importer_gekuerzten_zeitraum` | `tests/unit/test_import_koordinator.py` |
| E1 | FR-001, FR-004, FR-005, FR-006, FR-007, FR-008 | `test_import_lufttemperatur_end_to_end_liefert_vollstaendiges_ergebnis` | `tests/integration/test_import_lufttemperatur_end_to_end.py` |

## Requirement-Abdeckung (Zusammenfassung)

| FR-ID | Abgedeckt durch | Status |
|---|---|---|
| FR-001 | B1, B2, S1, S2, S3, K1, E1 | ✅ |
| FR-004 | S2, S3, E1 | ✅ |
| FR-005 | D1, L1, Z1, K1, E1 | ✅ |
| FR-006 | D2, L2, K2, E1 | ✅ |
| FR-007 | B3, B4, B5, L3, E1 | ✅ |
| FR-008 | L4, E1 | ✅ |
| FR-002 | – | Zurückgestellt (Folge-Slice) |
| FR-003 | – | Zurückgestellt (Folge-Slice) |

## Zurückgestellt

Siehe Abschnitt „Zurückgestellt" in [tests/test_plan_import_client.md](./test_plan_import_client.md):
FR-002 (Koordinate außerhalb Deutschlands) und FR-003 (Stationsliste nicht abrufbar) sind nicht Teil
dieses Vertical Slice und daher hier ohne Test.
