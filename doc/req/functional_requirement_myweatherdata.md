# Functional Requirements - MyWeatherData

---

## FR_01: Pruefung der Standortgrenze Deutschland

**Quelle:** USER_STORY_01

**Requirement:** Wenn eine Koordinate fuer die Stationssuche uebergeben wird, muss das MyWeatherData-System pruefen, ob die Koordinate innerhalb Deutschlands liegt.

**EARS-Pattern:** Event-Driven

**Begruendung:** Die Standortpruefung muss unzulaessige Datenanfragen ausserhalb der Projektgrenze verhindern.

---

## FR_02: Auswahl der naechstgelegenen verfuegbaren Station

**Quelle:** USER_STORY_01

**Requirement:** Wenn mehrere verfuegbare DWD-Wetterstationen fuer eine gueltige Koordinate ermittelt werden, muss das MyWeatherData-System die Station mit der kleinsten Distanz auswaehlen.

**EARS-Pattern:** Event-Driven

**Begruendung:** Die eindeutige Stationsauswahl muss reproduzierbare Abrufergebnisse sicherstellen.

---

## FR_03: Fehlerreaktion bei fehlender Station

**Quelle:** USER_STORY_01

**Requirement:** Wenn fuer eine gueltige Koordinate keine verfuegbare DWD-Wetterstation ermittelt wird, dann muss das MyWeatherData-System einen Fehlerzustand mit fachlicher Rueckmeldung ausgeben.

**EARS-Pattern:** Unwanted Behavior

**Begruendung:** Die explizite Fehlerreaktion muss eine nachvollziehbare Nutzerfuehrung ermoeglichen.

---

## FR_04: Begrenzung des Abrufzeitraums

**Quelle:** USER_STORY_02

**Requirement:** Wenn ein Abrufzeitraum uebergeben wird, dann darf das MyWeatherData-System Datenabrufe ausserhalb von 01.01.2015 bis 31.12.2025 nicht starten.

**EARS-Pattern:** Unwanted Behavior

**Begruendung:** Die Zeitraumgrenze muss die Einhaltung des fachlich definierten Datenbestands sicherstellen.

---

## FR_05: Unterstuetzung der vier Wetterkategorien

**Quelle:** USER_STORY_02

**Requirement:** Das MyWeatherData-System muss fuer den Datenabruf ausschliesslich Lufttemperatur, Niederschlag, Wind und Sonneneinstrahlung verarbeiten.

**EARS-Pattern:** Ubiquitous

**Begruendung:** Die feste Kategorieliste muss den Projektumfang konsistent halten.

---

## FR_06: Protokollierung bei Abruffehler

**Quelle:** USER_STORY_02

**Requirement:** Wenn ein Datenabruf aus dem DWD Climate Data Center fehlschlaegt, dann muss das MyWeatherData-System den Fehler mit Zeitstempel und Fehlerursache protokollieren.

**EARS-Pattern:** Unwanted Behavior

**Begruendung:** Die Fehlerprotokollierung muss die Stoerungsanalyse und Nachvollziehbarkeit sicherstellen.

---

## FR_07: Kennzeichnung teilweise fehlender Kategorien

**Quelle:** USER_STORY_02

**Requirement:** Wenn ein Datenabruf abgeschlossen ist und mindestens eine angeforderte Wetterkategorie fehlt, dann muss das MyWeatherData-System die fehlenden Kategorien explizit kennzeichnen.

**EARS-Pattern:** Unwanted Behavior

**Begruendung:** Die Kennzeichnung muss die fachliche Bewertung unvollstaendiger Ergebnisse absichern.

---

## FR_08: Persistenz mit eindeutiger Schluesselkombination

**Quelle:** USER_STORY_03

**Requirement:** Das MyWeatherData-System muss je Kombination aus Station, Zeitstempel und Wetterkategorie hoechstens einen Messwert speichern.

**EARS-Pattern:** Ubiquitous

**Begruendung:** Die Eindeutigkeitsregel muss Duplikate in der lokalen Datenbank verhindern.

---

## FR_09: Protokollierung uebersprungener Duplikate

**Quelle:** USER_STORY_03

**Requirement:** Wenn beim Import Duplikate erkannt werden, dann muss das MyWeatherData-System die Anzahl der uebersprungenen Datensaetze protokollieren.

**EARS-Pattern:** Unwanted Behavior

**Begruendung:** Die Protokollierung muss die Pruefbarkeit der Deduplizierung sicherstellen.

---

## FR_10: Behandlung ungueltiger Importdatensaetze

**Quelle:** USER_STORY_03

**Requirement:** Wenn ein Importdatensatz ein ungueltiges Format besitzt, dann darf das MyWeatherData-System diesen Datensatz nicht speichern.

**EARS-Pattern:** Unwanted Behavior

**Begruendung:** Die Formatpruefung muss fehlerhafte Persistenz und Dateninkonsistenz vermeiden.

---

## FR_11: Filtertreuer Datenexport

**Quelle:** USER_STORY_04

**Requirement:** Wenn ein Export mit Standort, Zeitraum und Kategorie gestartet wird, muss das MyWeatherData-System ausschliesslich Datensaetze exportieren, die alle gesetzten Filterbedingungen erfuellen.

**EARS-Pattern:** Event-Driven

**Begruendung:** Die Filtertreue muss eine fachlich korrekte Weiterverarbeitung der Exportdaten sichern.

---

## FR_12: CSV-Ausgabe mit Pflichtfeldern

**Quelle:** USER_STORY_04

**Requirement:** Wenn der Export im Format CSV gestartet wird und Datensaetze vorliegen, muss das MyWeatherData-System eine CSV-Datei mit den dokumentierten Pflichtfeldern erzeugen.

**EARS-Pattern:** Event-Driven

**Begruendung:** Die verbindliche CSV-Struktur muss eine stabile Nutzung in Drittsystemen sicherstellen.

---

## FR_13: JSON-Ausgabe nach dokumentierter Struktur

**Quelle:** USER_STORY_04

**Requirement:** Wenn der Export im Format JSON gestartet wird und Datensaetze vorliegen, muss das MyWeatherData-System eine JSON-Datei gemaess dokumentierter Struktur erzeugen.

**EARS-Pattern:** Event-Driven

**Begruendung:** Die verbindliche JSON-Struktur muss Integrationsfehler bei der Weiterverarbeitung reduzieren.

---

## FR_14: Unterdrueckung leerer Exporte

**Quelle:** USER_STORY_04

**Requirement:** Wenn die Exportabfrage keine Datensaetze liefert, dann darf das MyWeatherData-System keine Exportdatei erzeugen.

**EARS-Pattern:** Unwanted Behavior

**Begruendung:** Die Unterdrueckung leerer Dateien muss irrefuehrende Exportergebnisse verhindern.

---

## FR_15: Pflichtfeldvalidierung vor Prozessstart

**Quelle:** USER_STORY_05

**Requirement:** Wenn der Prozessstart im User Interface ausgeloest wird, muss das MyWeatherData-System Standort, Zeitraum und mindestens eine Wetterkategorie als Pflichtfelder validieren.

**EARS-Pattern:** Event-Driven

**Begruendung:** Die Pflichtfeldpruefung muss fehlerhafte Prozessstarts verhindern.

---

## FR_16: Datumsreihenfolgevalidierung

**Quelle:** USER_STORY_05

**Requirement:** Wenn das Enddatum vor dem Startdatum liegt, dann darf das MyWeatherData-System den Prozessstart nicht freigeben.

**EARS-Pattern:** Unwanted Behavior

**Begruendung:** Die Datumsreihenfolgepruefung muss fachlich ungueltige Abfragen verhindern.

---

## FR_17: Statusanzeige waehrend aktiver Verarbeitung

**Quelle:** USER_STORY_06

**Requirement:** Solange Abruf und Speicherung aktiv ausgefuehrt werden, muss das MyWeatherData-System im User Interface den Status laufend anzeigen.

**EARS-Pattern:** State-Driven

**Begruendung:** Die Laufstatusanzeige muss den Bearbeitungszustand transparent machen.

---

## FR_18: Fehlerstatus mit Schrittzuordnung

**Quelle:** USER_STORY_06

**Requirement:** Wenn der Prozess in Abruf oder Speicherung fehlschlaegt, dann muss das MyWeatherData-System im User Interface den Status Fehler mit Zuordnung zum fehlerhaften Prozessschritt anzeigen.

**EARS-Pattern:** Unwanted Behavior

**Begruendung:** Die Schrittzuordnung muss eine zielgerichtete Fehlerbehebung ermoeglichen.

---

## FR_19: Aggregation nach Darstellungsaufloesung

**Quelle:** USER_STORY_07

**Requirement:** Wenn die Darstellungsaufloesung auf taeglich, monatlich oder jaehrlich gesetzt wird, muss das MyWeatherData-System die Visualisierungsdaten entsprechend aggregieren.

**EARS-Pattern:** Event-Driven

**Begruendung:** Die korrekte Aggregation muss fachlich belastbare Trendvergleiche sicherstellen.

---

## FR_20: Kennzeichnung von Datenluecken in Diagrammen

**Quelle:** USER_STORY_07

**Requirement:** Wenn in einem visualisierten Zeitraum Messwerte fehlen, dann muss das MyWeatherData-System die betroffenen Bereiche als Datenluecken kennzeichnen.

**EARS-Pattern:** Unwanted Behavior

**Begruendung:** Die Lueckenkennzeichnung muss Fehlinterpretationen in der Analyse verhindern.

---

## FR_21: Leerdatenzustand bei fehlender Ergebnismenge

**Quelle:** USER_STORY_07

**Requirement:** Wenn die Visualisierungsabfrage keine Messwerte liefert, dann muss das MyWeatherData-System einen Leerdatenzustand anstelle eines Diagramms anzeigen.

**EARS-Pattern:** Unwanted Behavior

**Begruendung:** Der Leerdatenzustand muss eine klare Unterscheidung zwischen fehlenden Daten und Diagrammfehlern ermoeglichen.

---

## FR_22: PNG-Export der aktuellen Ansicht

**Quelle:** USER_STORY_08

**Requirement:** Wenn der PNG-Export gestartet wird, muss das MyWeatherData-System die aktuell sichtbare Visualisierung als PNG-Datei speichern.

**EARS-Pattern:** Event-Driven

**Begruendung:** Der Ansichtsbezug muss sicherstellen, dass Export und UI-Darstellung konsistent sind.

---

## FR_23: Exportabbruch bei unbeschreibbarem Zielpfad

**Quelle:** USER_STORY_08

**Requirement:** Wenn der Zielpfad fuer den PNG-Export nicht beschreibbar ist, dann darf das MyWeatherData-System keine PNG-Datei erzeugen.

**EARS-Pattern:** Unwanted Behavior

**Begruendung:** Die Pfadpruefung muss fehlerhafte Dateiausgaben verhindern.

---

## FR_24: Fehlermeldung bei technischem Exportfehler

**Quelle:** USER_STORY_08

**Requirement:** Wenn der PNG-Export technisch fehlschlaegt, dann muss das MyWeatherData-System eine nachvollziehbare Fehlermeldung ausgeben.

**EARS-Pattern:** Unwanted Behavior

**Begruendung:** Die Fehlermeldung muss eine pruefbare Diagnose fuer den Exportfehler bereitstellen.
