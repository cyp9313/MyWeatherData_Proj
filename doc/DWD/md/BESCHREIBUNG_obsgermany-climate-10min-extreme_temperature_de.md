
# Zusammenfassung: 10-minütige Stationsmessungen der Extremwerte der Temperaturen für Deutschland

**Quelle:** `BESCHREIBUNG_obsgermany-climate-10min-extreme_temperature_de.pdf`
**Version:** v24.03
**Ausgabedatum:** 2024-03-29
**Datensatz-ID:** `urn:x-wmo:md:de.dwd.cdc::obsgermany-climate-10min-extreme_temperature`

## Überblick

Der Datensatz enthält 10-minütige Messungen der Extremwerte der Temperatur (Maximum/Minimum) der DWD-Stationen sowie rechtlich und qualitativ gleichgestellter Partnernetze. Beim Download werden umfangreiche Stationsmetadaten mitgeliefert (Stationsverlegungen, Instrumentenwechsel, Wechsel der Bezugszeit, Änderungen in den Algorithmen).

- **Zeitliche Abdeckung:** 1989-03-07 bis heute
- **Räumliche Abdeckung:** Deutschland
- **Projektion:** WGS 84 (EPSG:4326)
- **Parameter:** Temperatur am Erdboden, Temperatur in 2 m
- **Einheiten:** °C
- **Statistische Verarbeitung:** Zeitreihe, 10-Minutenmaximum, 10-Minutenminimum

## Verzeichnisstruktur

Der Datensatz ist in vier Verzeichnisse aufgeteilt:

| Verzeichnis | Aktualisierung | Qualitätsprüfung |
|---|---|---|
| `historical/` | jährlich | abgeschlossen (versioniert) |
| `recent/` | täglich (letzte 500 Tage, rollierend) | noch nicht abgeschlossen |
| `now/` | stündlich (< 1h, Vortag rollierend) | noch nicht abgeschlossen |
| `meta_data/` | täglich | Metadaten zu Stationen, Instrumenten, Messvorschriften |

Zusätzliche Datei: `historical/zehn_min_tx_Beschreibung_Stationen.txt` mit aktueller geographischer Position und zeitlicher Abdeckung je Station.

## Datenformat

- **Namensschema (historical):** `*_{product_code}_{station_id}_{begin_date}_{end_date}_hist.zip`
- **Namensschema (now):** `*_{product_code}_{station_id}_now.zip`
- **Namensschema (recent):** `*_{product_code}_{station_id}_akt.zip`
- **Namensschema (meta_data):** `*_{product_code}_{station_id}.zip`
- **Zeitstempel:** vor Jahr 2000 in MEZ, ab Jahr 2000 in UTC (historical); now/recent immer UTC

Je Station wird ein ZIP-Archiv bereitgestellt. Die Metadaten-Archive enthalten:
- `Metadaten_Parameter*` – Zusatzinfos zu Parametern (Beginn, Ende, Einheit, Messvorschrift)
- `Metadaten_Geraete*` – Historie der Sensor-/Geberhöhen, Gerätetypen, Messverfahren
- `Metadaten_Stationsname*` – Historie der Stationsnamen und Betreiber
- `Metadaten_Geographie*` – Historie geografischer Metadaten (Länge, Breite, Stationshöhe)

## CSV-Format

**Dialekt:** Trennzeichen `;`, Zeilenende `\r\n`, mit Kopfzeile, Zitatzeichen `"`

| Spalte | Beschreibung | Einheit | Format |
|---|---|---|---|
| `MESS_DATUM` | Referenzdatum | – | `YYYYMMDDHH24` |
| `QN` | Qualitätsniveau | numerical code | `990` |
| `TX_10` | Maximum der Lufttemperatur in 2 m Höhe während der letzten 10 Minuten (Fehlwert = -999) | °C | `990.0` |
| `TX5_10` | Maximum der Lufttemperatur in 5 cm Höhe während der letzten 10 Minuten (Fehlwert = -999) | °C | `990.0` |
| `TN_10` | Minimum der Lufttemperatur in 2 m Höhe während der letzten 10 Minuten (Fehlwert = -999) | °C | `990.0` |
| `TN5_10` | Minimum der Lufttemperatur in 5 cm Höhe während der letzten 10 Minuten (Fehlwert = -999) | °C | `990.0` |

## Qualitätsinformation (QN)

- **QN = 1:** nur formale Prüfung
- **QN = 2:** nach individuellen Kriterien geprüft
- **QN = 3:** automatische Prüfung und Korrektur

Die Qualitätskontrolle folgt den in Kaspar et al. (2013) beschriebenen Routinen: automatisierte Tests (Vollständigkeit, zeitliche/räumliche Konsistenz, statistische Schwellwerte, Software QualiMet) sowie eine manuelle Qualitätskontrolle.

## Datenherkunft

Die Daten stammen aus den Stationsmessnetzen des DWD sowie rechtlich und qualitativ gleichgestellten Partnernetzen. Details zu Beobachtungs- und Messverfahren siehe VuB 3 Beobachterhandbuch (DWD, 2014a), VuB 3 Technikerhandbuch (DWD, 2014b) und VuB 2 Wetterschlüsselhandbuch (DWD, 2013).

## Unsicherheiten

- Stationen der Partnernetze können von WMO-Vorschriften abweichen.
- Langzeitstabilität kann beeinträchtigt sein durch: (1) Änderungen der Stationshöhe bei Verlegungen (besonders relevant für Wind und Temperatur), (2) Instrumentenwechsel, (3) unterschiedliche Qualitätsprüfverfahren (Behrendt et al., 2011), (4) Übermittlungs-/Softwarefehler und weitere Faktoren (Freydank, 2014).
- Relevante Metadaten dazu: `Metadaten_Geographie*`, `Metadaten_Geraete*`.

## Hinweise für Anwendungen

- Bei gemeinsamer Nutzung von `historical/`, `recent/` und `now/` auf zeitliche Überlappung und unterschiedliche Qualitätskontrolle achten.
- Daten mit QN=1 können markante Fehler enthalten – ggf. besser geprüfte Stunden-/Tageswerte statt 10-Minutenwerte verwenden.
- Für Trenduntersuchungen sind die stationsspezifischen Metadaten (`Metadaten_Parameter*`, `Metadaten_Geraete*`, `Metadaten_Geographie*`) unbedingt zu beachten.

## Kontakt

Deutscher Wetterdienst, CDC – Vertrieb Klima und Umwelt, Frankfurter Straße 135, 63067 Offenbach
Tel: +49 (0) 69 8062-4400, E-Mail: klima.vertrieb@dwd.de

## Copyright

Creative Commons BY 4.0 ("CC BY 4.0")

## Stand der Dokumentation

Gepflegt vom Deutschen Wetterdienst, Climate Data Center (CDC) – Betrieb; zuletzt editiert am 2024-05-06.
