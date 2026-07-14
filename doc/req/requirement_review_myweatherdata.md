# Requirement Review - MyWeatherData

## Zusammenfassung

Das Requirement-Set ist strukturiert und in weiten Teilen konsistent. Die Grund-Traceability von Epic zu User Story zu Functional Requirement ist vorhanden. Wesentliche Risiken bestehen bei Vollstaendigkeit der Traceability auf Story-Ebene sowie bei Testbarkeit durch fehlende normative Referenzen.

## Findings

| Prioritaet | Fundstelle | Problem | Auswirkung | Empfehlung |
|---|---|---|---|---|
| P1 | doc/req/user_story_myweatherdata.md (USER_STORY_04), doc/req/functional_requirement_myweatherdata.md (FR_12, FR_13) | CSV- und JSON-Export verweisen auf "dokumentierte Pflichtfelder" bzw. "dokumentierte Struktur", ohne dass im Requirement-Satz ein referenziertes normatives Artefakt vorhanden ist. | Exporttests sind nicht eindeutig spezifizierbar; erhoehtes Risiko fuer uneinheitliche Implementierung und Abnahmeprobleme. | Verbindliches Exportschema (CSV-Felder, JSON-Struktur, Pflicht/Optional) als versioniertes Artefakt referenzieren und in FR_12/FR_13 eindeutig verlinken. |
| P1 | doc/req/user_story_myweatherdata.md (USER_STORY_05, AK1 und AK2), doc/req/functional_requirement_myweatherdata.md (FR_15, FR_16) | USER_STORY_05 fordert Validierung von Deutschlandbezug und Projektzeitraumgrenzen im UI; FR_15/FR_16 decken nur Pflichtfelder und Datumsreihenfolge ab, nicht explizit Deutschlandgrenze und Zeitraumgrenzen 01.01.2015-31.12.2025 beim UI-Prozessstart. | Direkte Story-zu-FR-Traceability ist unvollstaendig; Risiko, dass UI-seitige Grenzvalidierung uneinheitlich oder spaet erfolgt. | Story-zu-FR-Abdeckung schliessen, indem die fehlenden UI-Validierungsregeln explizit in FR-Traceability aufgenommen werden. |
| P2 | doc/req/epic_myweatherdata.md (EPIC_03 Akzeptanzkriterium Standort), doc/req/user_story_myweatherdata.md (USER_STORY_05) | EPIC_03 akzeptiert Koordinaten oder aufgeloesten Standort; USER_STORY_05 beschreibt nur Koordinateneingabe, kein expliziter Scope fuer Standortaufloesung. | Potenzieller Scope-Konflikt zwischen Epic und Story-Backlog; Risiko fuer spaete Nachforderungen. | Verbindlich festlegen, ob Standortaufloesung Pflichtbestandteil oder explizit out of scope ist, und dies konsistent in Epic/Story spiegeln. |
| P2 | doc/req/user_story_myweatherdata.md (USER_STORY_06, AK2 und AK4), doc/req/functional_requirement_myweatherdata.md (FR_17, FR_18) | USER_STORY_06 fordert Status "abgeschlossen mit Ergebnisinformation" sowie Reset des alten Fehlerstatus bei Neustart; FRs decken nur "laufend" und "Fehler" ab. | UI-Statusautomat ist unvollstaendig spezifiziert; erhoehtes Regressionsrisiko in Endzustand und Wiederanlauf. | Traceability auf vollstaendigen Statuslebenszyklus erweitern (laufend, abgeschlossen, Fehler, Reset bei Neustart). |
| P2 | doc/req/user_story_myweatherdata.md (USER_STORY_08, AK4), doc/req/functional_requirement_myweatherdata.md (FR_24) | Story fordert Nutzbarkeit der Anwendung nach technischem Exportfehler; FR_24 fordert nur Fehlermeldung, nicht den Systemzustand danach. | Fehlerrobustheit ist nicht vollstaendig testbar; Gefahr von verdeckten Blockadezustaenden nach Exportfehlern. | Systemverhalten nach Exportfehler explizit spezifizieren und mit FR-Traceability absichern. |
| P3 | doc/req/functional_requirement_myweatherdata.md (FR_02) | Bei Distanzgleichstand zwischen Stationen ist keine deterministische Tie-Break-Regel festgelegt. | Nicht-deterministisches Verhalten in Grenzfaellen; instabile Testergebnisse moeglich. | Deterministische Gleichstandsregel fachlich festlegen (z. B. stabile Stations-ID-Reihenfolge). |

## Traceability-Matrix

| Epic | User Story | Functional Requirements | Bewertung |
|---|---|---|---|
| EPIC_01 | USER_STORY_01 | FR_01, FR_02, FR_03 | Vollstaendig, mit P3-Detail zum Tie-Break in FR_02. |
| EPIC_01 | USER_STORY_02 | FR_04, FR_05, FR_06, FR_07 | Vollstaendig und konsistent zu Zeitraum/Kategorien/Abruffehlern. |
| EPIC_02 | USER_STORY_03 | FR_08, FR_09, FR_10 | Vollstaendig und testbar abgedeckt. |
| EPIC_02 | USER_STORY_04 | FR_11, FR_12, FR_13, FR_14 | Inhaltlich abgedeckt, aber P1-Testbarkeitsluecke wegen fehlendem Exportschema. |
| EPIC_03 | USER_STORY_05 | FR_15, FR_16 | Teilabdeckung; P1-Luecke bei Deutschland- und Zeitraumgrenzen im UI-Kontext. |
| EPIC_03 | USER_STORY_06 | FR_17, FR_18 | Teilabdeckung; P2-Luecken bei Abschlussstatus und Fehlerstatus-Reset. |
| EPIC_04 | USER_STORY_07 | FR_19, FR_20, FR_21 | Weitgehend abgedeckt; Leerdatenfall klar spezifiziert. |
| EPIC_04 | USER_STORY_08 | FR_22, FR_23, FR_24 | Teilabdeckung; P2-Luecke bei geforderter Nutzbarkeit nach Exportfehler. |

## Offene Fragen

- Wo ist das normative Exportschema fuer CSV und JSON verbindlich versioniert?
- Ist Standortaufloesung aus Ortsname in EPIC_03 verpflichtend oder optional?
- Soll die UI-Validierung der Zeitraumgrenzen bereits vor Prozessstart zwingend sein oder reicht nachgelagerte Validierung im Abruf?
- Welche deterministische Regel gilt bei gleicher Distanz mehrerer DWD-Stationen?

## Empfehlung fuer naechsten Schritt

1. P1-Themen zuerst schliessen: Exportschema normativ referenzieren und Story-zu-FR-Luecke in USER_STORY_05 beheben.
2. Danach P2-Themen im UI-Status- und Fehlerverhalten konsistent durchgaengig absichern.
3. P3-Determinismus fuer Stationsgleichstand nachziehen und entsprechende Testfaelle ergaenzen.
