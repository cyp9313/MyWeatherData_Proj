---
name: "bdd_format"
description: "Formuliere und pruefe BDD-Akzeptanzkriterien fuer MyWeatherData im Gegeben/Wenn/Dann-Stil. Verwende diesen Skill fuer User Stories, Edge Cases und testbare Akzeptanzkriterien."
argument-hint: "User Story oder Akzeptanzkriterien"
applyTo: "doc/req/*.md"
---

# Skill: BDD-Akzeptanzkriterien

## Aufgabe

Formuliere Akzeptanzkriterien im BDD-Stil. Jedes Kriterium beschreibt einen beobachtbaren Systemzustand oder ein beobachtbares Ergebnis.

## Format

```markdown
- Gegeben <Ausgangszustand>, wenn <Aktion oder Ereignis>, dann <erwartetes Ergebnis>.
```

## Regeln

- Verwende Deutsch.
- Schreibe pro Kriterium genau einen Ausgangszustand, ein Ereignis und ein erwartetes Ergebnis.
- Nenne konkrete Randbedingungen, wenn sie relevant sind: Zeitraum, Koordinate, Wetterkategorie, Datenbestand, Zielpfad.
- Fuege mindestens ein negatives oder fehlerbezogenes Kriterium hinzu, wenn die Story Eingaben, Datenabruf, Export oder Dateisystemzugriff betrifft.
- Vermeide nicht beobachtbare Ergebnisse wie "funktioniert korrekt" oder "ist benutzerfreundlich".

## Typische MyWeatherData-Szenarien

- Gueltige Koordinate innerhalb Deutschlands.
- Ungueltige Koordinate ausserhalb Deutschlands.
- Zeitraum innerhalb oder ausserhalb 01.01.2015 bis 31.12.2025.
- DWD-Daten erfolgreich verfuegbar.
- DWD-Daten fehlen oder Download bricht ab.
- Export liefert Daten oder leeres Ergebnis.
- Visualisierung enthaelt Datenluecken.

## Review-Fragen

- Ist das erwartete Ergebnis messbar?
- Ist das Kriterium automatisiert oder manuell pruefbar?
- Deckt die Kriterienliste Happy Path und mindestens einen Edge Case ab?
