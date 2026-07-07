---

name: "user_story"

description: "Erstelle oder verfeinere User Stories für das MyWeatherData-Projekt anhand der bestehenden Epics. Verwende diesen Skill, wenn aus Epics konkrete User Stories mit Akzeptanzkriterien abgeleitet werden sollen."

argument-hint: "Epic-ID oder Beschreibung der gewünschten User Story"

applyTo: "doc/req/*.md"

---

# Skill: User Stories erstellen – MyWeatherData

## Aufgabe

Wenn der Nutzer aus einem Epic User Stories ableiten möchte, nutze das unten definierte User-Story-Template. Halte dich exakt an die Struktur und Sprache Deutsch. Füge neue User Stories in die Datei `doc/req/user_story_myweatherdata.md` ein.

---

## User-Story-Template

```markdown
## USER_STORY_<NN>: <Titel>

**Epic:** <EPIC_ID>

**User Story:** Als <Rolle> möchte ich <Ziel/Aktion>, damit <Nutzen/Grund>.

**Akzeptanzkriterien:**

- Gegeben <Ausgangszustand>, wenn <Aktion/Ereignis>, dann <erwartetes Ergebnis>.
- Gegeben <Ausgangszustand>, wenn <Aktion/Ereignis>, dann <erwartetes Ergebnis>.
- Gegeben <Ausgangszustand>, wenn <Aktion/Ereignis>, dann <erwartetes Ergebnis>.

**INVEST-Prüfung:**

- Independent: <kurze Begründung>
- Negotiable: <kurze Begründung>
- Valuable: <kurze Begründung>
- Estimable: <kurze Begründung>
- Small: <kurze Begründung>
- Testable: <kurze Begründung>

---

## Regeln für das Ausfüllen des Templates

| Feld                   | Vorgabe                                                            |
| ---------------------- | ------------------------------------------------------------------ |
| `USER_STORY_<NN>`      | Fortlaufende zweistellige Nummer, z. B. `USER_STORY_01`            |
| **Epic**               | Muss eine existierende Epic-ID referenzieren                       |
| **User Story**         | Muss dem Format „Als ... möchte ich ..., damit ..." folgen         |
| **Akzeptanzkriterien** | 3–5 testbare Kriterien im Given/When/Then-Stil                     |
| **INVEST-Prüfung**     | Für alle sechs INVEST-Kriterien kurze Bewertung angeben            |
| Zeitraum               | Wenn relevant, 01.01.2015 bis 31.12.2025 beachten                  |
| Wetterdaten            | Lufttemperatur, Niederschlag, Wind und Sonneneinstrahlung beachten |


## Kontext: Bestehende Epics

Die folgenden Epics existieren bereits in `doc/req/epic_myweatherdata.md`. Jede User Story muss genau einem bestehenden Epic zugeordnet werden.

| ID | Titel | Kern |
|---|---|---|
| EPIC_01 | DWD Climate Data Center API | Datenabruf vom DWD CDC via HTTP/FTP |
| EPIC_02 | Lokale Datenbank | SQLite-Speicherung, Import/Export, Deduplizierung |
| EPIC_03 | User Interface | GUI/Web-Oberfläche zur Konfiguration und Steuerung |
| EPIC_04 | Visualisierung | Interaktive Zeitreihen-Diagramme, Export als PNG |
