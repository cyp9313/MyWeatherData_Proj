This document summarizes the content of the presentation "Generative AI in System and Software Development - Module 2 - Requirement Engineering".

## `GenAI in SW Development - Module 2.md`

### 2. Generative AI in System and Software Development – Module 2: Requirement Engineering

#### **Chinese Translation (中文翻译)**

---

### **生成式人工智能在系统与软件开发中的应用 – 模块2：需求工程**

---

#### **Agenda (目录)**

1.  **需求工程基础 (Grundlagen Requirement Engineering)**
    *   **核心概念**:
        *   **史诗 (Epic)**: 描述战略层面上的大型特性或计划。
        *   **用户故事 (User Story)**: 从用户角度出发，将史诗分解为可交付的增量，聚焦于“谁 (Wer)”、“什么 (Was)”和“为什么 (Warum)”。
        *   **功能需求 (Functional Requirement)**: 从系统角度出发，详细说明技术实现，聚焦于“如何 (Wie)”和系统“必须做什么 (Was das System tun muss)”。
    *   **GenAI 的作用**:
        *   **史诗层面**: 协助进行功能头脑风暴、技术选型、识别依赖关系，并建议如何将史诗“切片 (Slicing)”为更小的逻辑组件。
        *   **用户故事层面**: 根据史诗描述生成用户故事，并推导和完善在手动创建中容易被忽略的边缘案例（Edge Case）的验收标准。
        *   **功能需求层面**: 通过注入系统架构文档来进行“情境工程”，将自然语言的用户故事转换为正式需求，并自动审查功能需求中的矛盾、模糊之处或缺失的参数。
    *   **EARS 语法**: 介绍 EARS（Easy Approach to Requirements Syntax），一种将自然语言约束在清晰、可测试规则中的文本模板。GenAI 非常擅长将用户故事精确地翻译成严格的 EARS 模式。

2.  **在需求工程中与 AI 协同工作 (Inhaltliches arbeiten mit AI im Requirement Engineering)**
    *   **从产品概念到史诗的结构化流程**:
        *   **阶段1-3**: 使用 AI 定义领域（情境工程）、产生广泛的功能创意（发散性思维），并作为研究助理进行技术选型。
        *   **阶段4-6**: 对照系统边界进行可行性检查（收敛性过滤）、将验证后的想法整合成结构化的史诗，并识别史诗间的依赖关系（数据流、接口、时间阻塞）。
    *   **史诗切片 (Epic Slicing)**: 敏捷开发需要“垂直切片”（基于功能），以快速生成可测试的价值。GenAI 可以提出逻辑切片策略，例如先实现“快乐路径 (Happy Path)”，再处理边缘案例。
    *   **用户故事**: GenAI 将技术笔记翻译成用户视角，并可根据 BDD (行为驱动开发) 格式（Given/When/Then）来制定验收标准。
    *   **验收标准和边缘案例**: 利用 AI 作为“魔鬼代言人 (Advocatus Diaboli)”来思考系统可能出现故障的场景，并为这些场景定义可测试的验收标准。
    *   **功能需求**: GenAI 负责将“用户焦点”转换为“系统焦点”，并严格遵循 EARS 等正式模板，以消除模糊性。同时，通过明确指令（如“必须使用‘MUSS’或‘DARF NICHT’”）来避免生成不确定的弱表达。

3.  **通过自定义提示、技能和智能体实现自动化 (Automatisierung mit Custom Prompts, Skills, Agents)**
    *   **混合设置 (Hybrid Setup)**: 结合使用快速的、模板化的命令（Prompts）来处理宏观结构，并利用专门的虚拟专家（Agents）进行严格的方法论细化。
    *   **项目文件夹结构**:
        *   **`copilot-instructions.md`**: 为所有工具和智能体提供全局系统上下文。
        *   **`/prompts`**: 存放用于处理史诗（如功能头脑风暴）的模板。
        *   **`/agents`**: 定义虚拟专家，如 `@Story_Crafter`（故事创建者）、`@Req_Engineer`（需求工程师）。
        *   **`/skills`**: 智能体的“工具箱”，如 INVEST 原则、BDD 格式、EARS 语法等。
    *   **智能体示例**:
        *   **故事创建者 (@Story_Crafter)**: 专注于将史诗切片转化为精确的用户故事，并强制对照 `/invest_criteria` 和 `/bdd_format` 等技能进行检查。
        *   **需求工程师 (@Req_Engineer)**: 将敏捷故事翻译成严格使用 EARS 语法的、可测试的硬性系统需求。
        *   **需求审查员 (@Req_Reviewer)**: 一个专职的审查智能体，不生成内容，只负责对照清单（如 `/req_review` 技能）检查工作产品，寻找矛盾、不一致和信息缺失。
    *   **工作流**:
        *   **基础**: `copilot-instructions.md` 提供全局上下文。
        *   **头脑风暴/结构化**: 使用自定义的 `/epic_brainstorming` 和 `/epic_slicing` 提示来处理和分解想法。
        *   **用户层面**: `@Story_Crafter` 利用技能创建用户故事和验收标准。
        *   **系统层面**: `@Req_Engineer` 利用技能生成功能需求。
        *   **质量关口**: `@Req_Reviewer` 对最终产出物进行审查。

---

#### **English Translation**

---

### **Generative AI in System and Software Development – Module 2: Requirement Engineering**

---

#### **Agenda**

1.  **Fundamentals of Requirement Engineering**
    *   **Core Concepts**:
        *   **Epic**: Describes a large feature or initiative at a strategic level.
        *   **User Story**: Breaks down epics into deliverable increments from the user's perspective, focusing on "Who," "What," and "Why."
        *   **Functional Requirement (FR)**: Details the technical implementation from the system's perspective, focusing on "How" and what "The system must do."
    *   **How GenAI Helps**:
        *   **At the Epic Level**: Assists with brainstorming features, scouting for technologies, identifying dependencies, and suggesting ways to "slice" an epic into smaller, logical components.
        *   **At the User Story Level**: Generates user stories from an epic description and helps derive and complete acceptance criteria for edge cases often overlooked in manual creation.
        *   **At the Functional Requirement Level**: Performs "Context Engineering" by being fed system architecture documents, transforms natural language user stories into formal requirements, and automatically reviews FRs for contradictions, ambiguities, or missing parameters.
    *   **EARS Syntax**: Introduces the "Easy Approach to Requirements Syntax" (EARS), a template that constrains natural language into a clear, testable structure. GenAI is exceptionally good at translating user stories precisely into these strict EARS patterns.

2.  **Working with AI in Requirement Engineering**
    *   **Structured Funnel from Product Idea to Epic**:
        *   **Phases 1-3**: Use AI to define the playing field (Context Engineering), generate a wide range of feature ideas (Divergent Thinking), and act as a research assistant for technology scouting.
        *   **Phases 4-6**: Conduct a reality check against system boundaries (Convergent Filtering), consolidate the validated idea into a structured epic, and identify inter-epic dependencies (data flows, interfaces, temporal blockers).
    *   **Epic Slicing**: Agile demands "vertical slicing" (function-based) to generate testable value quickly. GenAI can propose logical slicing strategies, such as implementing the "Happy Path" first, then addressing edge cases.
    *   **User Stories**: GenAI translates technical notes into the user's perspective and can formulate acceptance criteria based on the BDD (Behavior-Driven Development) format (Given/When/Then).
    *   **Acceptance Criteria & Edge Cases**: Use AI as an "Advocatus Diaboli" (Devil's Advocate) to brainstorm scenarios where the system could fail and define testable acceptance criteria for them.
    *   **Functional Requirements**: GenAI is responsible for translating the "user focus" to the "system focus" and strictly adhering to formal templates like EARS to eliminate ambiguity. It can also be instructed to avoid weak phrasing by using strict prohibitions (e.g., "Exclusively use 'MUST' or 'MUST NOT'").

3.  **Automation with Custom Prompts, Skills, and Agents**
    *   **The Hybrid Setup**: Combines fast, template-based commands (Prompts) for high-level structures with specialized virtual experts (Agents) for rigorous, methodical elaboration.
    *   **Project Folder Structure**:
        *   **`copilot-instructions.md`**: Provides the global system context for all tools and agents.
        *   **`/prompts`**: Contains templates for working with epics (e.g., feature brainstorming).
        *   **`/agents`**: Defines the virtual experts, such as `@Story_Crafter`, `@Req_Engineer`.
        *   **`/skills`**: The "toolbox" for the agents, containing definitions for INVEST criteria, BDD format, EARS syntax, etc.
    *   **Agent Examples**:
        *   **The Story Crafter (@Story\_Crafter)**: Specializes in deriving precise user stories from epic slices, enforcing checks against skills like `/invest_criteria` and `/bdd_format`.
        *   **The Requirement Engineer (@Req\_Engineer)**: Translates agile stories into hard, testable system requirements using the strict EARS syntax.
        *   **The Requirement Reviewer (@Req\_Reviewer)**: A dedicated agent that generates nothing but only reviews work products against checklists (its `/req_review` skill) to find contradictions, inconsistencies, and missing information.
    *   **Workflow**:
        *   **Basis**: `copilot-instructions.md` provides the global context.
        *   **Brainstorming/Structuring**: Use custom prompts like `/epic_brainstorming` and `/epic_slicing` to process and break down ideas.
        *   **User-Level**: `@Story_Crafter` uses skills to create user stories and acceptance criteria.
        *   **System-Level**: `@Req_Engineer` uses its skill to generate functional requirements.
        *   **Quality Gate**: `@Req_Reviewer` performs the final review of the deliverables.

---

#### **Deutsche Zusammenfassung (德语总结)**

---

### **Generative KI in der System- und Softwareentwicklung – Modul 2: Requirement Engineering**

---

#### **Agenda (Inhalt)**

1.  **Grundlagen Requirement Engineering**
    *   **Kernkonzepte**:
        *   **Epic**: Beschreibt eine umfangreiche Initiative auf strategischer Ebene.
        *   **User Story**: Bricht Epics aus der Nutzerperspektive in lieferbare Inkremente herunter (Fokus: Wer, Was, Warum).
        *   **Functional Requirement (FR)**: Detailliert die technische Umsetzung aus der Systemperspektive (Fokus: Wie und Was das System tun muss).
    *   **Wie Gen-KI hilft**:
        *   **Epic-Ebene**: Hilft beim Brainstorming von Features, Scouting von Technologien, Identifizieren von Abhängigkeiten und schlägt sinnvolle "Schnitte" (Slicing) vor.
        *   **User-Story-Ebene**: Generiert User Stories aus einer Epic-Beschreibung und leitet Akzeptanzkriterien für Edge Cases (z.B. Verhalten bei Sensorausfall) ab.
        *   **FR-Ebene**: Transformiert natürlichsprachliche User Stories in formale Requirements und prüft diese automatisiert auf Widersprüche oder fehlende Parameter.
    *   **EARS-Syntax**: Die KI ist besonders gut darin, User Stories exakt in die strengen Muster der EARS-Syntax (Easy Approach to Requirements Syntax) zu übersetzen, um Mehrdeutigkeit zu reduzieren.

2.  **Inhaltliches Arbeiten mit KI im Requirement Engineering**
    *   **Strukturierter Trichter (Von der Produktidee zum Epic)**: Ein 6-Phasen-Prozess, der KI für Context Engineering, divergentes Denken (Feature-Ideen), Technology Scouting, konvergentes Filtern (Reality Check), Konsolidierung zum Epic und Vernetzung von Epics nutzt.
    *   **Epic Slicing**: Agil erfordert "vertikales Slicing", um schnell testbaren Wert zu generieren. Die KI kann logische Slices vorschlagen (z.B. "Happy Path" zuerst, dann Edge Cases).
    *   **User Stories & Akzeptanzkriterien**: Die KI übersetzt technische Notizen in die Nutzerperspektive und formuliert Akzeptanzkriterien im BDD-Format (Given/When/Then). Als "Advocatus Diaboli" deckt sie realistische Edge Cases auf.
    *   **Functional Requirements**: Die KI überführt den Nutzer-Fokus in den System-Fokus und hält sich strikt an formale Schablonen wie EARS, um weiche Formulierungen zu vermeiden (Anweisung: "Verwende ausschließlich MUSS oder DARF NICHT").

3.  **Automatisierung mit Custom Prompts, Skills, Agents**
    *   **Hybrides Setup**: Kombination von schnellen, schablonenhaften Prompts für grobe Strukturen mit spezialisierten virtuellen Experten (Agents) für die methodische Ausarbeitung.
    *   **Ordnerstruktur (`.github/`)**:
        *   **`copilot-instructions.md`**: Globaler Projektkontext.
        *   **`/prompts`**: Schablonen für wiederkehrende Aufgaben (z.B. Epic-Brainstorming).
        *   **`/skills`**: Das "Handwerkszeug" der Agents (z.B. INVEST-Kriterien, BDD-Format).
        *   **`/agents`**: Die virtuellen Experten selbst (z.B. `@Story_Crafter`).
    *   **Agenten-Beispiele**:
        *   **@Story_Crafter**: Leitet aus Epic-Slices präzise User Stories ab und formuliert Akzeptanzkriterien.
        *   **@Req_Engineer**: Übersetzt agile Stories in harte, testbare System-Requirements mittels EARS-Syntax.
        *   **@Req_Reviewer**: Ein dedizierter Prüf-Agent, der nichts generiert, sondern Arbeitsprodukte auf Konformität und Qualität prüft.
    *   **Workflow**: Ein klar definierter Prozess von der Ideen-Generierung mit Prompts über die Ausarbeitung auf User- und System-Ebene durch Agents bis hin zum finalen Qualitäts-Check durch den Reviewer-Agent.

---

