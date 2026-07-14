# Epics - MyWeatherData

## Systemgrenzen

- Externe Datenquelle: Open-Data-Bereich des Climate Data Center (CDC) des Deutschen Wetterdienstes (DWD).
- Lokale Persistenz: SQLite-Datenbank innerhalb der Anwendung.
- Interaktion: User Interface zur Konfiguration von Standort, Zeitraum und Wetterkategorien.
- Auswertung: Visualisierung historischer Wetterdaten.
- Ausgabe: Export von Daten und Visualisierungen.

## Uebergreifende fachliche Leitplanken

- Datenzeitraum ist auf 01.01.2015 bis 31.12.2025 begrenzt.
- Standortbezug erfolgt ueber Koordinaten innerhalb Deutschlands.
- Stationsbezug erfolgt ueber die naechstgelegene verfuegbare DWD-Wetterstation.
- Wetterkategorien sind Lufttemperatur, Niederschlag, Wind und Sonneneinstrahlung.

---

## EPIC_01: DWD-Datenanbindung und Stationszuordnung

**Ziel:** Das System stellt historische Wetterdaten aus dem DWD Climate Data Center fuer gueltige Standorte in Deutschland verlässlich bereit.

**Beschreibung:**
Dieses Epic etabliert die externe Systemgrenze zum DWD und definiert die fachlich korrekte Zuordnung von Koordinaten zu einer naechstgelegenen verfuegbaren Wetterstation. Es umfasst den Datenabruf fuer die vier projektdefinierten Wetterkategorien im gueltigen Zeitraum. Das Epic legt die Grundlage fuer alle nachfolgenden Persistenz-, UI- und Visualisierungsfunktionen.

**Akzeptanzkriterien:**
- Gegeben eine gueltige Koordinate innerhalb Deutschlands, wird die naechstgelegene verfuegbare DWD-Wetterstation eindeutig bestimmt.
- Datenabrufe ausserhalb des Zeitraums 01.01.2015 bis 31.12.2025 werden abgelehnt.
- Fuer Lufttemperatur, Niederschlag, Wind und Sonneneinstrahlung koennen historische Daten fuer den gueltigen Zeitraum geladen werden.
- Fehler bei Netzwerk, Datenquelle oder unvollstaendiger Datenlieferung werden protokolliert und als Fehlerzustand bereitgestellt.

**Umfang:**
- Anbindung an DWD-Open-Data-Endpunkte.
- Stationszuordnung anhand geographischer Distanz.
- Abruf- und Parsing-Logik fuer die vier Wetterkategorien.
- Fehlerbehandlung und fachliche Protokollierung.

**Abhaengigkeiten:**
- Keine vorgelagerten Epics.
- Liefert Daten- und Stationsgrundlage fuer EPIC_02, EPIC_03 und EPIC_04.

**Vorgeschlagene vertikale Slices:**
- S1 Happy Path: Gueltige Koordinate fuehrt zu Stationszuordnung und erfolgreichem Abruf einer Kategorie.
- S2 Validierung: Ungueltiger Zeitraum oder Koordinate ausserhalb Deutschlands wird mit fachlicher Meldung abgelehnt.
- S3 Fehlerfall: Netzwerk- oder Quellenfehler wird protokolliert und als Abruffehler ausgewiesen.
- S4 Datenqualitaet: Teilweise fehlende Kategorien oder Messluecken werden gekennzeichnet.
- S5 Integration: Einheitliches Ergebnisformat fuer Uebergabe an lokale Datenbank.

---

## EPIC_02: Lokale Wetterdatenhaltung und Export

**Ziel:** Das System speichert abgerufene Wetterdaten konsistent in einer lokalen Datenbank und stellt filterbaren Export bereit.

**Beschreibung:**
Dieses Epic etabliert die interne Datenhaltung als zentrale Quelle fuer Analyse, UI und Visualisierung. Es regelt die persistente Ablage mit Duplikatschutz und stellt fachlich gefilterte Exporte bereit. Das Epic reduziert wiederholte externe Abrufe und ermoeglicht reproduzierbare Auswertungen.

**Akzeptanzkriterien:**
- Messwerte werden mit Stationsreferenz, Zeitstempel und Wetterkategorie konsistent gespeichert.
- Doppelte Datensaetze mit gleicher Kombination aus Station, Kategorie und Zeitstempel werden nicht erneut gespeichert.
- Daten koennen nach Standortbezug, Zeitraum und Kategorie fachlich korrekt gefiltert abgefragt werden.
- Export erzeugt fuer nicht-leere Ergebnismengen gueltige CSV- oder JSON-Dateien, bei leerer Ergebnismenge darf keine Datei erzeugt werden.

**Umfang:**
- Datenbankschema fuer Stationen, Messwerte und Kategorien.
- Importpfad von DWD-Abrufdaten in die lokale Datenbank.
- Fachliche Filterabfragen fuer Ort, Zeitraum und Kategorie.
- Exportfunktionen fuer CSV und JSON inklusive Fehlfallbehandlung.

**Abhaengigkeiten:**
- Benoetigt abrufbare und strukturierte Daten aus EPIC_01.
- Liefert Datenbasis fuer EPIC_03 und EPIC_04.

**Vorgeschlagene vertikale Slices:**
- S1 Happy Path: Erfolgreicher Import neuer Messwerte in die lokale Datenbank.
- S2 Validierung: Duplikate werden erkannt und nicht gespeichert.
- S3 Happy Path: Gefilterte Abfrage liefert korrekte Ergebnismenge.
- S4 Fehlerfall: Leere Ergebnismenge beim Export fuehrt zu Meldung ohne Dateierzeugung.
- S5 Integration: Stabiler Exportvertrag fuer CSV/JSON zur Weiterverarbeitung in UI und Drittsystemen.

---

## EPIC_03: Konfigurations- und Steuerungs-UI

**Ziel:** Das System stellt eine Bedienoberflaeche bereit, mit der Fachanwender den End-to-End-Ablauf von Datenauswahl bis Export steuern.

**Beschreibung:**
Dieses Epic bildet die Interaktionsgrenze zum Anwender. Es umfasst die Erfassung und Validierung von Standort, Zeitraum und Wetterkategorien sowie die Steuerung von Abruf, Speicherung und Export. Das Epic sorgt fuer transparente Zustandsanzeigen waehrend und nach der Verarbeitung.

**Akzeptanzkriterien:**
- Das UI akzeptiert nur Koordinaten innerhalb Deutschlands oder einen in Koordinaten aufgeloesten Standort innerhalb Deutschlands.
- Das UI akzeptiert nur Start- und Enddatum innerhalb 01.01.2015 bis 31.12.2025.
- Das UI startet den Ablauf nur, wenn Standort, Zeitraum und mindestens eine Wetterkategorie gesetzt sind.
- Das UI zeigt Prozesszustand als laufend, abgeschlossen oder Fehler mit klar zuordenbarer Rueckmeldung an.

**Umfang:**
- Eingabeflaechen fuer Standort, Zeitraum und Kategorien.
- Validierungslogik fuer Pflichtfelder und gueltige Wertebereiche.
- Orchestrierung von Abruf, Speicherung und Exportausloesung.
- Status- und Fehlerrueckmeldungen fuer den Gesamtprozess.

**Abhaengigkeiten:**
- Benoetigt Stations- und Abruffunktionen aus EPIC_01.
- Benoetigt Persistenz- und Exportfunktionen aus EPIC_02.
- Liefert Filter- und Steuerungszustand fuer EPIC_04.

**Vorgeschlagene vertikale Slices:**
- S1 Happy Path: Gueltige Eingaben starten erfolgreichen Abruf- und Speicherablauf.
- S2 Validierung: Pflichtfelder und Wertebereichsverletzungen blockieren den Prozessstart.
- S3 Fehlerfall: Prozessfehler werden dem fehlerhaften Schritt zugeordnet angezeigt.
- S4 Edge Case: Enddatum vor Startdatum und leere Kategorieauswahl werden eindeutig gefuehrt.
- S5 Integration: Durchgaengiger End-to-End-Ablauf bis zum Export aus dem UI.

---

## EPIC_04: Analyseorientierte Visualisierung und Bildexport

**Ziel:** Das System visualisiert historische Wetterdaten je Kategorie auswertbar und exportiert die aktuelle Darstellung als PNG.

**Beschreibung:**
Dieses Epic liefert die analytische Sicht auf gespeicherte Zeitreihendaten. Es stellt kategoriegerechte Diagramme mit waehlbarer Aufloesung bereit und unterscheidet sauber zwischen Leerdaten- und Fehlerzustand. Das Epic ermoeglicht den Export der aktuell sichtbaren Visualisierung als Bilddatei.

**Akzeptanzkriterien:**
- Fuer jede Wetterkategorie wird eine passende Zeitreihendarstellung aus lokal gespeicherten Daten erzeugt.
- Die Aggregation taeglich, monatlich und jaehrlich liefert fachlich korrekte Werte zur gewaehlten Aufloesung.
- Fehlende Messwerte im Zeitraum werden als Datenluecken kenntlich gemacht.
- Bei nicht beschreibbarem Zielpfad fuer PNG-Export wird keine Datei erzeugt und ein Fehlerzustand angezeigt.

**Umfang:**
- Datenabfrage und Aufbereitung fuer Visualisierungszwecke.
- Diagrammkomponenten fuer die vier Wetterkategorien.
- Aggregationslogik fuer taeglich, monatlich und jaehrlich.
- PNG-Export der aktuell sichtbaren Darstellung inklusive Fehlfallbehandlung.

**Abhaengigkeiten:**
- Benoetigt Datenhaltung und Filter aus EPIC_02.
- Benoetigt Steuerungs- und Filterzustand aus EPIC_03.

**Vorgeschlagene vertikale Slices:**
- S1 Happy Path: Kategorieauswahl zeigt korrekte Zeitreihe im gueltigen Zeitraum.
- S2 Happy Path: Umschaltung der Aufloesung aktualisiert die Aggregation korrekt.
- S3 Edge Case: Datenluecken werden in der Darstellung markiert.
- S4 Fehlerfall: Leerdatenzustand und technischer Fehlerzustand werden getrennt dargestellt.
- S5 Integration: PNG-Export liefert die aktuell sichtbare Visualisierung als Datei.

---

## Epic-Abhaengigkeiten

1. EPIC_01 ist fachlicher Startpunkt fuer externe Datenbereitstellung.
2. EPIC_02 baut auf EPIC_01 auf und erzeugt die lokale Datenbasis.
3. EPIC_03 integriert EPIC_01 und EPIC_02 fuer die Nutzersteuerung.
4. EPIC_04 baut auf EPIC_02 und EPIC_03 fuer Analyse und Bildexport auf.
