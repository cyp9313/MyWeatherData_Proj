---
name: python-guidelines
description: 'Projektweite Python-Konventionen für MyWeatherData (Hexagonal Architecture, Typing, Exception-Handling, TDD-Workflow, Tooling, src-Layout). Use when: Python-Code unter src/ oder tests/ neu angelegt, strukturiert oder reviewt werden soll, oder wenn Fragen zu Paketstruktur, Ports/Adapter-Trennung, Typisierung, Fehlerbehandlung oder Testvorgehen in Python-Code auftreten.'
---

# Python-Guidelines (MyWeatherData)

## Zweck

Dieser Skill bündelt die verbindlichen Konventionen für den Python-Code von MyWeatherData (Import-Client, künftig Core/Datenhaltung/UI/Visualisierung). Er ist Referenz für jede Implementierungsarbeit unter `src/` und `tests/` und wird sowohl beim **Anlegen** neuen Codes als auch beim **Review** bestehenden Codes herangezogen.

Tech-Stack-Grundlage: [doc/techstack/techstack-uebersicht.md](../../../doc/techstack/techstack-uebersicht.md) (Python, `requests`/`pandas`, SQLite, Streamlit, Plotly).

## src-Layout

- Produktivcode ausschließlich unter `src/myweatherdata/<paket>/...` (src-Layout, kein Code direkt unter dem Repo-Root).
- Tests ausschließlich unter `tests/unit/` (isolierte Komponententests, keine externen Abhängigkeiten wie Netzwerk/Dateisystem außer Fixtures) und `tests/integration/` (Zusammenspiel mehrerer Bausteine, weiterhin ohne echten Netzwerkzugriff – Fixture-Bytes statt Live-Requests).
- Test-Fixtures unter `tests/fixtures/<quelle>/` (z. B. `tests/fixtures/dwd/`).
- Python-Version: `>= 3.11`.

## Hexagonal Architecture (Layering)

Jede Komponente wird nach Domäne/Port/Adapter getrennt:

- **`domain/`** – reine Fachlogik/Wertobjekte (Dataclasses, Enums, Berechnungen). Keine Abhängigkeit auf `ports/` oder Adapter-Pakete (z. B. `import_client/`), keine I/O (kein Netzwerk, keine Dateisystemzugriffe).
- **`ports/`** – ausschließlich `Protocol`-Definitionen (Schnittstellen) und die dazugehörigen technologieneutralen Exceptions. Ports gehören konzeptionell der aufrufenden Seite (z. B. Core/Application), auch wenn aus Scope-Gründen (YAGNI) noch kein eigenes Package für diese Seite existiert – das Protocol-Modul dokumentiert diese Eigentümerschaft dann per Docstring. Ports importieren nur `domain/`-Typen, nie Adapter-Code.
- **Adapter-Pakete** (z. B. `import_client/`) – konkrete Implementierungen, die Ports realisieren (`class X(Protocol-Implementierung)`), dürfen `domain/` und `ports/` importieren, aber niemals umgekehrt.

**Abhängigkeitsrichtung:** Adapter → Ports → Domain. Nie andersherum. Ein Import von `domain/` nach `import_client/` (oder einem anderen Adapter-Paket) ist ein Architekturverstoß.

Technologiespezifische Exceptions (z. B. `requests.RequestException`) dürfen die Adapter-Grenze nicht als Cross-Layer-Kontrakt verlassen: Sie werden im Adapter gezielt abgefangen und in eine technologieneutrale, im zugehörigen `ports/*_port.py`-Modul definierte Exception (z. B. `HttpClientError`) umgewandelt.

## Typing

- `mypy --strict` muss für `src/` fehlerfrei durchlaufen.
- Fachliche Wertobjekte als `@dataclass` (bevorzugt `frozen=True`, wo Unveränderlichkeit sinnvoll ist).
- Schnittstellen als `typing.Protocol`, nicht als abstrakte Basisklassen, sofern kein gemeinsamer Implementierungscode nötig ist.
- Rückgabetypen und Parameter immer vollständig annotiert, auch bei privaten Hilfsfunktionen.
- Dev-Dependency `pandas-stubs` nur aufnehmen, wenn `pandas` tatsächlich als Abhängigkeit verwendet wird (siehe Tooling/Abhängigkeiten).

## Exception-Policy

- **Kein** `except Exception` (und kein nacktes `except:`). Immer die konkrete(n) erwartete(n) Exception-Klasse(n) fangen.
- Fachliche Fehlerfälle, für die ein Functional Requirement eine normale Rückgabe vorsieht (z. B. leeres Ergebnis + Hinweistext), werden **nicht** als Exception modelliert, sondern als regulärer Rückgabewert.
- Fachliche Fehlerfälle, für die ein Functional Requirement einen Fehler/Abbruch vorsieht, werden als **typisierte** Exception modelliert (eigene Klasse, kein generischer `Exception`/`ValueError`-Wildwuchs).
- Technologiespezifische Exceptions von Drittbibliotheken (`requests`, `zipfile`, …) werden an der Adapter-Grenze in technologieneutrale, projekteigene Exceptions übersetzt (siehe Hexagonal Architecture oben).
- Ein `grep`-Check gegen `except Exception` ist fester Bestandteil der Qualitätssicherung vor Abschluss einer Implementierung.

## TDD-Workflow

1. Test zuerst schreiben (unit- oder integrationstestbasiert je nach Baustein).
2. Test ausführen und **rot** bestätigen (Test schlägt erwartungsgemäß fehl, bevor Produktivcode existiert).
3. Minimalen Produktivcode ergänzen, der den Test grün macht.
4. Test erneut ausführen und **grün** bestätigen.
5. Bei Bedarf refactoren, dabei Tests durchgehend grün halten.

Für neue Bausteine wird kein Code geschrieben, bevor nicht der zugehörige Test existiert und rot bestätigt wurde.

## Tooling

| Zweck | Kommando |
|---|---|
| Tests ausführen | `pytest -v` |
| Testabdeckung | `pytest --cov` |
| Statische Typprüfung | `mypy --strict src` |
| Linting | `ruff check` |
| Formatierungsprüfung | `ruff format --check` |

Alle vier Kommandos (`pytest`, `mypy --strict`, `ruff check`, `ruff format --check`) müssen vor Abschluss einer Implementierungsphase fehlerfrei durchlaufen.

## Abhängigkeiten (Dependency-Policy)

- Neue Produktiv- oder Dev-Abhängigkeiten werden nur aufgenommen, wenn ein klarer Mehrwert gegenüber der Python-Standardbibliothek besteht (z. B. `pandas` erst nach technischem Spike, siehe jeweiliger Implementierungsplan).
- Default für Datei-/CSV-/ZIP-Verarbeitung ist die Standardbibliothek (`csv`, `zipfile`, `datetime`).
