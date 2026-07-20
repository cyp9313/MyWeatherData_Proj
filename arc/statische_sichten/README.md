# Statische Sichten – MyWeatherData

Dieser Ordner enthält die statischen Architektursichten (arc42-Kapitel 3 und 5) des Systems **MyWeatherData**, jeweils als Markdown-Beschreibung mit eingebetteten PlantUML-Diagrammen.

| Sicht | Beschreibung | Diagramme |
|---|---|---|
| Kontextsicht | [kontextsicht.md](./kontextsicht.md) | [kontextsicht-fachlich.puml](./kontextsicht-fachlich.puml), [kontextsicht-technisch.puml](./kontextsicht-technisch.puml) |
| Komponentensicht | [komponentensicht.md](./komponentensicht.md) | [komponentensicht-ebene1.puml](./komponentensicht-ebene1.puml), [komponentensicht-ebene2-core.puml](./komponentensicht-ebene2-core.puml), [komponentensicht-ebene2-import-client.puml](./komponentensicht-ebene2-import-client.puml), [komponentensicht-ebene2-datenhaltung.puml](./komponentensicht-ebene2-datenhaltung.puml) |
| Klassensicht | [klassensicht.md](./klassensicht.md) | [klassensicht-core.puml](./klassensicht-core.puml), [klassensicht-import-client.puml](./klassensicht-import-client.puml), [klassensicht-datenhaltung.puml](./klassensicht-datenhaltung.puml), [klassensicht-ui.puml](./klassensicht-ui.puml), [klassensicht-visualisierung.puml](./klassensicht-visualisierung.puml) |

Die drei Sichten bauen aufeinander auf: Die Komponentensicht verfeinert die Kontextsicht, die Klassensicht verfeinert einzelne Komponenten der Komponentensicht.

## Hinweis: Export-Funktion vorerst nicht Teil der Architektur

Die Export-Funktion (Bereitstellung gespeicherter Wetterdaten als CSV-Datei, siehe [EPIC-001](../../req/epic/EPIC-001-datenimport-export-dwd.md), [US-006](../../req/user-story/)) ist **fachlich weiterhin geplant**, wird aber **erst in Version 2** umgesetzt. Sie wurde daher bewusst aus allen drei statischen Sichten (Kontext-, Komponenten- und Klassensicht) entfernt, um den aktuellen Umsetzungsstand (Version 1) korrekt abzubilden.

Beim Start der Umsetzung von Version 2 müssen die Sichten entsprechend um die Export-Komponente ergänzt werden:

- **Kontextsicht:** Beziehung „System → Nutzer:in: Wetterdaten als Datei bereitstellen (Export)“ (fachlich) sowie die technische Realisierung über eine CSV-Datei wieder ergänzen.
- **Komponentensicht:** Komponente `Export` in Ebene 1 sowie die Teilkomponente `Export-Orchestrierung` in der Ebene-2-Verfeinerung von `Core` wieder ergänzen (Anbindung ausschließlich über `Core`, keine direkte Beziehung zu anderen Fach-Komponenten).
- **Klassensicht:** Prüfen, ob die Export-Komponente das [Kriterium für Klassenverfeinerung](../../.github/skills/ar-klassen-sicht/SKILL.md) erfüllt, und bei Bedarf ein eigenes Klassendiagramm ergänzen.

Für diese Ergänzungen den Agent `ar-architecture-designer-static-views` bzw. die Skills `ar-kontext-sicht`, `ar-komponenten-sicht` und `ar-klassen-sicht` verwenden.
