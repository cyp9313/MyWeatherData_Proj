# EARS Best Practices – Pattern im Detail

Vertiefende Regeln und Beispiele zum Skill [SKILL.md](../SKILL.md). Die Beispiele sind bewusst domänenneutral bzw. an Automotive-/Luftfahrt-Klassikern orientiert und lassen sich auf beliebige Functional Requirements (z.B. Datenimport, Konfiguration, Visualisierung) übertragen.

## 1. Ubiquitous (Allgegenwärtig)

- Keine Vorbedingung, kein Trigger, kein Zustand – gilt uneingeschränkt, solange das System existiert/läuft.
- Typisch für: Kapazitäten, Grenzwerte, grundlegende Eigenschaften, Compliance-Vorgaben.
- Syntax: `Das [System] muss [Systemantwort].`
- Beispiele:
  - "Das Kameramodul muss einen Bildwinkel von 120 Grad abdecken."
  - "Das Exportmodul muss CSV-Dateien im UTF-8-Encoding erzeugen."

## 2. Event-Driven (Ereignisgesteuert)

- Reaktion **genau dann**, wenn ein definiertes Ereignis eintritt – vorher passiert nichts.
- Trigger muss ein konkretes, beobachtbares Ereignis sein (Nutzeraktion, Signal, Zeitpunkt).
- Syntax: `Wenn [Trigger], muss [System] [Systemantwort].`
- Beispiele:
  - "Wenn der Mute-Button gedrückt wird, muss das Infotainment-System alle Audioausgaben stummschalten."
  - "Wenn der Nutzer den Datenimport startet, muss das Importmodul die ausgewählte Datei einlesen."

## 3. State-Driven (Zustandsgesteuert)

- Verhalten ist an die **Dauer** eines Zustands gekoppelt, nicht an ein einzelnes Ereignis.
- Zustand muss klar begonnen und beendet werden können (eindeutige Ein-/Austrittsbedingung).
- Syntax: `Solange [Zustand], muss/darf [System] [Systemantwort].`
- Beispiele:
  - "Solange sich das Fahrzeug im Wartungsmodus befindet, darf das Motorsteuergerät keine OTA-Updates installieren."
  - "Solange kein Standort ausgewählt ist, darf die Konfigurationsoberfläche den Datenabruf nicht auslösen."

## 4. Unwanted Behavior (Unerwünschtes Verhalten)

- Deckt Fehlerfälle, Ausfälle, ungültige Eingaben, Grenzüberschreitungen ab – **immer mit Gegenmaßnahme**, nicht nur Feststellung des Fehlers.
- Sollte in der FR-Datei zusätzlich unter "Fehlerfälle / Randbedingungen" auftauchen, damit Fehlerbehandlung nicht nur in der Beschreibung "versteckt" ist.
- Syntax: `Wenn [Unerwünschtes Ereignis], dann muss [System] [Systemantwort].`
- Beispiele:
  - "Wenn die errechnete Fluggeschwindigkeit nicht verfügbar ist, muss das Kontrollsystem die modellierte Fluggeschwindigkeit nutzen."
  - "Wenn die DWD-Schnittstelle nicht erreichbar ist, muss das Importmodul eine Fehlermeldung anzeigen und den Import abbrechen."

## 5. Optional Feature (Optionale Funktion)

- Für Anforderungen, die nur gelten, wenn eine bestimmte Ausbaustufe/Hardware/Lizenz vorhanden ist.
- "Wo"-Bedingung beschreibt **Vorhandensein eines Features**, keinen Zustand und kein Ereignis (Abgrenzung zu State-Driven/Event-Driven).
- Syntax: `Wo [Feature vorhanden], muss das [System] [Systemantwort].`
- Beispiele:
  - "Wo ein Radarsensor verbaut ist, muss die Software den adaptiven Tempomaten aktivieren."
  - "Wo eine Premium-Lizenz aktiviert ist, muss die Anwendung den Export nach GeoJSON anbieten."

## 6. Complex (Kombination)

- Für Anforderungen, bei denen mehrere Bedingungsarten gleichzeitig zutreffen.
- **Feste Reihenfolge der Bausteine**: `Wo [Feature] → Solange [Zustand] → Wenn [Trigger] → Dann muss [System] [Systemantwort]`. Nicht benötigte Bausteine entfallen, die Reihenfolge der vorhandenen bleibt erhalten.
- Beispiele:
  - "Solange das Flugzeug am Boden ist, wenn Umkehrschub befohlen wird, dann muss das Kontrollsystem den Einsatz der Schubumkehr ermöglichen." (Solange + Wenn)
  - "Wo ein Regensensor verbaut ist, solange es regnet, wenn die Geschwindigkeit 30 km/h überschreitet, dann muss das Fahrassistenzsystem die Scheibenwischer-Intervallstufe automatisch erhöhen." (Wo + Solange + Wenn)

## Objektive Messbarkeit

- Vage: "Das System muss die Daten schnell importieren." → Nicht testbar.
- Konkret: "Das Importmodul muss 10.000 Datensätze in unter 5 Sekunden importieren." → Testbar.
- Vage: "Das System muss die Koordinaten sinnvoll validieren." → Nicht testbar.
- Konkret: "Wenn die eingegebenen Koordinaten außerhalb der Grenzen Deutschlands liegen, dann muss das System eine Fehlermeldung anzeigen und den Datenabruf verhindern." → Testbar (Unwanted Behavior).

## Häufige Anti-Patterns

| Anti-Pattern | Problem | Lösung |
|---|---|---|
| "Das System muss X und Y und Z" (mehrere unabhängige Regeln in einem Satz) | Unklar, welcher Teil bei einem Fehlschlag betroffen ist | In separate Anforderungssätze/FRs aufteilen |
| Trigger und Zustand vermischt ("Wenn sich im Wartungsmodus befindet") | Falsches Pattern gewählt (State-Driven statt Event-Driven) | "Solange" statt "Wenn" für andauernde Zustände verwenden |
| Fehlerfall nur als Nebensatz in einer Ubiquitous-Anforderung erwähnt | Fehlerbehandlung wird beim Review leicht übersehen | Als eigene Unwanted-Behavior-Anforderung formulieren und in "Fehlerfälle / Randbedingungen" aufnehmen |
| Optionales Feature als Zustand formuliert ("Solange ein Radarsensor verbaut ist") | Feature-Vorhandensein ist keine Zustandsänderung zur Laufzeit | "Wo" statt "Solange" verwenden |
| Systemantwort mit vagen Adjektiven ("schnell", "benutzerfreundlich", "korrekt") | Nicht objektiv prüfbar | Konkrete Werte/Zustände/Grenzwerte angeben |
| Falsche Reihenfolge bei Complex-Sätzen (z.B. "Wenn ..., solange ...") | Widerspricht der EARS-Konvention, erschwert Lesbarkeit/Traceability | Reihenfolge Wo → Solange → Wenn → Dann einhalten |
| Pauschal "das System" statt konkreter Komponente | Unklare Verantwortlichkeit, erschwert Architektur-Mapping | Konkreten Systemnamen/Komponente aus Glossar/Architektur verwenden |
