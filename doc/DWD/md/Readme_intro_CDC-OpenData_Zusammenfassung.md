# Zusammenfassung: CDC-OpenData area (DWD)

**Quelle:** `Readme_intro_CDC-OpenData.pdf`
**Stand:** August 2020

## Überblick

Das DWD Climate Data Center (CDC) bietet über die **CDC-OpenData area** freien Zugang zu Klimadaten. Es gelten die Nutzungsbedingungen des CDC. Die Daten sind in stündlicher, täglicher, monatlicher, jährlicher oder mehrjähriger Auflösung verfügbar (zusätzlich 1-Minuten-Niederschlags- sowie 10-Minuten-Messungen für Temperatur, Niederschlag, Wind und Sonnenschein).

Bereitgestellte Datenkategorien:
1. Beobachtete Parameter von DWD-Stationen
2. Abgeleitete Parameter an den Stationsstandorten
3. Rasterfelder für Deutschland
4. Regionale Mittelwerte für Deutschland und seine Bundesländer
5. Rasterfelder für Europa
6. Regionale Reanalyse
7. Globale Klimastationsdaten

### Datenqualität & Struktur
- Unterverzeichnisse **„recent"** (noch nicht vollständig qualitätsgeprüft) und **„historical"** (vollständige Qualitätskontrolle durchlaufen).
- Für 1- und 10-Minuten-Messungen zusätzlich ein **„now"**-Verzeichnis mit den aktuellsten Daten.
- Durch fortlaufende Qualitätskontrolle können archivierte Daten nachträglich korrigiert werden → Daten sind versioniert; die jeweils aktuellste Version liegt unter „historical".
- Zeitreihen können Inhomogenitäten enthalten (z. B. durch Stationsverlegung oder Gerätewechsel) – Metadaten sollten beachtet werden.
- Änderungen werden über ein Change-Log und einen CDC-Newsletter kommuniziert; es gibt Listen zu erwarteter zukünftiger Änderungen und registrierter Fehler.

## 1. Beobachtete Parameter an DWD-Stationen

- Historische und aktuelle meteorologische Parameter: Lufttemperatur, Bodentemperatur, Niederschlag, Feuchte, Druck, Windgeschwindigkeit/-richtung, Sichtweite, Solarstrahlung, Sonnenscheindauer, Bewölkung.
- Daten sind pro Station gezippt inkl. Metadaten (auf Deutsch).
- Auflösungen: 10-Minuten, stündlich, täglich, monatlich, mehrjährige Mittel (1961–1990, 1971–2000, 1981–2010).
- Ca. 400 aktive Klimastationen; Stationslisten im „help"-Verzeichnis.
- Historische „Terminwerte" (standardisierte Beobachtungszeiten) reichen teils weiter zurück als Stundenwerte; verfügbar u. a. für Luftdruck, Temperatur, Bewölkung, Dampfdruck/rel. Feuchte, Bodenzustand, Sichtweite, Wind.
- 81 Stationen liefern „Terminwerte" von 36 Parametern im traditionellen KL-Format.
- Stadtklima-Stationen liegen in stündlicher Auflösung vor.
- **Niederschlag**: dediziertes Netz mit ca. 2000 aktiven Stationen, Auflösungen 1-Minute, 10-Minuten, stündlich, täglich, monatlich.
- Schneehöhe und Wasseräquivalent: täglich.
- Beobachtete Wetterphänomene (Gewitter, Glatteis, Graupel, Hagel, Nebel, Frost, Sturm ≥6/8 Bft, Tau) – teils bis ins 19. Jahrhundert zurückreichend, täglich/monatlich/jährlich.
- Phänologische Daten (~1200 Stationen; z. B. Apfel, Birke, Schneeglöckchen, Weizen, Wein) von Sofort- und Jahresmeldern.
- Radiosondenaufstiege: hochauflodende (2–10 s, mit Ballonposition) und niedrigauflösende Daten; monatliche Temperaturprofile von 12 Radiosondenstationen (original und homogenisiert).

## 2. Abgeleitete Parameter an Stationsstandorten

- Agrarmeteorologische Modelle liefern Bodenparameter: potenzielle/reale Verdunstung (Gras, sandiger Lehm), Bodenfeuchte, Bodentemperatur (5/10/20/50/100 cm Tiefe), maximale Frosteindringtiefe.
- Auflösung: täglich, monatlich, mehrjährig; ca. 320 Stationsstandorte, Zeitreihen ab 1991.
- Technische Parameter: Heiz- und Kühlgradtage.

## 3. Rasterfelder für Deutschland

- **Niederschlagsraster**:
  - Laufend aktualisiert: RADOLAN (Radar+Stationen, stündlich/täglich), REGNIE (nur Stationen, täglich/monatlich/mehrjährig), sowie monatliche/halbjährliche/jährliche/mehrjährige Raster (ab 1881).
  - Reprozessiert: RADKLIM Version 2017.002 (Stundensummen ab 2001; 5-Minuten-Summen ab 2001).
- KOSTRA-DWD: Starkregenstatistik mit Wiederkehrperioden.
- Agrarmeteorologische Bodenparameter (Feuchte, Temperatur 5 cm, Verdunstung): täglich/monatlich/mehrjährig.
- Lufttemperatur (Mittel/Max/Min), Sonnenscheindauer, Dürreindex, Schnee-/Frosttage, Schwellenwertüberschreitungen: monatlich/jährlich/mehrjährig.
- Solarstrahlung (1×1 km): Global-, Diffus- und Direktstrahlung (monatlich/jährlich/mehrjährig), aus Satelliten- und Bodenmessdaten.
- Windenergieparameter: mehrjährige Mittel (1×1 km und 200×200 m).
- Projekt **QuWind100**: hochauflösende Windklimatologie (100×100 m) für 1981–2010, Höhen 100–200 m.
- Projekt **TRY** (Testreferenzjahre, 1995–2012): monatliche/tägliche/stündliche Raster (1×1 km) für Temperatur, Feuchte, Druck, Taupunkt, Wasserdampfgehalt, Bewölkung, Windrichtung/-geschwindigkeit, Strahlung.
- Phänologische Jahresraster für ca. 50 Phasen, inkl. Vegetationsbeginn/-ende.

## 4. Regionale Mittelwerte für Deutschland und Bundesländer

- Monatliche, saisonale und jährliche Mittel (Temperatur, Niederschlag, Sonnenscheindauer), abgeleitet aus den Rasterfeldern.
- Klimatologische Indizes als Jahresmittel: Tage mit Niederschlag ≥10 mm / ≥20 mm, heiße Tage (Tmax ≥30 °C), Sommertage (Tmin ≥25 °C), Frosttage (Tmin <0 °C), Eistage (Tmax <0 °C).

## 5. Rasterfelder für Europa

- 2001–2010: 5×5 km Raster, monatlich/täglich, für Lufttemperatur (Mittel/Max/Min, 2 m) und Windgeschwindigkeit (10 m).
- Monatliche Bewölkung aus Satellitendaten.

## 6. Regionale Reanalyse

- **COSMO-REA6**: stündliche Felder für Europa, 1995–2016, 6×6 km Auflösung, Format DWD grib1 (rotierte Koordinaten).
- Parameter: Druck (reduziert/nicht reduziert), Niederschlag, Temperatur (Min/Max/Mittel), relative/spezifische Feuchte, Windkomponenten U/V, Windböen, Strahlung (diffus/direkt), Grenzschichthöhe, integrierter Wasserdampf, Bewölkung – je nach Parameter auf den untersten 6 Modelllevels und/oder in 10 m (Wind) bzw. 2 m (Temperatur) Höhe.

## 7. Globale Klimastationsdaten

- Historische und aktuelle Monatsdaten aus CLIMAT-Meldungen (qualitätsgeprüft): Lufttemperatur (Mittel/Max/Min), Niederschlag, Anzahl Niederschlagstage, Sonnenscheindauer, Druck, Dampfdruck, sowie abgeleitete mehrjährige Mittel.
- Zusätzlich vorliegend: geprüfte Monatsdateien der CLIMAT-Meldungen (Monat/Jahr/Format) mit weiteren Parametern.