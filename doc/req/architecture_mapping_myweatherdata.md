# Architektur-Mapping - MyWeatherData

## FR-Abdeckungsmatrix

| FR-ID | Kurzbeschreibung | Architektur-Baustein(e) | Diagramm(e) |
|---|---|---|---|
| FR_01 | Standortgrenze Deutschland pruefen | UI, Orchestrierungsservice | Kontext, Komponenten, Sequenz, Aktivitaet |
| FR_02 | Naechstgelegene Station waehlen | Stationszuordnung, DWD-Client | Komponenten, Sequenz, Aktivitaet |
| FR_03 | Fehler bei fehlender Station | UI-Status, Orchestrierungsservice | Sequenz, Aktivitaet, Zustand |
| FR_04 | Zeitraum begrenzen | UI-Validierung, Orchestrierungsservice | Komponenten, Sequenz, Aktivitaet |
| FR_05 | Vier Wetterkategorien verarbeiten | DWD-Client, Datenmodell | Komponenten, Sequenz |
| FR_06 | Abruffehler protokollieren | Logging, Orchestrierungsservice | Komponenten, Sequenz, Aktivitaet, Zustand |
| FR_07 | Fehlende Kategorien kennzeichnen | DWD-Client, Orchestrierungsservice, UI | Sequenz, Aktivitaet, Zustand |
| FR_08 | Eindeutige Persistenz (Station+Zeit+Kategorie) | Persistenzservice, SQLite | Komponenten, Sequenz |
| FR_09 | Uebersprungene Duplikate protokollieren | Persistenzservice, Logging | Komponenten, Sequenz, Aktivitaet |
| FR_10 | Ungueltige Importdatensaetze verwerfen | Persistenzservice, Logging | Komponenten, Sequenz, Aktivitaet |
| FR_11 | Filtertreuer Export | Exportservice, SQLite | Komponenten, Sequenz, Aktivitaet |
| FR_12 | CSV mit Pflichtfeldern erzeugen | Exportservice | Komponenten, Sequenz |
| FR_13 | JSON nach Struktur erzeugen | Exportservice | Komponenten, Sequenz |
| FR_14 | Leeren Export unterdruecken | Exportservice, UI-Status | Sequenz, Aktivitaet, Zustand |
| FR_15 | Pflichtfelder vor Prozessstart validieren | UI, Orchestrierungsservice | Komponenten, Sequenz, Aktivitaet |
| FR_16 | Enddatum vor Startdatum blockieren | UI-Validierung | Sequenz, Aktivitaet |
| FR_17 | Status "laufend" anzeigen | UI-Status, Orchestrierungsservice | Kontext, Sequenz, Zustand |
| FR_18 | Fehlerstatus mit Schrittzuordnung | UI-Status, Orchestrierungsservice | Sequenz, Aktivitaet, Zustand |
| FR_19 | Aggregation nach Aufloesung | Visualisierungsservice | Komponenten, Sequenz, Aktivitaet |
| FR_20 | Datenluecken kennzeichnen | Visualisierungsservice, UI | Sequenz, Aktivitaet, Zustand |
| FR_21 | Leerdatenzustand anzeigen | Visualisierungsservice, UI | Sequenz, Aktivitaet, Zustand |
| FR_22 | PNG der aktuellen Ansicht exportieren | Visualisierungsservice, PNG-Export | Komponenten, Sequenz, Aktivitaet |
| FR_23 | Exportabbruch bei unbeschreibbarem Pfad | PNG-Export, UI-Status | Sequenz, Aktivitaet, Zustand |
| FR_24 | Fehlermeldung bei technischem Exportfehler | PNG-Export, UI-Status | Sequenz, Aktivitaet, Zustand |

## Diagramm-Zuordnung

| Diagramm | Zweck | FR-Abdeckung |
|---|---|---|
| myweatherdata_context.puml | Systemkontext und Systemgrenzen | FR_01, FR_04, FR_17 |
| myweatherdata_components.puml | Interne Architekturbausteine und Schnittstellen | FR_01-FR_24 (strukturell) |
| myweatherdata_sequence_main_flow.puml | End-to-End-Interaktion von Validierung bis Export/Visualisierung | FR_01-FR_24 (flussbezogen) |
| myweatherdata_activity_flow.puml | Entscheidungs- und Fehlerpfade im Prozess | FR_01, FR_03-FR_07, FR_09-FR_11, FR_14-FR_16, FR_18-FR_24 |
| myweatherdata_state_process.puml | Prozessstatus und Zustandsuebergaenge | FR_17, FR_18, FR_21, FR_23, FR_24 |

## Validierung

- Abgedeckt: FR_01 bis FR_24 sind mindestens einem Architekturbaustein und einem Diagramm zugeordnet.
- Nicht abgedeckt: Keine FR ohne Diagrammzuordnung.

## Offene Punkte

- FR_19 definiert Aggregation (taeglich/monatlich/jaehrlich), aber keine expliziten Aggregationsregeln je Kategorie.
- FR_12 und FR_13 verweisen auf dokumentierte Pflichtfelder/Struktur; diese Feldlisten sind in den FRs nicht ausgefuehrt.
- FR_23 verlangt pruefbaren Zielpfad fuer PNG-Export, aber der Pfadauswahlmechanismus ist nicht spezifiziert.
