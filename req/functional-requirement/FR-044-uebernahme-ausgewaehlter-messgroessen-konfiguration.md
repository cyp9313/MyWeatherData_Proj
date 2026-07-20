# FR-044: Übernahme ausgewählter Messgrößen in die Konfiguration

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-012: Messgrößen für die Wetterdatenabfrage auswählen

## Beschreibung
Wenn die Auswahl einer oder mehrerer Messgrößen (Lufttemperatur, Niederschlag, Wind, Sonneneinstrahlung) bestätigt wird, muss die Streamlit-Konfigurationsoberfläche alle ausgewählten Messgrößen als Teil der Konfiguration übernehmen.

## Eingabe / Vorbedingungen
- Mindestens eine der vier verfügbaren Messgrößen (Lufttemperatur, Niederschlag, Wind, Sonneneinstrahlung) wurde ausgewählt
- Die Auswahl wurde bestätigt

## Verarbeitungslogik / Ablauf
1. Auswahl der Messgrößen entgegennehmen.
2. Bestätigung der Auswahl entgegennehmen.
3. Prüfen, ob mindestens eine Messgröße ausgewählt ist.
4. Bei positivem Ergebnis: alle ausgewählten Messgrößen als Teil der Konfiguration übernehmen.

## Ausgabe / Ergebnis
Alle bei der Bestätigung ausgewählten Messgrößen (eine, mehrere oder alle vier) sind Teil der Konfiguration.

## Fehlerfälle / Randbedingungen
- Bestätigung ohne ausgewählte Messgröße ist in FR-045 geregelt.

## Akzeptanzkriterien
- [ ] Bei Bestätigung mit genau einer ausgewählten Messgröße wird diese als Teil der Konfiguration übernommen
- [ ] Bei Bestätigung mit mehreren ausgewählten Messgrößen werden alle ausgewählten Messgrößen als Teil der Konfiguration übernommen
- [ ] Bei Bestätigung mit allen vier verfügbaren Messgrößen werden alle vier Messgrößen als Teil der Konfiguration übernommen

## Abhängigkeiten
- Liefert die ausgewählten Messgrößen als Eingangsgröße für US-013 (Konfiguration bestätigen und Datenabruf auslösen)
- Vorbedingung für die Bestätigung der Konfiguration ist die Erfüllung von FR-045 (mindestens eine Messgröße ausgewählt)

## Anmerkungen
Keine.
