---

name: "functional_requirement"

description: "Erstelle oder verfeinere Functional Requirements für das MyWeatherData-Projekt anhand bestehender User Stories und Akzeptanzkriterien. Verwende diesen Skill, wenn formale, testbare Systemanforderungen im EARS-Format erstellt oder überarbeitet werden sollen."

argument-hint: "User-Story-ID, Beschreibung der gewünschten Functional Requirements oder Name der Requirement-Datei"

applyTo: "doc/req/*.md"

---

# Skill: Functional Requirements erstellen – MyWeatherData

## Aufgabe

Wenn der Nutzer aus bestehenden User Stories und Akzeptanzkriterien Functional Requirements ableiten möchte, nutze das unten definierte **Functional-Requirement-Template**. Halte dich exakt an die Struktur und Sprache Deutsch. Formuliere die Anforderungen aus Sicht des Systems und nicht aus Sicht des Nutzers.

Füge neue Functional Requirements in die Datei `doc/req/functional_requirement_myweatherdata.md` ein oder lege dort eine neue Sektion an.

---

## Functional-Requirement-Template

Jedes Functional Requirement folgt diesem Schema:

```markdown
## FR_<NN>: <Titel>

**Quelle:** <USER_STORY_ID>

**Requirement:** <Requirement im EARS-Format>

**EARS-Pattern:** <Ubiquitous | Event-Driven | State-Driven | Unwanted Behavior | Optional Feature | Complex>

**Begründung:** <Ein kurzer Satz, warum dieses Requirement für das System notwendig ist.>
```

---

## EARS-Pattern

Verwende für jedes Functional Requirement genau eines der folgenden EARS-Pattern:

| Pattern | Syntax |
|---|---|
| Ubiquitous | Das <Systemname> muss <Systemantwort>. |
| Event-Driven | Wenn <Trigger>, muss das <Systemname> <Systemantwort>. |
| State-Driven | Solange <Zustand>, muss/darf das <Systemname> <Systemantwort>. |
| Unwanted Behavior | Wenn <unerwünschtes Ereignis>, dann muss das <Systemname> <Systemantwort>. |
| Optional Feature | Wo <Feature vorhanden ist>, muss das <Systemname> <Systemantwort>. |
| Complex | Solange <Zustand>, wenn <Trigger>, dann muss das <Systemname> <Systemantwort>. |

---

## Regeln für das Ausfüllen des Templates

| Feld | Vorgabe |
|---|---|
| `FR_<NN>` | Fortlaufende zweistellige Nummer, z. B. `FR_01`, `FR_02`, `FR_03` |
| **Titel** | Kurz, fachlich eindeutig und systembezogen |
| **Quelle** | Muss eine existierende User Story referenzieren, z. B. `USER_STORY_01` |
| **Requirement** | Muss im EARS-Format formuliert sein |
| **Requirement** | Genau eine Anforderung pro Requirement |
| **Requirement** | Muss eindeutig, testbar und messbar sein |
| **Requirement** | Muss aus Sicht des Systems formuliert sein |
| **EARS-Pattern** | Muss genau eines der definierten Pattern sein |
| **Begründung** | Genau ein kurzer Satz |
| Sprache | Deutsch |
| Verbindlichkeit | Verwende „muss“ oder „darf nicht“ |
| Verbotene Wörter | Vermeide „sollte“, „kann“, „idealerweise“, „möglichst“, „gegebenenfalls“ |
| Zeitraum | Wenn relevant, muss der Zeitraum 01.01.2015 bis 31.12.2025 berücksichtigt werden |
| Ort | Wenn relevant, muss die Einschränkung auf Koordinaten innerhalb Deutschlands berücksichtigt werden |
| Wetterdaten | Wenn relevant, müssen Lufttemperatur, Niederschlag, Wind und Sonneneinstrahlung berücksichtigt werden |

---

## Qualitätsregeln

Functional Requirements müssen folgende Qualitätskriterien erfüllen:

- Eindeutigkeit: Die Anforderung darf keine mehrdeutigen Begriffe enthalten.
- Testbarkeit: Die Anforderung muss durch Testfälle überprüfbar sein.
- Nachvollziehbarkeit: Jede Anforderung muss auf mindestens eine User Story zurückführbar sein.
- Atomarität: Jede Anforderung beschreibt genau eine Systemfunktion.
- Konsistenz: Die Anforderung darf bestehenden Epics, User Stories oder Requirements nicht widersprechen.
- Vollständigkeit: Relevante Randbedingungen wie Zeitraum, Standort, Datenkategorie und Fehlersituationen müssen genannt werden.

---

## Kontext: Projekt MyWeatherData

Das Projekt MyWeatherData dient der Abfrage, Speicherung, Visualisierung und dem Export historischer Wetterdaten aus dem DWD Climate Data Center.

Der erlaubte Zeitraum ist vom 01.01.2015 bis zum 31.12.2025.

Der Ort wird über eine beliebige geografische Koordinate innerhalb Deutschlands bestimmt. Das System verwendet die nächstgelegene verfügbare DWD-Wetterstation.

Folgende Wetterdaten müssen berücksichtigt werden:

- Lufttemperatur
- Niederschlag
- Wind
- Sonneneinstrahlung

Das System besteht aus folgenden Hauptbereichen:

- API zum Datenimport und Datenexport vom DWD Climate Data Center
- Lokale Datenbank zur Speicherung und Verwaltung der Wetterdaten
- User Interface zur Konfiguration von Ort, Zeitraum und Wetterdaten
- Visualisierung der Wetterdaten entsprechend den Benutzervorgaben

---

## Beispiel-Output

Wenn der Nutzer z. B. Functional Requirements für `USER_STORY_02: Historische Wetterdaten abrufen` anfragt, erzeuge:

```markdown
## FR_05: Abruf historischer Wetterdaten

**Quelle:** USER_STORY_02

**Requirement:** Wenn der Nutzer eine gültige Wetterstation, einen gültigen Zeitraum zwischen dem 01.01.2015 und dem 31.12.2025 und mindestens eine Wetterkategorie auswählt, muss das MyWeatherData-System die entsprechenden historischen Wetterdaten aus dem DWD Climate Data Center abrufen.

**EARS-Pattern:** Event-Driven

**Begründung:** Der Abruf historischer Wetterdaten ist die zentrale Funktion des DWD-API-Moduls.

---

## FR_06: Beschränkung auf unterstützte Wetterkategorien

**Quelle:** USER_STORY_02

**Requirement:** Das MyWeatherData-System muss ausschließlich die Wetterkategorien Lufttemperatur, Niederschlag, Wind und Sonneneinstrahlung für den Datenabruf bereitstellen.

**EARS-Pattern:** Ubiquitous

**Begründung:** Die unterstützten Wetterkategorien sind durch die Projektbeschreibung festgelegt.

---

## FR_07: Behandlung fehlgeschlagener Datenabrufe

**Quelle:** USER_STORY_02

**Requirement:** Wenn der Datenabruf aus dem DWD Climate Data Center fehlschlägt, dann muss das MyWeatherData-System den Fehler protokollieren und dem Nutzer eine verständliche Fehlermeldung anzeigen.

**EARS-Pattern:** Unwanted Behavior

**Begründung:** Fehler beim Datenabruf müssen nachvollziehbar sein und für den Nutzer verständlich kommuniziert werden.
```