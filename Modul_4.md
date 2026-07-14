---

### `Modul_4_Trilingual.md` (模块 4 - 架构 Architecture)

#### **Deutsche Zusammenfassung (Detailliert)**

**Generative KI in der System- und Softwareentwicklung – Modul 4: Architektur**

**1. Einführung in Text-to-Diagram und PlantUML**
*   **Die visuelle Lücke der KI**: LLMs haben ein exzellentes logisches Verständnis, können aber keine klassischen Zeichenprogramme (wie Visio) bedienen.
*   **Die Lösung (Text-to-Diagram)**: Tools wie **PlantUML**, Mermaid oder Graphviz nutzen strukturierten Text (Code), um deterministisch Diagramme zu rendern.
*   **Docs-as-Code**: Da die Architektur als Text vorliegt, lässt sie sich versionieren (Git) und von einer KI lesen/modifizieren. Medienbrüche werden vermieden (Text-Transformation ist die Paradedisziplin der KI).
*   **Wie Gen-KI hilft**:
    *   *Übersetzungsmaschine*: Transformiert Requirements in Sekunden in PlantUML.
    *   *Abstraktionsvermögen*: Extrahiert Abhängigkeiten aus langen Epics.
    *   *Review & Refactoring*: Validiert PlantUML-Code gegen Systemgrenzen.
*   **Best Practices**:
    *   *Human-in-the-Loop*: Der erste Wurf der KI ist eine Baseline (Diskussionsgrundlage).
    *   *Context Engineering*: Harte Restriktionen mitgeben, um "Happy Path"-Sycophancy zu vermeiden.
    *   *Iteratives Anpassen*: Feedback in natürlicher Sprache geben (z.B. "Füge eine Zwei-Faktor-Authentifizierung ein").

**2. Statische Architektursichten**
Fokus auf Struktur ("Was existiert", "Wer kommuniziert mit wem") ohne zeitliche Abläufe. Top-Down Ansatz.
*   **Kontext-Sicht (Big Picture)**: Das System (z.B. V2G Ladesäule) ist eine Blackbox. Definiert Systemgrenzen und externe Entitäten (Akteure, Nachbarsysteme). KI extrahiert externe Akteure aus Epics.
*   **Komponenten-Sicht (Whitebox)**: Öffnet das System. Zeigt logische/physische Bausteine und Allokation. Hier zeigt sich, ob Hard Constraints eingehalten werden.
    *   *Prompting-Tipp*: Ohne explizite Anweisung ("Kein TLS-Chip!") würde die KI eine Standard-Architektur zeichnen. Constraints im globalen Kontext erzwingen ein Software-TLS.
*   **Klassen-Sicht**: Baupläne der Software (Objekte, Daten, Verhalten, Attribute, Methoden). Direkte Vorstufe zum Quellcode.
    *   *KI-Stärke*: LLMs "kennen" Standards wie ISO 15118 und können sofort ein valides Datenmodell in PlantUML generieren.

**3. Funktionale und Dynamische Sichten**
*   **Sequenz-Sicht**: Fokus auf Zeit und Interaktion (chronologischer Nachrichtenaustausch, synchrone/asynchrone Aufrufe). Standard für Netzwerkprotokolle (ISO 15118). KI hilft bei der Protokoll-Visualisierung und Edge-Case Exploration (z.B. Timeout-Fallbacks modellieren).
*   **Zustands-Sicht (State Machine)**: Herzstück der Embedded-Software. Deterministisches Verhalten und "Safety First" (Vermeidung von Deadlocks).
    *   *KI-Stärke*: Lückenanalyse (Finden fehlender Error States) und Text-to-State (für Menschen mühsam, für LLMs trivial).
*   **Aktivitäts-Sicht**: Algorithmen & Concurrency. Modelliert Kontroll-/Datenfluss und parallele Verarbeitung (Threads, Forks, Joins im RTOS). KI visualisiert Concurrency, um z.B. CPU-Blockaden zu prüfen.
*   **Timing-Sicht (HSI)**: Harte Echtzeitbedingungen auf einer exakten physikalischen Zeitachse. Essenziell für Watchdogs oder PWM-Signale. KI übersetzt Normen direkt in Timing-Verläufe.

**4. Automatisierung mit Agents und Skills**
*   **Der Architektur-Designer (@Architecture_Designer)**: Eine "Single Source of Truth", die Requirements deterministisch in PlantUML transformiert, unter Einhaltung harter Grenzen.
*   **Agent-System Prompt (Auszug)**:
    *   *Rolle*: Senior-Architekt (ISO 15118, V2G).
    *   *Denkweise*: Analytisch, präzise, modelliert proaktiv Fehlerzustände. Kein Happy-Path.
    *   *Harte Vorgaben*: 1. Kein Hardware-Krypto-Beschleuniger (MbedTLS erzwingen). 2. Sicherheits-Thread darf niemals blockiert werden.
*   **Skills**: Spezifische Anweisungen für jede Sicht (z.B. `/sequenz_sicht`). Der Skill zwingt die KI, in Schritten zu arbeiten: Eingabe analysieren -> Akteure identifizieren -> Happy Path entwerfen -> Einschränkungen (`alt/else` Blöcke) durchsetzen -> Ausgabe generieren.

---
#### **Chinese Translation (Detailed)**

**生成式人工智能在系统与软件开发中的应用 – 模块 4：架构**

**1. 文本转图表 (Text-to-Diagram) 与 PlantUML 简介**
*   **AI 的视觉盲区**: LLM 是文本机器，具有极强的逻辑理解力，但不会使用 Visio 等绘图软件“画图”。
*   **解决方案 (Text-to-Diagram)**: 使用 **PlantUML**、Mermaid 或 Graphviz 等工具，利用纯结构化文本（代码）确定性地渲染出序列图、组件图和类图。
*   **架构即代码 (Docs-as-Code)**: 纯文本架构易于版本控制 (Git)，可嵌入 Markdown 中，最重要的是：**可由 AI 读取、编写和修改**（文本转换是 Gen-AI 的拿手好戏）。
*   **Gen-AI 的帮助**:
    *   *翻译机*: 几秒钟内将业务需求转化为语法正确的 PlantUML 代码。
    *   *抽象能力*: 从长篇 Epic 中提取复杂的依赖关系。
    *   *审查与重构*: 验证 PlantUML 代码是否符合系统边界。
*   **最佳实践**:
    *   *人在回路 (Human-in-the-Loop)*: AI 的初稿仅作为讨论基础 (Baseline)。
    *   *情境工程 (Context Engineering)*: 必须提供硬性约束，否则 AI 会画出忽略限制的“快乐路径”图表。
    *   *通过 Prompt 迭代*: 用自然语言给出反馈（例如“在后端和新组件之间添加双因素认证”）。

**2. 静态架构视图**
关注系统结构（“有什么”，“谁和谁通信”），不包含时间顺序。采用自顶向下 (Top-Down) 方法。
*   **上下文视图 (Big Picture)**: 系统（如 V2G 充电桩）作为黑盒。定义系统边界和外部实体。AI 可通过读取 Epic 自动提取外部参与者。
*   **组件视图 (Whitebox)**: 打开系统，定义逻辑/物理模块及其分配。在此处必须体现是否遵守了硬性约束。
    *   *防“迎合”提示*: 如果不明确指示（“没有 TLS 芯片！”），AI 会画出标准架构。我们通过全局配置强制 AI 优化纯软件的 TLS 栈。
*   **类视图**: 软件的蓝图（数据、行为、属性、方法）。是实施源代码（C++/Python）的直接基础。
    *   *AI 的优势*: LLM 非常“熟悉” ISO 15118 等标准，能直接从协议描述生成有效的 PlantUML 数据模型。

**3. 功能与动态视图**
*   **序列视图 (Sequence View)**: 聚焦时间和交互（按时间顺序的消息交换、同步/异步调用）。是 IoT/嵌入式网络协议建模的标准。AI 可实现协议可视化，并探索边缘案例（强制加入超时回退路径）。
*   **状态视图 (State Machine)**: 嵌入式软件的核心。定义系统状态、触发器和转换。决定性行为和“安全第一”（避免死锁）。
    *   *AI 的优势*: 差距分析（Gap Analysis，找出缺失的错误状态）和“文本转状态”（这极大降低了人类由于繁琐分支导致的错误率）。
*   **活动视图 (Activity View)**: 算法与并发 (Concurrency)。展示详细的控制/数据流，是 RTOS 中多线程、分叉 (Forks) 和合并 (Joins) 的最佳工具。AI 可帮助可视化并发，以检查 CPU 阻塞是否会威胁安全线程。
*   **时序视图 (Timing View)**: 硬件-软件接口 (HSI) 和硬实时条件（毫秒/微秒）。AI 能将 IEC 61851 等规范直接转化为精准的 PlantUML 时序曲线，从而暴露出架构瓶颈（如缺乏硬件加速导致的 CPU 阻塞）。

**4. 使用智能体和技能实现自动化**
*   **架构设计师 (@Architecture_Designer)**: 作为“唯一事实来源”的智能体，将需求转化为确定性的 PlantUML 模型。
*   **智能体系统 Prompt (摘录)**:
    *   *角色*: 嵌入式系统高级架构师 (ISO 15118, V2G)。
    *   *思维方式*: 分析性、精确、安全导向。**不做“快乐路径”**，主动对错误和硬件限制建模。
    *   *硬性规定 (绝对不可违反)*: 1. 没有硬件加密加速器，必须使用软件 TLS (MbedTLS)。 2. 安全监控线程绝对不能被 TLS 线程阻塞。
*   **技能 (Skills)**: 如 `/sequenz_sicht`，强制 AI 按步骤执行：分析输入 -> 识别参与者 -> 设计快乐路径 -> 实施约束（插入 `alt/else` 处理超时）-> 输出有效的 PlantUML。

---
#### **English Translation (Detailed)**

**Generative AI in System and Software Development – Module 4: Architecture**

**1. Intro to Text-to-Diagram and PlantUML**
*   **The AI's Visual Gap**: LLMs are text machines with excellent logical understanding but cannot operate classic drawing programs (like Visio).
*   **The Solution (Text-to-Diagram)**: Tools like **PlantUML**, Mermaid, or Graphviz use structured text (code) to deterministically render diagrams.
*   **Docs-as-Code**: Because the architecture is plain text, it can be version-controlled (Git) and effortlessly read, written, and modified by AI (text transformation is Gen-AI's core strength).
*   **How Gen-AI Helps**:
    *   *Translation Engine*: Transforms requirements into valid PlantUML code in seconds.
    *   *Abstraction Power*: Extracts dependencies from lengthy Epics.
    *   *Review & Refactoring*: Validates existing PlantUML against system boundaries.
*   **Best Practices**:
    *   *Human-in-the-Loop*: The AI's first draft is just a baseline for discussion.
    *   *Context Engineering*: Provide Hard Constraints to avoid sycophantic "Happy Path" diagrams.
    *   *Iterative Prompting*: Provide natural language feedback to modify the diagram (e.g., "Add 2FA on success").

**2. Static Architecture Views**
Focuses on structure ("What exists", "Who communicates with whom") without temporal sequences. Top-Down approach.
*   **Context View (Big Picture)**: The system (e.g., V2G charger) is a black box. Defines boundaries and external actors. AI can extract external actors directly from Epics.
*   **Component View (Whitebox)**: Opens the system to define logical/physical blocks and allocation. This view must demonstrate how Hard Constraints are handled.
    *   *Prompting Tip*: Without explicit instruction, AI will draw standard architectures (with crypto-chips). We force it via global context to optimize for a Software-based TLS stack.
*   **Class View**: The blueprint of the software (data, behavior, attributes, inheritance). The granular basis for source code.
    *   *AI Strength*: LLMs "know" standards like ISO 15118 perfectly and can instantly generate a valid PlantUML data model from a protocol description.

**3. Functional and Dynamic Views**
*   **Sequence View**: Focuses on time and interaction (chronological messages, sync/async calls). Standard for network protocols. AI visualizes protocols and explores edge cases (e.g., integrating a fallback path for CPU-overload timeouts).
*   **State Machine View**: The heart of embedded software. Deterministic behavior and "Safety First" (preventing deadlocks).
    *   *AI Strength*: Gap Analysis (finding missing Error States) and Text-to-State translation (trivial for LLMs, tedious for humans).
*   **Activity View**: Algorithms & Concurrency. Details step-by-step control/data flow. Best tool for parallel threads, forks, and joins in an RTOS. AI helps visualize concurrency to check if blocking TLS-stacks threaten the Safety-Thread.
*   **Timing View (HSI)**: Hard real-time conditions on an exact physical time axis. Essential for watchdogs and PWM signals. AI translates norms (like IEC 61851) directly into precise timing curves, revealing architectural bottlenecks (e.g., CPU blocking).

**4. Automation with Agents and Skills**
*   **The Architecture Designer (@Architecture_Designer)**: The "Single Source of Truth" agent that transforms requirements into deterministic PlantUML models.
*   **Agent System Prompt (Excerpt)**:
    *   *Role*: Senior Embedded Systems Architect (ISO 15118, V2G).
    *   *Mindset*: Analytical, precise, safety-oriented. **No "Happy Path" architectures**. Proactively model error states and hardware limits.
    *   *HARD CONSTRAINTS*: 1. NO hardware crypto-accelerator (Software TLS required). 2. Safety monitoring thread must NEVER be blocked by the TLS thread.
*   **Skills**: E.g., `/sequenz_sicht`. Forces the AI to follow execution steps: Analyze input -> Identify actors -> Design Happy Path -> Enforce Constraints (insert `alt/else` for timeouts) -> Generate valid PlantUML code only.

---
