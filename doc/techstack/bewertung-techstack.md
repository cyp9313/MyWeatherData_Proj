# Bewertung Tech-Stack – MyWeatherData

## Kontext
Grundlage dieser Bewertung ist das Brainstorming zum Tech-Stack für die Umsetzung der Epics [EPIC-001](../../req/epic/EPIC-001-datenimport-export-dwd.md) (Datenimport/-export DWD), [EPIC-002](../../req/epic/EPIC-002-lokale-datenhaltung.md) (lokale Datenhaltung), [EPIC-003](../../req/epic/EPIC-003-ui-konfiguration.md) (UI-Konfiguration) und [EPIC-004](../../req/epic/EPIC-004-visualisierung.md) (Visualisierung).

Für jeden Baustein des Stacks wurden drei Alternativen anhand einheitlicher Kriterien bewertet. Skala je Kriterium: 1 (schlecht) bis 5 (sehr gut).

## Bewertungskriterien
| Kriterium | Beschreibung |
|---|---|
| Lernkurve | Wie schnell ist die Technologie für ein Trainingsprojekt zu erlernen/anzuwenden? |
| Integrationsaufwand | Wie einfach lässt sich die Technologie mit den anderen Stack-Bausteinen kombinieren? |
| Eignung für Anforderungen | Wie gut passt die Technologie zu den konkreten Anforderungen der Epics? |
| Performance/Skalierung | Reicht die Performance für Zeiträume 2015–2025 und die zu erwartende Datenmenge? |
| Ökosystem/Community | Verfügbarkeit von Libraries, Dokumentation, Beispielen, Support |

Gewichtung für den Gesamtscore (gleichgewichtet, da Trainingsprojekt): je Kriterium Faktor 1, Gesamtscore = Summe der Einzelwerte (max. 25).

## 1. Programmiersprache / Plattform

| Option | Lernkurve | Integrationsaufwand | Eignung | Performance | Ökosystem | Gesamt |
|---|---|---|---|---|---|---|
| **Python** ✅ | 5 | 5 | 5 | 3 | 5 | **23** |
| TypeScript/Node.js | 3 | 3 | 3 | 4 | 4 | 17 |
| Java/Kotlin | 2 | 3 | 3 | 5 | 4 | 17 |

**Begründung:** Python bietet die schnellste Umsetzung dank `pandas`/`requests` für den DWD-Import und lässt sich nahtlos mit SQLite, Streamlit und Plotly kombinieren – alles in einer Sprache/einem Prozess.

## 2. DWD-Datenimport (HTTP-Client / Parsing)

| Option | Lernkurve | Integrationsaufwand | Eignung | Performance | Ökosystem | Gesamt |
|---|---|---|---|---|---|---|
| **Eigener HTTP-Client + Parser (`requests`/`httpx` + `pandas`)** ✅ | 4 | 5 | 5 | 4 | 4 | **22** |
| Wetterdienst (Python-Lib) | 5 | 4 | 4 | 4 | 3 | 20 |
| FTP/Bulk-Download-Skript + Batch-Import | 2 | 3 | 3 | 4 | 3 | 15 |

**Begründung:** Ein eigener Client mit `requests`/`httpx` + `pandas` bietet volle Kontrolle über Parsing und Fehlerbehandlung passend zu den in [doc/DWD/md](../DWD/md) dokumentierten Formaten und bleibt vollständig im Python-Ökosystem des gewählten Stacks. Die Fertig-Bibliothek `wetterdienst` bleibt als Fallback-Option attraktiv, falls der Eigenaufwand zu hoch wird.

## 3. Lokale Datenbank

| Option | Lernkurve | Integrationsaufwand | Eignung | Performance | Ökosystem | Gesamt |
|---|---|---|---|---|---|---|
| **SQLite** ✅ | 5 | 5 | 5 | 3 | 5 | **23** |
| DuckDB | 3 | 4 | 4 | 5 | 3 | 19 |
| PostgreSQL (lokal via Docker) | 2 | 2 | 3 | 5 | 4 | 16 |

**Begründung:** SQLite benötigt keine Serverinstallation, ist als Einzeldatei einfach zu handhaben und in Python über `sqlite3`/SQLAlchemy nativ unterstützt – ideal für ein Einzelnutzer-Trainingsprojekt mit überschaubarer Datenmenge.

## 4. UI-Technologie (Konfigurationsoberfläche)

| Option | Lernkurve | Integrationsaufwand | Eignung | Performance | Ökosystem | Gesamt |
|---|---|---|---|---|---|---|
| **Streamlit** ✅ | 5 | 5 | 4 | 4 | 4 | **22** |
| Web-App (React/Vue + REST-Backend) | 2 | 2 | 4 | 4 | 5 | 17 |
| CLI + generierte HTML-Reports | 4 | 4 | 2 | 4 | 3 | 17 |

**Begründung:** Streamlit erlaubt den Aufbau einer interaktiven Konfigurationsoberfläche (Ort, Zeitraum, Messgrößen gemäß EPIC-003) rein in Python, ohne separates Frontend/Backend, und lässt sich direkt mit Plotly-Diagrammen kombinieren.

## 5. Visualisierung

| Option | Lernkurve | Integrationsaufwand | Eignung | Performance | Ökosystem | Gesamt |
|---|---|---|---|---|---|---|
| **Plotly** ✅ | 4 | 5 | 5 | 4 | 4 | **22** |
| Matplotlib | 4 | 4 | 3 | 4 | 5 | 20 |
| D3.js / Chart.js | 2 | 2 | 4 | 4 | 4 | 16 |

**Begründung:** Plotly liefert interaktive Zeitreihen-Diagramme (Zoom, Hover, mehrere Messgrößen gemeinsam gem. US-018) mit sehr guter Integration in Streamlit und `pandas`-DataFrames.

## Gesamtergebnis

| Baustein | Gewählte Technologie | Gesamtscore |
|---|---|---|
| Sprache/Plattform | Python | 23/25 |
| Datenimport | Eigener HTTP-Client + Parser (requests/httpx + pandas) | 22/25 |
| Datenbank | SQLite | 23/25 |
| UI | Streamlit | 22/25 |
| Visualisierung | Plotly | 22/25 |

Der gewählte Stack **Python + SQLite + Streamlit + Plotly** erzielt in allen Kategorien die höchsten oder zweithöchsten Gesamtscores und bietet dabei den geringsten Integrationsaufwand, da alle Komponenten im selben Sprach-Ökosystem (Python) zusammenspielen. Details und Begründung je Baustein sind in der [Techstack-Übersicht](./techstack-uebersicht.md) zusammengefasst.
