# DWD-Test-Fixtures

Platzhalter für die im [Testplan](../../test_plan_import_client.md) referenzierten Beispieldateien:

- `stationsliste_beispiel.txt` — kleine Stationsliste inkl. Tie-Break-Paar (FR-004). Wird in Phase 6 (Stationssuche) anhand des DWD-Format-Spikes (siehe `arc/statische_sichten/klassensicht.md`, Weitere Confirmation-Punkte) erstellt.
- `10minutenwerte_TU_00003_beispiel_hist.zip` — gültige, fehlerhafte und `-999`-Fehlwert-Zeilen sowie eine Datenlücke-Zeitraum. Wird in Phase 7 (Lufttemperatur-Import) erstellt.

Beide Dateien werden erst angelegt, sobald der DWD-Format-Spike das exakte Spalten-/Dateiformat sowie den ZIP-Produktcode bestätigt hat.
