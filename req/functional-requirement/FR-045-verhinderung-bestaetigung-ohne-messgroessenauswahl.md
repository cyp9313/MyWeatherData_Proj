# FR-045: Verhinderung der Bestätigung ohne Messgrößenauswahl

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-012: Messgrößen für die Wetterdatenabfrage auswählen

## Beschreibung
Wenn eine Bestätigung der Konfiguration ausgelöst wird, ohne dass mindestens eine Messgröße ausgewählt wurde, muss die Streamlit-Konfigurationsoberfläche die Bestätigung verhindern und einen Hinweis anzeigen, dass mindestens eine Messgröße erforderlich ist.

## Eingabe / Vorbedingungen
- Keine Messgröße wurde ausgewählt
- Die Bestätigung der Konfiguration wurde ausgelöst

## Verarbeitungslogik / Ablauf
1. Auslösung der Bestätigung entgegennehmen.
2. Prüfen, ob mindestens eine Messgröße ausgewählt wurde.
3. Bei negativem Ergebnis: Bestätigung verhindern.
4. Hinweis anzeigen, dass mindestens eine Messgröße erforderlich ist.

## Ausgabe / Ergebnis
Die Bestätigung wird verhindert, ein Hinweistext wird angezeigt.

## Fehlerfälle / Randbedingungen
- Bestätigungsversuch ohne Messgrößenauswahl: Verhinderung der Bestätigung und Anzeige eines Hinweises auf die erforderliche Messgrößenauswahl

## Akzeptanzkriterien
- [ ] Bei einem Bestätigungsversuch ohne ausgewählte Messgröße wird die Bestätigung verhindert
- [ ] Ein Hinweis wird angezeigt, dass mindestens eine Messgröße erforderlich ist

## Abhängigkeiten
- Wirkt als Vorbedingung für US-013 (Konfiguration bestätigen und Datenabruf auslösen)

## Anmerkungen
Keine.
