# FR-047: Verhinderung der Bestätigung bei unvollständiger Konfiguration

## Status
Review

## Priorität
Must have

## Zugehörige User Story
US-013: Konfiguration bestätigen und Datenabruf auslösen

## Beschreibung
Wenn versucht wird, eine unvollständige Konfiguration ohne Ort, ohne Zeitraum oder ohne ausgewählte Messgröße zu bestätigen, muss die Streamlit-Konfigurationsoberfläche die Bestätigung verhindern und alle zu diesem Zeitpunkt fehlenden Angaben benennen.

## Eingabe / Vorbedingungen
- Mindestens eine der Angaben Ort, Zeitraum oder Messgröße fehlt
- Die Bestätigung der Konfiguration wird ausgelöst

## Verarbeitungslogik / Ablauf
1. Bestätigungsversuch entgegennehmen.
2. Prüfen, ob Ort, Zeitraum und mindestens eine Messgröße vollständig vorliegen.
3. Bei negativem Ergebnis: Bestätigung verhindern.
4. Alle zu diesem Zeitpunkt fehlenden Angaben ermitteln.
5. Hinweis mit allen fehlenden Angaben anzeigen.

## Ausgabe / Ergebnis
Die Bestätigung wird verhindert, ein Hinweis mit allen fehlenden Angaben wird angezeigt.

## Fehlerfälle / Randbedingungen
- Fehlender Ort bei Bestätigungsversuch: siehe auch FR-040
- Fehlende Messgrößenauswahl bei Bestätigungsversuch: siehe auch FR-045
- Fehlender Zeitraum bei Bestätigungsversuch: wird durch dieses FR abgedeckt
- Mehrere fehlende Angaben gleichzeitig: alle fehlenden Angaben werden gemeinsam benannt

## Akzeptanzkriterien
- [ ] Bei einem Bestätigungsversuch mit fehlendem Ort, fehlendem Zeitraum oder fehlender Messgrößenauswahl wird die Bestätigung verhindert
- [ ] Alle zum Zeitpunkt der Bestätigung fehlenden Angaben werden benannt

## Abhängigkeiten
- Ergänzt FR-040 (fehlender Ort) und FR-045 (fehlende Messgrößenauswahl) um die kombinierte Prüfung aller drei Konfigurationsteile inklusive Zeitraum und die gleichzeitige Benennung aller fehlenden Angaben
- Wirkt als Vorbedingung für FR-046

## Anmerkungen
Keine.
