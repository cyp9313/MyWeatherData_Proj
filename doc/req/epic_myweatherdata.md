# Epics – MyWeatherData

---

## EPIC_01: DWD Climate Data Center API

**Ziel:** Bereitstellung einer zuverlässigen Schnittstelle zum Open-Data-Angebot des Deutschen Wetterdienstes (DWD), um historische Wetterdaten automatisiert abrufen zu können.

**Beschreibung:**
Implementierung eines API-Moduls, das über das Climate Data Center (CDC) des DWD Wetterdaten für beliebige Standorte in Deutschland abruft. Das Modul ermittelt anhand von GPS-Koordinaten die nächstgelegene Wetterstation und lädt die gewünschten Datensätze (Temperatur, Niederschlag, Wind, Sonneneinstrahlung) für den konfigurierten Zeitraum herunter.

**Akzeptanzkriterien:**
- Gegeben eine geografische Koordinate, wird die nächstgelegene DWD-Wetterstation korrekt identifiziert.
- Daten für alle vier Wetterkategorien (Lufttemperatur, Niederschlag, Wind, Sonneneinstrahlung) können abgerufen werden.
- Der Abruf ist auf den Zeitraum 01.01.2015 bis 31.12.2025 beschränkt.
- Fehler beim Datenabruf (z. B. Netzwerkprobleme, fehlende Daten) werden abgefangen und protokolliert.
- Das Modul ist über eine einheitliche Python-Schnittstelle aufrufbar.

**Umfang:**
- Anbindung an den DWD Open-Data-FTP/HTTP-Server
- Stationssuche anhand von Koordinaten (Haversine-Distanz)
- Download und Parsing der CSV-Rohdaten je Wetterkategorie
- Fehlerbehandlung und Logging
- Unit-Tests für die API-Funktionen

---

## EPIC_02: Lokale Datenbank

**Ziel:** Persistente, strukturierte Speicherung der vom DWD abgerufenen Wetterdaten in einer lokalen Datenbank für schnellen Zugriff und Wiederverwendung ohne erneuten Download.

**Beschreibung:**
Aufbau eines Datenbankmoduls, das die heruntergeladenen Wetterdaten in einer lokalen relationalen Datenbank (SQLite) speichert und verwaltet. Das Modul stellt Funktionen bereit, um Daten zu importieren, abzufragen und zu exportieren, sowie eine Deduplizierungslogik, um Redundanzen beim wiederholten Import zu vermeiden.

**Akzeptanzkriterien:**
- Wetterdaten werden mit korrektem Zeitstempel, Stationsreferenz und Datenkategorie gespeichert.
- Bereits vorhandene Datensätze werden beim erneuten Import nicht dupliziert.
- Datenbankabfragen nach Ort, Zeitraum und Wetterkategorie liefern korrekte Ergebnisse.
- Die Datenbank kann vollständig exportiert oder auf einen definierten Zeitraum/Ort gefiltert exportiert werden.
- Das Schema ist dokumentiert und versioniert.

**Umfang:**
- Datenbankschema-Design (Stationen, Messwerte, Kategorien)
- Import-Pipeline vom API-Modul in die Datenbank
- CRUD-Operationen (Schwerpunkt Read/Write)
- Export-Funktion (CSV, JSON)
- Datenbank-Migrationskonzept
- Integration Tests

---

## EPIC_03: User Interface

**Ziel:** Bereitstellung einer benutzerfreundlichen Oberfläche, über die der Nutzer Standort, Zeitraum und gewünschte Wetterdaten konfigurieren und den Datenabruf sowie den Export steuern kann.

**Beschreibung:**
Entwicklung eines grafischen User Interfaces (GUI) oder einer Web-basierten Oberfläche, die es dem Nutzer ermöglicht, ohne Programmierkenntnisse die gewünschten Parameter einzustellen. Der Nutzer wählt Koordinaten oder einen Ort, definiert den Zeitraum und selektiert die anzuzeigenden Wetterdaten. Das UI löst im Hintergrund den Datenabruf und die Speicherung aus.

**Akzeptanzkriterien:**
- Der Nutzer kann Koordinaten oder Ortsname eingeben; die nächstgelegene Station wird angezeigt.
- Start- und Enddatum sind frei wählbar innerhalb von 01.01.2015 bis 31.12.2025.
- Wetterkategorien (Temperatur, Niederschlag, Wind, Sonneneinstrahlung) sind einzeln an- und abwählbar.
- Der Status des Datenabrufs (laufend, abgeschlossen, Fehler) wird dem Nutzer angezeigt.
- Ein Export-Button ermöglicht den Download der Daten als CSV oder JSON.

**Umfang:**
- UI-Framework-Auswahl und Grundgerüst (z. B. Streamlit oder Tkinter)
- Eingabefelder für Koordinaten/Ort, Zeitraum, Datenkategorien
- Statusanzeige für Datenabruf und Datenbankoperationen
- Anbindung an API- und Datenbankmodul
- Exportfunktion im UI

---

## EPIC_04: Visualisierung

**Ziel:** Anschauliche und interaktive Darstellung der gespeicherten Wetterdaten gemäß den Nutzervorgaben, um Trends, Muster und Anomalien schnell erkennbar zu machen.

**Beschreibung:**
Entwicklung einer Visualisierungskomponente, die Wetterdaten aus der lokalen Datenbank als Diagramme und Grafiken darstellt. Diagrammtypen werden je nach Wetterkategorie ausgewählt (z. B. Liniendiagramm für Temperatur, Balkendiagramm für Niederschlag). Die Darstellung ist konfigurierbar und in das User Interface integriert.

**Akzeptanzkriterien:**
- Wetterdaten werden als interaktive Zeitreihen-Diagramme dargestellt.
- Mindestens vier Diagrammtypen (je einer pro Wetterkategorie) sind implementiert.
- Zeitraum und Darstellungsauflösung (täglich, monatlich, jährlich) sind im UI einstellbar.
- Diagramme können als Bilddatei (PNG) exportiert werden.
- Die Visualisierungskomponente ist vollständig in das UI integriert.

**Umfang:**
- Auswahl und Integration einer Diagrammbibliothek (z. B. Matplotlib, Plotly)
- Zeitreihen-Diagramm für Lufttemperatur
- Balken-/Flächendiagramm für Niederschlag
- Linien-/Pfeildiagramm für Wind (Geschwindigkeit und ggf. Richtung)
- Liniendiagramm für Sonneneinstrahlung
- Aggregationsfunktionen (täglich, monatlich, jährlich)
- Export der Diagramme als PNG
