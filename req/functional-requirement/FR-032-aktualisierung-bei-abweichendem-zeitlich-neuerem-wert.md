# FR-032: Aktualisierung des gespeicherten Werts bei inhaltlich abweichendem, zeitlich neuerem Import für identische Kombination

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-008: Duplikate bei wiederholtem Import vermeiden

## Beschreibung
Wenn der Import-Client für eine Kombination aus Station, Messgröße und Zeitstempel, für die in der SQLite-Datenbank bereits ein Datensatz existiert, einen Messwert importiert, der vom gespeicherten Messwert abweicht, muss der Import-Client den gespeicherten Messwert durch den neu importierten Messwert ersetzen.

## Eingabe / Vorbedingungen
- Für eine Kombination aus Station, Messgröße und Zeitstempel existiert bereits ein Datensatz in der SQLite-Datenbank (siehe FR-029)
- Ein neuer Import liefert für dieselbe Kombination einen Messwert, der vom gespeicherten Messwert abweicht (z. B. nachträglich korrigierte DWD-Daten)

## Verarbeitungslogik / Ablauf
1. Beim Import prüfen, ob für die Kombination aus Station, Messgröße und Zeitstempel bereits ein Datensatz in der SQLite-Datenbank existiert (siehe FR-029).
2. Falls ein Datensatz existiert, den importierten Messwert mit dem gespeicherten Messwert vergleichen.
3. Bei Abweichung den gespeicherten Messwert durch den neu importierten Messwert ersetzen, ohne einen zusätzlichen Datensatz anzulegen.
4. Bei Übereinstimmung der Werte keine Änderung vornehmen (siehe FR-029).

## Ausgabe / Ergebnis
Nach dem Import enthält der Datensatz der betroffenen Kombination aus Station, Messgröße und Zeitstempel den zuletzt importierten Messwert; die Anzahl der Datensätze für diese Kombination bleibt unverändert.

## Fehlerfälle / Randbedingungen
- Der zeitliche Abstand zwischen zwei Importen derselben Kombination hat keinen Einfluss auf die Aktualisierung: Bei jedem Import mit abweichendem Messwert überschreibt der jeweils zuletzt importierte Messwert den zuvor gespeicherten Messwert.

## Akzeptanzkriterien
- [ ] Wird für eine Kombination aus Station, Messgröße und Zeitstempel ein Messwert importiert, der vom gespeicherten Messwert abweicht, wird der gespeicherte Messwert durch den neu importierten Wert ersetzt
- [ ] Nach der Aktualisierung existiert weiterhin genau ein Datensatz für diese Kombination

## Abhängigkeiten
- Baut auf FR-029 (keine zusätzlichen Datensätze bei identischer Kombination aus Station, Messgröße und Zeitstempel) auf
- Löst die in US-008 ursprünglich offene Frage zum Umgang mit inhaltlich abweichenden Werten (z. B. korrigierte DWD-Daten)

## Anmerkungen
Klarstellung durch den Auftraggeber: Bei einer Wertabweichung wird stets der zeitlich zuletzt importierte (neueste) Wert übernommen; eine Versionierung oder Historisierung abweichender Werte ist nicht vorgesehen.
