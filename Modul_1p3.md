This document summarizes the content of the presentation "Generative AI in System and Software Development - Module 1 - Introduction".

## `GenAI in SW Development - Module 1.md`

### 3. Generative AI in System and Software Development – Module 1: Introduction

#### **Chinese Translation (中文翻译)**

---

### **生成式人工智能在系统与软件开发中的应用 – 模块1：引言**

---

#### **Agenda (目录)**

1.  **生成式 AI、大语言模型 (LLM) 和智能体 AI (Agentic AI) 的基础与工作原理**
    *   AI 领域的定位
    *   工作原理 I：Tokenization 和概率
    *   工作原理 II：Transformer 架构
    *   与 LLM 协同工作 I：风险与道德
    *   与 LLM 协同工作 II：聊天、提示 (Prompting) 和上下文 (Context)
    *   与 LLM 协同工作 III：智能体 AI
    *   GenAI 使用的成本和定价模型
2.  **定制化：提示 (Prompts)、技能 (Skills)、智能体 (Agents)**
    *   定制化概念
    *   `copilot-instructions.md`
    *   自定义提示
    *   技能
    *   智能体
3.  **引言：V-模型产品开发中的 AI 智能体**
    *   **基本考量**:
        *   **理想中的完美 AI**: 在一个理想世界里，AI 可以无缝地将需求工程的产出直接转化为通过验证测试的产品。但在现实中，由于变体管理、安装空间、组件和制造等边界条件，AI 需要处理设计约束。
        *   **有缺陷的 AI**: 现实中的 AI 是会犯错的 (fehlerbehaftete AI)。如果一个流程有多个步骤，而 AI 在每一步都有一个很小但非零的错误率（例如，99% 的准确率），那么整个流程端到端无差错的概率会随着步骤的增加而急剧下降。
    *   **应对措施**:
        *   在 V-模型的每个关键阶段（需求工程、架构、设计、实施）之后，引入一个由 AI 辅助的“审查 (Review)”环节。
        *   同样，在测试的每个阶段（单元测试、集成测试、验证测试）也引入 AI 辅助审查。
        *   通过这种方式，可以在每个步骤后及时发现并纠正错误，从而将端到端的成功率从一个很低的水平（例如，~67/100）提升到一个非常高的水平（例如，~99/100）。
    *   **结论 (Fazit)**:
        *   **智能体 AI (Agentic-AI)**: 需要构建和编排一个智能体系统。
        *   **智能体质量**: 高质量的智能体可以提高命中率，减少流程步骤，从而对 Token 消耗和成本产生积极影响。
        *   **审查与测试流程**: 审查和测试仍然是必不可少的，并且 AI 智能体也可以用于这些审查和测试任务。
        *   **工程人员的转变**: 工程师的角色将从“领域专家”转变为“通才”，他们需要承担端到端的责任，而 AI 专业知识是基本前提。

---

#### **English Translation**

---

### **Generative AI in System and Software Development – Module 1: Introduction**

---

#### **Agenda**

1.  **Basics and Functionality of Generative AI, Large Language Models (LLMs), and Agentic AI**
    *   Positioning in the AI Landscape
    *   How it Works I: Tokenization and Probability
    *   How it Works II: The Transformer Architecture
    *   Working with LLMs I: Risks and Ethics
    *   Working with LLMs II: Chat, Prompting, and Context
    *   Working with LLMs III: Agentic AI
    *   Costs and Pricing Models for GenAI Usage
2.  **Customization: Prompts, Skills, Agents**
    *   Concept of Customization
    *   `copilot-instructions.md`
    *   Custom Prompts
    *   Skills
    *   Agents
3.  **Introduction: AI Agents in Product Development in the V-Model**
    *   **Fundamental Considerations**:
        *   **Perfect AI**: In an ideal world, a perfect AI could seamlessly transform the output of Requirement Engineering directly into a product that passes a Validation Test. In reality, AI must handle design constraints due to factors like variant management, installation space, components, and manufacturing boundary conditions.
        *   **Fallible AI**: Real-world AI is fallible (fehlerbehaftete AI). If a process consists of multiple steps and the AI has a small but non-zero error rate at each step (e.g., 99% accuracy), the probability of the entire end-to-end process being flawless drops sharply as the number of steps increases.
    *   **Countermeasures**:
        *   Introduce an AI-assisted "Review" step after each critical phase on the left side of the V-Model (Requirement Engineering, Architecture, Design, Implementation).
        *   Similarly, introduce AI-assisted reviews on the right side for each testing phase (Unit Test, Integration Test, Validation Test).
        *   By doing this, errors can be caught and corrected promptly after each step, significantly raising the end-to-end success rate from a very low number (e.g., ~67/100) to a very high one (e.g., ~99/100).
    *   **Conclusion (Fazit)**:
        *   **Agentic-AI**: The orchestration of an agent system is required.
        *   **Quality of Agents**: High-quality agents increase the hit rate and reduce the number of process steps, which in turn has a positive impact on token consumption and costs.
        *   **Review and Test Processes**: These processes remain necessary, and AI agents can also be utilized for these review and testing tasks.
        *   **Shift in Engineering**: The role of engineers will shift from being "domain experts" to "generalists" who take on end-to-end responsibility, with AI expertise being a fundamental prerequisite.

---


#### **Deutsche Zusammenfassung (德语总结)**

---

### **Generative KI in der System- und Softwareentwicklung – Modul 1: Einführung**

---

#### **Agenda (Inhalt)**
*(This section summarizes point 3 of the agenda)*

3.  **Einführung: AI Agents in der Produktentwicklung im V-Modell**
    *   **Grundlegende Überlegungen**:
        *   **Perfekte KI**: In einer idealen Welt würde die KI Anforderungen direkt in ein validiertes Produkt umwandeln. Die Realität erfordert jedoch die Berücksichtigung von Randbedingungen wie Variantenmanagement oder Bauraum.
        *   **Fehlerbehaftete KI**: Realistische KI hat eine Fehlerquote. Bei einem mehrstufigen Prozess sinkt die Wahrscheinlichkeit eines fehlerfreien Gesamtergebnisses mit jedem Schritt exponentiell. (z.B. bei 99% Trefferquote pro Schritt ist die Erfolgswahrscheinlichkeit nach 10 Schritten nur noch ~90%, bei 95% nur noch ~60%).
    *   **Maßnahmen**:
        *   Einführung von KI-assistierten "Review"-Phasen nach jedem wesentlichen Schritt im V-Modell (Requirement Engineering, Architektur, Design, Implementierung).
        *   Ebenso werden auf der rechten Seite des V-Modells die Testphasen (Unit Test, Integration Test, Validation Test) durch KI-Reviews unterstützt.
        *   Durch diese iterativen Qualitäts-Checks wird die Gesamt-Erfolgsquote drastisch erhöht (z.B. von ~67/100 auf ~99/100).
    *   **Fazit**:
        *   **Agentic-AI**: Die Orchestrierung eines Agenten-Systems ist der Schlüssel.
        *   **Qualität der Agents**: Eine hohe Trefferquote der Agenten reduziert die Anzahl der Prozessschritte und damit den Token-Verbrauch und die Kosten.
        *   **Review- und Testprozesse**: Bleiben unerlässlich, können aber ebenfalls durch KI-Agenten unterstützt werden.
        *   **Wandel im Engineering**: Die Rolle des Ingenieurs verschiebt sich vom "Domänen-Experten" zum "Generalisten" mit End-to-End-Verantwortung. KI-Expertise wird zur Grundvoraussetzung.

---
