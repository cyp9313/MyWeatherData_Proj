# FR-040: Verhinderung der Bestätigung ohne Ortsangabe

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-010: Ort/Koordinate für die Wetterdatenabfrage auswählen

## Beschreibung
Wenn eine Bestätigung der Konfiguration ausgelöst wird, ohne dass eine Koordinate eingegeben oder ausgewählt wurde, muss die Streamlit-Konfigurationsoberfläche die Bestätigung verhindern und einen Hinweis anzeigen, dass ein Ort erforderlich ist.

## Eingabe / Vorbedingungen
- Keine Koordinate wurde eingegeben oder ausgewählt
- Die Bestätigung der Konfiguration wurde ausgelöst

## Verarbeitungslogik / Ablauf
1. Auslösung der Bestätigung entgegennehmen.
2. Prüfen, ob eine Koordinate eingegeben oder ausgewählt wurde.
3. Bei negativem Ergebnis: Bestätigung verhindern.
4. Hinweis anzeigen, dass ein Ort erforderlich ist.

## Ausgabe / Ergebnis
Die Bestätigung wird verhindert, ein Hinweistext wird angezeigt.

## Fehlerfälle / Randbedingungen
- Bestätigungsversuch ohne Ortsangabe: Verhinderung der Bestätigung und Anzeige eines Hinweises auf die erforderliche Ortsangabe

## Akzeptanzkriterien
- [ ] Bei einem Bestätigungsversuch ohne eingegebene oder ausgewählte Koordinate wird die Bestätigung verhindert
- [ ] Ein Hinweis wird angezeigt, dass ein Ort erforderlich ist

## Abhängigkeiten
- Wirkt als Vorbedingung für US-013 (Konfiguration bestätigen und Datenabruf auslösen)

## Anmerkungen
Keine.
