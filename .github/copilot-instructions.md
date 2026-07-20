# MyWeatherData – Hinweise für AI Coding Agents

Projektbeschreibung: siehe [README.md](../README.md). Lokale Wetter-App zur Visualisierung historischer DWD-Wetterdaten (Lufttemperatur, Niederschlag, Wind, Sonneneinstrahlung).

## Projektphase

Dieses Repository befindet sich aktuell in der **Requirements- und Architekturphase**. Es existiert noch kein Anwendungscode (kein `src/`-Verzeichnis) – Änderungen betreffen primär Markdown-Dokumente unter `req/`, `arc/` und `doc/`. Vor dem Anlegen von Code prüfen, ob eine passende Anforderung/Architektursicht bereits existiert bzw. angelegt werden muss.

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

Statische Sichten (Kontext-, Komponenten-, Klassensicht) werden als PlantUML-Diagramme unter `arc/statische_sichten/` abgelegt (aktuell noch leer). Für deren Erstellung/Review die Skills `ar-kontext-sicht`, `ar-komponenten-sicht` bzw. `ar-klassen-sicht` verwenden, oder den Agent `ar-architecture-designer-static-views`.

## Tech-Stack

Siehe [doc/techstack/techstack-uebersicht.md](../doc/techstack/techstack-uebersicht.md) (Herleitung: [bewertung-techstack.md](../doc/techstack/bewertung-techstack.md)): Python, eigener HTTP-Client (`requests`/`httpx` + `pandas`) für den DWD-Import, SQLite für die lokale Datenhaltung, Streamlit als UI, Plotly für die Visualisierung. DWD-Rohdatenformate sind unter [doc/DWD/md](../doc/DWD/md) dokumentiert.

## Vorhandene Agents & Skills für Requirements-/Architekturarbeit

- Agent `rq-story-crafter`: leitet User Stories aus Epics ab, prüft INVEST, formuliert BDD-Akzeptanzkriterien.
- Agent `rq-requirement-engineer`: übersetzt User Stories in EARS-konforme Functional Requirements unter Berücksichtigung des Tech-Stacks.
- Agent `ar-architecture-designer-static-views`: erstellt/reviewt Kontext-, Komponenten- und Klassensicht als PlantUML.

Diese Agents/Skills bevorzugt für die jeweilige Aufgabe nutzen, statt Anforderungs- oder Architekturdokumente manuell "from scratch" zu formulieren.

## Konventionen

- Alle Dokumente (Epics, User Stories, FRs, Architektur) werden auf **Deutsch** verfasst.
- Status-Werte: `Draft` · `Review` · `Approved` · `In Arbeit` · `Done` · `Verworfen`.
- Priorisierung nach MoSCoW: `Must have` · `Should have` · `Could have` · `Won't have`.
- IDs sind projektweit eindeutig und werden nach Löschung nicht wiederverwendet.
