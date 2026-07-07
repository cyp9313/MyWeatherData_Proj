# User Stories – MyWeatherData

---

## USER_STORY_01: Nächstgelegene Wetterstation ermitteln

**Epic:** EPIC_01

**User Story:** Als Nutzer möchte ich eine geografische Koordinate eingeben, damit die Anwendung automatisch die nächstgelegene DWD-Wetterstation für meinen Standort auswählt.

**Akzeptanzkriterien:**
- Gegeben eine gültige Koordinate innerhalb Deutschlands, wenn ich die Stationssuche starte, dann wird die nächstgelegene aktive DWD-Station angezeigt.
- Gegeben mehrere nahegelegene Stationen, wenn die Distanz berechnet wird, dann wird die Station mit der kleinsten Haversine-Distanz ausgewählt.
- Gegeben eine ungültige Koordinate, wenn ich die Stationssuche starte, dann erhalte ich eine verständliche Fehlermeldung.
- Gegeben keine verfügbare Station in Reichweite, wenn die Suche abgeschlossen ist, dann wird der Zustand protokolliert und im UI angezeigt.

**INVEST-Prüfung:**
- Independent: Die Story ist unabhängig umsetzbar, da sie nur die Stationssuche betrifft.
- Negotiable: Details zur Distanzschwelle und Fehlerdarstellung sind abstimmbar.
- Valuable: Der Nutzer erhält ohne manuelle Recherche direkt die passende Station.
- Estimable: Aufwand ist klar abschätzbar durch definierte Such- und Distanzlogik.
- Small: Der Funktionsumfang ist auf Eingabevalidierung und Stationsauswahl begrenzt.
- Testable: Die Ergebnisse sind über Testkoordinaten und erwartete Stationen eindeutig prüfbar.

---

## USER_STORY_02: Wetterdaten vom DWD abrufen

**Epic:** EPIC_01

**User Story:** Als Nutzer möchte ich Wetterdaten für Temperatur, Niederschlag, Wind und Sonneneinstrahlung abrufen, damit ich historische Messwerte für meinen gewählten Zeitraum nutzen kann.

**Akzeptanzkriterien:**
- Gegeben eine gültige Station und Kategorieauswahl, wenn ich den Abruf starte, dann werden Datensätze für alle gewählten Wetterkategorien heruntergeladen.
- Gegeben ein Zeitraum außerhalb 01.01.2015 bis 31.12.2025, wenn ich den Abruf starte, dann wird der Abruf mit einer validierten Fehlermeldung abgelehnt.
- Gegeben eine temporäre Netzwerkstörung, wenn der Download fehlschlägt, dann wird der Fehler protokolliert und ein erneuter Versuch ermöglicht.
- Gegeben ein erfolgreicher Download, wenn das Parsing abgeschlossen ist, dann liegen strukturierte Datensätze mit Zeitstempel und Stationsbezug vor.

**INVEST-Prüfung:**
- Independent: Die Story kann ohne UI-Detailimplementierung als API-Funktion geliefert werden.
- Negotiable: Retry-Strategie und Protokolltiefe können angepasst werden.
- Valuable: Der Nutzer erhält die zentralen Wetterdaten in einem Schritt.
- Estimable: Der Umfang ist durch bekannte Datenquellen und Formate gut planbar.
- Small: Fokus liegt auf Abruf, Validierung und Rückgabeformat.
- Testable: Erfolgs- und Fehlerfälle sind mit Mock-Datenquellen reproduzierbar testbar.

---

## USER_STORY_03: Messwerte dedupliziert speichern

**Epic:** EPIC_02

**User Story:** Als Systembetreiber möchte ich importierte Wetterdaten ohne Duplikate speichern, damit die Datenbank konsistent bleibt und Abfragen korrekte Ergebnisse liefern.

**Akzeptanzkriterien:**
- Gegeben ein bereits importierter Datensatz, wenn derselbe Datensatz erneut importiert wird, dann wird kein doppelter Eintrag angelegt.
- Gegeben neue Messwerte, wenn der Import ausgeführt wird, dann werden nur nicht vorhandene Datensätze gespeichert.
- Gegeben eindeutige Schlüssel aus Station, Kategorie und Zeitstempel, wenn gespeichert wird, dann wird die Eindeutigkeit technisch erzwungen.
- Gegeben ein Importlauf mit Duplikaten, wenn der Lauf endet, dann enthält das Protokoll die Anzahl übersprungener Datensätze.

**INVEST-Prüfung:**
- Independent: Die Story betrifft primär Persistenzregeln und ist separat entwickelbar.
- Negotiable: Konkrete Schlüsseldefinition und Logging-Details sind verhandelbar.
- Valuable: Konsistente Daten verhindern Fehlinterpretationen in Export und Visualisierung.
- Estimable: Aufwand ist über Schemaanpassung und Importlogik gut abschätzbar.
- Small: Der Scope ist klar auf Deduplizierung im Importpfad begrenzt.
- Testable: Duplikatfälle lassen sich mit kontrollierten Importdaten eindeutig prüfen.

---

## USER_STORY_04: Gefilterten Datenexport durchführen

**Epic:** EPIC_02

**User Story:** Als Nutzer möchte ich gespeicherte Wetterdaten gefiltert nach Ort, Zeitraum und Kategorie exportieren, damit ich sie außerhalb der Anwendung weiterverwenden kann.

**Akzeptanzkriterien:**
- Gegeben ein gewählter Ort, Zeitraum und mindestens eine Kategorie, wenn ich den Export starte, dann enthält die Exportdatei nur passende Datensätze.
- Gegeben die Auswahl CSV, wenn der Export abgeschlossen ist, dann ist die Datei mit Kopfzeile und standardkonformen Trennzeichen erstellt.
- Gegeben die Auswahl JSON, wenn der Export abgeschlossen ist, dann entspricht die Struktur dem dokumentierten Export-Schema.
- Gegeben ein leeres Abfrageergebnis, wenn der Export gestartet wird, dann erhalte ich eine klare Meldung ohne leere Dateierzeugung.

**INVEST-Prüfung:**
- Independent: Die Story kann auf bestehenden Datenbankabfragen aufsetzen und ist eigenständig.
- Negotiable: Dateinamenkonventionen und Feldreihenfolge sind abstimmbar.
- Valuable: Exportierbare Daten erhöhen den praktischen Nutzen für Analyse und Berichte.
- Estimable: Aufwand ist über bekannte Ausgabeformate und Filterlogik kalkulierbar.
- Small: Der Umfang ist auf selektiven Export in zwei Formate fokussiert.
- Testable: Filterkriterien und Dateiinhalte sind automatisiert überprüfbar.

---

## USER_STORY_05: Suchparameter im UI konfigurieren

**Epic:** EPIC_03

**User Story:** Als Nutzer möchte ich Ort, Zeitraum und Wetterkategorien in einer Oberfläche eingeben, damit ich ohne Programmierkenntnisse den Datenabruf steuern kann.

**Akzeptanzkriterien:**
- Gegeben die geöffnete Anwendung, wenn ich Koordinaten oder einen Ortsnamen eingebe, dann wird die Eingabe validiert und für die Stationssuche übernommen.
- Gegeben eine Datumsauswahl, wenn ich Start- und Enddatum setze, dann akzeptiert das UI nur Werte zwischen 01.01.2015 und 31.12.2025.
- Gegeben die Kategorienauswahl, wenn ich Kategorien aktiviere oder deaktiviere, dann wird die Auswahl für den Abruf korrekt gespeichert.
- Gegeben unvollständige Pflichtangaben, wenn ich den Abruf starte, dann zeigt das UI konkrete Hinweise zur Korrektur.

**INVEST-Prüfung:**
- Independent: Die Story fokussiert auf Eingabelogik und kann separat geliefert werden.
- Negotiable: Layout und konkrete Validierungshinweise sind anpassbar.
- Valuable: Nutzer können das System ohne technische Hürden bedienen.
- Estimable: Aufwand ist durch klar definierte Eingabefelder gut einschätzbar.
- Small: Der Umfang bleibt auf Formular und Validierungsregeln begrenzt.
- Testable: Eingabe- und Validierungsverhalten ist mit UI-Tests prüfbar.

---

## USER_STORY_06: Abrufstatus im UI verfolgen

**Epic:** EPIC_03

**User Story:** Als Nutzer möchte ich den Status des Datenabrufs sehen, damit ich weiß, ob der Prozess läuft, erfolgreich war oder ein Fehler aufgetreten ist.

**Akzeptanzkriterien:**
- Gegeben ein gestarteter Abruf, wenn der Prozess aktiv ist, dann zeigt das UI den Status "laufend" mit Fortschrittsindikator.
- Gegeben ein erfolgreich abgeschlossener Abruf, wenn der Prozess endet, dann zeigt das UI den Status "abgeschlossen" mit Ergebnisübersicht.
- Gegeben ein technischer Fehler, wenn der Abruf abbricht, dann zeigt das UI den Status "Fehler" mit verständlicher Kurzbeschreibung.
- Gegeben mehrere aufeinanderfolgende Abrufe, wenn ich die Historie öffne, dann sind die letzten Statusmeldungen nachvollziehbar einsehbar.

**INVEST-Prüfung:**
- Independent: Die Story erweitert die Rückmeldungsschicht und ist modular umsetzbar.
- Negotiable: Tiefe der Fortschrittsanzeige und Historienlänge sind verhandelbar.
- Valuable: Transparenz über den Prozess reduziert Unsicherheit und Fehlbedienung.
- Estimable: Aufwand ist anhand klarer Statuszustände gut planbar.
- Small: Fokus liegt auf Anzeigezuständen und Rückmeldungen.
- Testable: Statusübergänge und Fehlerszenarien sind reproduzierbar testbar.

---

## USER_STORY_07: Interaktive Zeitreihen anzeigen

**Epic:** EPIC_04

**User Story:** Als Nutzer möchte ich Wetterdaten als interaktive Zeitreihen visualisieren, damit ich Trends und Ausreißer über den gewählten Zeitraum schnell erkenne.

**Akzeptanzkriterien:**
- Gegeben gespeicherte Messwerte, wenn ich eine Wetterkategorie auswähle, dann wird ein passendes Diagramm mit Zeitachse angezeigt.
- Gegeben ein großer Zeitraum, wenn ich in das Diagramm zoome oder verschiebe, dann aktualisiert sich die Darstellung ohne Datenverlust.
- Gegeben eine Änderung der Auflösung, wenn ich täglich, monatlich oder jährlich wähle, dann wird die Aggregation korrekt angewendet.
- Gegeben fehlende Messwerte in Teilzeiträumen, wenn das Diagramm gerendert wird, dann werden Lücken nachvollziehbar markiert.

**INVEST-Prüfung:**
- Independent: Die Story ist als eigenständige Visualisierungsfunktion lieferbar.
- Negotiable: Interaktionsumfang und Standarddiagrammtypen sind anpassbar.
- Valuable: Visualisierte Trends unterstützen schnelle Erkenntnisse aus den Daten.
- Estimable: Aufwand ist über Bibliotheksfunktionen und Aggregationslogik kalkulierbar.
- Small: Scope konzentriert sich auf Anzeige, Interaktion und Aggregationsumschaltung.
- Testable: Korrekte Darstellung ist mit Referenzdatensätzen und UI-Checks prüfbar.

---

## USER_STORY_08: Diagramme als PNG exportieren

**Epic:** EPIC_04

**User Story:** Als Nutzer möchte ich erzeugte Wetterdiagramme als PNG exportieren, damit ich Ergebnisse in Präsentationen und Berichten verwenden kann.

**Akzeptanzkriterien:**
- Gegeben ein gerendertes Diagramm, wenn ich den PNG-Export auslöse, dann wird eine PNG-Datei im gewählten Zielpfad gespeichert.
- Gegeben definierte Exportparameter, wenn ich den Export starte, dann werden Titel, Achsenbeschriftungen und Legenden im Bild übernommen.
- Gegeben ein nicht beschreibbarer Zielpfad, wenn ich den Export ausführe, dann erhalte ich eine klare Fehlermeldung ohne Anwendungsabsturz.
- Gegeben mehrere Wetterkategorien in separaten Ansichten, wenn ich jeweils exportiere, dann entspricht jede Datei der aktuell sichtbaren Darstellung.

**INVEST-Prüfung:**
- Independent: Die Story kann auf bestehender Visualisierung aufsetzen, ohne andere Features zu blockieren.
- Negotiable: Dateibenennung und Standardauflösung sind abstimmbar.
- Valuable: Exportierbare Visualisierungen sind direkt für externe Kommunikation nutzbar.
- Estimable: Aufwand ist über klaren Exportworkflow gut abschätzbar.
- Small: Der Umfang ist auf Exportfunktion und Fehlerbehandlung begrenzt.
- Testable: Dateierzeugung, Format und Inhalte sind automatisiert validierbar.
