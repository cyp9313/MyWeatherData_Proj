# FR-048: Verhinderung eines zweiten, parallelen Datenabrufs bei laufendem Vorgang

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-013: Konfiguration bestätigen und Datenabruf auslösen

## Beschreibung
Solange ein Datenabruf für eine zuvor bestätigte Konfiguration läuft, wenn diese Konfiguration erneut bestätigt wird, muss die Streamlit-Konfigurationsoberfläche die Auslösung eines zweiten, parallelen Datenabrufs verhindern und einen Hinweis auf den laufenden Vorgang anzeigen.

## Eingabe / Vorbedingungen
- Ein Datenabruf für eine zuvor bestätigte Konfiguration läuft noch (siehe FR-046)
- Dieselbe Konfiguration wird erneut bestätigt

## Verarbeitungslogik / Ablauf
1. Laufenden Datenabruf und die zugehörige bestätigte Konfiguration erfassen.
2. Erneute Bestätigung entgegennehmen.
3. Prüfen, ob für die bestätigte Konfiguration bereits ein Datenabruf läuft.
4. Bei positivem Ergebnis: Auslösung eines zweiten, parallelen Datenabrufs verhindern.
5. Hinweis auf den laufenden Vorgang anzeigen.

## Ausgabe / Ergebnis
Es wird kein zweiter, paralleler Datenabruf ausgelöst; ein Hinweis auf den laufenden Vorgang wird angezeigt.

## Fehlerfälle / Randbedingungen
- Erneute Bestätigung derselben Konfiguration während ein Datenabruf noch läuft: Verhinderung eines zweiten Datenabrufs und Anzeige eines Hinweises auf den laufenden Vorgang

## Akzeptanzkriterien
- [ ] Bei erneuter Bestätigung einer Konfiguration, für die bereits ein Datenabruf läuft, wird kein zweiter, paralleler Datenabruf ausgelöst
- [ ] Bei diesem Bestätigungsversuch wird ein Hinweis auf den laufenden Vorgang angezeigt

## Abhängigkeiten
- Setzt einen bereits ausgelösten Datenabruf gemäß FR-046 voraus

## Anmerkungen
Keine.
