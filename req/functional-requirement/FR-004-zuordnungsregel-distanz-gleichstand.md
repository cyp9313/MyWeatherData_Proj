# FR-004: Zuordnungsregel bei Distanz-Gleichstand mehrerer Stationen

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-001: Nächstgelegene Wetterstation ermitteln

## Beschreibung
Wenn zwei oder mehr Stationen bei der Ermittlung der nächstgelegenen Station eine identische, minimale Entfernung zur angegebenen Koordinate aufweisen, muss der Import-Client die Station mit der niedrigsten Stations-ID als Ergebnis auswählen.

## Eingabe / Vorbedingungen
- Die Ermittlung der nächstgelegenen Station wurde ausgelöst
- Mindestens zwei Stationen weisen zur angegebenen Koordinate dieselbe minimale Entfernung auf

## Verarbeitungslogik / Ablauf
1. Entfernungen aller Stationen zur angegebenen Koordinate berechnen (siehe FR-001).
2. Prüfen, ob mehrere Stationen dieselbe minimale Entfernung aufweisen.
3. Bei Gleichstand: Stations-IDs der betroffenen Stationen vergleichen.
4. Station mit der niedrigsten Stations-ID als Ergebnis auswählen.

## Ausgabe / Ergebnis
Genau eine Station (mit der niedrigsten Stations-ID unter den Gleichstand-Kandidaten) wird als Ergebnis zurückgegeben, inklusive Stations-ID, Stationsname und Entfernung in km.

## Fehlerfälle / Randbedingungen
- Keine (Sonderfall ist bereits die Kernregel dieses Functional Requirements)

## Akzeptanzkriterien
- [ ] Bei identischer, minimaler Entfernung mehrerer Stationen wird genau eine Station als Ergebnis ausgewählt
- [ ] Die ausgewählte Station ist diejenige mit der niedrigsten Stations-ID unter den Gleichstand-Kandidaten

## Abhängigkeiten
- FR-001: Nächstgelegene Station für Koordinate innerhalb Deutschlands ermitteln (liefert die berechneten Entfernungen als Grundlage)

## Anmerkungen
Die Regel „aufsteigend nach Stations-ID" ist gemäß Anmerkung in US-001 ein Vorschlag und noch nicht final mit dem Team/PO abgestimmt. Vor einer Hochstufung auf Status `Approved` ist eine verbindliche Bestätigung dieser Regel durch den PO erforderlich.
