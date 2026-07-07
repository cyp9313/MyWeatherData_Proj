This document summarizes the content of the presentation "Generative AI in System and Software Development - Module 1.2 - Customization".

## `GenAI in SW Development - Module 1.2.md`

### 4. Generative AI in System and Software Development – Module 1.2: Customization

#### **Chinese Translation (中文翻译)**

---

### **生成式人工智能在系统与软件开发中的应用 – 模块1.2：定制化**

---

#### **基本概念：定制化的四个层次**

为了让 AI 在特定项目中更高效、更可控地工作，可以采用分层定制的策略。

1.  **项目惯例 (Projekt Konventionen)**
    *   **作用**: 提供在整个项目上下文中**始终**有效的基本信息和规则。
    *   **实现**: 通过根目录下的 `.github/copilot-instructions.md` 文件。
    *   **核心原则**: "按需提供，越少越好" (So viel wie nötig, so wenig wie möglich)。此文件会在每次聊天会话时被读取，因此应保持简洁，只包含最关键的、全局性的指令。

2.  **自定义提示 (Custom Prompts)**
    *   **作用**: 为需要重复执行的任务创建模板化的指令。
    *   **实现**: 在 `.github/prompts/` 目录下创建 `<名称>.prompt.md` 文件。
    *   **结构**: 文件内部通常包含 `name` (名称)、`description` (描述) 和 `argument-hint` (参数提示)。
    *   **调用**: 在聊天窗口中通过输入 `/` 加上提示名称来直接调用，并可附带参数（如文件路径）。

3.  **技能 (Skills)**
    *   **作用**: 封装用于**特定任务**的信息、流程和规范。它们是构成更复杂功能（如自定义提示和智能体）的“知识模块”或“工具箱”。
    *   **实现**: 在 `.github/skills/` 目录下为每个技能创建一个子目录，如 `<技能名称>/`，其中包含一个核心的 `SKILL.md` 文件，以及可选的脚本、参考文档、模板等。
    *   **特点**:
        *   **开放标准**: 旨在成为一个开放标准，方便在不同的 AI 系统间切换（例如，从 GitHub Copilot 切换到 Claude Code）。
        *   **可重用性**: 可以在聊天中直接调用，也可以被自定义提示和智能体使用。
    *   **调用**: 在聊天窗口中通过输入 `/` 加上技能名称来调用。

4.  **智能体 (Agents)**
    *   **作用**: AI 智能体是能够**独立**执行特定任务的虚拟专家。它们是最高级别的抽象。
    *   **实现**: 在 `.github/agents/` 目录下创建 `<名称>.agent.md` 文件。
    *   **能力**:
        *   可以被**技能**赋能，从而获得执行特定任务的知识。
        *   可以使用**外部工具**（如 `read`, `search`）与环境互动。
        *   可以调用其他的**子智能体**来完成更复杂的任务。
    *   **调用**: 可以通过聊天窗口的 `@` 菜单来选择并激活一个智能体。

---

#### **English Translation**

---

### **Generative AI in System and Software Development – Module 1.2: Customization**

---

#### **Fundamentals: The Four Layers of Customization**

To make AI work more efficiently and controllably within a specific project, a layered customization strategy can be applied.

1.  **Project Conventions**
    *   **Purpose**: To provide fundamental information and rules that are **always** valid within the entire project context.
    *   **Implementation**: Through the `copilot-instructions.md` file located in the root `.github/` directory.
    *   **Core Principle**: "As much as necessary, as little as possible." This file is read with every chat session, so it should be kept concise and contain only the most critical, global instructions.

2.  **Custom Prompts**
    *   **Purpose**: To create templated commands for repetitive tasks.
    *   **Implementation**: By creating `<NAME>.prompt.md` files within the `.github/prompts/` directory.
    *   **Structure**: The file typically includes a `name`, `description`, and an `argument-hint`.
    *   **Invocation**: Can be called directly in the chat window by typing `/` followed by the prompt's name, optionally with arguments (like a file path).

3.  **Skills**
    *   **Purpose**: To encapsulate information, processes, and specifications for **specific tasks**. They serve as the "knowledge modules" or "tool-kit" for building more complex functionalities like Custom Prompts and Agents.
    *   **Implementation**: By creating a subdirectory for each skill under `.github/skills/`, such as `<Skill_Name>/`. This folder contains a core `SKILL.md` file and optional supporting files like scripts, reference documents, or templates.
    *   **Features**:
        *   **Open Standard**: Intended to be an open standard, making it easier to switch between different AI systems (e.g., from GitHub Copilot to Claude Code).
        *   **Reusability**: Can be invoked directly in the chat, or be used by Custom Prompts and Agents.
    *   **Invocation**: Can be called in the chat window by typing `/` followed by the skill's name.

4.  **Agents**
    *   **Purpose**: AI Agents are virtual experts capable of executing specific tasks **independently**. They represent the highest level of abstraction.
    *   **Implementation**: By creating `<NAME>.agent.md` files in the `.github/agents/` directory.
    *   **Capabilities**:
        *   Can be empowered by **Skills** to gain knowledge for specific tasks.
        *   Can use external **Tools** (e.g., `read`, `search`) to interact with the environment.
        *   Can call other **Sub-Agents** to accomplish more complex tasks.
    *   **Invocation**: Can be selected and activated from the `@` menu in the chat window.

---

#### **Deutsche Zusammenfassung (德语总结)**

---

### **Generative KI in der System- und Softwareentwicklung – Modul 1.2: Customization**

---

#### **Grundlagen: Die vier Customization-Ebenen**

Um die KI effizient und steuerbar in einem Projekt einzusetzen, wird eine hierarchische Anpassungsstrategie verwendet.

1.  **Projekt-Konventionen (`copilot-instructions.md`)**
    *   **Zweck**: Enthält grundlegende Informationen und Anweisungen, die im gesamten Projektkontext **immer** gelten.
    *   **Prinzip**: "So viel wie nötig, so wenig wie möglich", da die Datei bei jedem Chat gelesen wird und den Kontext für alle Interaktionen bildet.

2.  **Custom Prompts (`/prompts`)**
    *   **Zweck**: Dienen als wiederverwendbare Vorlagen für sich wiederholende Aufgaben.
    *   **Aufbau**: Eine `.prompt.md`-Datei mit `name`, `description` und optional `argument-hint`.
    *   **Aufruf**: Direkt im Chatfenster über den Befehl `/Prompt_Name`, optional mit einem Argument (z.B. einem Dateipfad).

3.  **Skills (`/skills`)**
    *   **Zweck**: Kapseln Informationen, Abläufe und Vorgaben für **bestimmte** Aufgaben. Sie sind der "Werkzeugkasten" für Agents und Prompts.
    *   **Aufbau**: Jeder Skill hat einen eigenen Ordner (`/<Skill_Name>/`) mit einer zentralen `SKILL.md`-Datei und optionalen weiteren Ressourcen (z.B. Referenzdokumente, Code).
    *   **Eigenschaften**:
        *   **Offener Standard**: Ermöglicht einen einfachen Wechsel zwischen verschiedenen KI-Anbietern.
        *   **Wiederverwendbar**: Können im Chat, von Prompts oder von Agents genutzt werden.

4.  **Agents (`/agents`)**
    *   **Zweck**: Sind virtuelle KI-Experten, die Aufgaben **selbständig** bearbeiten können. Sie stellen die höchste Abstraktionsebene dar.
    *   **Aufbau**: Eine `.agent.md`-Datei, die den Namen, die Beschreibung, die zu verwendenden Tools (`read`, `search` etc.) und das KI-Modell definiert.
    *   **Fähigkeiten**:
        *   Werden durch **Skills** befähigt.
        *   Verwenden **Tools**, um mit der Umgebung zu interagieren.
        *   Können andere **Sub-Agents** aufrufen.
    *   **Aufruf**: Werden über das `@`-Menü im Chatfenster ausgewählt und aktiviert.

---
