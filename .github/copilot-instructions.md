# MyWeatherData – Hinweise für AI Coding Agents

Projektbeschreibung: siehe [README.md](../README.md). Lokale Wetter-App zur Visualisierung historischer DWD-Wetterdaten (Lufttemperatur, Niederschlag, Wind, Sonneneinstrahlung).

## Projektphase

Requirements und statische Architektursichten (Kontext-, Komponenten-, Klassensicht) sind für die Kernbereiche angelegt. Die Implementierung hat begonnen: Für den **Import-Client** (Vertical Slice FR-001/004/005/006/007/008) existiert produktiver Code unter `src/myweatherdata/` (Hexagonal Architecture: `domain/`, `ports/`, `import_client/`) sowie eine grüne Testsuite unter `tests/unit/` und `tests/integration/`. Der Import-Client befindet sich aktuell in Implementierung/Review (siehe `pjm/import-client-implementation-plan.md`, autoritative Plan-Baseline, inkl. Real-DWD-Kontraktverifikation). Core, Datenhaltung, UI und Visualisierung sind weiterhin nur als Requirements/Architektursichten vorhanden, ohne Anwendungscode. Vor dem Anlegen von Code prüfen, ob eine passende Anforderung/Architektursicht bereits existiert bzw. angelegt werden muss.

## Anforderungen: Struktur & Fundstellen

Hierarchie: `Epic (EPIC-xxx)` → `User Story (US-xxx)` → `Functional Requirement (FR-xxx)`, jede Ebene verlinkt ihre übergeordnete Ebene per ID.

| Ebene | Verzeichnis | Übersicht |
|---|---|---|
| Epics | [req/epic/](../req/epic/) | – |
| User Stories | [req/user-story/](../req/user-story/) | BDD-Akzeptanzkriterien (Gegeben/Wenn/Dann), INVEST-geprüft |
| Functional Requirements | [req/functional-requirement/](../req/functional-requirement/) | EARS-Syntax |
| Gesamtübersicht | [req/README.md](../req/README.md) | ID-Konventionen, Status-Werte, MoSCoW-Priorisierung |
| Traceability | [req/traceability-matrix.md](../req/traceability-matrix.md) | Vollständige Zuordnung Epic → User Story → FR |

Neue Anforderungen immer aus dem passenden `TEMPLATE-*.md` im jeweiligen Ordner ableiten, Namenskonvention `<ID>-<sprechender-titel>.md` einhalten und die Parent-ID (Epic bzw. User Story) verlinken. Details siehe [req/README.md](../req/README.md).

## Architektur

Statische Sichten (Kontext-, Komponenten-, Klassensicht) werden als PlantUML-Diagramme unter `arc/statische_sichten/` abgelegt; dynamische Sichten (Sequenzdiagramme) unter `arc/dynamische_sichten/`. Für deren Erstellung/Review die Skills `ar-kontext-sicht`, `ar-komponenten-sicht` bzw. `ar-klassen-sicht` verwenden, oder den Agent `ar-architecture-designer-static-views`.

## Tech-Stack

Siehe [doc/techstack/techstack-uebersicht.md](../doc/techstack/techstack-uebersicht.md) (Herleitung: [bewertung-techstack.md](../doc/techstack/bewertung-techstack.md)): Python, eigener HTTP-Client (`requests`/`httpx` + `pandas`) für den DWD-Import, SQLite für die lokale Datenhaltung, Streamlit als UI, Plotly für die Visualisierung. DWD-Rohdatenformate sind unter [doc/DWD/md](../doc/DWD/md) dokumentiert.

## Vorhandene Agents & Skills für Requirements-/Architektur-/Implementierungsarbeit

- Agent `rq-story-crafter`: leitet User Stories aus Epics ab, prüft INVEST, formuliert BDD-Akzeptanzkriterien.
- Agent `rq-requirement-engineer`: übersetzt User Stories in EARS-konforme Functional Requirements unter Berücksichtigung des Tech-Stacks.
- Agent `ar-architecture-designer-static-views`: erstellt/reviewt Kontext-, Komponenten- und Klassensicht als PlantUML.
- Agent `sw-import-client-developer`: implementiert den Import-Client strikt nach `pjm/import-client-implementation-plan.md`, Hexagonal Architecture und TDD.
- Agent `sw-destructive-reviewer`: unabhängige Destructive QA des Import-Clients (schreibt/ändert nur Tests und `tests/destructive-qa-log.md`, niemals Produktionscode).

Diese Agents/Skills bevorzugt für die jeweilige Aufgabe nutzen, statt Anforderungs- oder Architekturdokumente manuell "from scratch" zu formulieren.

## Konventionen

- Alle Dokumente (Epics, User Stories, FRs, Architektur) werden auf **Deutsch** verfasst.
- Status-Werte: `Draft` · `Review` · `Approved` · `In Arbeit` · `Done` · `Verworfen`.
- Priorisierung nach MoSCoW: `Must have` · `Should have` · `Could have` · `Won't have`.
- IDs sind projektweit eindeutig und werden nach Löschung nicht wiederverwendet.
