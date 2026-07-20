# Generative AI in der System und Software Entwicklung
## Modul 1 – Einführung (Customization: Prompts, Skills, Agents)

### Customization Ebenen (Layer)
1. **Projekt Konventionen**: Grundlegende Informationen, die im Projektkontext immer gelten.
2. **Custom Prompts**: Prompt-Vorlagen, für sich wiederholende Aufgaben.
3. **Skills**: Informationen, Abläufe und Vorgaben für bestimmte Aufgaben.
4. **Agents**: AI-Agents, die Aufgaben selbständig bearbeiten können.

### GitHub Copilot Verzeichnisstruktur: `.github/`
* `copilot-instructions.md`: Wichtige Anweisungen und Kontext.
* `/prompts`: Vordefinierte Prompts.
* `/skills`: Skills (ggf. inkl. Referenz-Dateien).
* `/agents`: Eigene AI-Agents.

### Projekt Konventionen
* `copilot-instructions.md` wird bei jedem Chat gelesen.
* "So viel wie nötig, so wenig wie möglich".

### Prompts
* Namenskonvention: `<NAME>.prompt.md`
* Aufbau: 1. Header/Definition, 2. Anweisungen/Kontext.
* Aufruf: `/Prompt_Name`.

### Skills
* Offener Standard, von verschiedenen AI Systemen verwendet.
* Namenskonvention Ordner: `.github/skills/<Skill_Name>`
* Datei: `SKILL.md` (Header, Anweisungen)
* Zusätzliche Dateien optional (`/scripts`, `/references`, `/assets`).

### Agents
* Führen bestimmte Aufgaben aus, können durch Skills befähigt werden.
* Namenskonvention: `<NAME>.agent.md`
* Aufbau: 1. Header/Definition (inkl. Tools, Model), 2. Anweisungen/Kontext.
* Auswahl über Menü im Chatfenster (`@AgentName`).
