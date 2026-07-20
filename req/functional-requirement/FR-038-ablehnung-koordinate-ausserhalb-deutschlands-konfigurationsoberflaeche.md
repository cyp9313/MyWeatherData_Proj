# FR-038: Ablehnung einer Koordinate außerhalb Deutschlands in der Konfigurationsoberfläche

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-010: Ort/Koordinate für die Wetterdatenabfrage auswählen

## Beschreibung
Wenn eine Koordinate außerhalb Deutschlands bestätigt wird, muss die Streamlit-Konfigurationsoberfläche die Eingabe ablehnen und einen Hinweis anzeigen, dass der Ort außerhalb des unterstützten Gebiets liegt.

## Eingabe / Vorbedingungen
- Eine syntaktisch gültige Koordinate wurde eingegeben oder ausgewählt, die außerhalb der Landesgrenzen Deutschlands liegt
- Die Eingabe wurde bestätigt

## Verarbeitungslogik / Ablauf
1. Koordinate entgegennehmen.
2. Prüfen, ob die Koordinate innerhalb der Landesgrenzen Deutschlands liegt.
3. Bei negativem Ergebnis: Eingabe ablehnen, Koordinate nicht als Ort für die Konfiguration übernehmen.
4. Hinweis anzeigen, dass der Ort außerhalb des unterstützten Gebiets liegt.

## Ausgabe / Ergebnis
Die Eingabe wird abgelehnt, ein Hinweistext wird angezeigt, die Koordinate wird nicht in die Konfiguration übernommen.

## Fehlerfälle / Randbedingungen
- Koordinate außerhalb Deutschlands: Ablehnung der Eingabe und Anzeige eines Hinweises auf das nicht unterstützte Gebiet

## Akzeptanzkriterien
- [ ] Bei Bestätigung einer Koordinate außerhalb Deutschlands wird die Eingabe abgelehnt
- [ ] Ein Hinweis wird angezeigt, dass der Ort außerhalb des unterstützten Gebiets liegt

## Abhängigkeiten
- Nutzt dieselbe Prüfgrundlage (Landesgrenzen Deutschlands) wie FR-002; die Ablehnung erfolgt hier bereits in der Konfigurationsoberfläche, vor Aufruf des Import-Clients

## Anmerkungen
Die Definition der Landesgrenzen Deutschlands als Prüfgrundlage ist konsistent mit FR-002 zu halten.
