---

### `Modul_5_Trilingual.md` (模块 5 - 软件设计与编码 SW-Design and Coding)

#### **Deutsche Zusammenfassung (Detailliert)**

**Generative KI in der System- und Softwareentwicklung – Modul 5: SW-Design und Coding**

**1. Software Design – Grundlagen**
*   **Herausforderung ("Schneller, aber schmutziger Code")**: KI generiert funktionierende Lösungen, ignoriert aber oft Architektur-Prinzipien. Typische Anti-Patterns:
    *   *Fehlende Trennung*: I/O (Hardware/DB) direkt in der Business-Logik.
    *   *Spaghetti-Code*: Riesige Funktionen ohne Abstraktion.
    *   *Inkonsistenz*: Wechselnde Programmierstile pro Datei.
*   **Lösung (Guardrails / Leitplanken)**:
    1.  **Architektur**: z.B. **Hexagonales Design (Ports & Adapters)**. Strikte Trennung von Kernlogik (Domain) und Infrastruktur. *KI-Anweisung*: "Programmiere gegen Schnittstellen (Interfaces/Ports), nicht gegen konkrete Implementierungen."
    2.  **Dateistruktur (Scaffolding)**: Ein leeres Repo hat keinen Kontext. Die KI muss zuerst die komplette Ordnerstruktur inkl. leerer Init-Skripte generieren.
    3.  **Design Patterns**: KI wendet Muster (Gang of Four) fehlerfrei an. *Ansatz*: Sag der KI nicht "Löse das Problem", sondern "Löse das Problem unter Anwendung von Pattern X".
        *   *Strategy Pattern*: Eliminiert `if-else` Wüsten (z.B. verschiedene Lade-Strategien).
        *   *Factory Pattern*: Vermeidet harte Kopplung bei Objekterstellung (z.B. `DummyMockSensor` für Tests).
        *   *Observer Pattern*: Event-basiert statt blockierendem Polling.
    4.  **Coding Guidelines**: Als IDE-Kontext hinterlegen. Beispiele für Python: *Strict Type Hinting*, *Google-Style Docstrings*, *Explizites Error Handling* (kein generisches `except Exception`), *Keine Magic Numbers*.

**2. Automatisierung mit Agents und Skills (Der "Design-First" Workflow)**
*   **Das Problem (Prompt-Falle)**: LLMs wollen sofort Code schreiben (Design-Bypass). Bei langen Chats entsteht **"Context Rot"** (KI vergisst Architekturregeln) und die **"Big-Bang-Falle"** (Versuch, alles auf einmal zu lösen).
*   **Die Lösung (Document-First Ansatz)**:
    *   Schritt 1: Guidelines als zentralen Skill definieren (`/python-guidelines`).
    *   Schritt 2: Agent erstellt erst ein Architektur-Dokument (`software_architecture.md`).
    *   Schritt 3: Agent führt Scaffolding (Bash-Skript) anhand des Dokuments aus.
    *   Schritt 4: Erstellung eines Micro-Design Implementierungsplans (`implementation_plan.md`) als Checkliste.
    *   Schritt 5: Geführte Implementierung Schritt für Schritt, evaluiert durch den Guideline-Skill.
    *   Schritt 6: Striktes **Review & Self-Correction** (Trennung von Kreativ- und Kritiker-Phase).

**3. Software Unit-Test (TDD)**
*   **Die Herausforderung**: Die KI unterliegt der **"Happy-Path-Illusion"** und schreibt tautologische Tests (Tests spiegeln die Fehler des Codes wider).
*   **Die Lösung**: **Test-Driven Development (TDD)** mit Hexagonaler Architektur.
    *   Schritt 4b: KI schreibt zuerst einen `test_plan.md` (Happy Path, Fehlerfälle, Edge Cases) gegen den Port.
    *   Schritt 5a (ROT-Phase): KI generiert **Mocks/Stubs** (z.B. `MockDwdApiAdapter`) und fehlschlagende Tests, isoliert von externen Systemen.
    *   Schritt 5b (GRÜN-Phase): KI implementiert den echten Code, bis die Tests passen.
    *   Schritt 7: **"Destructive QA"-Review**. Harter Persona-Wechsel der KI zum "Zerstörer", um blind Spots zu finden und den Code mutwillig abstürzen zu lassen.

**4. Debugging & Bugfixing**
*   **Die "Fix-Loop of Death"**: Blindes Stacktrace-Kopieren führt zu "Whack-a-Mole" (eins repariert, zwei kaputt), reiner Symptombehandlung und "Context Pollution".
*   **Der strukturierte Bugfixing-Workflow (Hypothesis-Driven)**:
    1.  **Isolation & Analyse**: KI darf KEINEN Code schreiben. Nur Stacktrace analysieren und Hypothesen bilden ("Denken erzwingen").
    2.  **Bug Reproduction**: TDD-Ansatz. KI schreibt einen Unit-Test, der genau diesen Fehler provoziert (Test ist Rot).
    3.  **Root-Cause Fix**: KI repariert die Ursache, bis der Test Grün ist.
    4.  **Post-Mortem**: KI erklärt den Fix und prüft auf Architekturschulden.

---
#### **Chinese Translation (Detailed)**

**生成式人工智能在系统与软件开发中的应用 – 模块 5：软件设计与编码**

**1. 软件设计 – 基础**
*   **挑战（“写得快，但代码脏”）**: Gen-AI 能快速生成可运行的解决方案，但在缺乏引导时经常无视架构原则。典型的反模式 (Anti-Patterns)：
    *   *关注点未分离*: 数据库查询或硬件 I/O 直接写在业务逻辑中。
    *   *面条代码 (Spaghetti-Code)*: 在没有抽象的巨大函数中生成复杂逻辑。
    *   *不一致*: 每个文件的代码风格或错误处理方式不同。
*   **解决方案（建立护栏 Guardrails）**:
    1.  **架构**: 例如**六边形架构 (Ports & Adapters)**。严格分离核心逻辑与外部基础设施。*AI 指令*: “必须针对接口 (Interfaces/Ports) 编程，而不是具体实现。”
    2.  **文件结构 (Scaffolding/脚手架)**: 空仓库无法给 AI 提供上下文。必须先让 AI 生成完整的文件夹结构和初始配置。
    3.  **设计模式 (Design Patterns)**: AI 熟练掌握经典的 GoF 模式。*方法*: 不要告诉 AI“解决这个问题”，而是说“使用 Pattern X 解决这个问题”。
        *   *策略模式 (Strategy)*: 消除难读的 `if-else` 分支（例如根据模式选择不同的充电策略）。
        *   *工厂模式 (Factory)*: 将对象创建分离，避免硬耦合（便于测试时返回 `DummyMockSensor`）。
        *   *观察者模式 (Observer)*: 基于事件响应，而非浪费资源的轮询 (Polling)。
    4.  **编码规范 (Coding Guidelines)**: 作为 IDE 的上下文。Python 示例：*严格的类型提示 (Strict Type Hinting)*，*Google 风格的 Docstrings*，*显式的错误处理* (禁用泛型的 `except Exception`)，*禁止使用魔法数字 (Magic Numbers)*。

**2. 使用智能体和技能实现自动化 (“设计优先” 工作流)**
*   **问题（Prompt 陷阱）**: LLM 倾向于跳过设计直接写代码。在长对话中会出现 **“上下文腐烂” (Context Rot)**（AI 逐渐忘记最初的架构规定），以及 **“大爆炸陷阱” (Big-Bang-Falle)**（试图一次性生成大量代码）。
*   **解决方案（“文档优先”方法）**:
    *   步骤 1: 将规范定义为全局 Agent 技能 (`/python-guidelines`)。
    *   步骤 2: Agent 首先生成架构文档 (`software_architecture.md`)。
    *   步骤 3: Agent 根据文档执行 Scaffolding（生成 bash 脚本创建目录）。
    *   步骤 4: 制定实施计划 (`implementation_plan.md`) 作为微观设计的清单。
    *   步骤 5: 按计划分布引导实施，并通过 Skill 自我评估代码质量。
    *   步骤 6: 严格的 **审查与自我纠正**（将“写代码”的创造阶段与“查代码”的批判阶段强硬分离）。

**3. 软件单元测试 (TDD)**
*   **挑战**: AI 存在 **“快乐路径错觉” (Happy-Path-Illusion)**，经常写出同义反复的测试（先写代码再写测试，测试完美复刻了代码中的逻辑错误），并且容易和私有方法产生硬耦合。
*   **解决方案**: 结合六边形架构的 **测试驱动开发 (TDD)**。
    *   步骤 4b: 在写代码前，AI 必须先写 `test_plan.md` (包括正常路径、错误情况、边缘情况)。
    *   步骤 5a (红灯阶段): AI 针对接口编写测试并生成 **Mocks/Stubs**（例如 `MockDwdApiAdapter`），隔离外部系统。
    *   步骤 5b (绿灯阶段): AI 编写真实的实现代码，直至测试通过。
    *   步骤 7: **“破坏性 QA” 审查**。强制 AI 切换人设为极其苛刻的测试员，目标是故意让刚刚生成的代码崩溃，以找出未覆盖的边缘案例。

**4. 调试与 Bug 修复 (Debugging & Bugfixing)**
*   **死亡修复循环 (Fix-Loop of Death)**: 盲目把报错丢给 AI 会导致“打地鼠”现象（修复一个 Bug，引入两个新 Bug）、只治标不治本，以及因为粘贴大量残缺代码导致的“上下文污染”。
*   **结构化的 Bug 修复工作流 (假设驱动)**:
    1.  **隔离与分析**: 严禁 AI 立即写代码！强制 AI 分析堆栈并在框架上下文中提出三个根本原因的“假设”。
    2.  **Bug 重现 (TDD 整合)**: AI 必须先写一个会失败的单元测试，精准触发这个 Bug。
    3.  **根本原因修复**: AI 修复代码，直到新测试和旧测试全部通过。
    4.  **事后分析 (Post-Mortem)**: AI 用三句话解释修复原理，并确认六边形架构未被破坏。

---
#### **English Translation (Detailed)**

**Generative AI in System and Software Development – Module 5: SW-Design and Coding**

**1. Software Design – Basics**
*   **The Challenge ("Fast but dirty code")**: Gen-AI generates working solutions quickly but often ignores architectural principles without guidance. Typical Anti-Patterns:
    *   *Lack of Separation of Concerns*: I/O or DB queries written directly into business logic.
    *   *Spaghetti Code*: Complex logic generated in massive functions with no abstraction.
    *   *Inconsistency*: Different programming styles or error handling in every file.
*   **The Solution (Establishing Guardrails)**:
    1.  **Architecture**: e.g., **Hexagonal Design (Ports & Adapters)**. Strict separation of core logic (Domain) from outer influences. *AI Instruction*: "Program against interfaces (Ports), not concrete implementations."
    2.  **File Structure (Scaffolding)**: An empty repo provides no context. The AI must first generate a consistent folder hierarchy.
    3.  **Design Patterns**: LLMs execute Gang of Four patterns flawlessly. *Approach*: Don't say "Solve the problem", say "Solve the problem using Pattern X".
        *   *Strategy Pattern*: Eliminates unreadable `if-else` blocks (e.g., dynamic charging strategies).
        *   *Factory Pattern*: Prevents hard coupling when creating objects (delivers a `DummyMockSensor` for tests).
        *   *Observer Pattern*: Event-driven reactions instead of processor-blocking polling.
    4.  **Coding Guidelines**: Defined as IDE context. Python examples: *Strict Type Hinting*, *Google-Style Docstrings*, *Explicit Error Handling* (no generic `except Exception`), *No Magic Numbers*.

**2. Automation with Agents and Skills (The "Design-First" Workflow)**
*   **The Problem (Prompt Trap)**: LLMs want to bypass design and write code immediately. Long chats lead to **"Context Rot"** (the model slowly forgets architectural guidelines) and the **"Big-Bang Trap"** (trying to generate 500 lines of code at once).
*   **The Solution ("Document-First" Approach)**:
    *   Step 1: Define guidelines as a central Agent Skill (`/python-guidelines`) triggered at every step.
    *   Step 2: Agent creates a `software_architecture.md` document first.
    *   Step 3: Agent executes scaffolding (creates folders and empty files via a bash script) based strictly on the document.
    *   Step 4: Breakdown task into an `implementation_plan.md` checklist.
    *   Step 5: Guided implementation, step-by-step, self-evaluated by the Skill.
    *   Step 6: **Review & Self-Correction**. A hard separation between the "creative phase" and "critic phase" to fix architectural violations autonomously.

**3. Software Unit-Test (TDD)**
*   **The Challenge**: The **"Happy-Path Illusion"** (LLMs ignore edge cases) and Tautological Tests (writing tests after code often mirrors the code's logical flaws).
*   **The Solution**: **Test-Driven Development (TDD)** with Hexagonal Architecture.
    *   Step 4b: The AI must write a `test_plan.md` (Happy Path, Error cases, Edge Cases) against the Port interface *before* coding.
    *   Step 5a (RED Phase): AI generates **Mocks/Stubs** (e.g., `MockDwdApiAdapter`) and failing tests to isolate domain logic from external systems.
    *   Step 5b (GREEN Phase): AI implements the adapter until tests pass.
    *   Step 7: **"Destructive QA" Review**. Force a hard persona switch. The AI acts as an extremely critical destroyer aiming to deliberately crash its own generated code to find blind spots.

**4. Debugging & Bugfixing**
*   **The "Fix-Loop of Death"**: Blindly pasting stack traces leads to "Whack-a-Mole" (fixing one line breaks two others), symptom treatment (empty exception blocks), and context pollution.
*   **Structured Bugfixing Workflow (Hypothesis-Driven)**:
    1.  **Isolation & Analysis**: Forbid code generation! Force the AI to analyze the stack trace and state 3 hypotheses for the root cause.
    2.  **Bug Reproduction (TDD)**: The AI writes a failing unit test that exactly provokes the bug.
    3.  **Root-Cause Fix**: The AI fixes the implementation until the new test and all old tests pass.
    4.  **Post-Mortem**: The AI explains the fix in 3 sentences and ensures Hexagonal boundaries remain intact.