# FR-039: Ablehnung eines ungültigen Eingabeformats für die Koordinate

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-010: Ort/Koordinate für die Wetterdatenabfrage auswählen

## Beschreibung
Wenn eine Koordinateneingabe in einem ungültigen Format bestätigt wird, muss die Streamlit-Konfigurationsoberfläche die Eingabe ablehnen und einen Hinweis auf das erwartete Eingabeformat anzeigen.

## Eingabe / Vorbedingungen
- Eine Eingabe für die Koordinate wurde bestätigt, die nicht dem erwarteten Zahlenformat entspricht (z. B. Text statt Zahlenwert)

## Verarbeitungslogik / Ablauf
1. Eingabe entgegennehmen.
2. Eingabeformat auf Gültigkeit (Zahlenwert) prüfen.
3. Bei negativem Ergebnis: Eingabe ablehnen, Koordinate nicht als Ort für die Konfiguration übernehmen.
4. Hinweis auf das erwartete Eingabeformat anzeigen.

## Ausgabe / Ergebnis
Die Eingabe wird abgelehnt, ein Hinweistext zum erwarteten Eingabeformat wird angezeigt.

## Fehlerfälle / Randbedingungen
- Ungültiges Eingabeformat (z. B. Text statt Zahlenwert): Ablehnung der Eingabe und Anzeige eines Formathinweises

## Akzeptanzkriterien
- [ ] Bei Bestätigung einer Eingabe mit ungültigem Format wird die Eingabe abgelehnt
- [ ] Ein Hinweis auf das erwartete Eingabeformat wird angezeigt

## Abhängigkeiten
- Die Formatprüfung muss vor der Prüfung auf Landesgrenzen (FR-038) erfolgen

## Anmerkungen
Das konkrete erwartete Eingabeformat (z. B. Dezimalgrad) ist technische Designentscheidung und nicht Gegenstand dieses Functional Requirements.
