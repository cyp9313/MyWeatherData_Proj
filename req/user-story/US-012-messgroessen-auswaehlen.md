# US-012: Messgrößen für die Wetterdatenabfrage auswählen

## Status
Review

## Priorität
Must have

## Zugehöriges Epic
EPIC-003: User Interface zur Konfiguration von Ort, Zeitraum und Daten

## User Story
Als **Nutzer:in der App**
möchte ich **eine oder mehrere Messgrößen (Lufttemperatur, Niederschlag, Wind, Sonneneinstrahlung) in der Konfigurationsoberfläche auswählen können**,
damit **ich nur die für mich relevanten Wetterdaten abrufe und angezeigt bekomme**.

## Beschreibung / Kontext
Die Auswahl der Messgrößen ist Teil der Konfiguration und bestimmt, welche der vier unterstützten Datenkategorien (siehe EPIC-001) beim Datenabruf berücksichtigt werden.

## Akzeptanzkriterien
Format: Gegeben / Wenn / Dann

1. **Gegeben** genau eine Messgröße wird ausgewählt
   **Wenn** die Auswahl bestätigt wird
   **Dann** wird diese Messgröße als Teil der Konfiguration übernommen

2. **Gegeben** mehrere Messgrößen werden ausgewählt
   **Wenn** die Auswahl bestätigt wird
   **Dann** werden alle ausgewählten Messgrößen als Teil der Konfiguration übernommen

3. **Gegeben** alle vier verfügbaren Messgrößen werden ausgewählt
   **Wenn** die Auswahl bestätigt wird
   **Dann** werden alle vier Messgrößen als Teil der Konfiguration übernommen

4. **Gegeben** keine Messgröße wurde ausgewählt
   **Wenn** die Konfiguration ohne Messgrößenauswahl bestätigt werden soll
   **Dann** wird die Bestätigung verhindert und ein Hinweis angezeigt, dass mindestens eine Messgröße erforderlich ist

## Zugehörige Functional Requirements
- [ ] FR-044: Übernahme ausgewählter Messgrößen in die Konfiguration
- [ ] FR-045: Verhinderung der Bestätigung ohne Messgrößenauswahl

## Abhängigkeiten
- Liefert die ausgewählten Messgrößen als Eingangsgröße für US-013 (Konfiguration bestätigen und Datenabruf auslösen)

## Anmerkungen
Keine.
