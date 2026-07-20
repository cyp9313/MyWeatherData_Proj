markdown_text = """
# Generative AI in der System und Software Entwicklung
## Modul 6 – Validierung
Graf, EME-PE/ESC, 16.07.2026

---

## Agenda und Inhalt
1. Systemvalidierung vs. Unit-Testing im KI-Kontext
2. Das Notebook als Validierungszentrale
3. Testspezifikation und Testdatengenerierung
4. Testausführung auf Systemebene
5. Testassessment und automatisiertes Reporting
6. Der KI-Auditor für Release-Freigaben
Übung 6: Projektarbeit – Validierung

---

## 1. Systemvalidierung vs. Unit-Testing im KI-Kontext

### Einordnung im V-Modell
* Wechsel auf den rechten Ast des V-Modells:
  * **Unit-Testing (Modul 5)**: „Are we building the product right?“
    -> Fokus liegt auf der technischen Ebene: Funktioniert der Code fehlerfrei? (Whitebox)
  * **Systemvalidierung (Modul 6)**: „Are we building the right product?“
    -> Fokus liegt auf der Systemebene: Erfüllt das integrierte Gesamtsystem die ursprünglichen System- und Stakeholder-Anforderungen? (Blackbox)

### Kernbotschaften und der neue Hebel der KI
* **Strikte Methodentrennung**:
  * Klare Abgrenzung der Validierung (System-/Akzeptanztests) vom entwicklungsnahen Unit-Testing.
  * Wichtig: Gen-AI brilliert im Software-Systemtest, ersetzt aber nicht den finalen Hardware-in-the-Loop (HiL) Test an der physischen Hardware, sondern beschleunigt diesen durch perfekte Spezifikationen.
* **Systemdenken statt Komponentendenken**:
  * Fokus verschiebt sich von isolierten Modulen auf das funktionierende Zusammenspiel der gesamten Architektur.
* **Der Rollenwechsel der Gen-AI**:
  * KI wird nicht mehr als primärer „Code-Assistent“ eingesetzt, sondern fungiert als semantischer Prüfer.
  * Sie schlägt die Brücke zwischen abstrakten Requirements und validierbaren Testfällen.
  
> Durch den Rollenwechsel liegt der Wert der KI nun im semantischen Abgleich von funktionalem Systemverhalten mit den textuellen Anforderungen. Dies bildet den entscheidenden ersten Schritt zur automatisierten Traceability.

---

## 2. Das Notebook als Validierungszentrale

### Klassische Docs-as-Code Alternativen für die System-Validierung
* Behavior-Driven Development (BDD / Gherkin)
* Keyword-Driven Testing (Robot Framework)
* Static Site Generators + CI/CD (MkDocs / Sphinx + Pytest)
* AsciiDoc im Systems Engineering

### Das Notebook als "Docs-as-Code" in der Systemvalidierung
* Das Notebook wird im Kontext der Systemvalidierung zur zentralen Single Source of Truth.
* Ein dynamisches Artefakt: keine zersplitterten Dokumente für Spezifikationen, isolierten Skripten für die Ausführung und manuellen Reports für die Bewertung.
* Fokus auf die Methodik: Im Zentrum steht der Prozess, wie Anforderungen, Testcode und Auswertung nahtlos in einem Dokument verwoben werden.

### Workflow: Symbiose aus KI, Code und Mensch
1. **Testspezifikation (Markdown)**: KI-Assistenz für Testfälle, Mensch validiert.
2. **Testausführung (Python)**: Deterministischer Systemcode, KI baut Infrastruktur (Runner, Adapter, Mocks).
3. **Testassessment (Hybrid)**: KI-basiert Logs semantisch bewerten, deterministische Asserts entscheiden über Pass/Fail.

---

## 3. Testspezifikation und Testdatengenerierung
* **Die Herausforderung**: Abstrakte Systemanforderungen müssen systematisch in messbare, ausführbare Testspezifikationen überführt werden.
* **Der Hebel der Generativen KI**:
  * Analytische Spezifikation: Die KI agiert als methodischer Test-Analyst.
  * Synthetische Datengenerierung: Die KI generiert auf Kommando strukturierte Testdaten.
* **Methodik & Guardrails**:
  * Äquivalenzklassenbildung, Grenzwertanalyse, Zustandsübergangstest, Entscheidungstabellentest, Szenariobasierter Test.

---

## 4. Testausführung auf Systemebene
* Vom Testkonzept zur deterministischen Ausführung. Das System wird stimuliert; das Notebook fungiert als deterministischer Test-Runner.
* Die Testausführung bleibt klassisches Software-Engineering – KI ändert nicht die physikalischen/technischen Gesetze der Systemintegration.
* Guardrails: Eine KI darf Testergebnisse nicht "erraten" oder "halluzinieren".
> Gen-AI baut „nur“ die deterministische Test-Infrastruktur (Runner, Adapter, Mocks), um das System testbar zu machen.

---

## 5. Testassessment und automatisiertes Reporting
* Vom deterministischen Code zum auditierbaren Report im Notebook.
* Rohe Log-Dateien und System-Outputs in einen lesbaren, auditierbaren Bericht (Docs-as-Code) überführen.
* Deterministische Bewertung (Code) prüft Grenzwerte und Status-Codes. KI-gestützte Aufbereitung analysiert Fehler-Traces und bereitet Logs lesbar auf.
* WICHTIG: Die KI testet NICHT und bewertet keine Systemgrenzen!

---

## 6. Der KI-Auditor für Release-Freigaben
* **Das Notebook als Audit-Input**: Wir übergeben das vollständig ausgeführte Notebook inklusiver der generierten Markdown-Tabellen an die KI.
* **Aufgabe der KI**: Anomalie-Erkennung, Prüfung der Traceability und Zusammenfassung für das Management.
* **Guardrails**:
  * Die KI erteilt niemals selbst die Release-Freigabe! Sie bereitet lediglich die Entscheidungsvorlage vor.
  * Human in the Loop: Ein Mensch (Release Train Engineer / QA Lead) liest das Audit-Summary und zeichnet rechtlich bindend ab.

---

### Gesamtfazit Validierung
* **Der Kreis schließt sich**: Vom Schreiben der Testspezifikation über die Ausführung und das Assessment bis zum Audit – alles passiert auditierbar in einer Umgebung (Notebook).
* **Die Rolle der Gen-AI**: Sie ist Beschleuniger, Infrastruktur-Bauer (Glue-Code) und scharfer Reviewer – aber niemals der Ausführende kritischer Tests oder der rechtliche Freigeber. Das V-Modell bleibt deterministisch, die KI macht es skalierbar.
"""

with open('Module_6_Validierung.md', 'w', encoding='utf-8') as f:
    f.write(markdown_text)
print("File created.")

