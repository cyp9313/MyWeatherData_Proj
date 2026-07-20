# INVEST-Kriterien im Detail

Detaillierte Prüffragen, typische Red Flags und Beispiele je Kriterium. Wird von [SKILL.md](../SKILL.md) beim Erstellen und Reviewen von User Stories referenziert.

---

## I – Independent (unabhängig)

**Definition:** Die Story sollte für sich alleine stehen und flexibel priorisierbar/umsetzbar sein, ohne dass sie zwingend auf eine andere offene Story wartet.

**Prüffragen:**
- Kann die Story in beliebiger Reihenfolge relativ zu anderen Stories im Backlog eingeplant werden?
- Gibt es eine harte technische oder fachliche Abhängigkeit, die im Feld "Abhängigkeiten" nicht dokumentiert ist?
- Wird auf Ergebnisse einer anderen, noch nicht abgeschlossenen Story verwiesen?

**Red Flags:**
- "Abhängigkeiten"-Feld verweist auf eine Story, die selbst noch in `Draft` ist.
- Zwei Stories beschreiben dasselbe UI-Element/dieselbe Komponente und überschneiden sich inhaltlich.

**Beispiel:**
- ❌ "Als Nutzer möchte ich Datensätze filtern, *nachdem* der Import (US-002) fertig ist" – harte Abhängigkeit ohne eigenständigen Wert.
- ✅ Import und Filterung als getrennte Stories, die jeweils für sich testbar sind (Filterung kann z.B. gegen Testdaten/Mocks entwickelt werden).

## N – Negotiable (verhandelbar)

**Definition:** Die Story ist kein Vertrag, sondern eine Einladung zum Gespräch zwischen PO/Kunde und Team über die beste Lösung.

**Prüffragen:**
- Beschreibt die Story das **Was/Warum**, ohne das **Wie** (Implementierungsdetail) vorzuschreiben?
- Bleibt Spielraum für alternative technische Lösungen im Team?
- Sind Details eher in Akzeptanzkriterien verhandelbar als im Story-Satz einzementiert?

**Red Flags:**
- Der Story-Satz enthält konkrete UI-Technologien, Algorithmen oder Datenbankstrukturen.
- Formulierungen wie "muss exakt so umgesetzt werden wie ..." ohne Verhandlungsspielraum.

**Beispiel:**
- ❌ "Als Nutzer möchte ich ein Dropdown-Menü mit Chart.js-Diagramm, das per REST-Endpunkt `/api/v2/data` Daten lädt."
- ✅ "Als Nutzer möchte ich Daten grafisch darstellen können, damit ich Trends leicht erkenne." (Technik wird im Gespräch/FR geklärt)

## V – Valuable (wertvoll)

**Definition:** Jede Story muss einen erkennbaren, möglichst messbaren Mehrwert für Endnutzer, Kunde oder Business liefern.

**Prüffragen:**
- Ist der "damit ..."-Teil ein echter Nutzen (nicht nur eine Aktivität ohne Grund)?
- Würde ein Stakeholder den Wert der Story ohne Rückfrage verstehen?
- Ist die Story rein technisch motiviert, ohne erkennbaren Nutzerbezug? (Dann ggf. als technische Aufgabe/FR statt User Story führen.)

**Red Flags:**
- "damit"-Satz fehlt oder ist eine Tautologie ("... damit ich es nutzen kann").
- Story beschreibt nur einen Zwischenschritt ohne für sich lieferbaren Wert.

**Beispiel:**
- ❌ "Als Entwickler möchte ich eine neue Tabelle `raw_data` anlegen, damit Daten gespeichert werden können." (rein technisch, kein Endnutzerwert – gehört eher als FR/Technical Task)
- ✅ "Als Nutzer möchte ich historische Daten importieren können, damit ich langfristige Trends auswerten kann."

## E – Estimable (schätzbar)

**Definition:** Das Team muss Aufwand, Komplexität und Risiko grob einschätzen können (z.B. in Story Points).

**Prüffragen:**
- Ist der Umfang klar genug umrissen, um ihn grob zu schätzen (nicht auf den Tag genau)?
- Sind alle notwendigen Informationen (Kontext, Rahmenbedingungen, verknüpfte FRs) vorhanden oder gibt es offene Blocker-Fragen?
- Ist die Story zu groß/vage, um überhaupt geschätzt zu werden ("Epic im Story-Gewand")?

**Red Flags:**
- Team kann sich in der Schätzrunde nicht einigen, weil zentrale Fragen offen sind ("Was passiert bei fehlerhaften CSV-Zeilen?").
- Beschreibung besteht nur aus einem Schlagwort ohne Kontext.

**Beispiel:**
- ❌ "Als Nutzer möchte ich Daten verwalten können." (zu vage, nicht schätzbar)
- ✅ Story mit klarer Beschreibung, konkreten Akzeptanzkriterien und benannten Rahmenbedingungen (Dateiformat, erwartete Datenmenge).

## S – Small (klein)

**Definition:** Die Story muss klein genug sein, um innerhalb eines Sprints (meist 2–3 Wochen) vollständig umgesetzt, getestet und ausgeliefert zu werden.

**Prüffragen:**
- Passt die Story realistisch in einen Sprint, inkl. Test?
- Enthält die Story mehrere "und"-verknüpfte Funktionalitäten, die eigentlich getrennte Stories wären?
- Lässt sich die Story weiter schneiden (Splitting), ohne den Wert (V) zu verlieren?

**Splitting-Strategien:** nach Workflow-Schritten, nach Datenvarianten/Formaten, nach CRUD-Operationen, nach Geräte-/Plattformvarianten, "Happy Path" zuerst, dann Fehlerfälle.

**Red Flags:**
- Story-Titel/Satz enthält "und" mehrfach oder mehrere unabhängige Akzeptanzkriterien-Blöcke zu unterschiedlichen Funktionen.
- Schätzung liegt deutlich über der Team-Kapazität eines Sprints.

**Beispiel:**
- ❌ "Als Nutzer möchte ich Daten importieren, validieren, visualisieren und exportieren können."
- ✅ Vier getrennte Stories: Import, Validierung, Visualisierung, Export – jede einzeln wertvoll und klein.

## T – Testable (testbar)

**Definition:** Es muss objektiv überprüfbar sein, wann die Story fertig ist – über konkrete Akzeptanzkriterien.

**Prüffragen:**
- Existiert mindestens ein Akzeptanzkriterium im Gegeben/Wenn/Dann-Format?
- Sind alle Kriterien so formuliert, dass zwei Personen unabhängig voneinander zum gleichen Testergebnis kommen (objektiv, messbar)?
- Vermeidet die Formulierung subjektive/unklare Begriffe ("schnell", "intuitiv", "benutzerfreundlich") ohne Messgröße?

**Red Flags:**
- Akzeptanzkriterien fehlen komplett oder sind nur ein einzelner Stichpunkt ohne Gegeben/Wenn/Dann-Struktur.
- Begriffe wie "sollte gut funktionieren" ohne konkrete Prüfbedingung.

**Beispiel:**
- ❌ "Der Import soll zuverlässig funktionieren."
- ✅ "**Gegeben** eine gültige CSV-Datei im erwarteten Format **Wenn** der Nutzer den Import startet **Dann** werden alle Zeilen ohne Fehlermeldung in die lokale Datenhaltung übernommen."
