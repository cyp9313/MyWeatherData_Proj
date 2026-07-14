# User Stories - MyWeatherData

---

## USER_STORY_01: Naechstgelegene DWD-Station fuer Koordinaten bestimmen

**Epic:** EPIC_01

**User Story:** Als Fachanwender moechte ich eine Koordinate innerhalb Deutschlands eingeben, damit ich automatisch die naechstgelegene verfuegbare DWD-Wetterstation nutzen kann.

**Akzeptanzkriterien:**
- Gegeben eine gueltige Koordinate innerhalb Deutschlands, wenn ich die Stationssuche starte, dann wird die naechstgelegene verfuegbare DWD-Wetterstation angezeigt.
- Gegeben mehrere nahe Stationen, wenn die Distanzberechnung ausgefuehrt wird, dann wird die Station mit der kleinsten Distanz ausgewaehlt.
- Gegeben eine Koordinate ausserhalb Deutschlands, wenn ich die Stationssuche starte, dann wird eine fachlich klare Fehlermeldung angezeigt.
- Gegeben keine verfuegbare Station fuer die Koordinate, wenn die Suche abgeschlossen ist, dann wird ein Fehlerzustand mit Hinweis zur Anpassung der Eingabe angezeigt.

**INVEST-Pruefung:**
- Independent: Erfuellt - Die Story ist funktional auf die Stationszuordnung begrenzt.
- Negotiable: Erfuellt - Darstellung und Wortlaut der Rueckmeldung sind abstimmbar.
- Valuable: Erfuellt - Nutzer erhalten direkt die passende Datenquelle.
- Estimable: Erfuellt - Eingaben, Regeln und Ergebnis sind klar definiert.
- Small: Erfuellt - Der Umfang bleibt auf Suche und Rueckmeldung begrenzt.
- Testable: Erfuellt - Positive und negative Koordinatenfaelle sind eindeutig testbar.

**Hinweis:** Keine Markierung erforderlich.

---

## USER_STORY_02: Wetterdaten fuer gueltigen Zeitraum abrufen

**Epic:** EPIC_01

**User Story:** Als Fachanwender moechte ich Wetterdaten der Kategorien Lufttemperatur, Niederschlag, Wind und Sonneneinstrahlung abrufen, damit ich historische Messwerte im Projektzeitraum analysieren kann.

**Akzeptanzkriterien:**
- Gegeben eine gueltige Station und einen Zeitraum zwischen 01.01.2015 und 31.12.2025, wenn ich den Abruf starte, dann werden die ausgewaehlten Kategorien erfolgreich geladen.
- Gegeben einen Zeitraum ausserhalb 01.01.2015 bis 31.12.2025, wenn ich den Abruf starte, dann wird der Abruf mit einer eindeutigen Fehlermeldung abgelehnt.
- Gegeben eine Netzwerkunterbrechung beim Abruf, wenn der Download fehlschlaegt, dann wird ein Abruffehler angezeigt und protokolliert.
- Gegeben nur teilweise verfuegbare Kategoriedaten, wenn der Abruf abgeschlossen ist, dann werden fehlende Kategorien klar ausgewiesen.

**INVEST-Pruefung:**
- Independent: Erfuellt - Die Story fokussiert auf den Abrufprozess.
- Negotiable: Erfuellt - Protokolltiefe und Fehlermeldungsdetail sind abstimmbar.
- Valuable: Erfuellt - Liefert den zentralen Zugang zu historischen Wetterdaten.
- Estimable: Erfuellt - Klarer Rahmen durch Zeitraum und Kategorien.
- Small: Erfuellt - Scope bleibt auf Abruf und Rueckmeldung.
- Testable: Erfuellt - Erfolgsfall, Zeitraumgrenze und Netzwerkfehler sind reproduzierbar.

**Hinweis:** Keine Markierung erforderlich.

---

## USER_STORY_03: Importierte Messwerte ohne Duplikate speichern

**Epic:** EPIC_02

**User Story:** Als Systembetreiber moechte ich importierte Messwerte ohne Duplikate speichern, damit die lokale Datenbasis konsistent bleibt.

**Akzeptanzkriterien:**
- Gegeben neue Messwerte, wenn der Import gestartet wird, dann werden Datensaetze mit Station, Zeitstempel und Kategorie gespeichert.
- Gegeben bereits vorhandene Datensaetze mit identischer Station, Zeitstempel und Kategorie, wenn dieselben Daten erneut importiert werden, dann werden keine Duplikate angelegt.
- Gegeben ein Importlauf mit Duplikaten, wenn der Lauf beendet ist, dann wird die Anzahl der uebersprungenen Datensaetze protokolliert.
- Gegeben ein ungueltiges Datenformat im Import, wenn der Import gestartet wird, dann wird der fehlerhafte Datensatz verworfen und als Fehler protokolliert.

**INVEST-Pruefung:**
- Independent: Erfuellt - Die Story ist auf Persistenzlogik begrenzt.
- Negotiable: Erfuellt - Details der Protokollausgabe sind abstimmbar.
- Valuable: Erfuellt - Verhindert inkonsistente und redundante Daten.
- Estimable: Erfuellt - Regeln fuer Eindeutigkeit sind klar spezifiziert.
- Small: Erfuellt - Der Umfang umfasst nur Import und Deduplizierung.
- Testable: Erfuellt - Duplikat- und Formatfehlerfaelle sind klar testbar.

**Hinweis:** Keine Markierung erforderlich.

---

## USER_STORY_04: Gefilterte Wetterdaten als CSV oder JSON exportieren

**Epic:** EPIC_02

**User Story:** Als Datenkonsument moechte ich Wetterdaten gefiltert nach Standort, Zeitraum und Kategorie exportieren, damit ich sie in anderen Werkzeugen weiterverarbeiten kann.

**Akzeptanzkriterien:**
- Gegeben eine gueltige Filterauswahl fuer Standort, Zeitraum und Kategorie, wenn ich den Export starte, dann enthaelt die Exportdatei nur passende Datensaetze.
- Gegeben das Format CSV, wenn der Export erfolgreich ist, dann wird eine CSV-Datei mit den dokumentierten Pflichtfeldern erzeugt.
- Gegeben das Format JSON, wenn der Export erfolgreich ist, dann wird eine JSON-Datei gemaess dokumentierter Struktur erzeugt.
- Gegeben eine leere Ergebnismenge, wenn ich den Export starte, dann wird keine Datei erzeugt und eine klare Meldung angezeigt.

**INVEST-Pruefung:**
- Independent: Erfuellt - Export ist als eigenstaendiger Nutzen umsetzbar.
- Negotiable: Erfuellt - Dateinamenkonventionen und Feldreihenfolge sind abstimmbar.
- Valuable: Erfuellt - Daten werden ausserhalb des Systems nutzbar.
- Estimable: Erfuellt - Formate und Filter sind fachlich klar.
- Small: Erfuellt - Fokus liegt auf einem klaren Exportziel.
- Testable: Erfuellt - Dateiinhalte und Fehlfall leeres Ergebnis sind messbar pruefbar.

**Hinweis:** Keine Markierung erforderlich.

---

## USER_STORY_05: Suchparameter im UI erfassen und validieren

**Epic:** EPIC_03

**User Story:** Als Fachanwender moechte ich Standort, Zeitraum und Wetterkategorien im UI erfassen, damit ich den Datenprozess ohne technische Vorarbeit starten kann.

**Akzeptanzkriterien:**
- Gegeben ein geoeffnetes UI, wenn ich eine Koordinate innerhalb Deutschlands eingebe, dann wird die Eingabe als gueltig akzeptiert.
- Gegeben ein Start- und Enddatum innerhalb 01.01.2015 bis 31.12.2025, wenn ich die Eingabe bestaetige, dann wird der Zeitraum als gueltig gespeichert.
- Gegeben fehlende Pflichtfelder, wenn ich den Prozessstart ausloese, dann wird der Start blockiert und die fehlenden Felder werden klar markiert.
- Gegeben ein Enddatum vor dem Startdatum, wenn ich den Prozessstart ausloese, dann wird eine konkrete Validierungsmeldung angezeigt.

**INVEST-Pruefung:**
- Independent: Erfuellt - Die Story betrifft die Eingabelogik des UI.
- Negotiable: Erfuellt - Layout und Meldungstexte sind abstimmbar.
- Valuable: Erfuellt - Reduziert Fehlbedienung vor dem Prozessstart.
- Estimable: Erfuellt - Gueltigkeitsregeln sind klar und begrenzt.
- Small: Erfuellt - Scope bleibt auf Erfassung und Validierung.
- Testable: Erfuellt - Pflichtfelder und Datumsgrenzen sind eindeutig testbar.

**Hinweis:** Keine Markierung erforderlich.

---

## USER_STORY_06: Prozessstatus im UI transparent anzeigen

**Epic:** EPIC_03

**User Story:** Als Fachanwender moechte ich den Status des laufenden Prozesses sehen, damit ich den Fortschritt und Fehlerursachen nachvollziehen kann.

**Akzeptanzkriterien:**
- Gegeben ein gestarteter Prozess, wenn Daten abgerufen und gespeichert werden, dann zeigt das UI den Status laufend.
- Gegeben ein erfolgreich beendeter Prozess, wenn der Ablauf abgeschlossen ist, dann zeigt das UI den Status abgeschlossen mit Ergebnisinformation.
- Gegeben ein Fehler in Abruf oder Speicherung, wenn der Prozess abbricht, dann zeigt das UI den Status Fehler mit Zuordnung zum fehlerhaften Schritt.
- Gegeben eine erneute Ausfuehrung nach einem Fehler, wenn ich den Prozess neu starte, dann wird der vorherige Fehlerstatus nicht als aktueller Lauf angezeigt.

**INVEST-Pruefung:**
- Independent: Erfuellt - Die Story fokussiert auf Rueckmeldelogik im UI.
- Negotiable: Erfuellt - Granularitaet der Statusinfos ist abstimmbar.
- Valuable: Erfuellt - Nutzer erhalten Transparenz ueber Prozesszustand.
- Estimable: Erfuellt - Statuszustaende sind klar abgrenzbar.
- Small: Erfuellt - Scope bleibt auf Status und Fehlerkommunikation.
- Testable: Erfuellt - Statuswechsel sind deterministisch pruefbar.

**Hinweis:** Keine Markierung erforderlich.

---

## USER_STORY_07: Zeitreihen pro Wetterkategorie analysieren

**Epic:** EPIC_04

**User Story:** Als Datenanalyst moechte ich Wetterdaten als Zeitreihen pro Kategorie visualisieren, damit ich Trends und Ausreisser im Zeitraum erkennen kann.

**Akzeptanzkriterien:**
- Gegeben vorhandene Messwerte in der lokalen Datenbank, wenn ich eine Wetterkategorie waehle, dann wird ein passendes Zeitreihendiagramm angezeigt.
- Gegeben die Aufloesung taeglich, monatlich oder jaehrlich, wenn ich die Aufloesung aendere, dann wird die Darstellung korrekt aggregiert aktualisiert.
- Gegeben fehlende Messwerte im gewaehlten Zeitraum, wenn das Diagramm geladen wird, dann werden Datenluecken deutlich markiert.
- Gegeben keine Messwerte fuer die Auswahl, wenn ich die Visualisierung oeffne, dann wird ein Leerdatenzustand statt eines irrefuehrenden Diagramms angezeigt.

**INVEST-Pruefung:**
- Independent: Erfuellt - Die Story betrifft die Anzeige und Aggregation.
- Negotiable: Erfuellt - Konkreter Diagrammtyp ist abstimmbar.
- Valuable: Erfuellt - Ermoeglicht datengetriebene Auswertung.
- Estimable: Erfuellt - Eingaben und erwartete Darstellungen sind klar.
- Small: Erfuellt - Der Umfang bleibt auf Visualisierung mit Aggregation.
- Testable: Erfuellt - Anzeige, Luecken und Leerdatenzustand sind messbar testbar.

**Hinweis:** Keine Markierung erforderlich.

---

## USER_STORY_08: Aktuelle Visualisierung als PNG exportieren

**Epic:** EPIC_04

**User Story:** Als Fachanwender moechte ich die aktuell sichtbare Visualisierung als PNG exportieren, damit ich sie in Berichten und Praesentationen verwenden kann.

**Akzeptanzkriterien:**
- Gegeben eine sichtbare Visualisierung, wenn ich den PNG-Export starte, dann wird eine PNG-Datei im gewaehlten Zielpfad erzeugt.
- Gegeben ein nicht beschreibbarer Zielpfad, wenn ich den Export starte, dann wird keine Datei erzeugt und ein Fehler angezeigt.
- Gegeben eine geaenderte Filterauswahl vor dem Export, wenn ich den Export ausloese, dann entspricht die exportierte Grafik der aktuell sichtbaren Darstellung.
- Gegeben ein technischer Fehler im Exportprozess, wenn der Export fehlschlaegt, dann bleibt die Anwendung nutzbar und zeigt eine nachvollziehbare Fehlermeldung.

**INVEST-Pruefung:**
- Independent: Erfuellt - Die Story ist auf den Bildexport begrenzt.
- Negotiable: Erfuellt - Dateiname und Standardpfad sind abstimmbar.
- Valuable: Erfuellt - Ergebnisse werden direkt extern nutzbar.
- Estimable: Erfuellt - Eingaben und Ausgaben sind klar umrissen.
- Small: Erfuellt - Fokus liegt auf einem einzelnen Exportziel.
- Testable: Erfuellt - Dateierzeugung und Fehlerfall sind eindeutig pruefbar.

**Hinweis:** Keine Markierung erforderlich.
