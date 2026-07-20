# FR-037: Übernahme einer gültigen Koordinate innerhalb Deutschlands

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-010: Ort/Koordinate für die Wetterdatenabfrage auswählen

## Beschreibung
Wenn eine gültige Koordinate innerhalb Deutschlands bestätigt wird, muss die Streamlit-Konfigurationsoberfläche die Koordinate als Ort für die Konfiguration übernehmen und dem Nutzer zur Kontrolle anzeigen.

## Eingabe / Vorbedingungen
- Eine syntaktisch gültige Koordinate (Zahlenwert) innerhalb der Landesgrenzen Deutschlands wurde eingegeben oder ausgewählt
- Die Eingabe wurde bestätigt

## Verarbeitungslogik / Ablauf
1. Koordinate entgegennehmen.
2. Eingabeformat der Koordinate auf Gültigkeit prüfen.
3. Prüfen, ob die Koordinate innerhalb der Landesgrenzen Deutschlands liegt.
4. Bei positivem Ergebnis: Koordinate als Ort für die Konfiguration übernehmen.
5. Übernommene Koordinate dem Nutzer zur Kontrolle anzeigen.

## Ausgabe / Ergebnis
Die bestätigte Koordinate ist als Ort Teil der Konfiguration und wird dem Nutzer zur Kontrolle angezeigt.

## Fehlerfälle / Randbedingungen
- Ablehnungsfälle (Koordinate außerhalb Deutschlands, ungültiges Format, fehlende Ortsangabe) sind in FR-038, FR-039 und FR-040 geregelt.

## Akzeptanzkriterien
- [ ] Bei Bestätigung einer gültigen Koordinate innerhalb Deutschlands wird diese als Ort für die Konfiguration übernommen
- [ ] Die übernommene Koordinate wird dem Nutzer zur Kontrolle angezeigt

## Abhängigkeiten
- Liefert die Koordinate als Eingangsgröße für FR-001 (nächstgelegene Wetterstation ermitteln)
- Vorbedingung für die Bestätigung der Konfiguration (US-013)

## Anmerkungen
Konkrete Eingabemethode (Texteingabe von Koordinaten, Kartenauswahl, Adresssuche) ist technische Designentscheidung und nicht Gegenstand dieses Functional Requirements.
