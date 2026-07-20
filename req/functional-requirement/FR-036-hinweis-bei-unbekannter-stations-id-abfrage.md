# FR-036: Hinweis bei Abfrage mit unbekannter Stations-ID

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-009: Gespeicherte Wetterdaten nach Station, Zeitraum und Messgröße abfragen

## Beschreibung
Wenn eine Abfrage mit einer Stations-ID ausgeführt wird, die in der lokalen Datenbank nicht existiert, muss die SQLite-Datenbank einen entsprechenden Hinweis zurückgeben, statt fehlerhafter Daten oder eines Absturzes.

## Eingabe / Vorbedingungen
- Eine Abfrage mit einer Stations-ID, einem Zeitraum und optional einer Messgröße liegt vor
- Die angefragte Stations-ID ist in der SQLite-Datenbank nicht vorhanden

## Verarbeitungslogik / Ablauf
1. Abfrage anhand der angegebenen Stations-ID ausführen.
2. Prüfen, ob die Stations-ID in der SQLite-Datenbank existiert.
3. Falls die Stations-ID nicht existiert, einen entsprechenden Hinweis erzeugen und zurückgeben.
4. Verarbeitung ohne Absturz oder Rückgabe fehlerhafter Daten fortsetzen.

## Ausgabe / Ergebnis
Ein Hinweis, dass die angefragte Stations-ID nicht existiert, wird zurückgegeben; es werden keine fehlerhaften Daten geliefert und die App stürzt nicht ab.

## Fehlerfälle / Randbedingungen
- Angefragte Stations-ID existiert nicht in der lokalen Datenbank: entsprechenden Hinweis zurückgeben statt fehlerhafter Daten oder Absturz

## Akzeptanzkriterien
- [ ] Bei einer Abfrage mit nicht existierender Stations-ID wird ein entsprechender Hinweis zurückgegeben
- [ ] Es werden keine fehlerhaften Daten zurückgegeben
- [ ] Die App stürzt in diesem Fall nicht ab

## Abhängigkeiten
- Ergänzt FR-033 und FR-034 um den Fall unbekannter Stations-ID

## Anmerkungen
Keine.
