# Functional Requirements – MyWeatherData

---

## FR_01: Validierung geografischer Koordinaten

**Quelle:** USER_STORY_01

**Requirement:** Wenn eine Koordinate für die Stationssuche eingegeben wird, muss das MyWeatherData-System prüfen, ob die Koordinate innerhalb Deutschlands liegt.

**EARS-Pattern:** Event-Driven

**Begründung:** Die Standortvalidierung muss fehlerhafte Stationszuordnungen verhindern.

---

## FR_02: Auswahl der nächstgelegenen aktiven Station

**Quelle:** USER_STORY_01

**Requirement:** Wenn mehrere aktive DWD-Stationen für eine gültige Koordinate verfügbar sind, muss das MyWeatherData-System die Station mit der kleinsten Haversine-Distanz auswählen.

**EARS-Pattern:** Event-Driven

**Begründung:** Die Distanzlogik muss eine eindeutige und reproduzierbare Stationswahl sicherstellen.

---

## FR_03: Unterstützung festgelegter Wetterkategorien

**Quelle:** USER_STORY_02

**Requirement:** Das MyWeatherData-System muss für den Datenabruf ausschließlich die Wetterkategorien Lufttemperatur, Niederschlag, Wind und Sonneneinstrahlung unterstützen.

**EARS-Pattern:** Ubiquitous

**Begründung:** Die Kategorienbegrenzung muss die Konsistenz mit dem Projektumfang erhalten.

---

## FR_04: Begrenzung des Abrufzeitraums

**Quelle:** USER_STORY_02

**Requirement:** Wenn ein Abrufzeitraum angegeben wird, muss das MyWeatherData-System Zeiträume außerhalb vom 01.01.2015 bis 31.12.2025 ablehnen.

**EARS-Pattern:** Event-Driven

**Begründung:** Die Zeitraumbeschränkung muss unzulässige Datenanfragen verhindern.

---

## FR_05: Protokollierung bei Abruffehler

**Quelle:** USER_STORY_02

**Requirement:** Wenn der Datenabruf aus dem DWD Climate Data Center fehlschlägt, dann muss das MyWeatherData-System den Fehler mit Zeitstempel und Fehlerursache protokollieren.

**EARS-Pattern:** Unwanted Behavior

**Begründung:** Die Fehlerprotokollierung muss eine nachvollziehbare Störungsanalyse ermöglichen.

---

## FR_06: Strukturierte Aufbereitung heruntergeladener Daten

**Quelle:** USER_STORY_02

**Requirement:** Wenn der Download von Wetterdaten abgeschlossen ist, muss das MyWeatherData-System die Rohdaten in strukturierte Datensätze mit Stationsreferenz, Zeitstempel und Kategorie überführen.

**EARS-Pattern:** Event-Driven

**Begründung:** Die Datenaufbereitung muss eine konsistente Weiterverarbeitung in Datenbank und Visualisierung sichern.

---

## FR_07: Duplikatschutz in der Persistenz

**Quelle:** USER_STORY_03

**Requirement:** Das MyWeatherData-System muss pro Kombination aus Stationsreferenz, Zeitstempel und Wetterkategorie höchstens einen Messwert speichern.

**EARS-Pattern:** Ubiquitous

**Begründung:** Die Eindeutigkeit muss redundante Datensätze in der Datenbank verhindern.

---

## FR_08: Protokollierung übersprungener Duplikate

**Quelle:** USER_STORY_03

**Requirement:** Wenn ein Importlauf Duplikate enthält, dann muss das MyWeatherData-System die Anzahl der übersprungenen Datensätze im Importprotokoll speichern.

**EARS-Pattern:** Unwanted Behavior

**Begründung:** Die Importtransparenz muss die Prüfbarkeit der Deduplizierungslogik sicherstellen.

---

## FR_09: Filterbasierter Export

**Quelle:** USER_STORY_04

**Requirement:** Wenn ein Export mit Ort, Zeitraum und Wetterkategorie ausgelöst wird, muss das MyWeatherData-System ausschließlich Datensätze exportieren, die alle gesetzten Filterkriterien erfüllen.

**EARS-Pattern:** Event-Driven

**Begründung:** Die Filterlogik muss eine präzise Datenausgabe für nachgelagerte Analysen sicherstellen.

---

## FR_10: Unterdrückung leerer Exportdateien

**Quelle:** USER_STORY_04

**Requirement:** Wenn eine Exportabfrage keine Datensätze liefert, dann darf das MyWeatherData-System keine Exportdatei erzeugen.

**EARS-Pattern:** Unwanted Behavior

**Begründung:** Die Unterdrückung leerer Dateien muss irreführende Ergebnisse vermeiden.

---

## FR_11: Validierung von Pflichtfeldern im UI

**Quelle:** USER_STORY_05

**Requirement:** Wenn der Datenabruf im User Interface gestartet wird, muss das MyWeatherData-System prüfen, ob Standort, Zeitraum und mindestens eine Wetterkategorie vollständig angegeben sind.

**EARS-Pattern:** Event-Driven

**Begründung:** Die Pflichtfeldprüfung muss fehlerhafte Abrufstarts verhindern.

---

## FR_12: Datumsvalidierung im UI

**Quelle:** USER_STORY_05

**Requirement:** Solange ein ausgewähltes Datum außerhalb vom 01.01.2015 bis 31.12.2025 liegt, darf das MyWeatherData-System den Datenabruf nicht starten.

**EARS-Pattern:** State-Driven

**Begründung:** Die Datumsgrenze muss die Einhaltung des gültigen Datenbestands absichern.

---

## FR_13: Statusanzeige während des Abrufs

**Quelle:** USER_STORY_06

**Requirement:** Solange ein Datenabruf aktiv ist, muss das MyWeatherData-System im User Interface den Status "laufend" anzeigen.

**EARS-Pattern:** State-Driven

**Begründung:** Die Statusanzeige muss den aktuellen Verarbeitungszustand transparent machen.

---

## FR_14: Statusanzeige nach Abrufende

**Quelle:** USER_STORY_06

**Requirement:** Wenn ein Datenabruf endet, muss das MyWeatherData-System im User Interface den Status "abgeschlossen" oder "Fehler" mit Ergebnis- oder Fehlerhinweis anzeigen.

**EARS-Pattern:** Event-Driven

**Begründung:** Die Abschlussrückmeldung muss den Abrufausgang eindeutig kommunizieren.

---

## FR_15: Aggregation für Darstellungsauflösung

**Quelle:** USER_STORY_07

**Requirement:** Wenn eine Darstellungsauflösung mit täglich, monatlich oder jährlich ausgewählt wird, muss das MyWeatherData-System die Messwerte entsprechend der gewählten Auflösung aggregieren.

**EARS-Pattern:** Event-Driven

**Begründung:** Die korrekte Aggregation muss eine fachlich richtige Trenddarstellung gewährleisten.

---

## FR_16: Kennzeichnung fehlender Messwerte

**Quelle:** USER_STORY_07

**Requirement:** Wenn in einem angezeigten Zeitraum Messwerte fehlen, dann muss das MyWeatherData-System die Lücken in der Visualisierung eindeutig kennzeichnen.

**EARS-Pattern:** Unwanted Behavior

**Begründung:** Die Lückenkennzeichnung muss Fehlinterpretationen in Zeitreihen vermeiden.

---

## FR_17: PNG-Export der aktuellen Visualisierung

**Quelle:** USER_STORY_08

**Requirement:** Wenn der PNG-Export ausgelöst wird, muss das MyWeatherData-System die aktuell sichtbare Visualisierung als PNG-Datei speichern.

**EARS-Pattern:** Event-Driven

**Begründung:** Der Bildexport muss die direkte Weiterverwendung der Ergebnisse ermöglichen.

---

## FR_18: Fehlerbehandlung bei unzulässigem Zielpfad

**Quelle:** USER_STORY_08

**Requirement:** Wenn der Zielpfad für den PNG-Export nicht beschreibbar ist, dann muss das MyWeatherData-System den Export abbrechen und eine Fehlermeldung anzeigen.

**EARS-Pattern:** Unwanted Behavior

**Begründung:** Die Pfadprüfung muss Dateisystemfehler kontrolliert behandeln.
