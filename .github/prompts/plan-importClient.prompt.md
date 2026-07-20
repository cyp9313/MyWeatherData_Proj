# Plan: Import-Client (Vertical Slice FR-001 + FR-004 + FR-005 + FR-006 + FR-007 + FR-008)

Ziel: Der Import-Client wird streng nach Hexagonal Architecture umgesetzt. Formaler Scope jetzt begrenzt auf FR-001 (Stationssuche), FR-004 (Tie-Break), FR-005 (Lufttemperatur-Import), FR-006 (Zeitraum-Kürzung), FR-007 (fehlerhafte Datensätze), FR-008 (Datenlücke). FR-002 (Landesgrenze) und FR-003 (Stationsliste nicht abrufbar) werden auf einen Folge-Slice verschoben. Erst wird eine echte Design-Lücke zwischen Komponenten- und Klassensicht geschlossen (inkl. Korrektur der Port-Eigentümerschaft), dann ein Python-Guidelines-Skill + vollständiges Scaffolding aufgesetzt, dann strikt TDD implementiert, abschließend eine separate Destructive-QA-Phase durchlaufen.

**Kernbefund (Architektur-Lücke):** Die Komponentensicht zeigt genau *einen* Eintrittspunkt von Core in den Import-Client, die Klassensicht aber zwei unverbundene Klassen (`StationsFinder`, `LufttemperaturImporter`) ohne Fassade. Lösung: Die bestehende `ImportSchnittstelle` ist ein **Core/Application-eigener Port** (nicht Import-Client-eigen), der künftig von einer neuen Klasse `LufttemperaturImportKoordinator` im Import-Client realisiert wird (Methode `importiere_lufttemperatur(koordinate, zeitraum) -> ImportErgebnis`). Dieser Koordinator orchestriert NUR den internen Ablauf `StationsFinder` → `LufttemperaturImporter` – NICHT den Core-weiten Ablauf (das bleibt Aufgabe des `DatenabrufKoordinator` in Core). `ImportErgebnis` wird zusätzlich um `station: StationsTreffer` (FR-001-Information: Stations-ID, Name, Distanz) sowie `verwendeter_zeitraum: Zeitraum` (der nach FR-006 ggf. gekürzte, tatsächlich verwendete Zeitraum) erweitert, damit beide Informationen strukturiert statt nur als Text-Hinweis beim Core ankommen.

## Steps

### Phase 0 – Python-Guidelines-Skill (Precondition)

1. `.github/skills/python-guidelines/SKILL.md` anlegen (Frontmatter/Stil wie bestehende Skills, z. B. `ar-klassen-sicht`), da noch kein projektweiter Python-Skill existiert. Inhalt: Hexagonal-Layering (domain/ports/adapters, Abhängigkeit nur nach innen), Typing (`mypy --strict`, Dataclasses, `Protocol` für Ports), Exception-Policy (keine `except Exception`, nur gezielte Exceptions), TDD-Workflow (rot→grün→refactor), Tooling (`pytest`, `ruff`, `mypy`), src-Layout-Konvention. Verbindliche Referenz ab Phase 3.

### Phase 1 – SW-Design-Abgleich (nur Dokumentation)

2. `arc/statische_sichten/klassensicht-import-client.puml` aktualisieren: `LufttemperaturImportKoordinator` ergänzen (mit Klarstellung: orchestriert nur den internen Import-Client-Ablauf, nicht Core); `ImportErgebnis` um `station: StationsTreffer` UND `verwendeter_zeitraum: Zeitraum` erweitern (zusätzlich zu `messwerte: list[Messwert]`, `hinweise: list[str]`) – Verifikation in diesem Schritt: FR-006 verlangt laut Text nur einen Hinweis auf die Kürzung, aber ohne strukturierte Rückgabe des tatsächlich verwendeten Zeitraums kann Core/UI die Kürzung nicht korrekt anzeigen (z. B. Achsenbeschriftung), daher wird das Feld ergänzt statt die Kürzung nur textuell zu kommunizieren; `IImport`-Interface NICHT hier neu implementieren, sondern als von Core besessenen Port referenzieren (siehe Schritt 3); `MessdatenImporter`+3 Subklassen weiterhin per Hinweistext als "Folgeausbau, nicht Phase 1" markieren (analog zum bestehenden CSV-Export-Hinweis in `arc/statische_sichten/README.md`); KEINE `KoordinateAusserhalbDeutschlandError`/`StationslisteNichtAbrufbarError` ergänzen (FR-002/003 deferred).
3. `arc/statische_sichten/klassensicht-core.puml`: `ImportSchnittstelle` (`IImport`) als Core-eigenes Port-Interface ergänzen (`importiere_lufttemperatur(koordinate, zeitraum): ImportErgebnis`), mit Hinweistext "wird von Import-Client (`LufttemperaturImportKoordinator`) realisiert" (Cross-Reference-Stil wie der bestehende Hinweis zu `Konfiguration`).
4. `arc/statische_sichten/klassensicht.md` Tabellen/Fließtext für Core und Import-Client entsprechend Schritt 2+3 anpassen. *(parallel zu 2/3)*
5. `arc/statische_sichten/komponentensicht-ebene2-import-client.puml`: Label „Core → Stationssuche" um Zeitraum ergänzen (Konsistenz). *(parallel)*
6. Neuer Ordner `arc/dynamische_sichten/`: `sequenzsicht.md` + `sequenzsicht-import-lufttemperatur.puml`, MIT `alt/else`-Zweigen für FR-004 (Tie-Break), FR-006 (Zeitraum-Kürzung), FR-007 (fehlerhafte Datensätze verwerfen), FR-008 (Datenlücke/leeres Ergebnis) zusätzlich zum Happy Path (kein Happy-Path-only mehr); kein Zweig für FR-002/003 (deferred); im Stil der bestehenden statischen Sichten.

### Phase 2 – Testplan-Dokument (depends on Phase 1)

7. `tests/test_plan_import_client.md` anlegen: tabellarische Testfall-Übersicht (Szenario, FR-ID, erwartetes Ergebnis) für Happy Path FR-001/FR-005 sowie Randfälle FR-004/FR-006/FR-007/FR-008; eigener Abschnitt "Zurückgestellt" mit FR-002/FR-003 + Verweis auf Folge-Slice. Dient als Checkliste, gegen die die TDD-Tests (Phase 4-8) und die spätere Traceability (Phase 9) abgeglichen werden.

### Phase 3 – Python-Scaffolding (depends on Phase 0+2)

8. Vollständige Paketstruktur anlegen, bevor die Implementierung beginnt: `pyproject.toml` (src-Layout `src/myweatherdata/`, Python ≥3.11, Deps: `requests` (fix); `pandas` NUR bedingt (siehe Decisions – Default ist die Standardbibliothek, `pandas` erst nach dem DWD-Format-Spike bei klarem Mehrwert aufnehmen); Dev-Deps: `pytest`, `pytest-cov`, `mypy`, `types-requests`, `ruff` (`pandas-stubs` nur falls `pandas` tatsächlich aufgenommen wird), `src/myweatherdata/__init__.py`, `src/myweatherdata/domain/__init__.py`, `src/myweatherdata/ports/__init__.py`, `src/myweatherdata/import_client/__init__.py`, `tests/__init__.py`, `tests/unit/__init__.py`, `tests/integration/__init__.py`, `tests/conftest.py` (Platzhalter), `tests/fixtures/dwd/` (Ordner mit Platzhalter-README für die beiden Fixture-Dateien).

### Phase 4 – Domäne & Ports (TDD, keine DWD-Abhängigkeit, depends on Phase 3)

9. Dedizierte Domänenmodule statt einem gemeinsamen Modul: `src/myweatherdata/domain/koordinate.py` (`Koordinate`), `domain/zeitraum.py` (`Zeitraum`), `domain/stationstreffer.py` (`StationsTreffer`), `domain/messwert.py` (`Messgroesse`-Enum vorerst nur `LUFTTEMPERATUR`, `Messwert`-Dataclass), `domain/import_ergebnis.py` (`ImportErgebnis` mit `station`, `messwerte`, `hinweise`, `verwendeter_zeitraum`). `src/myweatherdata/ports/import_schnittstelle_port.py`: NUR das Protocol `ImportSchnittstelle` (importiert Domänentypen, definiert keine eigenen); Docstring dokumentiert es als Core/Application-Port, den der Import-Client implementiert. `src/myweatherdata/ports/http_client_port.py`: Protocol `HttpClient` + technologieneutrale Exception `HttpClientError` (kein Leck `requests`-spezifischer Typen über die Port-Grenze).
10. Test zuerst: `tests/unit/test_zeitraum.py` (rot) → `Zeitraum` implementieren (grün).

### Phase 5 – Bausteine (parallel möglich, je eigene Datei, depends on Phase 4)

11. `tests/unit/test_distanz.py` → `import_client/distanz.py` (Haversine).
12. `tests/unit/test_datensatz_validator.py` → `import_client/datensatz_validator.py`.

(Landesgrenze/Bounding-Box-Baustein entfällt in diesem Slice – FR-002 deferred.)

### Phase 6 – HTTP & Stationssuche (depends on Phase 4+5)

13. `import_client/http_client.py` (`RequestsHttpClient`, fängt gezielt `requests.RequestException`, kein `except Exception`; wandelt sie in die technologieneutrale `HttpClientError` (aus `ports/http_client_port.py`) um – `requests.RequestException` verlässt den Adapter nie als Cross-Layer-Kontrakt; kein eigener `StationslisteNichtAbrufbarError`-Typ, da FR-003 deferred – `HttpClientError` propagiert unverändert, TODO-Docstring-Verweis auf Folge-Slice).
14. `tests/conftest.py`: `FakeHttpClient` (Protocol-Implementierung, url→bytes|Exception).
15. `tests/unit/test_stationsfinder.py` → `import_client/dwd_stationsliste_parser.py` (bevorzugt mit Standardbibliothek `csv`; `pandas` nur falls der DWD-Format-Spike einen klaren Mehrwert zeigt, siehe Decisions) + `import_client/stationsfinder.py` (FR-001, FR-004 Tie-Break: numerischer Vergleich der Stations-ID bei Gleichstand, Ausgabe behält die ursprüngliche, führende-Nullen-String-Repräsentation bei, z. B. `"00003"` bleibt `"00003"` statt `"3"` – Regel selbst vorbehaltlich PO-Bestätigung, siehe Weitere Confirmation-Punkte).

### Phase 7 – Lufttemperatur-Import (depends on Phase 6)

16. `tests/unit/test_dwd_zip_reader.py` → `import_client/dwd_zip_reader.py` (bevorzugt `zipfile`+`csv` aus der Standardbibliothek; `pandas` nur bei klarem Mehrwert laut Spike).
17. `tests/unit/test_lufttemperatur_importer.py` (Happy Path, FR-006 Kürzung inkl. Rückgabe des tatsächlich verwendeten Zeitraums, FR-007 fehlerhafte Zeilen, FR-008 Datenlücke) → `import_client/lufttemperatur_importer.py`.

### Phase 8 – Fassade & Integration (depends on Phase 7)

18. `tests/unit/test_import_koordinator.py` → `import_client/import_koordinator.py` (`LufttemperaturImportKoordinator`, realisiert `ImportSchnittstelle`; Test prüft explizit, dass `ImportErgebnis.station` die von `StationsFinder` ermittelte `StationsTreffer` unverändert enthält, sowie dass `ImportErgebnis.verwendeter_zeitraum` bei einer FR-006-Kürzung den tatsächlich importierten, gekürzten Zeitraum widerspiegelt).
19. `tests/integration/test_import_lufttemperatur_end_to_end.py` mit echten Fixture-Bytes, kein Netzwerkzugriff.

### Phase 9 – Qualitätssicherung & Abschluss (depends on Phase 8)

20. `pytest -v`, `mypy --strict src`, `ruff check`/`ruff format --check`, grep-Check gegen `except Exception`.
21. `tests/traceability.md`: FR-001/004/005/006/007/008 → Testfälle, abgeglichen gegen `tests/test_plan_import_client.md` (Schritt 7); FR-002/003 als "zurückgestellt" referenziert.

### Phase 10 – Destructive QA (depends on Phase 9, eigenständiges Abschlussgate)

22. Ein Reviewer sucht AKTIV nach Fehlerfällen und Architekturverstößen, u. a.: verdeckte `except Exception`, `requests`-spezifische Exceptions, die über die `HttpClient`-Port-Grenze lecken, Domänenmodule mit Abhängigkeit auf Adapter-Code (Richtungsverstoß), leere Stationsliste, `Zeitraum.start > ende`, Distanz-Gleichstände bei mehr als 2 Stationen, Koordinate-Wertebereichsverletzungen (z. B. Breitengrad/Längengrad außerhalb ±90°/±180°), ungültiges Encoding im ZIP, doppelte Zeitstempel. NICHT Teil dieser Destructive QA: Prüfung „Koordinate exakt auf 0,0/Grenzregion Deutschlands" – das ist Landesgrenzprüfung und gehört zum zurückgestellten FR-002. Für jeden gefundenen Defekt wird ZUERST ein fehlschlagender Test ergänzt, erst danach der Fix umgesetzt (rot→grün, wie in Phase 4-8). Ergebnisse werden in `tests/destructive-qa-log.md` festgehalten.

## Relevante Fixtures

- `tests/fixtures/dwd/stationsliste_beispiel.txt` — kleine Stationsliste inkl. Tie-Break-Paar (FR-004)
- `tests/fixtures/dwd/10minutenwerte_TU_00003_beispiel_hist.zip` — gültige, fehlerhafte, `-999`-Fehlwert-Zeilen + Datenlücke-Zeitraum

## Verification

1. Jeder TDD-Schritt: Test schreiben → `pytest <test>` rot bestätigen → Minimalcode → grün bestätigen.
2. Gesamte Suite: `pytest -v`, `mypy --strict src`, `ruff check`, `ruff format --check`.
3. Manuell: PlantUML-Diagramme rendern (VS Code Preview) und Selbstcheck-Liste aus `arc/statische_sichten/klassensicht.md` durchgehen.
4. `tests/test_plan_import_client.md` (Phase 2) gegen `tests/traceability.md` (Phase 9) manuell abgleichen — keine offene Zeile ohne Test.
5. `tests/destructive-qa-log.md` (Phase 10) von zweiter Person reviewen lassen.

## Decisions

- Formaler Scope: FR-001, FR-004, FR-005, FR-006, FR-007, FR-008. FR-002 (Landesgrenze) und FR-003 (Stationsliste nicht abrufbar) werden auf einen Folge-Slice verschoben; `pjm/vertical-slice-prototyp.md` bleibt UNVERÄNDERT (Exclusion-Liste nennt namentlich ohnehin nur FR-002/003).
- Empfehlung für den Folge-Slice: FR-002 mit echtem Grenzpolygon (keine Bounding-Box) und als normaler Rückgabewert (kein Exception) umsetzen; FR-003 als typisierte technische Exception (in dieser Session bestätigt).
- `ImportSchnittstelle` ist konzeptionell ein Core/Application-Port; da in diesem Slice kein eigenes Core-Package gebaut wird (YAGNI, analog zur MessdatenImporter-Entscheidung), bleibt das Protocol-Modul unter `src/myweatherdata/ports/`, mit Docstring-Vermerk zur Core-Eigentümerschaft.
- `Koordinate`/`Zeitraum`/`StationsTreffer`/`Messwert`/`Messgroesse`/`ImportErgebnis` je eigenes Modul unter `domain/`; das Port-Modul enthält nur Protocol-Definitionen.
- `ImportErgebnis` führt zusätzlich die Felder `station: StationsTreffer` und `verwendeter_zeitraum: Zeitraum` (strukturierte Rückgabe der FR-006-Kürzung statt reinem Text-Hinweis; in Phase 1 verifiziert).
- `LufttemperaturImportKoordinator` orchestriert nur den internen Import-Client-Ablauf, nicht den Core-weiten Ablauf.
- `requests.RequestException` wird im `RequestsHttpClient`-Adapter in die technologieneutrale `HttpClientError` (Port-Ebene) umgewandelt; kein technologiespezifischer Typ überquert die Port-Grenze. FR-003-User-Facing-Behandlung bleibt deferred.
- FR-004-Tie-Break vergleicht Stations-IDs numerisch, gibt aber die ursprüngliche, führende-Nullen-String-Repräsentation unverändert zurück (kein `int()`-Downcast).
- `pandas` ist eine BEDINGTE Abhängigkeit: Default ist die Python-Standardbibliothek (`csv`, `zipfile`, `datetime`); `pandas` wird nur aufgenommen, wenn der DWD-Format-Spike (vor Phase 6/7) einen klaren Implementierungsvorteil zeigt.
- Sequenzdiagramm jetzt mit `alt/else` für FR-004/006/007/008 (kein Happy-Path-only mehr).
- Python-Guidelines-Skill wird VOR dem Scaffolding angelegt (Phase 0).
- Neue Phase 10 "Destructive QA" als Abschlussgate; Defekte werden immer zuerst per fehlschlagendem Test reproduziert, bevor sie behoben werden.
- Ausgeschlossen (unverändert): Streamlit, SQLite, Plotly, CSV-Export, Niederschlag/Wind/Sonne, Core-Orchestrierung, FR-002, FR-003.

## Weitere Confirmation-Punkte (andere Verantwortliche)

1. FR-004-Tie-Break-Regel „aufsteigend nach Stations-ID" ist laut FR-004 selbst noch nicht PO-bestätigt (technisch bereits geklärt: numerischer Vergleich, Ausgabe behält führende Nullen bei).
2. Landesgrenze Deutschland (Bounding-Box vs. Polygon) — für den Folge-Slice mit PO klären; Empfehlung dieser Session ist ein echtes Grenzpolygon.
3. Ablageort von `Messgroesse`/`Messwert` als geteilter Domänentyp über Import-Client/Datenhaltung/Core hinweg — mit Core-/Datenhaltung-Verantwortlichem abstimmen (Datenhaltung-Klassensicht definiert `Messgroesse` aktuell eigenständig in `klassensicht-datenhaltung.puml`), damit Import-Client nicht von einem Datenhaltung-Paket abhängt.
4. Exaktes Spalten-/Dateiformat der DWD-`help`-Stationsliste sowie exakter ZIP-Produktcode/Namensschema — technischer Spike anhand einer echten DWD-Beispieldatei vor Phase 6/7. Ergebnis des Spikes entscheidet zugleich, ob `pandas` als Abhängigkeit aufgenommen wird (Default: Standardbibliothek, siehe Decisions).
5. Priorisierung/Timing des Folge-Slice für FR-002/003 — PO-Entscheidung ausstehend.
