# Generative AI in der System und Software Entwicklung
## Modul 1 – Einführung

### Agenda und Inhalt
1. Grundlagen und Funktionsweise von Generative AI, Large Language Modells und Agentic AI
   - Einordnung in die AI-Landschaft
   - Funktionsweise I – Tokenisierung und Wahrscheinlichkeit
   - Funktionsweise II – Die Transformer-Architektur
   - Arbeit mit LLMs I – Risiken und Ethik
   - Arbeit mit LLMs II – Chat, Prompting und Context
   - Arbeit mit LLMs III – Agentic AI
   - Kosten und Preismodell für die Nutzung von Gen-AI
2. Customization: Prompts, Skills, Agents
3. Einführung: AI Agents in der Produktentwicklung im V-Modell

### 1. Grundlagen und Funktionsweise von Gen-AI, LLM und Agentic AI
**Einordnung in die AI-Landschaft**
* Artificial Intelligence (AI): Ursprünglich oft regelbasiert (Expertensysteme). Ziel: Maschinen sollen Probleme lösen.
* Machine Learning (ML): Keine Regeln programmieren, Maschine findet Regeln selbst durch statistische Optimierung.
* Deep Learning (DL): Nutzt neuronale Netze mit vielen Schichten für abstrakte Merkmale.
* Generative AI (GenAI): Erstellt neue Daten ("Generiere mir ein Bild...").
* Large Language Model (LLM): Generative Modelle, spezialisiert auf Text.
* Agentic AI: Führen mittels externen Tools selbständig Aufgaben durch.

**Funktionsweise I – Tokenisierung und Wahrscheinlichkeit**
* Tokenisierung: Text in Tokens zerlegen (Wort, Teilwort). Spart Speicher, erkennt Zusammenhänge.
* Vektoren & Embeddings: Jedes Token wird ein Vektor im mathematischen Raum (semantische Nähe).
* Next-Token-Prediction: Ein extrem fortschrittliches „Auto-Complete“ basierend auf Wahrscheinlichkeitsverteilung.

**Funktionsweise II – Die Transformer-Architektur**
* Transformer (2017): Verarbeiten ganze Textblöcke parallel.
* Self-Attention: Modell prüft bei jedem Wort die Beziehung zu allen anderen Wörtern im Kontext.
* Trainingsphasen: Pre-training (Internetdaten), SFT (Supervised Fine-Tuning - Instruktionen folgen), RLHF (Menschliches Feedback).
* GPT: Generative Pre-trained Transformer. Künstliche Intelligenz ist Mathematik (Statistik), kein Verständnis.

**Arbeit mit LLMs I – Risiken und Ethik**
* Halluzinationen: Kreative Fehler, plausibel klingend aber falsch.
* Stochastische Papageien: Plappern nach Wahrscheinlichkeit, ohne Verständnis.
* Bias: Reproduzieren Vorurteile aus Trainingsdaten.
* Fehlerhafte Berechnungen: GPTs können keine echte Mathematik.
* Datensicherheit: Vorsicht bei eigenen Daten. Bosch Tools (GenAI Marketplace) dürfen für interne Daten (bis SC-2) verwendet werden.

**Arbeit mit LLMs II – Chat, Prompting und Context**
* Das Chat Window (Kurzzeitgedächtnis): Chat-Bias (Fokus auf Beginn und Ende). "Context Rot" bei langen Chats.
* Prompting-Strategien: Chain-of-Thought, Few-Shot Prompting, System Prompts.
* Temperatur: Niedrig = konservativ, Hoch = kreativ.
* Prompt Strukturierung: Persona, Ziel, Erwartetes Ergebnis, Formatierung (Markdown).
* Context Engineering: Inline, Dateiuploads, System-Integration (RAG). Formate: Reiner Text, Markdown, CSV/JSON/XML sind sehr gut. PDFs & Excel sind fehleranfällig.
* Sandwich Methode: Mensch (Vorarbeit) -> KI (Heavy Lifting) -> Mensch (Feinschliff).

**Arbeit mit LLMs III – Agentic AI**
* Von Chatbots (reagieren auf Input) zu AI-Agents (autonome Aufgabenbearbeitung mit Tools).
* Anatomie eines Agents: Wahrnehmung (Perception) -> Gehirn/Planung (Cognition) -> Werkzeuge (Tools & Actions) -> Feedback-Schleife (Evaluation).
* Herausforderungen & Best Practices: Human-in-the-Loop, Klare Zielvorgaben, Datenschutz & Sicherheit (geringste Rechte), Transparenz.

**Kosten und Preismodell**
* GitHub Copilot: Abrechnung basierend auf Token.
* Kostenoptimierung: Modellauswahl (stark vs. mittel vs. schnell), kurzer Kontext, kurze Sessions, effektives Prompting.
