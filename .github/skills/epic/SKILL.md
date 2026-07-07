---
name: "epic"
description: "Erstelle oder verfeinere Epics für das MyWeatherData-Projekt anhand des festgelegten Epic-Templates. Verwende diesen Skill wenn der Nutzer ein neues Epic anlegen, ein bestehendes Epic überarbeiten oder die Epic-Datei erweitern möchte."
argument-hint: "Beschreibung des gewünschten Epics oder Name der Epic-Datei"
applyTo: "doc/req/*.md"
---

# Skill: Epic erstellen – MyWeatherData

## Aufgabe

Wenn der Nutzer ein neues Epic anlegen oder ein bestehendes Epic erweitern möchte, nutze das unten definierte **Epic-Template**. Halte dich exakt an die Struktur und Sprache (Deutsch). Füge das neue Epic in die Datei `doc/req/epic_myweatherdata.md` ein oder lege dort eine neue Sektion an.

---

## Epic-Template

Jedes Epic folgt diesem Schema:

```markdown
## EPIC_<NN>: <Titel>

**Ziel:** <Einzeiliger Satz, der den Nutzen und den Zweck des Epics beschreibt.>

**Beschreibung:**
<Zwei bis vier Sätze, die erläutern, was implementiert wird, welche Komponenten betroffen sind
und wie das Epic in das Gesamtsystem eingebettet ist.>

**Akzeptanzkriterien:**
- <Kriterium 1 im Format „Gegeben … wird/kann …" oder als klare Aussage>
- <Kriterium 2>
- <Kriterium 3>
- <Kriterium 4>
- <Kriterium 5>

**Umfang:**
- <Lieferobjekt oder Aktivität 1>
- <Lieferobjekt oder Aktivität 2>
- <Lieferobjekt oder Aktivität 3>
- <Lieferobjekt oder Aktivität 4>
- <Lieferobjekt oder Aktivität 5>
```

---

## Regeln für das Ausfüllen des Templates

| Feld | Vorgabe |
|---|---|
| `EPIC_<NN>` | Fortlaufende zweistellige Nummer, z. B. `EPIC_05` |
| **Ziel** | Genau ein Satz; beginnt mit einem Substantiv (Infinitiv vermeiden) |
| **Beschreibung** | Kein Aufzählungsformat; fließender Text |
| **Akzeptanzkriterien** | Messbar und testbar; 4–7 Punkte; Zeitraum 01.01.2015–31.12.2025 beachten wenn relevant |
| **Umfang** | Konkrete Lieferobjekte oder Aktivitäten; 4–7 Punkte; keine vagen Aussagen |

---

## Kontext: Bestehende Epics

Die folgenden Epics existieren bereits in `doc/req/epic_myweatherdata.md`. Vergib keine bereits verwendete Nummer und vermeide inhaltliche Überschneidungen:

| ID | Titel | Kern |
|---|---|---|
| EPIC_01 | DWD Climate Data Center API | Datenabruf vom DWD CDC via HTTP/FTP |
| EPIC_02 | Lokale Datenbank | SQLite-Speicherung, Import/Export, Deduplizierung |
| EPIC_03 | User Interface | GUI/Web-Oberfläche zur Konfiguration und Steuerung |
| EPIC_04 | Visualisierung | Interaktive Zeitreihen-Diagramme, Export als PNG |

---

## Beispiel-Output

Wenn der Nutzer z. B. ein Epic für „Authentifizierung und Zugangsverwaltung" anfragt, erzeuge:

```markdown
## EPIC_05: Authentifizierung und Zugangsverwaltung

**Ziel:** Absicherung des lokalen Zugangs zur Anwendung durch eine einfache Nutzerverwaltung.

**Beschreibung:**
Implementierung einer minimalen Authentifizierungsschicht, die den Start der Anwendung
durch einen konfigurierbaren PIN oder ein Passwort schützt. Zugangsdaten werden lokal
und sicher gespeichert. Das Modul ist als optionale Komponente konzipiert und kann
deaktiviert werden.

**Akzeptanzkriterien:**
- Gegeben ein gesetztes Passwort, wird der Anwendungsstart ohne korrekte Eingabe verweigert.
- Zugangsdaten werden nicht im Klartext gespeichert (mindestens bcrypt-Hash).
- Der Nutzer kann das Passwort über die Einstellungen ändern.
- Die Authentifizierung kann in der Konfigurationsdatei vollständig deaktiviert werden.
- Fehlerhafte Anmeldeversuche werden im Log protokolliert.

**Umfang:**
- Konfigurationsschema für Authentifizierungseinstellungen
- Passwort-Hashing und -Verifikation (bcrypt)
- Login-Dialog im UI
- Einstellungsseite zum Passwort ändern/Funktion deaktivieren
- Unit-Tests für Hashing und Verifikationslogik
```
