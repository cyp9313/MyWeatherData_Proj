# BDD Best Practices – Gegeben/Wenn/Dann im Detail

Vertiefende Regeln und Beispiele zum Skill [SKILL.md](../SKILL.md). Die Beispiele sind bewusst domänenneutral gehalten und lassen sich auf beliebige User Stories (z.B. Datenimport, Konfiguration, Visualisierung) übertragen.

## Die drei Bausteine im Detail

### Gegeben – Ausgangssituation
- Beschreibt den **Zustand vor** der Aktion, nicht die Aktion selbst.
- So minimal wie möglich: nur Vorbedingungen nennen, die für das Ergebnis relevant sind.
- Mehrere Vorbedingungen mit **Und** verbinden, wenn sie logisch zusammengehören:
  ```
  Gegeben eine Eingabedatei "daten.csv" liegt lokal vor
  Und die Datei enthält Datensätze für den Zeitraum 01.01.2025–31.01.2025
  ```

### Wenn – Aktion/Ereignis
- Genau **eine** auslösende Aktion oder ein Ereignis pro Szenario.
- Aktiv und fachlich formuliert, nicht technisch/UI-lastig.
- Warnsignal: Mehrere "Wenn" oder ein "Wenn" mit "und dann..." → Hinweis auf mehrere Szenarien, die getrennt werden sollten.

### Dann – Erwartetes Ergebnis
- Objektiv und automatisiert überprüfbar (keine Interpretation nötig).
- Enthält nach Möglichkeit konkrete Werte/Zustände statt vager Aussagen.
- Mehrere Prüfungen nur mit "Und" verbinden, wenn sie zur selben Regel gehören.

## Deklarativ statt imperativ

**Schlecht (imperativ, UI-Klickpfad):**
```
Gegeben der Nutzer öffnet die App
Wenn der Nutzer auf "Import" klickt
Und der Nutzer die Datei im Dialog auswählt
Und der Nutzer auf "OK" klickt
Dann eine Erfolgsmeldung erscheint
```
Problem: Beschreibt UI-Mechanik statt fachliches Verhalten. Bricht bei jeder UI-Änderung.

**Gut (deklarativ, fachliches Verhalten):**
```
Gegeben eine gültige Eingabedatei "daten.csv" ist ausgewählt
Wenn der Import gestartet wird
Dann werden die Datensätze in der lokalen Datenbank gespeichert
Und die Anzahl importierter Datensätze wird angezeigt
```

## Ein Verhalten pro Szenario

**Schlecht (mehrere Regeln vermischt):**
```
Gegeben eine Importdatei liegt vor
Wenn der Import gestartet wird
Dann werden gültige Datensätze gespeichert
Und fehlerhafte Datensätze werden übersprungen und geloggt
Und bei leerer Datei erscheint eine Fehlermeldung
```
→ Testet 3 unabhängige Regeln in einem Szenario. Aufteilen in 3 Szenarien.

**Gut (aufgeteilt):**
```
Szenario 1 – Erfolgreicher Import
Gegeben eine Eingabedatei mit ausschließlich gültigen Datensätzen liegt vor
Wenn der Import gestartet wird
Dann werden alle Datensätze in der lokalen Datenbank gespeichert

Szenario 2 – Teilweise fehlerhafte Daten
Gegeben eine Eingabedatei enthält 2 gültige und 1 fehlerhaften Datensatz
Wenn der Import gestartet wird
Dann werden die 2 gültigen Datensätze gespeichert
Und der fehlerhafte Datensatz wird übersprungen und im Importprotokoll aufgeführt

Szenario 3 – Leere Datei
Gegeben eine ausgewählte Datei enthält keine Datensätze
Wenn der Import gestartet wird
Dann erscheint die Fehlermeldung "Keine Datensätze zum Import gefunden"
```

## Objektive Messbarkeit

- Vage: "Der Import ist schnell." → Nicht testbar.
- Konkret: "Der Import von 10.000 Datensätzen dauert unter 5 Sekunden." → Testbar.
- Vage: "Die Daten werden korrekt angezeigt." → Nicht testbar.
- Konkret: "Das Diagramm zeigt für jeden Tag im gewählten Zeitraum genau einen Datenpunkt je Messgröße." → Testbar.

## Abdeckung pro Story

Für jede User Story sollten die Akzeptanzkriterien in Summe mindestens abdecken:
1. **Happy Path** – Standardfall, alles läuft wie erwartet.
2. **Negativ-/Fehlerfall** – ungültige Eingabe, fehlende Datei, Verbindungsfehler o.ä.
3. **Randfälle** – leere Daten, Grenzwerte (z.B. Zeitraumgrenzen), doppelte Importe, fehlende Berechtigung.

## Häufige Anti-Patterns

| Anti-Pattern | Problem | Lösung |
|---|---|---|
| Ein Szenario mit vielen "And"-Ketten über mehrere Regeln | Schwer wartbar, unklarer Fehlschlag-Grund | In mehrere Szenarien mit je einer Regel aufteilen |
| "Wenn" beschreibt UI-Klicks statt Verhalten | Bricht bei UI-Änderungen, kein fachlicher Fokus | Deklarativ auf Fachebene formulieren |
| "Dann" mit vagen Adjektiven ("schnell", "benutzerfreundlich") | Nicht objektiv prüfbar | Konkrete Werte/Zustände angeben |
| Nur Happy Path vorhanden | Fehlerverhalten ungetestet/unspezifiziert | Mind. 1 Negativfall ergänzen |
| Gegeben enthält Aktionen statt Zustand | Vermischt Vorbedingung und Auslöser | Aktion ins "Wenn" verschieben |
