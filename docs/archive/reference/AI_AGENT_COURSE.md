**The New SDLC With Vibe Coding From ad-hoc prompting to Agentic Engineering** 

**Authors: Addy Osmani, Shubham Saboo, and Sokratis Kartakis** 

The new SDLC with vibe coding 

## **Acknowledgements** 

## **Content contributors** 

Elia Secchi Julia Wiesinger Anant Nawalgaria 

## **Curators and editors** 

Anant Nawalgaria 

## **Designer** 

Michael Lanning 

May 2026 

2 

## **Table of contents** 

|Introduction|6|
|---|---|
|Why this paper, why now|9|
|Who this paper is for|9|
|The shift from syntax to intent|10|
|AI Agents: A Quick Refresher|10|
|What is vibe coding?|11|
|The spectrum: vibe coding to agentic engineering|12|
|Context engineering: the real skill|15|
|The new software development life cycle|19|
|The traditional SDLC under pressure|19|
|How AI transforms each phase|21|
|Requirements and planning|21|
|Design and architecture|21|
|Implementation|22|
|Testing and quality assurance|22|



## **Table of contents** 

|Code review and deployment|23|
|---|---|
|Maintenance and evolution|24|
|The factory model: building the system that builds software|24|
|Harness Engineering: What surrounds the model|26|
|What's in the harness|28|
|Harness in SDLC|29|
|1. Requirements, Planning, & Architecture (Configuring the Harness)|29|
|2. Implementation (Running the Harness)|29|
|3. Testing & QA (The Feedback Loop)|30|
|4. Code Review, Deployment, & Maintenance (Observing the Harness)|30|
|The developer's evolving role: conductors and orchestrators|31|
|The conductor: hands-on, real-time direction|32|
|The orchestrator: async, multi-agent delegation|33|
|The 80% problem|34|
|Coding agents in practice|35|



## **Table of contents** 

|Where coding agents fit in the developer's day|35|
|---|---|
|Vibe Coding Production-ready Agents|36|
|The Economics of AI Development|39|
|The Hidden Debt of Vibe Coding (Low CapEx, High OpEx)|40|
|The Investment of Agentic Engineering (High CapEx, Low OpEx)|41|
|Context Engineering as a Financial Lever|41|
|Scaling Efficiency via Dynamic Context and Skills|42|
|Intelligent Model Routing|42|
|Where to start|43|
|For individual developers|43|
|For engineering leaders|44|
|For organizations|45|
|Conclusion: Intent as the new Interface|47|
|Endnotes|49|



The new SDLC with vibe coding 

The most profound shift in software engineering isn't a new language, framework, or cloud service. It's the transition from writing code to expressing intent, and trusting intelligent systems to translate that intent into working software. 

## **Introduction** 

For most of computing history, programming has been an act of translation: understand the problem in human terms, design a solution in abstract terms, then render it in syntax a machine can execute. Each step introduces friction. That friction is now collapsing. Software engineering is undergoing its most significant transformation since the introduction of 

May 2026 

6 

The new SDLC with vibe coding 

high-level programming languages. For decades, the developer's primary interface with the machine has been syntax: curly braces, semicolons, type annotations, and the precise grammar of programming languages. That era is ending. 

A new paradigm has arrived in which developers express what they want to build rather than how to build it. The machine handles implementation. The human provides intent, architecture, and judgment. This isn't a distant future - it's the daily reality for a rapidly growing number of professional developers. As of early 2026, 85% of professional developers regularly use AI Coding Agents, 51% use them daily, and an estimated 41% of all new code is AI-generated.[1] 

This shift didn't happen overnight. It began with autocomplete - simple token prediction in the editor. Then came inline code suggestions that could complete entire functions. Next, chat-based interfaces allowed developers to describe features in natural language and receive working implementations. Now, fully autonomous agents can clone repositories, plan multi-file changes, execute them in sandboxed environments, run tests, and submit pull requests - all without a human typing a single line of code. 

May 2026 

7 

The new SDLC with vibe coding 

Figure 1: From Autocomplete to Autonomy 

The implications for the software development life cycle (SDLC) are profound. Every phase - from requirements gathering to deployment to maintenance - is being reshaped by AI capabilities. But this transformation isn't uniform or simple. The spectrum ranges from casual "vibe coding," where a developer prompts an AI and accepts whatever comes back, to disciplined "agentic engineering," where AI acts as a powerful implementation engine within carefully designed systems of constraints, tests, and feedback loops, with humans retaining oversight over architecture, correctness, and quality. 

The distinction matters. Telling a CTO that your team is vibe coding their payment processing system will, and should, raise alarm bells. Telling that same CTO that your team practices agentic engineering, with AI handling implementation under human-designed constraints while test coverage ensures correctness, is a fundamentally different conversation. 

May 2026 

8 

The new SDLC with vibe coding 

This paper provides the foundation for that conversation. We trace the spectrum from casual vibe coding to disciplined agentic engineering, examine how the developer's role is shifting from writing code to exercising judgment — from conductor to orchestrator — and lay out what it takes to adopt these tools in ways that produce software you can actually depend on. 

## **Why this paper, why now** 

New tools, capabilities, and paradigms emerge weekly. Engineering teams need a framework for making sense of this landscape - not a snapshot that will be outdated in months, but a set of principles and mental models that will remain useful as the specific tools evolve. 

## **Who this paper is for** 

This paper is for software engineers, engineering managers, architects, and technical leaders who want to understand how AI is reshaping the SDLC and adopt these new capabilities without sacrificing the discipline that production software demands. We assume familiarity with modern software development practices but not with the specifics of AI or machine learning. 

May 2026 

9 

The new SDLC with vibe coding 

## **The shift from syntax to intent** 

Before we go further, we need a shared picture of what an agent is and what vibe coding actually means. Both terms have accumulated enough meanings that they need to be unpacked carefully. 

## **AI Agents: A Quick Refresher** 

An AI agent is a software system that perceives a goal, plans steps to reach it, takes actions through tools, observes the results, and iterates until the goal is met or it hits a stopping condition. Where a chatbot produces a response and waits for the next prompt, an agent runs its own loop. You give it a goal at the top, then it decides what to do next at each step. 

Figure 2: The Agent Loop - Perceive, plan, act, observe, iterate. 

May 2026 

10 

The new SDLC with vibe coding 

Every agent, however simple or sophisticated, is built from five parts. The November 2025 Introduction to Agents whitepatper covers each in depth.² For our purposes here, the short version: 

- **The model** is the reasoning engine. It reads the current context, decides what should happen next, and produces the next thought, the next tool call, or the next message. 

- **Tools** connect the model to the world. They include APIs the agent can call, code it can execute, databases it can query, and other agents it can delegate to. 

- **Memory** is the state. It allows the agent to recall past interactions, retrieve projectspecific rules, and retain context across sessions so it never starts from a blank slate. 

- **Orchestration** is the code that runs the loop. It assembles the context for each model call, dispatches tool calls, captures their results, and decides whether to continue. 

- **Deployment** is what turns the prototype into a service: hosting, identity, observability, and the production infrastructure the agent runs on. 

These four parts work together in a continuous loop: get the mission, scan the scene, think it through, take action, observe and iterate. The loop is the beating heart of every agent. Everything else in this paper, and everything in the rest of the course, is a variation on this loop. 

## **What is vibe coding?** 

In February 2025, Andrej Karpathy posted a description of a new way of programming that resonated widely across the software engineering community. He described an approach where you "fully give in to the vibes, embrace exponentials, and forget that the code even 

May 2026 

11 

The new SDLC with vibe coding 

exists." In this mode, a developer describes what they want in natural language, accepts the AI's output, and when something breaks, copies the error message back into the prompt and asks the AI to fix it.[2] 

The term went viral because it captured something real: many developers were already working this way but hadn't had language for it. Within months, "vibe coding" became a common descriptor for any AI-assisted development workflow, which created confusion. Is a senior engineer using an AI assistant to implement a well-specified feature "vibe coding"? Is a team using AI agents to execute a carefully planned architecture? The term was applied so broadly it began to lose meaning. 

By early 2026, Karpathy himself acknowledged that the original framing was too narrow, introducing the term "agentic engineering" to describe the more disciplined end of the spectrum.[4] 

## **The spectrum: vibe coding to agentic engineering** 

Rather than treating vibe coding and agentic engineering as a binary, we find it more useful to think of them as endpoints on **a spectrum** . The key differentiator is not whether you use AI. It's how much structure, verification, and human judgment surrounds the AI's output. 

May 2026 

12 

The new SDLC with vibe coding 

**==> picture [470 x 356] intentionally omitted <==**

**----- Start of picture text -----**<br>
Dimension Vibe Coding Structured AI-Assisted  Agentic<br>Coding Engineering<br>Intent specification Casual natural  Detailed prompts  Formal specs,<br>language prompts with examples  architecture docs,<br>and constraints<br>memory files<br>"Does it seem  Manual  Automated test<br>Verification<br>to work?" testing, spot-checking suites, CI/CD gates,<br>LM judges<br>Codebase  Minimal; developer  Selective review of  Comprehensive<br>understanding may not read the  critical paths review of architecture;<br>generated code AI handles<br>implementation details<br>Error handling Copy-paste error  Developer diagnoses  Agents self-diagnose<br>messages back to  root cause, AI  within defined bounds;<br>the AI humans handle<br>implements fix<br>architectural issues<br>Appropriate scope Prototypes,  Features within  Production systems,<br>scripts, personal  established codebases team-scale<br>projects, hackathons development<br>Risk profile High; acceptable for  Moderate; human  Low; systematic<br>disposable code judgment at  verification at<br>key checkpoints every stage<br>**----- End of picture text -----**<br>


Table 1: The Spectrum from Vibe Coding to Agentic Engineering 

May 2026 

13 

The new SDLC with vibe coding 

Figure 3: The Vibe Coding to Agentic Engineering Spectrum 

**==> picture [79 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
     Applied Tip: Ww<br>**----- End of picture text -----**<br>


The right position on this spectrum depends on the stakes. A weekend prototype can be pure vibe coding. A production API handling financial transactions demands agentic engineering. Most real work falls somewhere in between, and the skill is knowing where to draw the line for each task. 

The single biggest differentiator between the two ends is how outputs get verified. In vibe coding, verification is optional; the developer runs the code and checks if it seems right. In agentic engineering, two mechanisms work together. **Tests** verify the deterministic parts of the system: a function given this input produces that output. **Evaluations** , or _evals_ , verify the 

May 2026 

14 

The new SDLC with vibe coding 

parts that are not deterministic: did the agent take the right trajectory of steps, choose the right tools, and produce a final response that meets the quality bar. Tests are checked by code; evals are checked by labelled datasets, scoring rubrics, and LM judges. Without both, the practice is always vibe coding, regardless of how sophisticated the prompts are. 

## **Context engineering: the real skill** 

As the field has matured, a key insight has emerged: the quality of AI-generated code depends less on the cleverness of your prompts and more on the quality of the _context_ provided. This realization has given rise to the concept of context engineering, the practice of providing AI agents with rich, structured information about your codebase, architecture, conventions, and intent.[5] 

Developers must consider six primary types of context: 

- **Instructions:** The agent's core role, goals, and operational boundaries. 

- **Knowledge:** Retrieved documents, architectural diagrams, and domain-specific data. 

- **Memory:** Short-term session logs (what just happened) and long-term persistent state (what the project is). 

- **Examples:** Few-shot behavioral demonstrations and codebase reference patterns. 

- **Tools:** The precise definitions of the APIs, scripts, and external services the agent 

- can invoke. 

- **Guardrails:** Hard constraints, formatting rules, and safety validations. 

May 2026 

15 

The new SDLC with vibe coding 

In AI code generation, context engineering involves carefully balancing which of these six elements the agent possesses _upfront_ versus what it can retrieve on _demand_ . This creates a critical separation between static and dynamic context. 

**Static context** is always loaded: system instructions, rule files ( `AGENTS.md` , `CLAUDE.md` , `GEMINI.md` ), global memory, and persona definitions. It defines who the agent is and how it behaves. Static context is expensive because every token is present in every interaction, regardless of relevance. 

**Dynamic context** is loaded on demand: skill instructions triggered by task matching, tool results retrieved during execution, documents fetched from RAG pipelines, and windowed session history. Dynamic context is efficient because the agent pays the token cost only when the information is needed. 

The design decision of what belongs in static context versus dynamic context is a genuine engineering trade-off. Too much static context wastes tokens and dilutes signals. Too little means the agent forgets critical rules. The best systems treat this boundary as a first-class architectural decision, reviewed and versioned like any other configuration. 

May 2026 

16 

The new SDLC with vibe coding 

Figure 4: Context Engineering — Static vs. Dynamic 

The most powerful pattern for managing dynamic context is **Agent Skills** : structured, portable packages of procedural knowledge that the agent loads only when the task calls for it. 

Rather than embedding every piece of specialized knowledge into the agent's system prompt, skills allow the agent to remain a lightweight generalist that flexes into specialist roles on demand through progressive disclosure. The agent sees only lightweight metadata at startup, loads full instructions when a task matches, and pulls deep reference material only when explicitly needed. The result is that an agent can carry dozens of specialized capabilities while paying the token cost for only the one it is actively using. 

May 2026 

17 

The new SDLC with vibe coding 

Agent Skills have seen rapid adoption across major coding agents and enterprise platforms because they solve four problems that have plagued AI agent development: 

- Context rot from overloaded prompts 

- Absence of procedural memory for LLMs 

- Operational overhead of multi-agent architectures 

- Need for portability across tools and vendors 

This section introduced the core principles of context engineering: the six types of context every agent needs, the trade-off between static and dynamic context, and Agent Skills as the key pattern for managing that trade-off at scale. 

The companion Day-3 paper in this series on Context Engineering: Sessions, Skills & Memory takes each of these ideas further, covering how to design and manage sessions, write and evaluate skills, build persistent memory across interactions, and optimize token economics for production systems. 

The shift from "prompt engineering" to "context engineering" reflects a deeper truth about working with AI. Models don't need cleverly worded instructions as much as they need the same context that a skilled human developer would need to do good work. The question isn't "how do I trick the AI into writing good code?" It's "what would a new team member need to know to contribute effectively, and how do I encode that knowledge in a form the AI can use?" 

Context engineering is the bridge between vibe coding and agentic engineering. It is also the bridge between this section and the next one, where we look at the structure that surrounds every model and makes it useful. 

May 2026 

18 

The new SDLC with vibe coding 

By shifting our focus from writing syntax to engineering this context, the bottlenecks in software creation fundamentally change. We are no longer waiting on human hands to type boilerplate; we are waiting on human minds to define the boundaries. This necessitates a complete reimagining of the traditional Software Development Life Cycle (SDLC), as the systems we use to build software now dictate the speed at which it is delivered." 

## **The new software development life cycle** 

## **The traditional SDLC under pressure** 

The software development life cycle has already been through one major transformation. Over the past two decades, most enterprises moved from sequential waterfall processes to iterative models: Agile sprints, continuous integration, DevOps pipelines, and rapid release cycles. That shift shortened feedback loops, brought testing closer to development, and made deployment a continuous process rather than a quarterly event. 

AI compresses this cycle dramatically, but unevenly: implementation that once took weeks can now be done in hours, while requirements, architecture, and verification remain stubbornly human-paced. The result is not a faster version of the old SDLC. It is a different workflow, where the boundaries between phases blur, iteration cycles shorten from weeks to minutes, and the developer's role shifts from primary implementor to system designer and quality arbiter. 

May 2026 

19 

The new SDLC with vibe coding 

Figure 5: Traditional SDLC vs. AI-Driven SDLC 

**A note on pace of change:** The phase-by-phase picture described above reflects the state of AI-driven SDLC  as of mid-2026. It is shifting fast. Early signs suggest that the compression will spread beyond implementation: teams are already experimenting with workflows where developers go directly from specs to review, with AI agents handling implementation, testing, and deployment in the background. The boundaries drawn in this section may look different in 12 months. What will remain constant is human judgment, taste, and the skill to verify AI output as the machines take on more of the implementation. 

May 2026 

20 

The new SDLC with vibe coding 

## **How AI transforms each phase** 

## **Requirements and planning** 

Requirements is the phase where the gap between intent and implementation has historically been widest. Translating business needs into technical specifications has been a manual, error-prone process that creates a persistent gap between what stakeholders want and what engineers build. 

Modern AI tools can participate directly in requirements refinement: generating user stories from product briefs, identifying edge cases that humans miss, producing API schemas from natural-language descriptions, and generating interactive prototypes from specification documents. Agentic development environments allow developers to go from a description to a working prototype in minutes, collapsing the requirements-to-prototype feedback loop to near zero. 

Requirements stop being a document handed off between teams. They become a conversation between humans and AI that produces specification and initial implementation simultaneously. 

## **Design and architecture** 

Architecture remains the most stubbornly human-centric phase of the SDLC, and for good reason. Architectural decisions are fundamentally about trade-offs: consistency vs. availability, complexity vs. flexibility, build vs. buy. These trade-offs depend on business context, organisational constraints, and long-term strategic considerations that AI cannot fully grasp. 

May 2026 

21 

The new SDLC with vibe coding 

AI excels at implementing architectural decisions once they are made. Given a clear architecture document, AI agents can scaffold entire applications, generate consistent patterns across modules, and ensure that new code conforms to established conventions. The developer's role shifts from writing boilerplate to making and documenting the structural decisions that boilerplate implements. 

## **Implementation** 

Modern coding agents can generate entire features from natural-language descriptions, implement complex algorithms, and produce multi-file changes that work together correctly. The productivity gains are real: industry surveys report 25 to 39% productivity improvements, with some tasks seeing larger gains.⁷ 

The picture is more nuanced than headline numbers suggest. A study by METR found that experienced developers using AI assistants actually took 19% longer on certain tasks, largely because of the time spent verifying, debugging, and correcting AI output.⁸ AI does not eliminate implementation work so much as transform it from writing to reviewing, guiding, and verifying. 

## **Testing and quality assurance** 

Testing AI-generated code requires evaluating not just what the agent produced, but how it got there. Output evaluation checks the final artifact: does the code compile, do the tests pass? Trajectory evaluation checks the full sequence of tool calls and intermediate reasoning. Both are necessary because a fluent output that skipped its verification steps is a more dangerous failure than one with a visible error. 

May 2026 

22 

The new SDLC with vibe coding 

AI also transforms test generation itself. Agents can produce test cases, including edge cases and property-based tests, that humans might not think of. More importantly, tests and evals become the primary mechanism for communicating intent to AI agents: a well-written eval suite tells the AI what "correct" means and provides an automated way to verify it. 

These practices are most effective when wired into a continuous quality flywheel: evaluate against a benchmark suite, diagnose failures by clustering root causes, optimize the prompts or tools that caused them, verify fixes against a regression suite, and monitor production traffic for new failure modes. Each cycle compounds. 

## **Code review and deployment** 

The review process itself is being augmented, with AI serving as a first-pass reviewer that can identify potential bugs, style violations, security vulnerabilities, and performance issues before a human reviewer sees the code. This does not replace human review, since contextdependent decisions about design, maintainability, and strategic alignment still require human judgment, but it significantly reduces the cognitive burden on reviewers. 

Deployment pipelines are becoming AI-aware as well. AI agents can monitor deployment health, automatically roll back problematic releases, and predict deployment risks based on the nature and scope of changes. Modern deployment platforms increasingly integrate with AI-powered observability to create feedback loops between production behaviour and development decisions. 

Day 5 in this series covers what changes for human reviewers when PR volume scales with agent output — bundled summaries, conditional LGTM, agent-driven code-review skills. 

May 2026 

23 

The new SDLC with vibe coding 

## **Maintenance and evolution** 

Perhaps the most underestimated transformation is in maintenance. Legacy codebases that were once impenetrable to new team members can now be navigated, understood, and modified with AI assistance. An AI agent can read a codebase, understand its patterns, identify the relevant files for a change, and implement modifications while respecting the existing architecture. 

This has significant implications for technical debt. Code that was considered "too risky to touch" because only its original authors understood it can now be safely refactored, modernized, and extended. AI agents can systematically migrate codebases between frameworks, update deprecated APIs, and modernize test suites - tasks that were previously so tedious and risky that they simply never happened. 

## **The factory model: building the system that builds software** 

The mental model that ties these transformations together is what we call the factory model. In this model, the developer's primary output is not code - it's the system that produces code. This system includes:[8] 

- Specifications and context that define what needs to be built 

- Agents that translate specifications into implementation 

- Tests and quality gates that verify correctness 

- Feedback loops that route failures back to agents for correction 

- Guardrails that constrain agents to safe, predictable behavior 

May 2026 

24 

The new SDLC with vibe coding 

A factory manager does not assemble every widget by hand. They design the assembly line and ensure quality control. The modern developer designs the development system and ensures that its output meets the required standard. Success comes from giving agents success criteria rather than step-by-step instructions, then letting them iterate. 

Figure 6: The Factory Model Developer designs the system -> agents produce the code -> tests verify the output. 

This raises the question that drives the rest of this paper: what is the central machine in the factory? What does the agent itself, the thing doing the work inside the assembly line, actually look like? 

May 2026 

25 

The new SDLC with vibe coding 

If the developer is the factory manager, the AI model is merely the raw engine on the factory floor. An engine on its own cannot manufacture a car; it needs belts, gears, safety sensors, and an assembly line. In the context of AI-assisted development, this surrounding machinery is known as the Harness. 

## **Harness Engineering: What surrounds the model** 

There is a temptation, when builders start working with AI agents, to treat the model as the system. A new model comes out, the agent gets smarter. An older model and the agent gets worse. The model becomes the explanation for everything good and bad. 

That intuition is wrong, and it leads to the wrong investments. The model is one input into a running agent. Everything else, the prompts, the tools, the context policies, the hooks, the sandboxes, the sub-agents, the observability, is the harness: the scaffolding wrapped around the model that lets it actually finish something.¹¹ 

A useful equation: 

May 2026 

26 

The new SDLC with vibe coding 

A raw model is not an agent. It becomes one once a harness gives it state, tool execution, feedback loops, and enforceable constraints. The behaviour developers experience when working with Claude Code, Cursor, Codex, Antigravity, Aider, or Cline is dominated by what the harness does, not just by which model is underneath. 

Figure 7: Harness Anatomy | Agent = Model + Harness 

May 2026 

27 

The new SDLC with vibe coding 

## **What's in the harness** 

Concretely, a harness includes: 

- **Instructions and Rule Files:** The text that defines who the agent is, what it cares about, 

- and what it is forbidden from doing. This includes `AGENTS.md` , `CLAUDE.md` , `GEMINI.md` , skill files, and sub-agent prompts. 

- **Tools:** The functions, MCP servers, and APIs the agent can call, plus the prose around them that tells the model when and how to call them. 

- **Sandboxes and execution environments:** Where the agent's code actually runs, what it has access to, what it cannot reach. 

- **Orchestration logic:** Sub-agent spawning, model routing, hand-offs between specialists, and the rules that govern when each one fires. 

- **Guardrails or Hooks:** Deterministic code that runs at specific lifecycle points: before a 

- tool call, after a file edit, before a commit. Hooks are the place for things the agent should never forget but often does. 

- **Observability:** Logs, traces, evaluations, cost and latency metering. Without observability, there is no way to tell whether the agent is doing well or quietly drifting. 

If that sounds like a lot of surface area, it is. And it is the team's surface area, not the model provider's. 

May 2026 

28 

The new SDLC with vibe coding 

## **Harness in SDLC** 

While the model itself determines _how_ to accomplish a task, the harness is the scaffolding that provides access to the tools, sandboxes, and orchestration needed to execute it. Therefore, this harness must be present in every phase where an AI agent operates. 

Here is how the harness actively operates across the different phases of the new SDLC: 

## **1. Requirements, Planning, & Architecture (Configuring the Harness)** 

This is where the harness is configured and calibrated. Before the AI writes any production code, the developer must set up the agent's environment. 

- **Harness Configuration:** Providing the Instructions and Rule Files (e.g., creating the `AGENTS.md` and defining architectural constraints) that the harness will load and make 

- available to the model. 

- **The Action:** The developer defines the tools the agent will have access to (like specific 

- APIs or database schemas) and sets the fundamental rules the agent cannot break. 

## **2. Implementation (Running the Harness)** 

During active coding, the harness acts as the boundary that keeps the AI model focused, secure, and productive. 

- **Harness Components Used:** Sandboxes, Execution Environments, and Tools. 

May 2026 

29 

The new SDLC with vibe coding 

- **The Action:** As the model generates code, it executes it within the harness's isolated sandbox. If the model needs to read a file or search the web, it uses the tools provided by the harness. 

## **3. Testing & QA (The Feedback Loop)** 

Testing in an agentic workflow relies heavily on the harness to facilitate autonomous self-correction. 

- **Harness Components Used:** Orchestration Logic and Guardrails. 

- **The Action:** When the agent writes a function, the harness provides the execution environment (such as a sandboxed terminal) that allows the automated tests to be executed. If a test fails, the orchestration logic captures the error output from that environment and routes it back to the model, asking it to try again. The harness is what creates this automated 'think -> act -> observe' loop." 

## **4. Code Review, Deployment, & Maintenance (Observing the Harness)** 

Even after the code is written, the harness ensures the agent behaves safely in live or near-live environments. 

- **Harness Components Used:** Hooks and Observability. 

- **The Action:** The harness runs deterministic hooks (e.g., blocking a commit if the agent tries to push a hard-coded password). Furthermore, the observability layer tracks token costs, latency, and agent drift, allowing human engineers to audit exactly _why_ an agent made a specific deployment decision. 

May 2026 

30 

The new SDLC with vibe coding 

The transition from 'vibe coding' to 'agentic engineering' is not simply about the tools you use—a developer can vibe code or apply agentic engineering using the exact same agent. Instead, it is defined by how deliberately you configure and apply the harness. Vibe coding relies on minimal or implicit scaffolding aimed purely at rapid implementation. Agentic engineering relies on clear, extensive harness abstractions that guide the AI from the very first planning document all the way through to production monitoring. 

The impact of this deliberate configuration is highly measurable. Public benchmarks make the size of the harness effect concrete. On Terminal Bench 2.0, one team moved a coding agent from outside the Top 30 to the Top 5 by changing only the harness, with no model change at all. A separate study at LangChain raised a coding agent's score on the same benchmark by 13.7 points by tweaking only the system prompt, tools, and middleware around a fixed model. 

The everyday version of this observation is crucial for teams adopting AI across the SDLC: when an agent does something wrong, the first instinct is to blame the model. More often, the failure traces back to a missing tool, a vague rule, an absent guardrail, or a context window stuffed with noise. Most agent failures, examined honestly, are configuration failures. 

## **The developer's evolving role: conductors and orchestrators** 

As AI takes over more of the implementation work, the developer's role is transforming in ways that are both exciting and disorienting. We find it useful to think of two modes that developers move between fluidly: conductor and orchestrator.[12] 

May 2026 

31 

The new SDLC with vibe coding 

Figure 8: Conductor vs. Orchestrator (Two modes of working with AI Agents) 

## **The conductor: hands-on, real-time direction** 

In conductor mode, a developer works in real-time with an AI pair-programmer. They're in the IDE, watching code appear, guiding the AI with prompts and corrections, and maintaining fine-grained control over what gets written. The AI is a powerful instrument, but the developer is actively directing every movement. 

May 2026 

32 

The new SDLC with vibe coding 

This mode is typical when working on complex logic, debugging tricky issues, or working in unfamiliar codebases where the developer needs to understand each change as it's made. Tools like GitHub Copilot, Google's Gemini Code Assist, Cursor, and Windsurf primarily support this mode through inline completions, chat interfaces, and edit-in-place capabilities. 

The conductor mode is natural for developers who come from traditional engineering backgrounds. It preserves the sense of understanding and control that many engineers value. The risk is that it can also become a bottleneck - if the developer is personally directing every keystroke, the throughput improvement from AI is limited. 

## **The orchestrator: async, multi-agent delegation** 

In orchestrator mode, the developer operates at a higher level of abstraction. They define goals, assign them to agents, and review results - but they're not watching code appear line by line. Agents may be working in the background, in parallel, on different parts of a codebase. The developer checks in periodically, reviews output, and provides course corrections. 

This mode is typical for well-defined tasks like bug fixes, feature implementations against established patterns, codebase migrations, and test generation. Tools like Google's Jules, GitHub Copilot's agent mode, Cursor's background agents, and Claude Code support this mode through async task execution, often working in sandboxed environments with full access to the repository, build tools, and test suites.[13] 

The orchestrator mode requires a different skill set. Instead of deep expertise in syntax and language idioms, it demands strong skills in: 

- **Specification:** Defining tasks precisely enough that an agent can execute them without ambiguity 

May 2026 

33 

The new SDLC with vibe coding 

- Decomposition: Breaking large tasks into appropriately sized units for agent execution 

- **Evaluation:** Quickly assessing whether agent output meets quality standards 

- **System design:** Designing the constraints, tests, and feedback loops that keep agents productive 

## **The 80% problem** 

A persistent challenge in AI-assisted development is what we call the 80% problem: AI agents can rapidly generate approximately 80% of the code for a feature, but the remaining 20% - the edge cases, error handling, integration points, and subtle correctness requirements - demands deep contextual knowledge that current models often lack.[14] 

The nature of AI errors has evolved from simple syntax mistakes to more insidious conceptual failures: wrong assumptions about business logic, failure to seek clarification on ambiguous requirements, missing edge cases, and architectural decisions that create subtle long-term maintenance burdens. These errors are harder to detect precisely because the code "looks right" and may even pass basic tests. 

The developers who navigate this challenge most effectively adopt a specific posture: they use AI for what it's good at (rapid implementation of well-specified tasks) while reserving their own attention for what AI struggles with (ambiguous requirements, architectural tradeoffs, and correctness verification). They don't try to be faster by accepting everything the AI produces. They try to be faster by focusing their expertise where it matters most. 

May 2026 

34 

The new SDLC with vibe coding 

Navigating this 80% problem effectively requires applying the right tool to the right phase of work. A developer operating as a 'Conductor' needs a different set of tools than one operating as an 'Orchestrator'. To understand how to map these operational modes to your daily workflow, we must categorise the current landscape of AI agents based on their autonomy and integration. 

## **Coding agents in practice** 

A developer building an agent today does most of the work from a terminal, often in natural language, often with another coding agent doing the typing. This is new. A year ago the same task meant frameworks, SDKs, and cloud consoles. The patterns that have replaced them are worth naming clearly, both for the developer who wants to use coding agents in their day, and for the developer who wants to build agents of their own. 

## **Where coding agents fit in the developer's day** 

Coding agents show up in three places in everyday work. Most developers use all three at once. 

**In the editor:** Inline completion that suggests the next line as the developer types. Chat panels that explain or modify code in place. Whole-codebase awareness inside the IDE. This is where most people first meet AI in coding, and where the work stays in flow. Examples include GitHub Copilot, Cursor, Windsurf, JetBrains AI Assistant. 

May 2026 

35 

The new SDLC with vibe coding 

**In the terminal:** Coding agents that the developer launches from the command line, hand a goal to in plain language, and let work across the codebase. Full file system access, multifile edits, the ability to run tools and tests and iterate based on results. This is where serious vibe coding happens today. Examples include Antigravity CLI, Claude Code, Codex CLI, Open Code, and Cline. 

**In the background:** Agents that take a task and run autonomously in cloud-hosted sandboxes, often for hours, often producing a pull request as output. The developer hands off and reviews it later. Examples include Google Jules, GitHub Copilot agent mode, Cursor's background agents and Google’s specialized AlphaEvolve agent for designing advanced algorithms. 

In practice, an editor agent helps when the developer is in the middle of writing code and wants suggestions, quick edits, or explanations without leaving flow. A terminal agent fits multi-file work, exploration of unfamiliar codebases, and tasks where the agent needs to run code and react to what it observes. A background agent fits well-specified tasks the developer can describe in a paragraph and walk away from, like fixing a known bug, generating a test suite, or migrating code from one framework to another. The same developer often uses all three in a single day. 

The right starting point depends on the task, not on which category sits highest on some autonomy ladder. 

## **Vibe Coding Production-ready Agents** 

Everything discussed so far has been about using coding agents to build software: writing features, fixing bugs, generating tests, refactoring code. But what happens when the thing you need to build is itself an agent? 

May 2026 

36 

The new SDLC with vibe coding 

A customer support bot that handles refund requests. A research assistant that crossreferences sources and produces grounded reports. An internal tool that monitors compliance and flags anomalies. These are not tasks you solve with a coding agent in your terminal. They are products that need their own tools, their own memory, their own evaluation, and their own deployment infrastructure. 

The same terminal-based workflow that produces prototype scripts now reaches these production agents. Building, evaluating, and deploying a real agent that runs at scale, with persistent memory, governance, and observability, has moved from a framework and cloud console task into something that happens in the same terminal, often by talking to the same coding agent the developer was already using. 

This workflow matters when the builder needs an agent that runs reliably for real users: persistent memory across sessions, scoped permissions on tools and data, eval coverage that catches regressions before they ship, observability that traces what the agent actually did. For one-off scripts or personal automation, a regular coding agent is enough; the agent is the destination. For agents that serve real users at scale, the agent is the product, and it needs the substrate underneath. 

Google's **Agents CLI** is built around this idea.¹⁴ It is a small command-line tool that bundles a set of skills for building agents on Google Cloud, and crucially, it works with whichever coding agent the developer prefers, Claude Code, Codex, or another. After a one-time install, the coding agent gains seven new skills covering the full ADK lifecycle: scaffolding a project, writing the agent code, evaluating it, deploying it to Agent Runtime, and wiring up observability. The developer does not learn a new SDK. They describe what they want, and the coding agent uses the skills to do the right thing at each step. 

May 2026 

37 

The new SDLC with vibe coding 

## Concretely, the entire build-evaluate-deploy loop looks like this: 

```
# One-time setup
uvx google-agents-cli setup
# Then in your coding agent:
> Build a support agent that answers questions from our docs.
> evaluate it on the FAQ dataset
> Deploy it to Agent Engine
```

Snippet 1: Agents CLI Setup and Build. 

Behind that single instruction, the coding agent scaffolds a project from a template, writes the ADK code, generates an evalset, runs it against the agent, deploys to Agent Runtime, and reports back. For developers who prefer to drive directly, the same operations are available as plain CLI commands ( `agents-cli create` , `agents-cli playground` , `agents-cli eval` , `agents-cli deploy` ). 

Production agents used to require a separate stack and a separate workflow from prototypes. Now the prototype that ran on the developer's laptop yesterday can become the production agent serving real users today, without a rewrite. 

The same workflow scales from one agent to many. ADK provides graph-based workflows, multi-agent workflows for building collaborative agents  and interaction mechanisms like shared session state, LLM-driven delegation, and explicit invocation, that combine into whatever multi-agent pattern fits the problem. 

Coordination across agents happens through shared session state for simple cases, through Model Context Protocol (MCP) for tool access, and through the Agent2Agent (A2A) protocol for cross-agent delegation.¹⁵ Anthropic's engineering team published an experiment in early 2026 in which agent teams running on this kind of architecture built a working C compiler in 

May 2026 

38 

The new SDLC with vibe coding 

Rust over two weeks, with humans setting direction and reviewing output but not writing the implementation.¹⁶ The bottleneck moved from writing the code to specifying what it should do and verifying that the agents did it. 

For builders, the practical implication is simple. The same vibe coding workflow that produces a script today produces a production agent tomorrow. The lifecycle, build, evaluate, deploy, observe, refine, lives in one place. The path from idea to running agent has collapsed from weeks to hours, and most of the work now happens in natural language. 

The practices that make this workflow production-grade at team scale, from specdriven development and structured code review to guardrails, sandboxing, and zero-trust development, are covered in the Day 5 companion paper: Spec-Driven Production Grade Development in the Age of Vibe Coding. 

## **The Economics of AI Development** 

When evaluating the impact of AI on the software development life cycle, the conversation often begins and ends with developer velocity: _how fast can we write code?_ However, for engineering leaders, the more critical metric is the Total Cost of Ownership (TCO). 

To understand the true cost of AI-assisted development, we must look at how different workflows shift the financial and operational burdens between Capital Expenditure (CapEx)— the upfront investment to build something—and Operational Expenditure (OpEx)—the ongoing cost to run, fix, and maintain it. Crucially, in the AI era, OpEx is heavily dictated by the **token economy** . 

May 2026 

39 

The new SDLC with vibe coding 

Figure 9: The Economics of AI Development 

## **The Hidden Debt of Vibe Coding (Low CapEx, High OpEx)** 

At first glance, vibe coding appears incredibly cost-effective. The barrier to entry is essentially zero: a standard monthly subscription to an AI assistant and a few casual prompts. The CapEx is negligible because the developer relies entirely on the model's baseline capabilities rather than investing time in system design. 

However, the economics of vibe coding hide a massive, compounding OpEx burden: 

- **The Token Burn Rate:** Every interaction with a Large Language Model (LLM) incurs a cost based on input and output tokens. In vibe coding, developers often dump massive, unstructured files into the context window and repeatedly ask the model to fix its own unverified mistakes. This creates an expensive "prompting loop" that burns through API tokens with low first-pass success rates. 

May 2026 

40 

The new SDLC with vibe coding 

- **Maintenance Tax:** Code written through ad-hoc prompting often lacks structural 

- consistency. When a bug arises six months later, human engineers must spend days reverse-engineering unstructured, AI-generated "spaghetti" code. 

- **Security Remediation:** Without an automated evaluation harness, the rapid generation of code leads to the rapid generation of vulnerabilities. The cost of fixing a security flaw in production is exponentially higher than catching it during the design phase. 

## **The Investment of Agentic Engineering (High CapEx, Low OpEx)** 

Agentic engineering flips this economic model. It requires a deliberate, upfront investment of engineering time and resources before a single line of production code is generated. 

The CapEx in agentic engineering includes designing API schemas, building deterministic test suites, and, most importantly, structuring the agent's context. While this upfront cost is higher, the marginal cost of shipping and maintaining a feature drops dramatically. The AI operates within a strictly governed "factory," meaning its output is structurally sound, pretested, and aligned with company standards. 

## **Context Engineering as a Financial Lever** 

In the token economy, context engineering is not just a technical skill—it is a financial strategy. LLMs charge for every piece of information you send them. Passing an entire 100,000-token repository into every prompt is financially unviable at scale. 

May 2026 

41 

The new SDLC with vibe coding 

Effective context engineering ensures the model receives a dense, high-signal payload (such as a precise `AGENTS.md` file and architectural guardrails) rather than a sprawling, noisy one. By providing the right context upfront, developers dramatically increase the agent's firstpass success rate, avoiding the costly trial-and-error loops that plague vibe coding. 

## **Scaling Efficiency via Dynamic Context and Skills** 

To truly optimize OpEx, advanced agentic engineering relies on **dynamic context** through the use of "skills" or tool calling (such as Model Context Protocol servers) which we cover in detail in day-3 paper. 

## **Intelligent Model Routing** 

Furthermore, agentic engineering allows for intelligent model routing. In a vibe coding workflow, a developer typically relies on a single, massive frontier model for every interaction—paying premium token prices just to ask the AI to fix a typo or generate a basic unit test. 

A well-designed factory model avoids this waste. It uses large, advanced models for highly complex tasks (Requirements, Architecture, and initial Implementation) but automatically routes deterministic, lower-complexity tasks (Test Generation, Code Review, and CI/CD monitoring) to smaller, faster, and significantly cheaper models. By orchestrating a multimodel ecosystem, engineering teams can maintain peak output quality while systematically driving down the operational token cost. 

May 2026 

42 

The new SDLC with vibe coding 

## **Where to start** 

The shift from syntax to intent is not a future state. It is the work in front of us today. Whether reading this as an individual builder or as a leader thinking about how a team or organisation adopts these tools, the same underlying principle holds: AI amplifies the engineering culture it lands in. The practices below translate that principle into action. 

## **For individual developers** 

1. **Set up an** `AGENTS.md` **(or equivalent) for the project** . Pick the convention that matches the coding agent of choice. Start with ten lines: stack, conventions, hard rules, workflow. Add a rule every time the agent does something it should not do again. 

2. **Install a set of skills** for your coding agents (like Agents CLI) to build, evaluate, deploy and optimize agents. 

3. **Pick one repetitive workflow and make it the first agent.** A research workflow, a code review process, a recurring report, a piece of content produced regularly. Use a coding agent for the prototype, and graduate it to a production agent through Agents CLI when it earns its keep. Building one agent end to end teaches more than reading about a hundred. 

4. **Write the tests and evals before generating the code.** Together they are the contract with the AI. A well-written test and eval suite communicates intent more precisely than any natural-language prompt, and turns AI-assisted development from vibe coding into agentic engineering. 

5. **Review every line the agent produces that is going to ship.** Be skeptical of anything that looks clever. Check imports for real packages. Verify that error handling covers realistic failure modes. Code that the team does not understand becomes debugging cost the team cannot afford. 

May 2026 

43 

The new SDLC with vibe coding 

6. **Maintain your developer skills.** AI handles the routine so the developer can focus on the challenging. That arrangement only works if the foundational skills, debugging, system design, intuition for performance and correctness, stay sharp. Treat AI as a way to apply expertise at a greater scale, not as a substitute for it. Regular practice with complex debugging, code review of AI output, and architecture discussions stay essential to growing as an engineer. 

## **For engineering leaders** 

1. Treat **Make context engineering a first-class engineering practice on the team.** `AGENTS.md` , system prompts, eval suites, and skill libraries as code: reviewed in pull requests, versioned with the project, owned by named engineers. Without this discipline, the harness drifts and agent behaviour becomes irreproducible across the team. 

2. **Set the bar at the eval, not the demo.** A working demo proves an agent can succeed once. A passing eval suite proves it succeeds reliably. But an eval without a clear rubric measures nothing. Define what you are scoring: task success, tool use quality, trajectory compliance, hallucination, and response quality. Require eval coverage with explicit rubrics as a precondition for any agent shipping into a shared workflow, the same way test coverage gates a service deployment. 

3. **Re-shape code review for AI-generated code.** AI-generated code requires the same or greater scrutiny than human-written code, with extra attention to hallucinated dependencies, inadequate error handling, and subtle correctness gaps that look right at a glance. Train reviewers on the failure modes of generated code, and tune review checklists accordingly. 

May 2026 

44 

The new SDLC with vibe coding 

4. **Distinguish prototyping work from production work in team norms.** Vibe coding is the right speed for exploration. Agentic engineering is the right discipline for production. Make the boundary explicit: which projects, which branches, which environments warrant which mode of working. Teams that keep this distinction blurry produce prototypes that ship by accident. 

5. **Invest in the harness components as a shared team asset.** Reusable system 

   - prompts, skill libraries, MCP server connections, and evaluation harnesses compound across projects. Treat them as infrastructure: documented, maintained, and improved deliberately. The teams that compound the most value from AI-assisted development are the ones that build their harness once and refine it many times. 

## **For organizations** 

1. **Treat AI-assisted development as an engineering investment, not a productivity feature.** The teams seeing the largest gains pair AI tooling with eval coverage, observability, and clear architectural standards. Rolling out a coding agent without that scaffolding produces speed without quality, which compounds into technical debt faster than any team can pay it down. 

2. **Invest in the production substrate before scale.** A vibe-coded prototype on a laptop is not a production system. What graduates one to the other is the operations discipline around it: trajectory and final-response evals run in CI, traces of every agent run, scoped permissions per agent, and security review tuned to the failure modes of generated code. Build this substrate before the first production agent ships, not after. 

3. **Adopt open standards for tools and inter-agent communication.** Model Context Protocol (MCP) for tool access and Agent2Agent (A2A) for cross-agent delegation are converging into the connective tissue of multi-agent systems. Choosing them now keeps the option to mix vendors and frameworks open, and avoids re-platforming later. 

May 2026 

45 

The new SDLC with vibe coding 

4. **Plan for hybrid teams of humans and agents, not human-only or agent-only workflows.** The strongest production results in the past year come from architectures where humans set direction, agents do the implementation, and clear handoff protocols govern the boundary. Code review processes, on-call rotations, and team structures all need to evolve to reflect that agents are now participants, not just tools. 

5. **Reframe hiring and skill development around judgment, not just implementation.** As implementation becomes faster and more automated, the bottleneck shifts to specification, evaluation, architectural judgment, and review. Hire and develop for those skills deliberately. The most valuable engineers in the next several years will be the ones who can direct agents well, not the ones who can write the most code. 

May 2026 

46 

The new SDLC with vibe coding 

## **Conclusion: Intent as the new Interface** 

The transition from syntax to intent is not a future prediction - it's a present reality. Developers are already spending more time describing what they want than specifying how to build it. The SDLC is already being compressed, restructured, and reimagined around AI capabilities. The question is not whether this transformation will happen, but how effectively individual developers, teams, and organizations will navigate it. 

The framework we've presented in this paper - the spectrum from vibe coding to agentic engineering, the conductor-to-orchestrator model of developer roles, the taxonomy of ambient, workflow, and autonomous agents, and the factory model of software production - provides a set of mental models for making sense of a rapidly evolving landscape. These models will remain useful even as the specific tools and capabilities evolve. 

Three principles stand out as durable: 

1. **Structure scales, vibes don't.** Vibe coding is a valid approach for exploration, prototyping, and personal projects. But for software that organizations depend on, the discipline of agentic engineering - specifications, tests, guardrails, and human oversight of architecture - is not optional. The gap between "it seems to work" and "it works correctly under all conditions" is where production outages, security vulnerabilities, and maintenance nightmares live. 

2. **AI amplifies your engineering culture.** Organizations with strong testing practices, clear architectural standards, and healthy code review processes get dramatically more value from AI-assisted development than those without. AI is a force multiplier - and it multiplies both your strengths and your weaknesses. 

May 2026 

47 

The new SDLC with vibe coding 

3. **The human role is evolving, not diminishing.** The builders who understand architecture, can define precise specifications, evaluate output critically, and design effective systems of constraints and feedback loops are more valuable than ever. The skills that matter are shifting from implementation to judgment, from writing code to designing the systems that produce code. 

We're at the beginning of a transformation that will reshape not just how software is built, but what kind of software is possible to build. Smaller teams will be able to tackle larger problems. Individual developers will be able to build and maintain systems that previously required entire departments. The barrier to creating software will continue to fall, opening the practice of software development to a broader population. 

The teams that thrive will be those that embrace AI as a powerful tool while maintaining the engineering discipline that has always been the foundation of reliable software. They'll be the ones who understand that the future of software engineering isn't about choosing between human expertise and AI capability - it's about designing systems where both contribute their unique strengths. 

_Generation is solved. Verification, judgment, and direction are the new craft._ 

May 2026 

48 

The new SDLC with vibe coding 

## **Endnotes** 

1. GetPanto, "AI Coding Assistant Statistics 2025-2026," htps://www.getpanto.ai/blog/ai-coding-assistantstatistics; Index.dev, "Developer Productivity Statistics with AI Tools," htps://www.index.dev/blog/ developer-productivity-statistics-with-ai-tools 

2. Karpathy, A., "Vibe Coding," X/Twitter post, February 2025. htps://x.com/karpathy/ status/1886192184808149383; Wikipedia, "Vibe coding," htps://en.wikipedia.org/wiki/Vibe_coding 

3. Osmani, A., "Agentic Engineering," 

htps://addyosmani.com/blog/agentic-engineering/ 

4. Karpathy, A., "From Vibe Coding to Agentic Engineering," 2026; The New Stack, "Vibe Coding is Passe," htps://thenewstack.io/vibe-coding-is-passe/ 

5. Glide Blog, "What is Agentic Engineering?" htps://www.glideapps.com/ blog/what-is-agentic-engineering; The New Stack, "Vibe Coding, Agentic Engineering," htps://thenewstack.io/vibe-coding-agentic-engineering/ 

6. CircleCI, "AI-Native SDLC," htps://circleci.com/blog/ai-sdlc/ 

7. GroovyWeb, "SDLC in the AI Era: Software Development 2026," htps://www.groovyweb.co/blog/sdlc-aiera-sofware-development-2026; EPAM, "From Traditional Software to a Native AI SDLC," htps://www.epam.com/about/newsroom/in-the-news/2026/from-traditional-sofwareto-a-native-ai-sdlc-how-genai-is-redefning-engineering 

8. Osmani, A., "The Factory Model," 

htps://addyosmani.com/blog/factory-model/ 

9. Deloitte, "AI in Software Engineering: Productivity Gains 2025-2026," projecting 30-35% gains across the full development process. 

10. METR, "Uplift Update: Measuring the Impact of AI Coding Tools," February 2026, htps://metr.org/blog/2026-02-24-uplift-update/ 

11. Google, "Introduction to Agents," Agents Whitepaper Series, November 2025. 

12. Osmani, A., "From Conductors to Orchestrators: The Future of Agentic Coding," htps://addyosmani.com/blog/future-agentic-coding/ 

May 2026 

49 

The new SDLC with vibe coding 

13. Google, "Jules: AI-Powered Coding Agent," 

htps://developers.googleblog.com/en/the-next-chapter-of-the-gemini-era-for-developers/ 

14. Osmani, A., "The 80% Problem in Agentic Coding," htps://addyo.substack.com/p/the-80-problem-in-agentic-coding 

15. Medium, Dave Patten, "The State of AI Coding Agents 2026: From Pair Programming to Autonomous AI Teams, htps://medium.com/@dave-paten/the-state-of-ai-coding-agents-2026-from-pairprogramming-to-autonomous-ai-teams-b11f2b39232a 

16. Lawfare, "When the Vibes Are Off: The Security Risks of AI-Generated Code," htps://www.lawfaremedia.org/aricle/when-the-vibe-are-off--the-security-risks-of -ai-generated-code 

17. Google, "Introduction to Agents," Multi-Agent Systems and Design Patterns section, November 2025. 

18. Google, "Agent Development Kit (ADK)," htps://google.github.io/adk-docs/; Kartakis, S., "From Zero to Multi-Agents: A Beginner's Guide to Google Agent Development Kit (ADK)," htps://medium.com/@sokratis.karakis/from-zero-to-multi-agents-a-beginners-guide -to-google-agent-development-kit-adk-b56e9b5f7861 

19. Google, "Agent-to-Agent (A2A) Protocol," htps://google.github.io/a2a-protocol/; Kartakis, S. and Hotz, H., "Generative AI in the Real World: Understanding A2A," O'Reilly Podcast, htps://www.oreilly.com/radar/podcast/generative-ai-in-the-real-world-understandinga2a-with-heiko-hotz-and-sokratis-karakis/ 

20. TLDL, "AI Coding Tools 2026," htps://www.tldl.io/resources/ai-coding-tools-2026; Kanerika, "GitHub Copilot vs Claude Code vs Cursor vs Windsurf," htps://kanerika.com/blogs/github-copilot-vs-claude-code-vs-cursor-vs-windsur/ 

21. Google, "Gemini Code Assist," 

htps://cloud.google.com/gemini/docs/codeassist/overview 

22. Dark Reading, "Coders Adopt AI Agents, but Security Pitfalls Lurk in 2026," htps://www.darkreading.com/application-security/coders-adopt-ai-agents-securitypitalls-lurk-2026 

23. Google, "Gemini CLI," 

htps://github.com/google-gemini/gemini-cli. 

24. Google, "Agent Tools: Interoperability with Model Context Protocol (MCP)," Agents Whitepaper Series, November 2025 

May 2026 

50 

The new SDLC with vibe coding 

25. Google, "Agent Quality" and "Prototype to Production," Agents Whitepaper Series, November 2025 

26. Lawfare, "When the Vibes Are Off: The Security Risks of AI-Generated Code," htps://www.lawfaremedia.org/aricle/when-the-vibe-are-off--the-security-risks-of-aigenerated-code 

27. DevOps.com, "AI-Generated Code Packages Can Lead to Slopsquatting Threat," htps://devops.com/ai-generated-code-packages-can-lead-to-slopsquating-threat/ 

28. Osmani, A., "Beyond Vibe Coding," O'Reilly Media, 2025-2026, htps://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749/ 

29. "Awesome LLM Apps," 

htps://github.com/Shubhamsaboo/awesome-llm-apps 

30. Osmani, A., "My LLM Coding Workflow Going Into 2026," htps://addyosmani.com/blog/ai-coding-workfow/ 

31. Questera, "7 AI Coding Trends to Watch in 2026," htps://www.questera.ai/blogs/7-ai-coding-trends-to-watch-in-2026 

32. DEV Community, "Programming in the Age of AI: From Code to Intent," htps://dev.to/roberobuti/programming-in-the-age-of-ai-from-code-to-intent-46eo 

May 2026 

51 

# **Agent Tools & Interoperability** 

**Authors: Kanchana Patlolla, Łukasz Olejniczak, and Pier Paolo Ippolito** 

Agent Tools & Interoperability 

## **Acknowledgements** 

## **Content contributors** 

Alan Blount Mike Smith Anant Nawalgaria Lukas Geiger 

## **Curators and editors** 

Anant Nawalgaria 

## **Designer** 

Michael Lanning 

May 2026 

2 

## **Table of contents** 

|Introduction|6|
|---|---|
|Why this paper, why now|8|
|Who this paper is for|9|
|The Vibe Coder’s View of MCP: Discovery, Configuration, & Connection|10|
|Discovery|11|
|Configuration|12|
|Connection|12|
|Bypassing the NxM Prototyping Problem|13|
|Why is this important?|14|
|Debugging Issues with MCP Servers|15|
|Vibe Coder Toolkit: Best Practices for MCP Consumption|15|
|Agent-to-Agent (A2A) Interoperability|17|
|The Evolution of Agentic Architectures|17|
|Bounded vs. Unbounded Domains|23|
|The GOTO Problem in Agentic Architecture|24|



## **Table of contents** 

|Building the Virtual Workforce|24|
|---|---|
|The Agent Card|25|
|Registries: From Public Marketplaces to Private Enterprises|25|
|Implementing A2A Protocols|26|
|Exposing A2A Agent|26|
|Connecting Remote A2A Agents|27|
|The Extensibility Layer: A2A as the Foundation for UI and Commerce|28|
|Monetizing A2A Agents|29|
|The Extensibility Layer: A2A as the Foundation for UI and Commerce|31|
|Agent-to-UI (A2UI) Interoperability|32|
|The Communication Gap|32|
|Generative UI & A2UI|32|
|What is Generative UI?|32|
|A2UI: A Secure Implementation|33|
|The Basic Catalog (and Bringing Your Own)|34|



## **Table of contents** 

|Generating A2UI: Two Patterns|35|
|---|---|
|When to Use Each Pattern|37|
|Interactive Artifacts & The Canvas|38|
|Canvas + A2UI|39|
|Best Practices|40|
|Let LLMs Generate A2UI|40|
|Hybrid Output for Flexibility|42|
|Summary|43|
|Agents and Commerce (AP2 and UCP)|43|
|Autonomous Procurement with a workflow example|43|
|Key characteristics and benefits of Protocols|43|
|What is AP2 and UCP?|44|
|UCP (Universal Commerce Protocol): The Ultimate Food Delivery App|45|
|AP2 (Agent Payments Protocol):**_The Parent's Credit Card with Strict Rules_**|**_46_**|
|Conclusion|47|
|Endnotes|48|



Agent Tools & Interoperability 

Software's next evolution isn't written: it's orchestrated by interoperable agents. 

## **Introduction** 

In Day 1, we outlined the paradigm shift from traditional software development to Agentic Engineering, introducing the Factory Model where your primary output as a developer is no longer raw syntax, but the system that produces code. We defined the core architecture of this system: 

May 2026 

6 

Agent Tools & Interoperability 

If Agentic Engineering represents the factory floor you are orchestrating, then **MCP** , **A2A** , **A2UI** , **AP2** , and **UCP** are the **Industry Standards** —the uniform nuts and bolts and screw sizes, data formats, and communication channels—that allow your machinery to safely interact with the rest of the world. 

Without these open protocols, every agent you build exists as an isolated "custom machine" in a garage. You are forced to spend your hours and tokens writing fragile, bespoke wrappers for every single tool and API connection, trapping you in a low-leverage **Conductor** role. 

By adopting standardized interoperability layers, you transform your agent's **Harness** into a modular, plug-and-play platform. You spend less time debugging custom JSON payloads and more time directing high-level intent as an **Orchestrator** . 

- **OpenResponses & Interactions API** are both **“Power Plugs”** , modern API approaches to LLM inference which support long running tasks.  These blur the line between a stateless single turn and a stateful agent. 

- **MCP (Model Context Protocol)** acts as the **"USB-C"** within your agent's harness, instantly connecting models to databases, filesystems, and web APIs. 

- **Skills** are **“Playbooks”** , very simple markdown instructions and scripts or tools which can be used in a sandbox environment like a terminal. 

- **A2A (Agent-to-Agent)** serves as the **"Factory Radio"** , allowing specialized agents to negotiate, brain-storm, and delegate tasks to each other. 

- **A2UI (Agent-to-User Interface)** behaves like a **"Generative Display Window"** , turning raw, complex JSON outputs into safe, interactive visual components for human operators. 

- **AP2 and UCP** act as the **"Global Supply Chain & Transaction Network"** , allowing agents to securely negotiate and execute autonomous commercial transactions. 

May 2026 

7 

Agent Tools & Interoperability 

This paper focuses on how vibe coders can rapidly utilize some of these protocols to construct a virtual data and execution team in a single afternoon. 

Figure 1: Ecosystem of Agent Protocols 

## **Why this paper, why now** 

In the era of vibecoding with less structure, harnesses and protocols help build trust in the agent development process. While velocity of outcome remains the primary driver for practitioners and developers, standardized protocols allow us to expand much further in achieving complex goals by transforming isolated "custom machines" into modular, interoperable platforms. Without agreed upon open standards, developers are creating tech 

May 2026 

8 

Agent Tools & Interoperability 

debt, each API is a standard-of-one. These are low-leverage tasks, writing fragile, bespoke wrappers for every tool, maintaining them over time and adapting to other’s needs. Adopting these layers allows for a shift from being a mere builder to a high-level orchestrator. 

## **Who this paper is for** 

This paper is specifically designed for software engineers, engineering managers, architects, and technical leaders who recognize that the shift toward Agentic Engineering requires strict adherence to protocols to maintain the fidelity and reliability of outcomes. It serves as a practical guide for "vibe coders" who prioritize speed and visual results, demonstrating how to construct a virtual data and execution team. 

## **Applied Tip:** 

In the Day 1 whitepaper, we recommended using an `AGENTS.MD` file to provide standard guidance for coding agents. 

Always begin by thinking deeply before you code—explicitly stating your assumptions, surfacing tradeoffs, and halting to ask for clarification the moment you encounter ambiguity rather than guessing silently. 

Write only the absolute minimum amount of code required to solve the immediate problem, strictly avoiding speculative features, unrequested abstractions, or predictive configurations. When editing existing code, make highly surgical changes by restricting your updates only to the exact lines necessary to fulfill the request, maintaining the existing style perfectly, and leaving adjacent, unbroken code completely untouched unless your changes directly orphaned an import or variable. 

Finally, approach every task through goal-driven execution by breaking it down into a clear, step-by-step plan with strong success criteria, such as writing a reproducing or failing test first and independently looping through verification until that specific goal is strictly met. 

May 2026 

9 

Agent Tools & Interoperability 

In our previous whitepaper, Agent Tools & Interoperability with Model Context Protocol (MCP), we laid out the enterprise architecture of MCP, detailing host-client-server topologies, custom server creation, and security governance. 

For the vibe coder, however, the priority is **consumption over creation** . You do not want to spend hours writing custom server configurations. You want to hook into existing public and private registries to instantly give your agent "plug-and-play" superpowers. This section covers how to consume MCP servers efficiently, how to bypass the NxM integration crisis, and how to debug transport layers when things break. 

Note: we will have a deeper look at Agent Skills in the next whitepaper and Security in the following. 

## **The Vibe Coder’s View of MCP: Discovery, Configuration, & Connection** 

The traditional enterprise way of bringing tools to an LLM is **bespoke hardwiring** . Every new connection requires custom REST wrappers, API keys, token refresh policies, and custom JSON parsers. MCP replaces this friction with a standardized socket. Setting up your coding agent involves three simple steps: 

Figure 2: Steps for Onboarding an MCP Server 

May 2026 

10 

Agent Tools & Interoperability 

## **Discovery** 

Vibe coders do not write custom connectors; they locate pre-built MCP servers from three primary sources: 

- **Public MCP Registries:** Publicly available registries host hundreds of pre-built servers (e.g., registry.modelcontextprotocol.io, github.com/mcp). These are excellent for rapid local prototyping but are unvetted and used at your own risk. 

- **Third-Party (3P) Remote MCP Servers:** Vetted platforms expose hosted endpoints. Discover managed pre-vetted MCP servers from official sources. For instance, official Google-published MCP servers (e.g., Google Maps, BigQuery, Google Docs) let your agent securely interact with managed services. 

- **Internal Registries:** Inside an organization, internal tools are exposed as MCP servers and cataloged in a secure registry. The technical implementation of this registry is typically managed via an API gateway, GCP Agent Registry, or a private microservice portal. 

## **Applied Tip:** 

When making a decision always consider security as a first priority, look for official instructions where possible. 

If using public community servers do not pass credentials, consider using services like Model Armor to avoid security issues. 

May 2026 

11 

Agent Tools & Interoperability 

## **Configuration** 

Before connecting, specify standard parameters detailing the server's scope and permissions. This includes setting up environment files to handle API credentials (such as Personal Access Tokens or OAuth secrets) and defining read/write permissions to protect your filesystem. 

**Applied Tip:** 

✅ Check for pre-requisites ✅ Identify scope, access criterias ✅ Include the specifications in the coding agent ✅ Authentication 

## **Connection** 

Once configured, the client establishes connection with the server. To verify the connection, the host client runs a basic handshake request to list the available tools and validate the output schema. 

May 2026 

12 

Agent Tools & Interoperability 

## **Bypassing the NxM Prototyping Problem** 

To appreciate why MCP is crucial for rapid prototyping, look at the integration math. If you are experimenting with N different LLMs (Gemini 3.1 Pro, Gemini 3 Flash, Gemini 3.5 Flash or a local open-source model) and want to connect them to M different external tools (Jira, BigQuery, GitHub, Google Drive), traditional ad-hoc development requires writing custom integration code for every single model-tool intersection: 

If you have 5 models and 10 tools, you must maintain **50 bespoke integration points** . If a single tool API changes, multiple parser loops break without a protocol in place. 

`Traditional Integration:               MCP Interoperability: Models       Tools                     Models       MCP        Tools` ── `[Model A] [Tool 1]                 [Model A]` ──┐ ┌── `[Tool 1]` ── `[Model B] [Tool 2]                 [Model B]` ──┼─ `[MCP]` ┼── `[Tool 2] [Model C]` ── `[Tool 3]                 [Model C]` ──┘ └── `[Tool 3] Effort: O(N x M)                      Effort: O(N + M)` 

Snippet 1: MCP Complexity 

May 2026 

13 

Agent Tools & Interoperability 

MCP reduces this complexity to linear scale: 

## **Why is this important?** 

By standardizing tool definitions, you connect standard transports directly into your agent’s Harness without writing integration code: 

- **stdio (Standard Input/Output):** Most often used with Local and Prototyping efforts. Your coding agent can run without a complex network connection setup, as it treats the tool as a local process. The host client launches the MCP server as a local background subprocess, passing JSON-RPC 2.0 messages over stdin and stdout. 

- **SSE (Server-Sent Events) over HTTP:** The host client (could be Local or a deployed agentic application) connects to a remote MCP endpoint over standard web protocols, streaming data to the agent in real-time. This has many advantages over the studio approach, fewer dependencies, always up to date, smaller footprint, and simpler lifecycle, but is a higher burden on the cloud hosted MCP server. 

Both options enable the vibecoders to adopt the platform without multiple custom integration layers. 

May 2026 

14 

Agent Tools & Interoperability 

## **Debugging Issues with MCP Servers** 

When your agent hallucinates parameters, calls the wrong tool, or fails to parse a payload, don't waste time blindly modifying your system instructions. Debug the transport pipes directly: 

- **MCP Inspector:** A native developer tool that runs a local web panel. It lets you manually query any local or remote MCP server, view the active tool schemas, manually test payload inputs, and inspect the raw JSON-RPC 2.0 packets without initiating your main agent workflow. 

- **Chrome DevTools:** Perfect when running web-based development environments or 

- debugging SSE connections, allowing you to trace incoming web streams and check for server latencies. 

## **Vibe Coder Toolkit: Best Practices for MCP Consumption** 

To maintain speed without sacrificing stability, vibe coders should adhere to the following guidelines when consuming MCP servers: 

## ✅ **Do's (Best Practices)** 

- Do audit public servers before connection: Always review the code of publicly available, open-source MCP servers before attaching them to an agent that has access to your local file system or credentials. 

- Do use RAG for tools: Keep your agent's context window clean. Dynamically load tools from a registry only when needed, and drop them from context when the task is complete to prevent attention dilution. 

May 2026 

15 

Agent Tools & Interoperability 

- Do leverage internal API Gateways and registries: If possible, rely on internal tool registries. This ensures you are consuming approved, governed data schemas rather than reinventing the wheel or running unvetted code. 

- Do use the MCP Inspector: When an agent hallucinates a tool call with their arguments, use the MCP Inspector or Chrome DevTools to look at the raw transport data rather than blindly tweaking the agent's system prompt. 

- Do include HITL: Show tool inputs to the user before calling the server, to avoid malicious or accidental data exfiltration 

- Do auditing needs: Log tool usage for audit purposes 

## ❌ **Don'ts (Common Pitfalls)** 

- Don't build if you can consume: Resist the urge to write custom REST API wrappers. Search for an existing MCP server first to maintain the "universal outlet" philosophy. 

- Don't use public, unverified MCPs in production: Open-source MCP servers are fantastic for weekend prototypes, but they carry security and reliability risks. Do not tie core business logic to unverified public endpoints or API wrapper code. 

- Don't hardcode credentials: During the Configuration phase, never paste API keys or auth tokens directly into your agent's prompt or local scripts. Rely on environment variables to pass credentials to the MCP server. 

- Don't connect to production: Use the MCP server with a development project, not production. LLMs are great at helping design and test applications, so leverage them in a safe environment without exposing real data. Be sure that your development environment contains non-production data (or obfuscated data). 

- Don’t use it for updates: If you must connect to real data, set the server to read-only mode, which executes all queries as a read-only. 

May 2026 

16 

Agent Tools & Interoperability 

- Don’t provide wide access to all the Projects: Scope your MCP server to a specific project, limiting access to only that project's resources where necessary and possible. 

Now we have learnt how to enable vibecoders to leverage the MCP tools for their AI Agent building, but AI agent building goes beyond tools, it is to enable users to bring interoperability across the ecosystem of applications. We will review how Agent interoperability works in the next section. 

## **Agent-to-Agent (A2A) Interoperability** 

As AI systems transition into distributed networks of specialized domain experts, standardized communication becomes essential for scaling. This section explores the Agentto-Agent (A2A) protocol as the foundational layer that resolves ecosystem fragmentation, enabling developers to discover, orchestrate, and monetize a globally interoperable virtual workforce. 

## **The Evolution of Agentic Architectures** 

To understand where **Vibe Coding** fits into the evolution of agentic architectures, we can observe a recurring pattern in technology: the shift from manual, low-level configuration to high-level, intent-based, declarative orchestration when users don’t say HOW to build something but WHAT they need. 

May 2026 

17 

Agent Tools & Interoperability 

A parallel trend is found in the history of IT infrastructure where we transitioned from manual configurations to "Infrastructure as Code"  declarative scripts. A similar trend happened in the history of Machine Learning. The visionary premise from Google behind Automated Machine Learning (AutoML) was to democratize AI by automating the "drudge work" of model creation: 

_"One way we hope to make AI more accessible is by simplifying the creation of machine learning models called neural networks. Today, designing neural nets is extremely time intensive... That’s why we’ve created an approach called AutoML, showing that it’s possible for neural nets to design neural nets. We hope AutoML will take an ability that a few PhDs have today …."_[1] 

Today, technology enables us to vibe code entire applications. However, the trajectory of agentic architectures used to vibe code these applications is currently mirroring **Monolithic to** one of the most significant shifts in software history: the transition from **Microservices architectures** . 

Just as early web applications were built as single, massive codebases where every function (billing, UI, database) was tightly coupled, many initial vibe coding projects relied on a **"Swiss Army knife" Single Agent Monolith** . _This involves relying on a single, highly sophisticated prompt where one agent wears multiple hats with many connected tools to handle everything from database queries to UI rendering and testing_ . While this allows a developer to wire together a prototype in a weekend, it eventually hits the same "Monolithic Ceiling" that plagued early web apps: 

**• Scaling Friction:** You cannot optimize just the "Database logic" without potentially confusing the "UI logic" residing in the same prompt. Also, the more tools a single agent has access to, the worse its decision-making becomes. _The search space for its next action is simply too large, leading to hallucinated parameters or triggering the wrong tools._ 

May 2026 

18 

Agent Tools & Interoperability 

- **Contextual Overload:** _Shoving overarching system instructions, dozens of complex tool schemas, and ongoing conversation history into a single prompt quickly maxes out the model's working memory._ 

- **The Single Point of Failure:** A bug in one "tool" or instruction can cause the entire agent to hallucinate or crash. Irrelevant or corrupted data stored in context gets carried over, breaking future reasoning. 

To overcome these bottlenecks one can follow a similar blueprint laid out by ML engineers and software engineers years ago. When early AutoML models successfully proved their business value, teams rarely left those auto-generated black boxes running the core business. To reach production scale they had to break this black box apart into observable, maintainable stages—data versioning, feature stores, drift detection. By specializing the components they applied a fundamental law of system design: **specialization as a scaling mechanism** . 

Figure 3: Monolithic Multi-agent Architecture 

May 2026 

19 

Agent Tools & Interoperability 

Internal specialization works by logically partitioning a monolithic agent into distinct, purpose-built sub-agents. Each agent is governed by a highly focused system prompt and a relevant subset of tools. It is still monolith because these internal sub-agents do not communicate across network boundaries. Instead, they share the same runtime and underlying memory. 

This logical partitioning allows developers to modularize complex definitions while maintaining the low-latency execution and simplified state management inherent to a singleprocess application. At the same time this modularity addresses the inherent limitations of single-agent systems through several key technical improvements: 

- **Reduction of Search Space:** By restricting a sub-agent's tools and skills (e.g., giving a DB agent only query tools), we drastically reduce tool-call errors and hallucinations. 

- **Mitigation of Attention Dilution:** Specialization allows the underlying LLM to focus on a single domain prompt, leading to sharper reasoning. 

- **Optimization of Contextual Load:** Because the orchestrator routes tasks instead of processing the entire logic tree, sub-agents maintain a high signal-to-noise ratio in their context windows. 

As agentic architectures mature, a significant ecosystem shift based on distributed multi-agent architectures is underway. Industry leaders—including Google, Salesforce, ServiceNow, and Workday—are moving beyond the provision of APIs. These organizations are deploying domain-specific AI agents designed to navigate their proprietary ecosystems with native precision. 

May 2026 

20 

Agent Tools & Interoperability 

Figure 4: Distributed Multi-Agent Architecture. An orchestrator delegates tasks across network boundaries to remote, domain-specific agents. 

This shift presents a strategic opportunity for developers. However, to reach the next tier of scale, technical and business leaders must ruthlessly prioritize their focus through a modern "Build vs. Buy" lens. 

While it is technically feasible to construct a multi-agent system using custom-built subagents for third-party platforms (e.g. custom subagent for ServiceNow or custom subagent for Salesforce etc), this approach introduces a significant Maintenance Tax. By opting for bespoke development of domain specialists, the developer assumes full responsibility for updating prompt logic and tool definitions reflecting upstream product updates and API schema changes. 

May 2026 

21 

Agent Tools & Interoperability 

A better architectural strategy for building high-value applications would be to leverage official specialist agents. These agents are maintained by teams with deep domain expertise, ensuring maximum reliability and performance. By offloading the maintenance of specialist domain logic to these official entities, the **Orchestrator** —and by extension, the developers— can focus entirely on the unique user value and core innovation of their application. 

However, attempting to orchestrate this virtual team of distributed AI specialists introduces a new bottleneck: **fragmentation** . Every one of these specialist agents can be built by a different team, using different technologies. Google’s agent might be written in Python, Go or Java using ADK, Salesforce’s agent might run on a LangChain framework, and Workday’s might use something completely bespoke. They exist outside our network boundaries, they speak different languages, expect completely different payload structures, process conversational state differently, and rely on varying transport layers. 

If a developer has to write custom integration code and handle bespoke error-correction loops for every single specialist they want to hire, the "Virtual Team" concept instantly turns into an integration endeavor. The maintenance tax of keeping all those custom bridges from collapsing would consume the entire project. 

This chaos of fragmentation is exactly what the **Agent-to-Agent (A2A) protocol** [A2A] is designed to standardize. A2A, originally developed by Google and now donated to the Linux Foundation,  introduces a universal layer of communication for agentic systems. It acts as the lingua franca for the AI ecosystem, abstracting away networking transport nuances, the underlying frameworks, programming languages, and payload disparities. 

It ensures that the central Orchestrator can discover, onboard, and collaborate with any specialist agent in the ecosystem, completely agnostic to how that specialist was built under the hood. Just as HTTP standardized the web, . **A2A standardizes the virtual workforce** 

May 2026 

22 

Agent Tools & Interoperability 

_"Does the caller need a result, or does the caller need another participant to take responsibility?" — that's the cleanest framing I've seen for this decision. The smell test of a central agent prompt growing into an accidental workflow engine is exactly how most teams discover they needed collaboration semantics three months too late.[19]_ 

But this raises the next architectural question: _If we are just delegating to external specialists, why can't we just treat them as standard tools?_ 

The nature of the engagement with specialists and tools is fundamentally different. Imagine a homeowner renovating a kitchen. They face a choice: _purchase the individual tools and who manuals to attempt the build themselves, or delegate the project to a domain specialist builds kitchens for a living_ . 

Tools are just passive instruments; a specialist is a collaborative partner. When you hire that specialist, you don't just hand them a single blueprint and walk away expecting a perfect kitchen to magically appear. They will hit edge cases or an oversight in your original design requiring them to pause, consult you on trade-offs, and resume. 

## **Bounded vs. Unbounded Domains** 

This is exactly one of the reasons why treating a specialist AI agent as a simple tool does not scale. A standard tool or API operates on a **fire-and-forget** mechanism. It expects a single, perfectly formatted request (the blueprint payload) and returns a response. Real-world software environments often contain the digital equivalent of crooked walls: ambiguous data structures, misleading requirements, and conflicting user preferences. 

May 2026 

23 

Agent Tools & Interoperability 

yAn agent, however, operates in an _unbounded_ problem-solving space. Real-world software environments are full of ambiguous data structures, misleading requirements, and conflicting user preferences. You rarely can specify all necessary details in a complex workflow without _crooked walls_ . multi-turn clarification. The digital equivalent of 

## **The GOTO Problem in Agentic Architecture** 

Because an agent's domain is unbounded, trying to force an agent into a standard tool wrapper introduces the architectural equivalent of a `GOTO` statement into your orchestrator. 

When you call a collaborative agent, the control flow leaves the expected, structured context. The agent might hit an interrupted state, request more information, and potentially never return the expected output to the original caller if the user changes their mind or abandons the prompt. 

You need a paradigm that isolates this messy, multi-turn state. You need a protocol that allows the domain agent to pause its execution, reach back out to the Orchestrator, negotiate a solution, and then resume its work without losing its conversational state. 

That is exactly the gap the **A2A protocol** fills. By isolating this collaborative routing to the A2A layer, we keep the tool layer (MCP) clean, predictable, and strictly structured. 

## **Building the Virtual Workforce** 

The introduction of the A2A protocol and the shift toward specialization does more than just solve technical bottlenecks—it creates the foundations for new marketplaces for expertise which represents a new model in how value is delivered. 

May 2026 

24 

Agent Tools & Interoperability 

Without A2A, a developer might build an application and struggle to maintain its growing complexity. In the A2A era, that same developer can focus on perfecting a high-value niche— such as an agent that specializes in "Real-time Regulatory Compliance". Whether built as a sophisticated multi-agent monolith or a distributed app, these systems can now be exposed to the world as A2A-compliant agents. This means that a specialist vibe coded in one part of the world can be discovered and "hired" by another Orchestrator across the globe. 

## **The Agent Card** 

To facilitate this discovery, every agent is defined by an Agent Card. This is the standardized "CV" of the AI world, providing a machine-readable identity that outlines: 

- **Capabilities:** What tasks the agent can perform. 

- **Security & Compliance:** Its data handling policies and permission requirements. 

- **Interaction Schemas:** How other agents should communicate with it via the A2A protocol. 

## **Registries: From Public Marketplaces to Private Enterprises** 

Once an agent is equipped with its Agent Card, it can be registered within an Agent Registry whose goal is to turn Agents into discoverable services. This offers two primary paths for developers: 

**1. Public Registries (Marketplaces):** Like a global talent agency, public registries allow developers to list their specialist agents for the world to find. This paves the way for building specialist agents for a specific industry and licensing its expertise to thousands of other orchestrators. 

May 2026 

25 

Agent Tools & Interoperability 

**2. Private Registries:** Within the enterprise, Agent Registries provide a secure, governed environment. Developers inside a large corporation can build a specialist agent that automates an internal workflow and register it for use by other departments, ensuring that expertise is shared across corporate boundaries without compromising security. 

Ultimately, the A2A protocol transforms the act of building isolated agentic applications into building the **foundational members of a global, interoperable digital workforce** . 

## **Implementing A2A Protocols** 

The practical implementation of the A2A architecture enables two distinct development motions: 

- exposing AI agent as A2A agent (the supply side) 

- orchestrating remote A2A agents (the demand side) 

## **Exposing A2A Agent** 

Packaging an agent for the A2A ecosystem involves three core steps: 

- **Defining the Agent Card:** Formal agent specification. 

- **Implementing the Agent Executor (The Translation Layer):** It translates incoming A2A requests and responses into the specific calls required by the underlying agentic frameworks (e.g., ADK, LangGraph, or  bespoke enterprise code). 

- **Establishing the A2A Endpoint:** Executor must be exposed as an A2A-compliant endpoint. 

May 2026 

26 

Agent Tools & Interoperability 

Figure 5: The supply-side exposure of a native AI agent as an A2A Server and its demand-side consumption via an A2A Client. 

## **Connecting Remote A2A Agents** 

In a mature ecosystem, an application does not natively possess deep knowledge of every domain it touches. Instead, it acts as an **Orchestrator** —a central hub whose primary cognitive load is dedicated to understanding user intent, managing the overarching workflow, and delegating specific tasks to specialized, remote A2A agents. 

Remote A2A agents operate as an autonomous, domain-bound contractor which communicates over the A2A protocol. Connecting to these remote agents generally follows one of two architectural patterns (code sample from Google ADK): direct point-to-point integration: 

May 2026 

27 

Agent Tools & Interoperability 

## **Python** 

```
# 1. Direct Instantiation via Hardcoded Endpoint
# Ideal for specific vendor integrations or private agents
billing_specialist = RemoteA2aAgent(
    name="billing_agent",
 endpoint="https://api.vendor.com/v1/billing/a2a"
)
```

Snippet 2: Direct remote A2A agent instantiation via a hardcoded endpoint. 

or by using agent registry to discover agents: 

## **Python** 

```
# 2. InDirect Instantiation via Agent Registry
registry = AgentRegistry(project_id=project_id, location=location)
```

```
#The registry resolves resource names and handles authentication validation
agent_name = f"projects/{project_id}/locations/{location}/agents/YOUR_AGENT_ID"
my_remote_agent = registry.get_remote_a2a_agent(agent_name=agent_name)
```

Snippet 3: Indirect remote A2A agent discovery and instantiation via an Agent Registry. 

## **The Extensibility Layer: A2A as the Foundation for UI and Commerce** 

By resolving the fragmentation inherent in the early AI ecosystem, A2A protocol establishes a unified communication layer which in turn enables developers to build atop this standardized substrate. While the core A2A protocol functions as a transport and negotiation backbone, realizing rich, transactional applications very often demand highly specialized capabilities. 

May 2026 

28 

Agent Tools & Interoperability 

This requirement is addressed through the mechanism of A2A Extensions[1] . It provides a standardized pattern for agents to securely advertise, negotiate, and execute optional, higher-order functionalities that transcend basic message passing. 

Three foundational frameworks that operate as native extensions atop the core A2A foundation include the **Agent-to-User Interface** (A2UI), designed to generate dynamic, stateful user experiences; the **Universal Commerce Protocol** (UCP), engineered to facilitate secure, autonomous agentic commerce; and the **Agent Payments Protocol** (AP2) which lays the groundwork for trusted, verifiable agentic payments. All three are discussed in more detail in the following sections. 

## **Monetizing A2A Agents** 

Making an agent work is only half the battle; the other half is ensuring long-term commercial sustainability. Following the success of the Software-as-a-Service (SaaS) paradigm, the A2A protocol naturally enables an **Agent-as-a-Service (AaaS)** model. This allows specialized agents to be offered in a consumption-based model through various sales channels. 

One example is utilizing the **Google Cloud Marketplace as a monetization engine** . Independent agent/software vendors and developers can list their A2A agents on the marketplace to instantly leverage the existing base of Google Cloud enterprise customers. Customers can procure these specialists and at the same time utilize their existing GCP financial commitments. Win-win for everyone. 

The marketplace infrastructure automatically handles the "hard part"—complex billing— by providing native support for hybrid pricing, such as the **"Flat fee with usage"** model. This allows vendors to charge a predictable base fee while monetizing compute or token-based overages. 

May 2026 

29 

Agent Tools & Interoperability 

Figure 6: The Agent-as-a-Service (AaaS) Lifecycle. 

Agents registered in the Google Cloud Marketplace are directly accessible to **Gemini Enterprise** app users. Gemini Enterprise is an advanced agentic platform that brings the best of Google AI to every employee for every workflow. It empowers teams to discover, create, share, and run AI agents within a single secure environment. By integrating with Agent Registries and operating as a native **A2A Client** , the platform augments the human experience by giving employees access to a broad ecosystem of specialized workers. At the same time Gemini Enterprise is a clear example of both an Agent as a Service platform (via its Assistant API), and it is also a host for remote agents. 

While cloud marketplaces and traditional payment gateways will handle the majority of Agent-as-a-Service (AaaS) billing, the A2A protocol also supports permissionless, machine-to-machine microtransactions for developers who want to avoid managing user accounts entirely. 

By utilizing the A2A Extensions framework `[A2AEXT]` , an agent's server can implement the **x402** (or L402) standard. In this pattern, the server intercepts a request and if “unpaid” returns an `HTTP 402 Payment Required` status code, bundled with a machine-readable 

May 2026 

30 

Agent Tools & Interoperability 

invoice. The calling agent executes the payment autonomously and retries the request with a cryptographic proof-of-payment token. This provides a standardized option for pay-per-call endpoints that require strictly stateless, automated billing. 

## **The Extensibility Layer: A2A as the Foundation for UI and Commerce** 

By resolving the fragmentation inherent in the early AI ecosystem, A2A protocol establishes a unified communication layer which in turn enables developers to build atop this standardized substrate. While the core A2A protocol functions as a transport and negotiation backbone, realizing rich, transactional applications very often demand highly specialized capabilities. This requirement is addressed through the mechanism of A2A Extensions [A2AEXT]. It provides a standardized pattern for agents to securely advertise, negotiate, and execute optional, higher-order functionalities that transcend basic message passing. 

Two foundational frameworks that operate as native extensions atop the core A2A foundation include the **Agent-to-User Interface (A2UI)** , designed to generate dynamic, stateful user experiences, and the **Universal Commerce Protocol (UCP)** , engineered to facilitate secure, autonomous agentic commerce. Both are discussed in more detail in the following sections. 

May 2026 

31 

Agent Tools & Interoperability 

## **Agent-to-UI (A2UI) Interoperability** 

## **The Communication Gap** 

When you ask a colleague, "How did Q4 perform by region?" they don't hand you a spreadsheet. They sketch a bar chart on the whiteboard, circle the standout regions, and add context. This is how humans share insights: through visuals and interaction. 

Yet our agents return raw JSON. You then build the chart yourself. Import libraries, configure axes, manage state. This context-switching between asking for insights and doing frontend work breaks the vibe coding flow. 

Agent-to-UI (A2UI) interoperability resolves this enabling Agents to generate complete, interactive user interfaces as outputs: not just JSON blobs. 

## **Generative UI & A2UI** 

## **What is Generative UI?** 

Generative UI is the concept of LLMs dynamically creating user interfaces at runtime based on user intent and context. Instead of developers hard-coding every possible UI state, the model generates appropriate interfaces on demand. When you ask "Compare Q4 sales by region", the system doesn't just retrieve data: it composes an interactive layout, cards, filters, and controls, tailored to that specific request. 

May 2026 

32 

Agent Tools & Interoperability 

This represents a shift from static, pre-built interfaces to dynamic, context-aware UIs. The challenge is doing this safely. Running arbitrary UI code generated by an LLM can pose security risks: code injection, XSS attacks, and uncontrolled side effects. 

## **A2UI: A Secure Implementation** 

A2UI is **a framework-agnostic standard for declaring UI intent** — Google's opensource way of letting agents describe interfaces in a portable, declarative format instead of streaming raw data or shipping arbitrary code. 

To see why a _format_ matters here, think about how a composer ships their work. They don't hand musicians a recording: they hand them sheet music. The same score plays on a piano, an orchestra, or a synthesizer; each instrument interprets the notation through its own voice. A2UI is sheet music for UI: the agent writes the intent (what to render and how it composes), and any renderer (e.g. React, Angular, Lit, Flutter, Jetpack Compose, SwiftUI, etc) performs it natively on the device the user actually has. The agent doesn't need to know whether you're targeting web, mobile, wearable, or appliance, it just knows the catalog of available components and any examples you want to give. 

That separation of concerns is what makes A2UI safe. The agent doesn't generate executable code (a security nightmare) and it doesn't ship pre-rendered pixels (which can't reflow or stay interactive). Instead it requests components from a trusted catalog (e.g. buttons, text fields, cards, your own charts) and the client renders them using its own component library. The catalog defines what's available, the agent decides how to arrange them, the client assembles the final structure. Compositional, like LEGO blocks, but the blocks are UI components from _your_ design system. 

May 2026 

33 

Agent Tools & Interoperability 

## **The Basic Catalog (and Bringing Your Own)** 

A2UI ships a basic catalog of 18 ready-to-use components for prototyping and demos: 

**==> picture [469 x 141] intentionally omitted <==**

**----- Start of picture text -----**<br>
Category Components<br>Layout Row, Column, List<br>Display Text, Image, Icon, Divider<br>Containers Card, Modal, Tabs<br>Media Video, AudioPlayer<br>Interactive as Button, TextField, CheckBox, Slider,<br>DateTimeInput, ChoicePicker<br>**----- End of picture text -----**<br>


Table 1: A2UI Basic Catalog 

This set was called "standard" in v0.8 and renamed to "basic" in v0.9, a deliberate signal that production frontends should bring their own catalog, mapping their existing components (your design-system buttons, your charts, your maps) to A2UI types. The agent doesn't change; only the renderer's catalog mapping does ( `ChoicePicker` was `MultipleChoice` in v0.8.) 

May 2026 

34 

Agent Tools & Interoperability 

Here's what an A2UI message looks like (v0.9 format): 

## **JSON** 

```
{
  "version": "v0.9",
  "updateComponents": {
    "surfaceId": "main",
    "components": [
      {"id": "root", "component": "Column", "children": ["title",
"summary", "export"]},
      {"id": "title", "component": "Text", "text": "Q4 Sales", "variant": "h1"},
      {"id": "summary", "component": "Text", "text": "Revenue grew 12% QoQ"},
      {"id": "export", "component": "Button", "child": "export-label",
       "action": {"event": {"name": "export_csv"}}},
      {"id": "export-label", "component": "Text", "text": "Export CSV"}
    ]
  }
}
```

Snippet 4: Example A2UI message 

Components form a flat adjacency list referenced by id, which makes the structure easy for an LLM to generate incrementally and easy for the client to update without re-rendering. A separate `createSurface` message (not shown) tells the client which id is the root. The client then renders this as a complete, interactive interface: no React code required. 

## **Generating A2UI: Two Patterns** 

There are two ways to produce A2UI in practice, and the choice is mostly about where the layout decision lives. 

May 2026 

35 

Agent Tools & Interoperability 

The **default** is to let the LLM emit A2UI directly: the model owns the layout, adapts it to user intent, and the same agent handles "compare these regions" and "show me trends" with different interfaces. Production code for this pattern uses the official `a2ui-agent-sdk` and lives in 4.4. 

The **specialization** is to have a tool return a fixed A2UI structure: one tool call, no LLM tokens spent on UI generation, fully predictable output. This is the right call when the layout is deterministic from inputs: every region's sales dashboard looks the same, every booking form has the same fields. Effectively, the tool is a server-side template. 

A clean tool-as-template tool does two things in its body: build the A2UI structure with **data bindings** (path references, not f-string interpolation) and return it. The framework's `A2uiPartConverter` (from `a2ui-agent-sdk` ) intercepts the tool's response and routes it to the client as an A2UI part, so the tool itself stays a plain Python function: 

## **Python** 

`from google.adk.agents import LlmAgent from google.adk.models import Gemini def  get_sales_dashboard(region: str) -> dict: """Build a data-bound sales dashboard for `region`.""" data = fetch_sales(region) return { "version": "v0.9", "updateComponents": { "surfaceId": "sales", "components": [ {"id": "root", "component": "Column", "children": ["title", "total", "drill"]}, {"id": "title", "component": "Text", "text": {"path": "/title"}, "variant": "h1"},` **Continues next page..** `.` 

May 2026 

36 

Agent Tools & Interoperability 

```
{"id": "total", "component": "Text", "text",{"path": "/total"}},
{"id": "drill", "component": "Button", "child": "drill-label",
                 "action":{"event":{"name": "expand_details"}}},
{"id": "drill-label", "component": "Text", "text": "Drill Down"},
],
},
}
agent = LlmAgent(
    name="sales_agent",
    model=Gemini(model="gemini-flash-latest"),
    tools=[get_sales_dashboard],
)
# Wire the converter at executor setup so this tool's response becomes an
A2UI part:
#   from a2ui.adk.send_a2ui_to_client_toolset import A2uiPartConverter
#   A2aAgentExecutorConfig(event_converter=A2uiPartConverter(catalog,
bypass_tool_check=True))
```

Snippet 5: LLM-generates-UI pattern 

Data values flow through a parallel `updateDataModel` message that resolves the `{path: "/title"}` references, so clients can re-render on data updates without re-sending the structure. The LLM only sees a structured tool response (not the rendered UI) so its context stays focused on what to do next, not on the UI it just built. 

## **When to Use Each Pattern** 

**==> picture [470 x 106] intentionally omitted <==**

**----- Start of picture text -----**<br>
Query Return<br>"What's the average?" Data (text)<br>"Compare these regions" UI generated by the LLM (§4.4)<br>"Show me my dashboard" UI built by a tool (this section)<br>API-to-API Data (JSON)<br>**----- End of picture text -----**<br>


Table 2: Query to Output Mapping 

May 2026 

37 

Agent Tools & Interoperability 

Use A2UI when interaction or visualization adds value beyond the raw data, and pick the pattern by who owns the layout decision: the LLM (intent-driven) or a deterministic template (input-driven). 

## **Interactive Artifacts & The Canvas** 

Traditional chat interfaces are linear. Each response is static. The canvas approach is different: it creates a persistent workspace where both the agent and user can edit. 

Instead of scrolling through chat history, you have a living document. The agent can modify sections. You can edit manually. Both changes are reflected in real-time. 

May 2026 

38 

Agent Tools & Interoperability 

## **Canvas + A2UI** 

Combining canvas persistence with A2UI interactivity creates useful workflows: 

Figure 7: User, Agent, Canvas interaction flow 

The UI isn't just rendered: it's a communication medium. The agent observes your interactions and responds accordingly. 

May 2026 

39 

Agent Tools & Interoperability 

## **Best Practices** 

## **Let LLMs Generate A2UI** 

For the LLM-generates-UI pattern (the default introduced in 4.2), hand-coding A2UI JSON is tedious. Use the official `a2ui-agent-sdk` ( `pip install a2ui-agent-sdk` ): the `A2uiSchemaManager` builds a system prompt that already embeds the catalog schema and worked examples, the catalog ships its own JSON-Schema validator, and the same SDK provides a parser for the `<a2ui-json>` blocks the agent emits. Then validate and retry on schema errors. 

## **Python** 

```
# pip install a2ui-agent-sdk google-adk
import asyncio, json
import jsonschema
from a2ui.schema.manager import A2uiSchemaManager
from a2ui.basic_catalog.provider import BasicCatalog
from a2ui.schema.constants import VERSION_0_9
from a2ui.parser.parser import parse_response
from google.adk.agents import LlmAgent
from google.adk.models import Gemini
from google.adk.runners import InMemoryRunner
from google.genai import types
# 1. The SDK loads the catalog, builds the validator, and renders a complete
#    system prompt with the schema and worked examples baked in.
schema_manager = A2uiSchemaManager(
    version=VERSION_0_9,
    catalogs=[BasicCatalog.get_config(version=VERSION_0_9)],
)
catalog = schema_manager.get_selected_catalog()
```

**Continues next page...** 

May 2026 

40 

Agent Tools & Interoperability 

```
agent = LlmAgent(
    model=Gemini(model="gemini-flash-latest"),
    name="ui_agent",
    instruction=schema_manager.generate_system_prompt(
        role_description="You generate interactive UIs as A2UI v0.9 messages.",
        ui_description="Use Cards, Lists, ChoicePickers, and Buttons to
present data.",
        include_schema=True,
        include_examples=True,
    ),
)
# 2. Run the agent. It emits text containing one or
more <a2ui-json>...</a2ui-json>
#    blocks; parse_response() extracts the parsed JSON. Validate, then retry
on errors.
async def create_ui(intent: str, data: dict, max_retries: int = 3) -> list:
    runner = InMemoryRunner(agent=agent, app_name="ui_demo")
    session = await runner.session_service.create_session(
        app_name="ui_demo", user_id="u",
        state={"expression": "{expression}"},  # escapes the SDK's
templating placeholder
    )
    query = f"{intent}\n\nData: {json.dumps(data)}"
    last_error = None
for _ in range(max_retries + 1):
        chunks = []
        msg = types.Content(role="user", parts=[types.Part(text=query)])
async for ev in runner.run_async(user_id="u",
session_id=session.id, new_message=msg):
if ev.content and ev.content.parts:
                chunks.extend(p.text for p in ev.content.parts if p.text)
        blocks = [rp.a2ui_json for rp in parse_response("".join(chunks))
if rp.a2ui_json]
try:
for b in blocks:
for m in (b ifisinstance(b, list) else [b]):
                    catalog.validator.validate(m)
return blocks
except jsonschema.ValidationError as e:
```

**Continues next page...** 

May 2026 

41 

Agent Tools & Interoperability 

```
            last_error = e
            path = "/".join(str(p) for p in e.absolute_path)
            query = (
f"Your previous response failed schema validation at {path}: "
                f"{e.message[:200]}\nFix this and retry:
{intent}\nData: {json.dumps(data)}"
            )
raise ValueError(f"Schema validation failed after {max_retries}
retries: {last_error}")
```

Snippet 6: A2uiSchemaManager implementation 

In production, wrap `create_ui()` in try/except and fall back to a text response on schema-validation failure. LLM output is stochastic, and the renderer should never see a malformed payload. 

## **Hybrid Output for Flexibility** 

Provide both data and UI so consumers can choose: 

## **JSON** 

```
{
"data": {"sales": [...]},
"ui": {"version": "v0.9", "updateComponents": {"surfaceId": "main",
"components": [...]}},
"ui_available": true
}
```

Snippet 7: Hybrid Output Example Schema 

API clients ignore the `ui` field and use `data` . Human-facing clients render the A2UI message. 

May 2026 

42 

Agent Tools & Interoperability 

## **Summary** 

Generative UI lets LLMs create user interfaces at runtime based on user intent. A2UI is Google's open-source standard for doing this safely: a framework-agnostic format for declaring UI intent, so the same agent message renders natively in Lit, Flutter, React, or your own design system. 

The security model matters: agents can't inject arbitrary code. They can only request components the renderer's catalog already trusts. That's what makes A2UI safe while still enabling dynamic, generative interfaces. 

## **Agents and Commerce (AP2 and UCP)** 

## **Autonomous Procurement with a workflow example** 

Vibe coders learn checkout, catalog , order capability and mandate with their agents. 

## **Key characteristics and benefits of Protocols** 

Typed schemas, Security and open source (Integration debt and vendor neutrality) 

## _Lab recommendations:_ 

htps://codelabs.developers.google.com/next26/adk-agent-commerce#0 

May 2026 

43 

Agent Tools & Interoperability 

While earlier sections focused on how coding agents interact with tools, other agents, and user interfaces within an Agentic framework, those interactions are often limited to "read" operations using protocols like MCP, A2A, and A2UI. As these systems evolve, agents must transition toward executing "actions" that carry real-world financial implications. 

Prioritizing commerce protocols and building a robust operational harness ensures your agents adhere strictly to industry standards when managing transactions. 

To understand how to implement these systems, we must first explore the nature of these protocols and their complementary roles. 

## **What is AP2 and UCP?** 

Figure 8: AP2 and UCP Ecosystem 

May 2026 

44 

Agent Tools & Interoperability 

Imagine you and your roommates are starving at 2:00 AM. You are too busy studying to stop, so you deploy your AI Smart Assistant to get food for the apartment.Here is how UCP (Universal Commerce Protocol) and AP2 (Agent Payments Protocol) split the workload to get that burrito to your dorm lobby. 

## **UCP (Universal Commerce Protocol): The Ultimate Food Delivery App** 

In 2024, your AI would have to manually open Chrome, go to the local burrito place's poorly designed website, try to click the "extra guac" checkbox, and hope the site doesn't crash. Instead, UCP acts like a universal translator. Every restaurant on campus publishes their menu, hours, and customization options in a clean, standard machine language. 

Your AI uses UCP to ask the restaurant’s system, "Are you still open? Do you have vegetarian burritos?". To build an order one could ask: "One chicken burrito, no onions, add sour cream, and a side of chips" and the restaurant responds back with the tax, delivery fee, and expected arrival time. 

In short: UCP is how your AI talks to the store, looks at the options, and builds the perfect order. Prior to UCP, your application would have been able to discover and get information. However the interactions between these different providers need to be orchestrated individually. By standardizing the interaction, we make it easier for non-humans to interact with each other. 

May 2026 

45 

Agent Tools & Interoperability 

## **AP2 (Agent Payments Protocol):** _**The Parent's Credit Card with Strict Rules**_ 

Now the food is in the cart, but your AI needs to pay. You obviously aren't going to type your actual debit card number into an AI prompt and say "Go wild." 

AP2 is the **open, shared protocol** that provides a common language for secure, compliant transactions between agents and merchants that lets your AI pay for the food only within rules you set. 

- **The Guardrails (The Mandate):** Before you send the AI off, you approve a digital rule: _"You can spend up to $25 at Taco Bell."_ 

- **The Handshake:** When the AI checks out, it doesn't show your card number. It shows a digital, encrypted "promissory note" signed by you that says: _"My human approved this $18.50 order."_ The restaurant's bank instantly verifies this digital signature. 

- **No Hidden Fees:** If the restaurant tries to sneakily charge you $50 instead of $18.50, the AP2 protocol blocks it instantly because it violates the rules you signed off on. 

**In short:** AP2 is the **secure lockbox** that lets your AI pay for things using your money, but ensures it can never buy a $1,000 TV by mistake. 

**==> picture [470 x 147] intentionally omitted <==**

**----- Start of picture text -----**<br>
UCP AP2<br>Brain that decides what to buy, handles the menu,  Is the wallet that securely handles how to pay<br>and puts the food in the cart. for it without you getting scammed.<br>Integrates with any business provider Integrates with payment<br>Unified integration:   Authorization & Auditability<br>Shared language:   Authenticity of Intent<br>Extensible architecture  Agent Error and Hallucination<br>Security-first approach Accountability<br>**----- End of picture text -----**<br>


Table 3: Comparison for UCP and AP2 

May 2026 

46 

Agent Tools & Interoperability 

- If you are a developer building your UCP agent  for a merchant or the payment processor, follow the instructions here. 

- If you are a developer building your AP2 agent for a merchant or the payment processor, follow the instructions here. 

- If you are a developer building an agent that consumes an AP2 agent such as a shopper, follow the instructions here. 

## **Conclusion** 

By adopting foundational standards like MCP, A2A, A2UI, AP2 and UCP, organizations can eliminate the crushing technical debt of bespoke integrations and focus entirely on orchestrating high-value business logic. This paradigm shift fundamentally elevates developers from mere mechanics wiring fragile APIs into true architects of a global, autonomous workforce. As these standardized communication layers mature, they will unlock entirely new economies of scale, transforming how enterprise software is built, consumed, and monetized. 

May 2026 

47 

Agent Tools & Interoperability 

## **Endnotes** 

1. A2A Community (2026) A2A Documentation: Extensions, _A2A Protocol_ , htps://a2a-protocol.org/latest/topics/extensions/ 

2. Antigravity Team (2026) Antigravity Editor: MCP Integration, _Antigravity Docs_ , htps://antigravity.google/docs/mcp 

3. Fowler M, Lewis J (2014) Microservices, _MartinFowler_ , htps://marinfowler.com/aricles/microservices.html 

4. Google A2A Team (2025) Announcing the Agent2Agent Protocol (A2A), _Google Developers Blog_ , htps://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ 

5. Google A2UI Team (2025) Introducing A2UI: An Open Project for Agent-Driven Interfaces, Google Developers Blog, htps://developers.googleblog.com/introducing-a2ui-an-open-projectfor-agent-driven-interaces/ 

6. Google A2UI Team (2026) A2UI v0.9: The New Standard for Portable, Framework-Agnostic Generative UI, _Google Developers Blog_ , htps://developers.googleblog.com/a2ui-v0-9-generative-ui/ 

7. Google A2UI Team (2026) A2UI [Computer Software], GitHub, htps://github.com/google/A2UI 

8. Google Cloud Databases Team (2025) MCP Toolbox for Databases: Simplify AI Agent Access to Enterprise Data, _Google Cloud Blog_ , htps://cloud.google.com/blog/products/ai-machine-learning/mcp-toolbox-fordatabases-now-suppors-model-context-protocol 

9. Google Cloud Team (2026) Announcing Agents-to-Payments (AP2) Protocol, _Google Cloud Blog_ , htps://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments -ap2-protocol?e=48754805 

10. Google Cloud Team (2026) Configure MCP in an AI Application, _Cloud Docs_ , htps://docs.cloud.google.com/mcp/confgure-mcp-ai-application#antigravity 

11. Google Stitch Team (2026) Google Stitch Documentation: MCP Setup, _Stitch with Google Docs_ , htps://stitch.withgoogle.com/docs/mcp/setup 

12. MCP Team (2026) Specification for Model Context Protocol, _MCP Docs_ , htps://modelcontextprotocol.io/specifcation/2025-11-25 

May 2026 

48 

Agent Tools & Interoperability 

13. Muchandi V (2026) Rad-skills: Gemini Skills for Rapid Agent Development, _GitHub_ , htps://github.com/VeerMuchandi/rad-skills 

14. Hotz H, (2026) The Agentic Commerce Revolution, _O'Reilly Radar_ , htps://www.oreilly.com/radar/the-agentic-commerce-revolution/ 

15. Pichai S (2017) Making AI Work for Everyone, _Google Blog_ , htps://blog.google/innovation-and-ai/products/making-ai-work-for-everyone/ 

16. Saboo S, Overholt K (2026) Developer’s Guide to AI Agent Protocols, _Google Developers Blog_ , htps://developers.googleblog.com/developers-guide-to-ai-agent-protocols/ 

17. Styer M, Patlolla K, Mohan M, Diaz S (2025) Agent Tools & Interoperability with Model Context Protocol (MCP), _Kaggle_ , htps://www.kaggle.com/whitepaper-agent-tools-and-interoperability-with-mcp 

18. The Linux Foundation (2026) A2A Protocol Surpasses 150 Organizations, Lands in Major Cloud Platforms, and Sees Enterprise Production Use in First Year, _Linux Foundation Press_ , htps://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major -cloud-platorms-and-sees-enterprise-production-use-in-frst-year 

19. Common AI Catalog and Registry Standard Documentation (2026), htps://github.com/Agent-Card/ai-catalog 

20. Ricardo Cataldi (2026), MCP vs A2A: Tools, Agents, and Where Each Protocol Belongs, htps://levelup.gitconnected.com/mcp-vs-a2a-tools-agents-and-where-eachprotocol-belongs-53e1f9ab9765 

21. Lukas Geiger (2026), Monetizing AI Agents: Ensuring Profitability htps://medium.com/google-cloud/monetizing-ai-agents-ensuring-proftability-92efa535ebb3 

May 2026 

49 

## **Agent Skills** 

**Authors: Tanvi Singhal, Gabriela Hernandez Larios, Debanshu Dus, Lavi Nigam, and Smitha Kolan** 

Agent Skills 

## **Acknowledgements** 

## **Curators and editors** 

Shubham Saboo 

## **Designer** 

Michael Lanning 

May 2026 

2 

## **Table of contents** 

|1. Introduction|4|
|---|---|
|2. What is an Agent Skill (and How to Build Your First One)|6|
|Skill Anatomy  & Progressive Disclosure|7|
|Path A: Translating what you already know|8|
|Path B: Crystallizing what the agent just did|9|
|Trying it out & How to install Skills today|10|
|Wait but how does a Skill differ from MCP and AGENTS.md?|11|
|3. Why did Agent Skills become so popular, so fast?|12|
|Skills for chatbots, for coding agents, or for multi-agent enterprise use cases?|13|
|4. Evaluating Skills|15|
|The Evaluation Toolkit|17|
|The trigger is the first gate|18|
|Output quality and tool trajectory|19|
|System vs. Skill: The Evaluation Illusion|21|
|Token budget: isolation is a trap|22|



## **Table of contents** 

|What "eval coverage" means|24|
|---|---|
|5. From Prototype to Production|25|
|What's actually inside an agent runtime|27|
|Why skills are the unit of improvement|28|
|The failure mode that breaks demos: context overflow|29|
|What this means for the token budget|31|
|6. On Meta-Skills and Self-Improving Skills|32|
|Where this falls apart|34|
|Where this is going|35|
|7. Composing and Packaging Skills|36|
|Execution Routing: DAG Orchestration|36|
|Environment Packaging: Capability Profiles|37|
|Populating the Graph: The Canonical Skill Taxonomy|37|
|Context Debt and Shifting Intelligence Left|38|
|Architectural Tradeoffs|38|



## **Table of contents** 

|Actionable Best Practices|39|
|---|---|
|8. How to Decide Among the Hundreds of Skills That Exist|39|
|9. Conclusion|41|
|Appendix A – The Practical Cheatsheet|43|
|The minimal SKILL.md|43|
|The folder structure.|44|
|Naming|44|
|The description field|45|
|The five rules|45|
|The quality principles|46|
|Do's and Don'ts|46|
|Skill smells (revise if you see these)|47|
|Eval coverage checklist|48|
|Deployment checklist|48|
|One-line mental model|49|



## **Table of contents** 

|Where to start tomorrow|49|
|---|---|
|Appendix B – Case Study: Domain Expertise as Code (Vertical Skills in Retail)|50|
|Why retail is the canonical case for skills|50|
|What the architecture looks like|51|
|An illustrative skills library|52|
|How does the same query route through the library|53|
|Ownership: who writes which skill|54|
|The read / draft / act ladder|55|
|Why is this harder to compete with than a custom agent|55|
|Cold start: where to actually begin|56|



Agent Skills 

Agent Skills turn any generalpurpose agent into a specialist on demand. No context bloat. Portable and lightweight. 

## **1. Introduction** 

Agent Skills are a way to equip your agent with knowledge and company context. An Agent Skill is a folder containing a `SKILL.md` file , with `scripts/` , `references/` , and `assets/` directories. **Section 2** covers the anatomy in detail. 

Agent Skills are becoming the standard for cross-platform portability. But why the sudden adoption velocity? We believe Agent Skills tackle four main friction points in AI agent development: 

**1. Too many instructions, worse results** . Dumping every instruction you can think of into a single system prompt inevitably degrades Large Language Model (LLM) performance, a problem known as context rot. Skills solve this by loading exclusively on demand. **Section 5** unpacks the research behind this. 

May 2026 

7 

Agent Skills 

**2. Knowing how, not just knowing what** . LLMs already have reasonable analogs for remembering what happened (episodic memory) and remembering facts (semantic memory). What they've lacked is a way to remember how to do things step by step, which is called procedural memory. Agent Skills can be seen as the first credible **procedural memory** primitive for LLM Agents. 

**3. Multi-agent overload** . The ecosystem was flooded with complex multi-agent systems that are notoriously hard to build and maintain. While still necessary for certain tasks, Skills **Section** 

allow a single general-purpose agent to seamlessly flex into many specialist roles. **3** develops this argument in depth, with a worked example. 

**4. Portability** . A folder with a markdown file is a remarkably lightweight primitive. Any agent with filesystem access can use them, making them perfectly portable across a multivendor AI landscape. 

In this whitepaper, we cater to two personas: Builders (those using Skills) and Developers (those creating, versioning, and managing them). We’ll gently walk through what a Skill is and how to use it ( **Sections 2 to 3** ), before diving into complex Developer topics like evaluation, production readiness, meta-skills, and composition ( **Sections 4 to 8** ). 

(Impatient? **Appendix A** offers a printable operational cheat sheet, and **Appendix B** walks through a retail case study). 

May 2026 

8 

Agent Skills 

## **2. What is an Agent Skill (and How to Build Your First One)** 

Agent Skills are a primitive for giving a general-purpose agent on-demand specialist competence. Yes, a Skill can be as simple as a single markdown file, but it doesn’t have to stop there, and the paradigm behind it is quite innovative. 

Today we are seeing Agent Skills emerge through two distinct  patterns: 

**The first path is driven by subject matter experts** , who already have institutional knowledge written down somewhere. Think of a compliance officer with a 30-page runbook, or an HR manager with onboarding guides for new hires. None of them need to learn to code to write and start using a Skill. They already have the content; the only job left is to translate it into a format the agent can use smartly. 

**The second path involves developers** wrapping agentic or coded workflows into Skills. If an agent successfully executes a non-trivial, repetitive task, you don't want it to have to figure out the process from scratch next time. Instead, you want the agent to create a Skill out of this successful run. In short, we are observing an emerging pattern: anything that is a good, reusable workflow becomes a Skill, and you don't have to write it yourself, the agent does, you review. This is already meta-skills territory, which we introduce gently here before going deep on it in **Section 6** . 

Both groups produce the same artifact, a **Skill** folder anchored by the `SKILL.md` primitive, but the journey to get there is different. 

May 2026 

9 

Agent Skills 

## **Skill Anatomy  & Progressive Disclosure** 

Before going into the different paths, let’s review the Skill anatomy. Every skill lives in its own directory and must contain a SKILL.md. To see the full canonical structure, as defined by the open standard at agentskills.io, let's look at a practical example. 

Below is an illustrative folder for a Skill designed to conduct daily cafe preparation. (Remember, the only mandatory file is `SKILL.md` . The rest is optional): 

**==> picture [469 x 155] intentionally omitted <==**

**----- Start of picture text -----**<br>
cafe-preparation/<br>├──  SKILL.md                        # Required: metadata + instructions<br>├──  scripts/                         # Optional: executable code (any language)<br>│   ├──  calc_quantities.py           # Estimates lattes, croissants, etc.<br>│   └──  convert_to_ingredients.py    # Converts drinks and pastries into..<br>├──  references/                      # Optional: supplementary context<br>│   ├──  menu_and_recipes.md          # Matcha latte: 3g powder, 200ml...<br>│   └──  minimums.md                  # Always prep for at least 40 lattes...<br>└──  assets/                          # Optional: templates, configs, schemas<br>    ├──  prep_sheet_template.md       # The final layout for the kitchen staff<br>    └──  shopping_list_template.md    # The layout for vendor ordering<br>**----- End of picture text -----**<br>


Snippet 1: Directory tree structure showing the standard layout and progressive disclosure design for the `cafe-preparation` skill. 

The innovative piece is the **progressive disclosure** . Skills load in three levels: 

**1. Metadata** (name + description) is always in the agent's context. 

`2. SKILL.md` body is loaded only when the skill triggers. 

**3. Bundled resources** are loaded strictly as needed (and scripts execute without ever polluting the token window). 

May 2026 

10 

Agent Skills 

This means you can have a hundred installed skills but only pay the tiny token cost for their metadata on every turn. Let's get practical and look at how to build one. 

## **Path A: Translating what you already know** 

A minimal SKILL.md template lives in Appendix A. You can copy it directly. The piece worth focusing on first is the YAML frontmatter, because it's the activation trigger: 

```
---
name: cafe-preparation
description: |
  Calculates daily ingredient needs and generates prep sheets for cafe operations.
  Use when the user asks to estimate daily quantities, convert drinks to
ingredients, or generate shopping lists.
  Do NOT use for employee shift scheduling or financial accounting.
---
```

Snippet 2: YAML frontmatter configuration for the `cafe-preparation` skill. 

There are two things worth getting right from the start: naming and the description field. 

**Naming** . When naming, be obvious and boring: use snake_case for directories (e.g., `bigquery_ingestion` ), kebab-case for skill names (e.g., `pdf-processing` ), and prefer the gerund form like `managing-databases` . Avoid generic names such as utils or tools and omit any internal jargon. 

**Description** . This is your routing algorithm. It is the only thing the model sees to decide whether to load the Agent Skill. State what it does, front-load trigger keywords, be pushy if the model under-triggers, and explicitly state what it is not for. 

May 2026 

11 

Agent Skills 

Once the SKILL.md is drafted, you build out the rest of the folder. This is where **progressive disclosure** starts paying off. Anything that doesn't need to be in the SKILL.md body goes somewhere else: 

- **Scripts** . Deterministic work (parsing exports, math, formatting) lives in scripts/. The model decides what to do; the script does the heavy lifting. 

- **References** . Knowledge that is only relevant once the skill is running (domain principles, definitions, edge case handling) lives in references/ and loads on demand. 

- **Assets** . Templates and schemas live in assets/. 

Rule of thumb: if the `SKILL.md` is starting to get long, the next paragraph probably belongs in references/ and not in the body. 

(Impatient? **Appendix A** offers a printable operational cheat sheet with curated Do’s and Don’ts to guide your initial Skill development).[1] 

## **Path B: Crystallizing what the agent just did** 

The second path starts from the other end. Instead of translating something you already have, you're crystallizing something the agent just did. 

The agent completed a task successfully. You noticed the workflow was reusable. You want the next instance of that kind of task to benefit from what was just learned. 

This is the meta-skills territory: Skills whose job is to capture or improve other Skills. Tools like Anthropic's skill-creator[2] , Nous Research's Hermes Agent[3] , and the self-improvingagent-skills pattern from awesome-llm-apps[4] all support this workflow. The agent watches a successful trajectory and proposes a SKILL.md draft. You review, instead of authoring. 

May 2026 

12 

Agent Skills 

The same quality bar applies. A reviewed, iterated, agent-drafted Skill can be excellent. An un-reviewed agent-drafted Skill is often worse than no Skill at all. We come back to this whole topic with much more depth in **Section 6** , where we cover meta-skills. 

## **Trying it out & How to install Skills today** 

Once the folder is ready (whether you wrote it or an agent drafted it for you), it is time to try it out. Drop it in the right place for your tool, restart the agent, and test it with a natural prompt. Watch the trace to confirm the skill actually triggered. Then try a prompt where it should NOT trigger and confirm it stays quiet. 

But where exactly is the "right place"? 

This is where things get a bit nuanced, and it's one of the downsides of the exploding popularity of Skills. Every agent or coding tool has converged on the format, but they each look in a slightly different place for it. Broadly, there are three paradigms for how you will interact with and install Skills today: 

1. The File Drop (Coding Agents & CLIs): For local environments, the pattern is file-based, you drop or install the skill folder into a specific hidden directory and the agent picks it up. While a highly welcome cross-tool convention is emerging around a shared .agents/ skills/ folder at your project root, many tools still protect their own bespoke paths. (Pro tip: If you bounce between multiple CLI tools and IDEs, community managers like skillport or openskills will automatically symlink your central skills library to every tool's expected location). 

May 2026 

13 

Agent Skills 

**2. The UI Install (Web & Enterprise Workspaces)** : If you are using web-based collaborative platforms or consumer AI chatbots, you rarely touch a terminal or a hidden folder. These platforms allow you to install, upload, or manage your Skill folders directly through a visual UI registry with just a few clicks, handling the routing behind the scenes for your whole team. 

**3. The Programmatic Route (Custom Frameworks)** : If you are building bespoke, noncoding agents from scratch (for example, using the Google Agent Development Kit), you load skills programmatically. You point your code to the folder path—such as registering it through a SkillToolset class[5] , which seamlessly auto-generates the necessary load_skill routing tools for the model under the hood. 

The overall pattern is the same everywhere: drop the skill folder into the right directory, restart the agent, and it picks it up. The "right directory" is what changes depending on the tool. 

A piece of advice: check the documentation of your specific coding agent or AI chatbot before assuming. The format is shared, but the install path, the activation rules, and the pertool details (allowed-tools whitelisting, security gates, plugin bundling) are not. 

## **Wait but how does a Skill differ from MCP and AGENTS.md?** 

To establish the architectural fit of Agent Skills, it helps to map these primitives. 

May 2026 

14 

Agent Skills 

**Skill vs. MCP** . These do not compete, they compose. Model Context Protocol is about reach: an MCP server connects the agent to an external system (Drive, Salesforce, BigQuery, or an - internal API). A Skill is about know how: it teaches the agent how to think about a particular kind of work. When a Skill needs data, it tells the agent to call a tool, typically one provided by an MCP server. 

**Skill vs. AGENTS.md** . From one side AGENTS.md is always loaded within the project; Skills load on demand. The cleanest setups use both. Keep AGENTS.md tight (project conventions, stack, build commands, etc.) and if needed use it also as a router into the Skills library, with a short catalog at the bottom that tells the agent what’s available. 

## **3. Why did Agent Skills become so popular, so fast?** 

Imagine it's early 2025. You are asked to build a system that offload repetitive back office work: generating slide decks from briefs while adhering to the company style, parsing structured invoicing PDFs, drafting HR onboarding guides, summarising weekly compliance reports, and tackling a long tail of similar tasks that will inevitably grow as the team finds new things to automate. 

Most likely, you would have defaulted to a multi-agent architecture. A router agent at the top dispatching to a handful of specialist sub-agents beneath it. You would then spend agonizing hours on CI/CD pipelines, orchestration logic, and ensuring that a deployment for the new HR sub-agent didn't break the invoice sub-agent. 

May 2026 

15 

Agent Skills 

With the release of Agent Skills, this workflow becomes vastly simpler. This friction is exactly how the Skill format was first created by Anthropic, with the first skills for reading PDFs and creating slides[6] , which represents a much lighter version to accomplish this. Instead of a router dispatching subagents, you have one agent with a library of skills. Skills can run commands, call MCP servers, and bundle Python scripts. The agent decides which to load when. You maintain skills, not agents, and the operational surface can shrink. 

## To be **very** clear: Agent Skills do not kill multi-agent architectures. 

Multi-agent remains the absolute right answer when you have genuine parallelism, real capability boundaries (different access, different security postures, different external systems), hierarchical decomposition where the abstraction layers actually differ, adversarial or check-and-balance setups, sub-agent intercommunication, or heterogeneous models. This list isn't exhaustive. 

What Skills did was introduce a missing architectural primitive. Many systems that were built multi-agent _by default_ can now be elegantly simplified to single-agent-with-skills _by design_ . 

## **Skills for chatbots, for coding agents, or for multi-agent enterprise use cases?** 

The first publicly visible skills were AI chatbot-shaped. The coding-agent narrative arrived within days or weeks. And once it did, skills exploded. They landed straight into the vibecoding fever and turned out to be the format developers had been wanting. 

May 2026 

16 

Agent Skills 

In some multi-agentic architectures, by definition, each sub-agent is already a specialist. A research agent might not need a research skill. Skills are more useful in scenarios when one general-purpose agent has the flexibility to become a specialist across different things, by design. However, there might be cases where multi-agent and skills do compose well, for example, if there is a need for each specialized agent to have its own scoped skill library. 

Now consider a logistics company with 100  process variants depending on product type, tools, route constraints, customer SLAs, regulatory zones, etc. How could this be solved elegantly and lightweight: 

- **One agent, one giant context window** . Causes immediate context rot and exorbitant token costs. 

- **RAG over the runbooks** . Probably the right answer two years ago. But you're now running a vector DB, an embedding model, and a chunking strategy whose quality has nothing to do with the actual procedures. 

- **Multi-agent, one subagent per process** . 100 subagents, each with a process-specific system prompt. An operational nightmare of 100 deployments, 100 evaluation surfaces, and complex routing layers. 

- **One agent, 100 skills** . This fits the skills format as there are many variants for the same job. The progressive disclosure of skills means 100 skills cost ~100 × 50 tokens = ~5,000 tokens of always-loaded metadata. Logistics requests carry strong activation cues: SKU, origin, weight, hazmat flag, SLA, which makes skill descriptions sharp and selection reliable. Procedures live in version control. Adding the 101st variant is a new folder, not a new deployment. Easier to maintain and to scale. 

However, the most important part is to always have a strict evaluation process and compare **Section 4** covers what that evaluation different performances to make the final decision ( work actually looks like in practice). 

May 2026 

17 

Agent Skills 

As a mental note, adoption follows the path of least resistance. Anyone who can write documentation can write a skill. That lowers the barrier and the latent procedural knowledge sitting in wikis, runbooks, and engineers' heads finally has somewhere structured to flow. 

## **4. Evaluating Skills** 

Now you have a first skill, or maybe a small library of them. The question that immediately follows is: how do you know they actually work? How skills fail, how to test them, and the four conditions every skill should pass before it earns a place in your library. 

## An Agent Skill without a test is a hope, not a capability. 

When researchers recently benchmarked 84 real-world agent tasks in SkillsBench (2025)[7] , they found that 19% performed worse with a skill than without one. These poorly designed skills were not just neutral noise, they actively degraded capability. Fortunately, these failures are predictable and fall into four distinct modes: 

**1. Trigger Failure:** The wrong skill fires, or the correct one fails to fire. 

**2. Execution Failure:** The skill triggers correctly, but produces incorrect output or errant tool calls. 

**3. Token Budget Failure:** A massive skill body crowds the context window, degrading performance on unrelated turns. 

**4. Regression:** A newly added skill overlaps with an existing one, breaking previously working routing. 

May 2026 

18 

Agent Skills 

Trigger failures surface in routing logs; execution failures in output quality; token budget failures under realistic context load; regression failures only when the full library is exercised together. 

Figure 1: Notice how the failure modes branch out. Trigger and execution failures happen on a single-turn level, while token budget and regression failures only appear when multiple skills interact under a heavy production load. 

May 2026 

19 

Agent Skills 

## **The Evaluation Toolkit** 

Five complementary testing patterns cover the full failure surface. 

**==> picture [470 x 403] intentionally omitted <==**

**----- Start of picture text -----**<br>
Pattern Description Example Failure Mode  When Required<br>Addressed<br>Eval-as-Unit-Test Test file for the  Three JSON eval cases  All Every skill,<br>skill running in CI  run via  agenteval  on  every change<br>on every change every push; a failing<br>test blocks merges<br>Golden Dataset Curated,  30 representative  Execution,  Draft tier<br>versioned (input,  queries with expected  Trigger and above<br>expected output)  tool calls/formats<br>pairs stored with  committed in the<br>the skill skill directory<br>LLM-as-Judge A peer model  Reference-guided  Execution Read-only<br>evaluates output  scoring across three  and draft<br>against a rubric  rubric dimensions, run<br>at scale twice with swapped<br>positions to neutralize<br>ordering bias<br>dversarial /   Systematic  One rephrasing and  Trigger,  Before action<br>Red-Team probing designed  one negative boundary  Execution –alllowed<br>to expose  case for every positive  graduation<br>failure modes trigger;  agentregress<br>flags regressions<br>Canary / Shadow  Deployment to  Shadow: Parallel  Regression Before each<br>Mode controlled traffic  offline comparison.  action-allowed<br>before full rollout Canary: 1% live  release<br>traffic monitored via<br>selftune  for 24 hours<br>**----- End of picture text -----**<br>


Table 1: The Evaluation Toolkit, outlining five complementary testing patterns designed to cover the full failure surface of Agent Skills. 

May 2026 

20 

Agent Skills 

Figure 2: This visual highlights the gatekeeping mechanism. The metadata acts as a thin routing layer, keeping the active token count low until the specific activation cues match the user intent. 

## **The trigger is the first gate** 

A skill that never fires cannot help. A skill that fires too broadly injects irrelevant context. 

Vercel's production analysis[8] revealed a 56% non-invocation rate for skills expected to activate consistently. More critically, a skill stripped of its instructions scored 58%, while the agent without the skill scored 63%. This 5-point deficit demonstrates that a poorly-designed skill can actively subtract capability. 

In this same study, Vercel also noted that a passive `AGENTS.md` index of project conventions achieved a 100% pass rate against a 53% baseline. This reinforces that skills are best reserved for narrow, action-specific workflows, whereas global context should remain in passive, always-accessible documentation. 

May 2026 

21 

Agent Skills 

Now, to hit the industry-standard 90% trigger accuracy rate, your `SKILL.md` description, the **only** thing the model sees during routing, must pass four checks: 

- **Testable specificity:** You must write 3 positive and 3 negative triggers. 

- **Clarity:** Ambiguous queries don't overlap with adjacent skills. 

- **Execution fidelity:** It describes actual performance, not aspirational behavior. 

- **Rephrasing stability:** It routes consistently regardless of how the user phrases the intent. 

## **Output quality and tool trajectory** 

Once a skill triggers, test both the final output (what the agent says) and the tool trajectory (what the agent does) separately. 

A smart way to do this is to use the **Evaluation-Driven Development (EDD)** . Invert the workflow by writing three JSON evaluation cases (Input, Expected Tools, Expected Output) before drafting the `SKILL.md` . It forces a clear functional spec upfront. When using **LLM-asJudge** to score outputs at scale, remember two non-negotiables: swap the positions of the reference and actual outputs to eliminate ordering bias, and calibrate against human ratings until you hit 90% agreement. 

Latitude's analysis (March 2026)[9] found that final-output-only scoring passes 20% to 40% more cases than trajectory-aware scoring. This gap represents instances where the agent reached the correct answer via an incorrect sequence of tool calls. Acceptable in readonly scenarios. Critical in action-allowed skills, where incorrect tool trajectories can cause irreversible side effects. 

May 2026 

22 

Agent Skills 

The Google ADK eval framework[10] offers three trajectory scoring modes: EXACT (exact order), IN_ORDER (ordered subset), and ANY_ORDER (unordered subset). Trajectory validation should align with the skill tier: read-only skills can use ANY_ORDER, action-allowed skills require IN_ORDER or EXACT. 

Figure 3: Follow the inversion path. Instead of writing code first, the workflow forces you to define expected tool trajectories and evaluation rubrics as the very first step. 

May 2026 

23 

Agent Skills 

## **System vs. Skill: The Evaluation Illusion** 

Trajectory testing evaluates the composite system of the host agent interacting with the skill rather than the skill in isolation. When a multi-skill trajectory fails, it is often impossible to decouple agent routing, instruction quality, or execution fidelity. To simplify calibration, evaluate skills via a "Single-Skill Sub-Agent pattern" (Agent + 1 Skill vs. Base Agent); save complex multi-skill co-loading for advanced production staging. 

**Evaluation-Driven Development** (EDD)[11] inverts the workflow by writing three JSON `SKILL.md` . It evaluation cases (Input, Expected Tools, Expected Output) before drafting the forces a clear functional spec upfront.This forces a clear functional specification upfront. A minimal eval case looks like this: 

## **JSON** 

```
{
  "case_id": "refund_dup_charge_001",
  "input": "I was charged twice for order #4521 last Tuesday",
  "expected_skill": "refund_processor",
  "expected_tool_calls":[
{"tool": "lookup_order", "args":{"order_id": "4521"}},
{"tool": "check_duplicate_charge", "args":{"order_id": "4521"}}
],
  "expected_output_format": "confirmation_with_refund_id",
  "rubric":["acknowledges duplicate", "cites order id", "provides next step"]
}
```

Snippet 3: A minimal JSON evaluation case example used in Evaluation-Driven Development (EDD) to explicitly define input parameters, expected tool trajectories, and evaluation rubrics upfront. 

Drafting three such cases upfront surfaces description ambiguities and tool-trajectory errors before they compound in the skill body. 

May 2026 

24 

Agent Skills 

When using LLM-as-Judge to score outputs at scale, remember two non-negotiables: swap the positions of the reference and actual outputs to eliminate ordering bias, and calibrate against human ratings until you hit 90% agreement. 

## **Token budget: isolation is a trap** 

Never evaluate a skill purely in isolation. Agents in production co-load 5 to 15 skills simultaneously. A skill body exceeding 5,000 tokens might work perfectly alone, but it will cause context rot when co-loaded. 

## **The Compound Evaluation Trap: Skill vs. Agent** 

Trajectory testing evaluates the composite system. The skill and the host agent together. If a test fails, avoid over-engineering the 'SKILL.md' for a specific model, which ruins portability. Instead, isolate execution logic from routing by using a "Two-Tiered Assert Framework": validate underlying tool code independently, and audit `SKILL.md` triggers across multiple model families to catch brittle, architecture-locked descriptions. 

MCPVerse[12] noted an 18.2% accuracy drop in Claude-4-Sonnet due to tool proliferation and found that all frontier context attention competition. Additionally, Chroma Research (2025)[13] models degrade as input grows, particularly when hindered by co-loaded noise. 

May 2026 

25 

Agent Skills 

Figure 4: Look at the performance gap between a single running skill and 15 co-loaded skills. The curve illustrates why passing an isolated test is a false positive for production readiness. 

Because of this, skills must graduate through strict tiers of authority: 

- **Read-Only:** LLM-as-Judge eval; 90% trigger accuracy. 

- **Draft-Only (Human Review):** 

- **Action-Allowed:** Full adversarial red-teaming; sustained success across multiple runs (not just a single lucky pass); no rollback events; sustained pass^k. 

May 2026 

26 

Agent Skills 

**pass^k** measures consistent, rather than occasional, success by running the evaluation $k$ times and requiring success on every run. On tau-bench (Yao et al., 2024)[14] , GPT-4o scored 61% on pass^1 but dropped below 25% on pass^8, demonstrating that single-run success is a poor predictor of production reliability. 

When calibrating these thresholds, two factors are critical: 

1. **Production Degradation:** ReliabilityBench[15] shows that production performance typically drops 20% to 30% compared to offline benchmark pass@1 numbers. 

2. **Simulation Bias:** Simulation-based evaluations can suffer from an optimistic bias of up to 

9% (the "Lost in Simulation"[16] finding). 

Consequently, human review of representative outputs remains the ultimate validation signal for action-allowed graduation. 

## **What "eval coverage" means** 

A skill achieves complete eval coverage by satisfying four conditions mapped directly to the primary failure modes: 

- **Trigger Failure:** Verifying trigger behavior with both positive (should fire) and negative (should not fire) test cases. 

- **Execution Failure:** Ensuring correct outputs across a representative range of expected inputs. 

- **Regression:** Confirming that adding the skill causes zero performance drops in the existing library. 

May 2026 

27 

Agent Skills 

- **Token Budget Failure:** Bounding the skill's token footprint to ensure it does not degrade performance on unrelated turns. 

This checklist governs graduation; failure on any single condition holds the skill in the draft tier, regardless of its happy-path performance. Once verified, the skill and its accompanying eval suite are ready for production deployment (detailed in **Section 5** ). 

## **5. From Prototype to Production** 

**Sections 1 to 4** covered what skills are, how to write one, and how to evaluate them. This section is about what changes when you put a working prototype in front of a real customer. The short version: the model is no longer the interesting part, and skills are the engineering primitive that lets you ship reliably. 

**Google's Agents CLI**[17 ] in Agent Platform is a CLI and skills package for building, evaluating, and deploying AI agents on Google Cloud. Agents are built with Google's Agent Development Kit (ADK) and Agents CLI handles everything around it: scaffolding, evaluation, deployment, and observability. 

May 2026 

28 

Agent Skills 

Figure 5: The Agents CLI install flow. One uvx command installs seven skills into the developer's existing coding agent, covering the full agent lifecycle (workflow, ADK code, scaffold, eval, deploy, publish, observability). The same skills work across Claude Code, Codex CLI, Antigravity, and any other compliant coding agent. 

The working example points to three properties that generalize beyond Google’s setup: 

- . The runtime is commoditized; the 

- **The expertise lives in the skills, not the runtime** seven skills are the durable asset. 

- **The skills package composes with what you already use** . Install the skills and your existing coding tool gains new capabilities; the same pattern to aim for internally: capabilities that compose into existing tooling, not another portal. 

May 2026 

29 

Agent Skills 

- **The full lifecycle ships as skills** . Scaffold, build, evaluate, deploy, publish, observe. Every stage that once needed its own tooling now fits the skills format. 

## **What's actually inside an agent runtime** 

Underneath the framework, the agent loop has converged across vendors: the runtime maintains a conversation, calls the model, executes tools, reads files, returns a response. What’s striking inside one of these runtimes is how little of the code is about reasoning. 

A recent reverse-engineering of Claude Code v2.1.88 (Liu, Zhao, Shang, and Shen, 2026)[18] found that 98.4% of the codebase is operational infrastructure: permission classifiers, context compaction pipelines, subagent delegation, session storage and only 1.6% is the agent loop itself. The model sits behind a remote API; the engineering around it is what makes the system production-grade. The companion site ccunpacked.dev maps the same architecture visually. 

This is the architectural insight behind everything that follows. As foundation models converge in baseline reasoning, the differentiator for autonomous reliability becomes the deterministic engineering around the model and inside that engineering, the unit that gets composed and reused is the skill. 

May 2026 

30 

Agent Skills 

Figure 6: The demo-to-deploy gap. Team confidence peaks early, then collapses on contact with a real customer environment. The instinct is to call it a model problem; it almost never is. 

## **Why skills are the unit of improvement** 

The naive theory of agent improvement is that better models produce better agents. In production, the model is the infrastructure and skills are the primitive that lets improvements ship. Each new skill is a small, owned, testable unit of capability (as we set up in **Section 1** ). When a new edge case appears, it takes editing one SKILL.md; the agent's effective capability grows without the challenges of monolithic prompt engineering. 

Three properties of skills make this work: 

- **They are conditional** . Loaded only when their description matches the task. 

May 2026 

31 

Agent Skills 

- **They are composable** . One skill can call tools from another, or chain downstream, without either knowing about the other (Section 7 develops the composition story in depth). 

- **They are owned** . Each lives in a versioned folder with a clear author, so improvement is distributed rather than bottlenecked through a central platform team. 

## Compare against the alternatives: 

**==> picture [471 x 219] intentionally omitted <==**

**----- Start of picture text -----**<br>
Improvement   Cycle time Failure mode Who can do it Context Tax<br>style<br>Model swap Days to weeks Regression in  ML/platform team None<br>unrelated tasks (weights-based)<br>System prompt   Minutes to hours Context rot,  Whoever owns the  Static<br>edit instruction conflict prompt file (every turn pays)<br>Fine-tune Weeks to months Catastrophic  ML team only None<br>forgetting,   (weights-based)<br>overfitting<br>New skill Hours to days Bounded with only  Any domain team Dynamic<br>matching turns (loaded<br>on-demand<br>when triggered)<br>**----- End of picture text -----**<br>


Table 2: Comparison of agent improvement methodologies across cycle times, failure modes, organizational ownership, and context costs. 

## **The failure mode that breaks demos: context overflow** 

The most common failure mode of agents in production is not hallucination. It is context overflow: the model receiving more context than it can effectively use, and degrading silently before the operator notices. Two strands of research ground this: 

May 2026 

32 

Agent Skills 

**Lost in the Middle (Liu et al., TACL 2024**[19] **)** . Across multi-document QA and retrieval, performance is highest when relevant information sits at the start or end of the input and degrades in the middle; a U-curve that holds even for models trained on long contexts. 

**Context Rot (Chroma Research, 2025**[20] **)** . Across 18 frontier models; Claude 4 Opus and Sonnet, Gemini 2.5, Qwen3; performance degrades as input grows, even when task difficulty is held constant. Every model gets worse, and faster when relevant content is hard to distinguish from distractors. The noise typical of real agent contexts (tool outputs, halfrelevant retrievals, intermediate reasoning) is among the worst. 

Figure 7: Context rot in practice. As prompt size grows, accuracy on a fixed task degrades, long before the context window fills. The dashed line shows the naive expectation; the curve shows what 18 frontier models actually do (Liu et al. 2024; Chroma 2025). 

May 2026 

33 

Agent Skills 

## **What this means for the token budget** 

Progressive disclosure, covered in **Section 2** , is the architectural answer: metadata for every skill loads at startup, a skill’s body loads only when its description matches, and supporting files load only when the body references them. 

The math is worth showing. Consider an agent with fifty distinct workflows. As a single system prompt, it loads 15,000 tokens every turn. As a skills library, it loads ~4,000 tokens of descriptions plus the ~2,000-token body of the one active skill with ~6,000 tokens total, with the other forty-nine bodies on disk. Anthropic has published examples where converting a workflow to skills cut active context from roughly 150,000 tokens to 2,000, a reduction of more than 98 percent. 

Figure 8: Token economics: a single big prompt versus a fifty-skill library. The library has fifty units of capability available, but only the active body sits in context at any moment. 

May 2026 

34 

Agent Skills 

Three practical implications follow: 

- **Capacity is the wrong metric** . A 1M-token window can show significant degradation at 50K tokens. 

- **Active context is a budget, not a vessel** . Every token in front of the model takes attention from every other. Treat the system prompt the way infra teams treat memory: a finite resource, allocated deliberately. 

- **Skills resolve the constraint** . They keep active context small while keeping available capability effectively unbounded. 

Once a team has a working library, the questions shift from maintaining a single skill to evolution, composition, and the larger ecosystem. 

## **6. On Meta-Skills and Self-Improving Skills** 

So far, every skill in this document has been written by a human. A domain expert sits down, drafts a SKILL.md, tests it, ships it. That's the right place to start. But once you have a working library, the natural next question is: can the agent help write, evaluate, and improve skills too? 

This is the meta-skills territory. Skills whose job is to author, evaluate, or improve other skills. In practice, these "meta-skills" fall into four buckets: 

May 2026 

35 

Agent Skills 

**1. Authoring** . Skills that take a description of a workflow and produce a draft SKILL.md. Google's ADK[21] has a "skill factory" pattern that does this through its `SkillToolset` . Anthropic ships a `skill-creator` Skill[22] that walks you through creation, evaluation, and tuning. 

**2. Assisted authoring from traces** . Instead of asking a human to describe a workflow, watch the agent do it successfully a few times, then turn that trace into a skill. The `skillcreator` workflow supports this directly through trace-based harvesting. The human's 

job shifts from writing the skill to confirming that the harvested version captures the right steps. 

Figure 9: The step-by-step loop demonstrates how real, successful production histories are transformed into reliable procedural memories without manual human drafting 

**3. Improvement** . Skills that take an existing skill plus a set of failing evaluation cases and propose edits. Saboo's SkillOptimizer[24] and Anthropic's description-optimization loop are both examples. Another is Karpathy's autoresearch pattern[25] , where an agent proposes a change to a target file, runs a bounded experiment, and keeps the change only if a metric improves. 

May 2026 

36 

Agent Skills 

Figure 10: Notice the evaluation gating. The agent can suggest changes to descriptions or instructions, but it cannot commit them to the library unless the unit tests pass. 

**4. Library evolution** . Skills that grow the library over time, the way Voyager grew its own Minecraft skill library[26] . The agent finishes a task it had no skill for, notices that it just solved a recurring problem, and proposes adding a new skill to cover it. Schmid's selflearning-skill[27] is a community reference implementation of this pattern. 

## **Where this falls apart** 

Meta-skills only work if your evaluation suite is good. An agent that's allowed to edit its own skills will happily optimize for whatever metric you point it at, including metrics that are easy to game. The Section 4 evaluation work is what keeps this honest. Without solid trigger accuracy tests, regression tests, and human spot-checks, an autonomous improvement loop will quietly make your library worse while reporting that it's getting better. 

A few habits that have held up: 

- **Anything an agent writes enters the library at the draft tier** , regardless of how confident the meta-skill is. It graduates through the same Read / Draft / Act ladder from **Section 4** as any human-written skill. 

May 2026 

37 

Agent Skills 

- **Keep a human in the loop for the first few edits** . Even when the metric clearly improves, scan the diff. The kind of mistake an agent makes (overfitting the description to a few test cases, breaking a downstream skill it didn't know existed) is exactly the kind a human catches in 30 seconds. 

- **Don't start with meta-skills** . Get the manual authoring loop working first. The fastest way to get a bad library is to point an agent at an empty folder and ask it to generate fifty skills. 

## **Where this is going** 

The pattern is settling into something like: humans write the first version of every skill, metaskills handle the repetitive part of maintenance (tuning descriptions, adding test cases, surfacing regressions), and a small subset of teams experiment with full self-extension. The interesting frontier is the third category, where the agent proposes new skills based on what it sees in production traffic. It's promising. It's also where things go wrong fastest if the evaluation gates aren't tight. 

The practical version of this is in **Appendix A** where the cheatsheet covers what to do (and not do) when you're tempted to let the agent write its own skills. 

May 2026 

38 

Agent Skills 

## **7. Composing and Packaging Skills** 

Real workflows do not fit inside a skill. The composition problem is how skills reference each other, pass state, and avoid circular dependencies. 

Passing raw LLM outputs between isolated skills in a monolithic system is ineffective: state gets obfuscated, execution becomes non-deterministic, and debugging is hard. Agent architecture has evolved from naive prompt chaining to predictable orchestration. 

## **Execution Routing: DAG Orchestration** 

Early architectures proved brittle and susceptible to compounding errors when early stages hallucinated. The industry solution is Directed Acyclic Graph (DAG) orchestration. 

- **Decoupled State:** State routing in a DAG architecture does not rely on accumulating execution history within the LLM's prompt. 

- **File Message Bus:** The DAG controller orchestrates handoffs by passing structured schema references between subagent nodes. 

- **Protected Attention:** Abstracting the payload from the model's text input prevents context window bloat and preserves the model's capacity. 

May 2026 

39 

Agent Skills 

## **Environment Packaging: Capability Profiles** 

Activating every skill degrades natural language routing and overwhelms the context window. Architects should utilize tools to manage "Capability Profiles," which function as specialized personas tailored to specific execution states. A profile acts as a modular tool bundle defining: 

- Active skills and tool access. 

- System instructions and operational guardrails. 

- Automated workflows and subagent topologies. 

- LLM parameters, such as model choice and temperature. 

During execution, the orchestration layer unloads previous system instructions and flushes stale variables before swapping the new Capability Profile into memory. This strict teardown and rebuild process prevents context loss. 

## **Populating the Graph: The Canonical Skill Taxonomy** 

To build DAG, discrete engineering capabilities map to specific node functions within an execution graph nodes: 

- **Generator:** Convert user intent into structured artifacts. 

- **Reviewer & Gate:** Deterministic gates blocking execution if validation fails. 

- **Pipeline:** Orchestrate linear paths within the broader DAG environment. 

- **Inversion & Recovery:** Force the agent to clarify assumption before execution. 

May 2026 

40 

Agent Skills 

- **Domain Context Wrappers:** Act as reference nodes teaching domain conventions. 

## **Context Debt and Shifting Intelligence Left** 

Skills burn model attention, which is a scarce resource. When authors attempt deterministic behavior at runtime by bloating skill descriptions (e.g., "ALWAYS DO X"), they accumulate **Context Debt** . Models learn to ignore these capitalized imperatives, exactly as a human developer ignores a wall of unreadable warning text. 

The engineering best practice is to **Shift Intelligence Left** . Instead of hoping an LLM correctly interprets complex rules at runtime, distill subjective judgments into skills. By pushing logic out of the LLM's prompt and into standard, testable scripts, you reduce the chaotic surface area of your application. 

## **Architectural Tradeoffs** 

**==> picture [470 x 193] intentionally omitted <==**

**----- Start of picture text -----**<br>
Architecture Mechanism Best For<br>Primary Benefit<br>Linear Pipelines Sequential text passing  Low engineering overhead  Single-domain,<br>between fixed nodes. and rapid prototyping. low-complexity<br>generative tasks.<br>DAG  Graph-based parallel  Cycle prevention and  Multi-agent workflows<br>Orchestration execution with file- strict context isolation. requiring high reliability.<br>bus state passing via<br>schema references.<br>Capability  Swappable, version- Rapid persona  Role-based<br>Profiles controlled parameter  switching with lifecycle  deployment and<br>and tool bundles. memory purging. domain-specific agents.<br>**----- End of picture text -----**<br>


Table 3: Architectural Tradeoffs among Linear Pipelines, DAG Orchestration, and Capability Profiles in multiagent skill systems. 

May 2026 

41 

Agent Skills 

## **Actionable Best Practices** 

- **Write Software, Not Rules:** Replace negative LLM instructions with deterministic software constraints that make invalid actions impossible. 

- **Implement Progressive Disclosure:** Load complex instructions dynamically only when the skill is explicitly invoked. 

- **Decouple State:** Never use the LLM context window as a database. Pass only URIs or pointers to the subagents via the file system or message bus. 

## **8. How to Decide Among the Hundreds of Skills That Exist** 

By early 2026, public skill marketplaces had crossed 40,000 listings, with the leading platform reporting tens of thousands of new skills published in the first weeks of January alone. At Google Cloud Next 2026, Google launched its official Agent Skills repository at `github.com/google/skills` , with skills installable via `npx skills install github. com/google/skills` for use across Antigravity CLI, and any other coding agent that supports the Skills standard. The Anthropic skills repository, the Google ADK skill library, the Google official skills repository, and community marketplaces such as `awesome-llm-apps` now host more skills than any practitioner could review individually. The selection problem is real and growing. 

Three heuristics help. 

1. First, prefer first-party skills for vendor-specific tools. Google's BigQuery skill, the official Stripe skill, anything written by the people who built the underlying system. They will be more correct and more maintained than community alternatives. 

May 2026 

42 

Agent Skills 

2. Second, pin everything you depend on. Community skills evolve, and an unpinned dependency that worked yesterday can fail tomorrow. 

3. Third, audit before adopting. A skill is code that runs in your context. Treat it like any other dependency, with the same supply-chain hygiene. 

Not all sources are equal. Three categories of skill source exist in early 2026, and the right operational stance is different for each: 

**==> picture [471 x 188] intentionally omitted <==**

**----- Start of picture text -----**<br>
Source Trust default Examples Who maintains it<br>First-party vendor  Trust by default;  google/agents-cli [28] , google/ The team that built the<br>skills pin a version skills [29] , google-gemini/gemini- underlying product<br>skills [30] , anthropics/skills [31] ,<br>stripe/ai [32] , microsoft/skills [33]<br>Organization-curated  Trust within  your-org/retail-skills, your- Your own domain<br>skills the org; review  org/finance-skills (private,  teams, with PR review<br>on adoption internally maintained)<br>Community skills Audit before  VoltAgent/awesome-agent- Volunteer authors,<br>adopting;  skills [34] , SkillsMP marketplace [35] ,  varying<br>pin aggressively addyosmani/agent-skills [36] ,  maintenance<br>individual GitHub repos commitment<br>**----- End of picture text -----**<br>


Table 4: Overview of Agent Skill sources categorized by trust defaults, official examples, and maintenance ownership. 

May 2026 

43 

Agent Skills 

## **9. Conclusion** 

We began this whitepaper by looking at a surprisingly simple concept: a folder containing a markdown file and a few optional scripts. Yet, this lightweight structure, the Agent Skill, is fundamentally reshaping how we build AI Agents. It finally provides foundation models with true, testable procedural memory, allowing them to remember how to execute tasks step-bystep. By relying on the magic of progressive disclosure, skills solve the problem of context rot. A single, general-purpose agent can now seamlessly access many specialized workflows without choking its token budget. 

The pattern we keep coming back to in this paper is that the format is deliberately small so that the interesting work happens around it, not inside it. Evaluating Skills under realistic co-loaded conditions is interesting. Composing Skills into workflows without using the context window as a message bus is interesting. Letting agents draft Skills from successful traces, with humans reviewing rather than authoring, is interesting. Encoding two decades of institutional knowledge into a versioned, testable, governable library is interesting. All of these are now tractable in a way they weren't twelve months ago, because the primitive exists. 

Throughout this paper, we have also tried to be specific about what's settled, what's still emerging, and what's likely to change. The format is settled: agentskills.io is now an open standard with adoption across every major coding agent, AI chatbot, and agent framework that matters. The architecture around it is still emerging: evaluation under co-loaded conditions, Skills-library-level optimization, agent-driven Skill creation, and the governance patterns that make all of this safe at scale. 

May 2026 

44 

Agent Skills 

If you are starting today, our suggestion is the one we've made throughout: start small, start with knowledge you already have, treat Skills as code, measure what you ship, and don't reach for a multi-agent architecture when a Skills will do. The teams that figure this out now will build cleaner systems than the teams that wait for the industry consensus to catch up. The format is settled. The work is just beginning. 

May 2026 

45 

Agent Skills 

## **Appendix A – The Practical Cheatsheet** 

This section is designed to be printable and standalone. It compresses the rest of the whitepaper into the decisions a team will face. 

## **The minimal SKILL.md** 

Copy-paste this. Adjust the placeholders. Done. 

```
---
name: skill-name
description: |
  [What it does in one verb-led sentence.] Use this skill when the user
  [trigger phrase 1], [trigger phrase 2], or [trigger phrase 3].
  Do NOT use for [anti-trigger 1] or [anti-trigger 2].
version: 1.0.0
license: MIT
allowed-tools: [Optional] Read Bash Write
metadata:
  author: [Optional] your-handle
---
# Skill Name
## When to use
- [Concrete scenario]
- [Concrete scenario]
## When NOT to use
- [Out-of-scope scenario]
## Workflow
1. [Step]
2. [Step]
3. See `references/advanced.md` for [edge case].
```

**Continues next page...** 

May 2026 

46 

Agent Skills 

`## Examples - Input: "..."` → `Output: "..." ## Output format - Use `assets/template.md` etc. ## Anti-patterns to avoid - Don't [...]` 

## **The folder structure** . 

## `skill_name/` 

├── `SKILL.md          # Required: YAML frontmatter + markdown instructions` ├── `scripts/          # Optional: executable helper scripts (Python, Bash)` ├── `references/       # Optional: supplementary context loaded as needed` ├── `assets/           # Optional: files used in output (templates,resources)` ├── `...               # Any additional files or directories` 

## **Naming** 

- Directory name: snake_case 

- Skill name: kebab-case 

- Prefer gerund form: `processing-pdfs` , not `pdf-processor` 

- Avoid generic names: `helper` , `utils` , `tools` , `data` 

- Avoid vendor prefixes: `claude-*` , `gemini-*` , `anthropic-*` 

- Avoid internal jargon outsiders won't recognize 

May 2026 

47 

Agent Skills 

## **The description field** 

The description is the routing algorithm. Spend more time here than anywhere else. 

- State **what it does** AND **when to use it** 

- Front-load trigger keywords ("Generate a commit message…", not "This skill helps with…") 

- Include **when NOT to use** to prevent over-triggering 

- Be pushy when the model under-triggers 

- ≤200 chars for API; ≤1024 chars in YAML. Most authors aim for ~50 words 

## **The five rules** 

**1. One skill, one job** . If you cannot describe what the skill does in one sentence, it is two skills. Decompose before writing. 

**2. Descriptions are an interface** . The agent picks skills by reading descriptions. A vague description means an unused skill. 

**3. Skills are dependencies** . Treat them like libraries. Version them, pin them, review them in PRs. A skill without a test is a hope, not a capability. 

**4. The right team owns the right skill** . Domain experts own domain skills. Do not let the AI team become a bottleneck for the organization's domain knowledge. 

**5. The agent runtime is interchangeable** . Do not tie skills to one runtime. Portability is part of the value. 

May 2026 

48 

Agent Skills 

## **The quality principles** 

**1. Run the task yourself first** . Real failure produces signal. Speculation produces noise. 

**2. Give the reason, not just the rule** . Models generalize wonderfully to edge cases when they understand _why_ an instruction exists. If you find yourself typing "ALWAYS" or "NEVER" in caps, pause and try explaining the rationale instead. 

**3. Every line should earn its place** . Keep gotchas, exact commands, business logic, antipatterns. Cut boilerplate the model already knows such as "always validate output". 

**4. One skill, one job** . If the description needs "and" between unrelated capabilities, split it. 

**5. Make instructions verifiable** . If the agent can't tell whether it followed the rule, the rule is too vague. 

**6. Bundle what repeats** . Helper code the agent keeps re-deriving belongs in `scripts/` . 

## **Do's and Don'ts** 

## **Do:** 

- Start small and concrete 

- Spend disproportionate time on the description field. It is the routing algorithm. Always include what it does, when to use, and when not to use 

- Trust progressive disclosure 

- Bundle deterministic work in `scripts/` , not as instructions 

- Treat Skills as code 

May 2026 

49 

Agent Skills 

- Remember: Skills + MCPs, not Skills vs. MCPs 

- Have test cases and controlled, programmatic evaluation (see **Section 4** for how to actually do this) 

## **Don't:** 

- Write vague descriptions like "helps with documents". Use specific verbs, trigger phrases, and a when-not-to-use clause 

- Write SKILL.md bodies over 5,000 words. Move detail to `references/` 

- Hard-code paths or secrets 

- Embed "always do X" rules that are more appropriate for AGENTS.md 

- Install untrusted third-party libraries or Skills without scanning 

- Reinvent MCP as scripts 

## **Skill smells (revise if you see these)** 

- **Over 5,000 words** . Probably two skills, or reference material that should live in `references/` 

- **Two domain teams could plausibly own it** . Not yet decomposed. Split along team boundaries 

- **You can't write three test cases for it** . Description is too vague; skill does too many things 

- **It does not reference any other resource** . Might just be a long instruction that belongs in the system prompt 

May 2026 

50 

Agent Skills 

- **You keep adding "edge cases" sections** . Each edge case probably wants its own skill 

- **Its description starts with "a helpful skill for…"** . Rewrite. The description should name the trigger, the inputs, and the output 

## **Eval coverage checklist** 

A skill is "evaluated" only when all four are satisfied: 

- ☐ **Trigger** . Positive AND negative test cases. Target 90% trigger accuracy 

- ☐ **Execution** . Correct outputs across a representative range of inputs 

- ☐ **Regression** . Adding this skill causes zero drops in the existing library suite 

- ☐ **Token budget** . Co-loaded with 5 to 15 frequently-active skills, does not degrade unrelated turns 

Any failure holds the skill at the draft tier, regardless of happy-path performance. 

## **Deployment checklist** 

- ☐ Frontmatter validates (lint passes) 

- ☐ Description includes what + when + when-not 

- ☐ Scripts have unit tests passing in CI 

- ☐ Eval suite passes in CI with min-pass threshold 

- ☐ Security scan clean (no secrets, no untrusted deps) 

May 2026 

51 

Agent Skills 

- ☐ Description reviewed by someone other than the author 

- ☐ Cross-tool install paths tested if shipping publicly 

- ☐ Org-level admin provisioning updated (if applicable) 

## **One-line mental model** 

**System prompt = instinct. AGENTS.md = project README. Tools / MCP = hands. RAG = library. Skills = the runbook the experienced colleague hands you on day one, and that the AI never forgets.** 

## **Where to start tomorrow** 

1. Take your most experienced practitioner aside for an hour. Ask them to narrate three workflows they do regularly. Record it. 

2. Pick the most repeated workflow. Run the prompts yourself, without any skill loaded. Note where the agent fails. Or let an agent  similar to () 

3. Draft a SKILL.md from the transcript. Write three eval cases (two positive, one negative) before drafting the body. 

4. Ship to a read-only tier. Test in production-like conditions. Iterate the description until trigger accuracy clears 90%. 

**Repeat. Build the library one workflow at a time. Resist the urge to let an LLM generate fifty skills on day one.** 

May 2026 

52 

Agent Skills 

## **Appendix B – Case Study: Domain Expertise as Code (Vertical Skills in Retail)** 

This section is the worked example of the whitepaper. It walks through how a large retailer would structure a skills library to capture the institutional knowledge that differentiates the brand from its competitors, and why that library, rather than any specific custom agent, is the durable strategic asset. Several major retailers have publicly described AI assistants with capabilities that match the architecture below. We describe the pattern, not the implementation of any single vendor. 

## **Why retail is the canonical case for skills** 

Two retailers running on the same agent runtime, accessing similar data through similar APIs, will produce wildly different shopping experiences. Retail expertise is the kind of knowledge that has historically been stuck in three places that AI systems have struggled to reach: in the heads of senior buyers, merchandisers, and category managers; in thirty-page operational runbooks that no one reads; and in Slack channels where the answer to "should we recommend this product with that one?" lives in a thread from 2023. 

Skills capture this knowledge in a form that the company's customer-facing systems will actually use. 

May 2026 

53 

Agent Skills 

## **What the architecture looks like** 

Figure 11. A skills-first retail architecture (illustrative). Customer surfaces (web chat, mobile app, in-store kiosk, voice agent) sit above an agent runtime that loads skills carrying merchandising, category, and compliance knowledge. The tools below are accessed via MCP and managed search integrations. 

May 2026 

54 

Agent Skills 

The architecture has three layers. The top layer is the customer surface: chat on the website, the mobile app, an in-store kiosk, a voice agent in the call center. Each surface is thin. It forwards user input to the runtime and renders the response. 

The middle layer is the agent runtime and the orchestrator that maintains the conversation, loads skills, calls tools, and assembles the reply. 

The bottom layer is the data and tools plane: the product catalog (often millions of SKUs), live inventory with store-level location data, customer profile and order history, the project knowledge base, and vector search over reviews, manuals, and specification sheets. 

What matters for this whitepaper is the middle layer. The runtime itself is generic: Google's Agent Development Kit, Anthropic's Claude Agent SDK, or any of the other runtimes that support the open Skills standard. The skills loaded into that runtime are specific to the retailer's domain, and they are what carry the brand's expertise to the customer. 

## **An illustrative skills library** 

What does that library actually look like? Below is a representative set of skills a major homeimprovement retailer would plausibly maintain. Each is one folder. Each has a single owner. Each has its own eval suite (using the patterns from Section 4). Together, they constitute the company's working memory of how it serves customers. 

- **project-guidance** . Encodes the trades' knowledge that turns a vague query ("how do I tile a shower?") into a step-by-step plan. Includes structural dependencies (substrate must be waterproofed before tiling), ordering logic (cuts before installation), and common-mistake callouts. Owned by the trades knowledge team. Read-only tier. 

May 2026 

55 

Agent Skills 

- **materials-list** . Takes a project description (voice, text, or partial list) and produces a 

- grouped bill-of-materials, including items the contractor is likely to forget. Owned by Pro merchandising. Draft-only tier: the customer reviews before purchasing. 

- **review-summarize** . Condenses long product reviews into pros, cons, and common use cases. Triggered when the customer asks about real-world experience with a product. Owned by personalization. Read-only tier. 

- **delivery-window** . Computes last-mile delivery options and ETAs given the customer's location, the store's availability, and the company's freight network. Owned by fulfillment. Read-only tier. 

- **return-policy** . Encodes the company's return rules, including the dozens of exceptions for special-order items, hazardous materials, custom cuts, and contract pricing. Owned by customer service. Read-only tier. Promotion to action-allowed (e.g. issuing a refund) requires a second skill with much tighter review. 

Each one is small enough to be reviewed, tested, and shipped independently. 

## **How does the same query route through the library** 

Consider what happens when a customer asks: "I want to remodel my kids' bathroom, what do I need?" 

The runtime loads the L1 descriptions of all skills at session start (~30 to 80 tokens each, ~2KB total). It identifies that `project-guidance` matches and loads its body, which produces an outline of the renovation steps. If the customer follows up about delivery, the `deliverywindow` skill loads. If they ask about returns on a specific item, `return-policy` loads. The previous skills can stay in context or be released as the conversation moves. 

May 2026 

56 

Agent Skills 

Notice what does not happen. There is no monolithic "remodeling assistant" agent that has been trained on every possible remodeling scenario. Each piece of expertise is loaded into context only when the conversation reaches it. The active context stays small. The available capability is effectively unbounded. 

## **Ownership: who writes which skill** 

The single most important governance decision a retailer makes about its skills library is who owns each skill. The principle is to distribute ownership to the teams that already own the underlying expertise: 

**==> picture [471 x 180] intentionally omitted <==**

**----- Start of picture text -----**<br>
Skill family Owner team Why<br>project-guidance,  Trades knowledge /  These teams hold the<br>product-fit category mgmt. merchandising and trade rules;<br>they edit them weekly anyway<br>materials-list Pro merchandising The Pro segment's specific BOM<br>logic is owned by the Pro team<br>delivery-window Store operations / fulfillment Real-time inventory and freight<br>rules change constantly; the team<br>that handles them owns the skill<br>review-summarize Personalization / data science Closest to the underlying NLP and<br>customer feedback signals<br>**----- End of picture text -----**<br>


Table 5: Distributed ownership model mapping retail skill families to the domain teams responsible for their underlying business logic. 

May 2026 

57 

Agent Skills 

## **The read / draft / act ladder** 

The second governance decision is what each skill is allowed to do. This is the same tier model from Section 4, applied with retail-specific examples: 

**==> picture [471 x 177] intentionally omitted <==**

**----- Start of picture text -----**<br>
Tier Capability Review Examples<br>Read-Only May fetch, query, or  Domain  review-summarize,<br>describe data; cannot  team approval store-locator,<br>mutate state project-guidance<br>Draft-Only May produce content  Domain team +  draft-customer-email,<br>for human review;  format owner materials-list<br>cannot send or commit<br>Action-Allowed May execute irreversible  Domain team +  issue-refund,<br>operations on  security/compliance  send-customer-message,<br>real systems + executive sign-off reserve-inventory<br>**----- End of picture text -----**<br>


Table 6: The read/draft/act governance ladder classifying skill capabilities, review requirements, and operational examples. 

This is far more defensible to a security team, and to the regulator who eventually shows up, than the alternative: a black-box agent that does whatever its training plus its system prompt produce. 

## **Why is this harder to compete with than a custom agent** 

If the competitor and our retailer are both running on the same generic agent runtime (and they are, because the runtime has commoditized), then matching the runtime is trivial. The skills library encodes the company's accumulated patterns. This is the central strategic point of the whitepaper. 

May 2026 

58 

Agent Skills 

A retailer that invests heavily in custom agents but neglects its skills library is investing in the part of the stack that competitors will reach for free. A retailer that invests in skills, even on a generic runtime, is building a durable asset that captures what the company actually knows. 

## **Cold start: where to actually begin** 

A useful exercise: take the team's most experienced practitioner aside for an hour, ask them to narrate three workflows they do regularly, and record the conversation. The transcript is, almost literally, the first draft of three skills. This is the kind of work that, before skills, had no obvious home. It now has one. 

Ling, G., Zhong, S., & Huang, R. (2026). Agent Skills: A Data-Driven Analysis of Claude Skills for Extending Large Language Model Functionality. arXiv:2602.08004. Analysis of 40,285 publicly listed skills from a major marketplace. 

Google Cloud Blog. (2026, April). Level Up Your Agents: Announcing Google's Official Skills Repository. htps://cloud.google.com/blog/topics/developers-practitioners/level-up-youragents-announcing-googles-ofcial-skills-repository. Repository: htps://github.com/ google/skills. Installable via `npx skills install github.com/google/skills` for Antigravity, and any compliant coding agent. 

May 2026 

59 

Agent Skills 

## **Endnotes** 

1. htps://codelabs.developers.google.com/geting-stared-with-antigravity-skills?utm_ campaign=CDR_0xf9030db1_default_b513044940&utm_medium=external&utm_source=blog#0 

2. htps://github.com/anthropics/skills/tree/main/skills/skill-creator 

3. htps://hermes-agent.nousresearch.com/docs/user-guide/features/skills 

4. htps://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/awesome_agent_skills /self-improving-agent-skills 

5. htps://adk.dev/skills/ 

6. htps://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills 

7. htps://arxiv.org/abs/2602.12670 

8. htps://vercel.com/blog/agents-md-outperorms-skills-in-our-agent-evals 

9. htps://latitude.so/blog/agent-frst-comparison-guide-vs-braintrust 

10. htps://adk.dev/evaluate/ 

11. htps://arxiv.org/html/2411.13768v2 

12. htps://arxiv.org/abs/2508.16260 

13. htps://research.trychroma.com/context-rot 

14. htps://arxiv.org/abs/2406.12045 

15. htps://arxiv.org/abs/2601.06112 

16. htps://arxiv.org/abs/2601.17087 

17. htps://google.github.io/agents-cli/ 

18. Liu, Zhao, Shang, and Shen (2026), reverse-engineering of Claude Code v2.1.88; companion site ccunpacked.dev 

19. Liu et al., “Lost in the Middle” (TACL 2024). htps://arxiv.org/abs/2601.06112 

20. Chroma Research, “Context Rot” (2025). htps://arxiv.org/abs/2601.17087 

May 2026 

60 

Agent Skills 

21. htps://developers.googleblog.com/en/developers-guide-to-building-adk-agents-with-skills/ 

22. htps://github.com/anthropics/skills 

23. htps://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md 

24. htps://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/awesome_agent_skills/ self-improving-agent-skills 

25. htps://github.com/karpathy/autoresearch 

26. htps://arxiv.org/abs/2305.16291 

27. htps://github.com/philschmid/self-learning-skill 

28. Google. (2026). Agents CLI: Unified CLI for the full ADK agent development lifecycle. htps://google. github.io/agents-cli/. Source repository: htps://github.com/google/agents-cli. The framework ships seven skills covering scaffold, build, eval, deploy, publish, and observability for agents built on Google Cloud, designed to plug into any coding agent that supports the Agent Skills standard. 

29. Google Cloud Blog. (2026, April). Level Up Your Agents: Announcing Google's Official Skills Repository. htps://cloud.google.com/blog/topics/developers-practitioners/level-up-your-agents-announcing` 

googles-ofcial-skills-repository. Repository: htps://github.com/google/skills. Installable via npx skills install github.com/google/skills` for Antigravity  and any compliant coding agent. 

30. Google Developers Blog. (2026, March). Closing the knowledge gap with agent skills. htps://developers. googleblog.com/closing-the-knowledge-gap-with-agent-skills/. Reports the Gemini API developer skill improving Gemini 3.1 Pro from 28.2% to 96.6% on SDK code generation across 117 prompts. Source skill: htps://github.com/google-gemini/gemini-skills. 

31. Anthropic. (2025-2026). anthropics/skills — Public repository for Agent Skills. htps://github.com/ anthropics/skills. Contains Anthropic's reference implementation of the Skills standard plus example skills for documents (docx, pdf, xlsx, pptx), MCP server building, and skill creation itself. 

32. Stripe. (2026). stripe/ai — One-stop shop for building AI-powered products and businesses with Stripe. htps://github.com/stripe/ai. Includes the stripe-best-practices skill (skills/stripe-best-practices/SKILL. md) for API selection, Connect setup, billing, and security; published and maintained by Stripe. 

33. Microsoft. (2026). microsoft/skills — Skills, MCP servers, Custom Agents, Agents.md for SDKs to ground Coding Agents. htps://github.com/microsof/skills. Microsoft's official skill collection for grounding coding agents in Azure SDKs and Microsoft Foundry. 

May 2026 

61 

Agent Skills 

34. VoltAgent. (2026). awesome-agent-skills — A curated collection of 1000+ agent skills from official dev teams and the community. htps://github.com/VoltAgent/awesome-agent-skills. Features official skills from Anthropic, Google Labs, Vercel, Stripe, Cloudflare, Netlify, Trail of Bits, Sentry, Expo, Hugging Face, Figma, and others, alongside community-built skills. Compatible with Claude Code, Codex, Antigravity, Cursor, GitHub Copilot, OpenCode, and Windsurf. 

35. Skills Marketplace. (2026). htps://skillsmp.com. An independent community-aggregated marketplace of 1.2M+ skills sourced from public GitHub repositories, with semantic search, occupation filtering, and minimum-quality indicators (2-star threshold). Marketplace operator explicitly recommends inspecting community skills before installation. 

36. Osmani, A. (2026). addyosmani/agent-skills — Production-grade engineering skills for AI coding agents. htps://github.com/addyosmani/agent-skills. 

May 2026 

62 

# **Vibe Coding Agent Security and Evaluation** 

**Authors: Sokratis Kartakis, Aron Eidelman, Wafae Bakkali, and Meltem Subasioglu** 

Vibe Coding Agent Security and Evaluation 

## **Acknowledgements** 

## **Content contributors** 

Priya Pandey Antonio Gulli Reah Miyara Sita Lakshmi Sangameswaran 

## **Curators and editors** 

Anant Nawalgaria 

## **Designer** 

Michael Lanning 

May 2026 

2 

## **Table of contents** 

|Introduction|6|
|---|---|
|Security: The Evolution to Secure Agentic Development|7|
|The Foundation: The 7-Pillar Agent Security Architecture|9|
|Sandboxes and Supply Chain Defence (Pillars 1 & 4)|13|
|Ephemeral Sandboxing and State Management|13|
|Mitigating Hallucinated Packages|14|
|Egress Governance and Non-Interactive Access|14|
|Vibe-Coding Specifics: Securing Application Logic (Pillar 4)|15|
|Application Vulnerabilities|16|
|Reconciling IDE Friction with CI/CD Enforcement|16|
|MCP Spoofing and Contextual Authorisation|17|
|Identity, Trust & High-Stakes Actions (Pillar 5)|18|
|The Confused Deputy and Delegated vs. Agentic Identity|18|
|Zero Ambient Authority and JIT Downscoping|19|
|Elicitation, MFA Challenges, and the "Vibe Diff"|19|



## **Table of contents** 

|Red, Blue, and Green Security Teaming (Pillar 6)|20|
|---|---|
|Invisible Payloads and Repository Poisoning|21|
|The Red Team (Agent Attacker): Injecting Adversarial Vibes|21|
|The Blue Team (Agent Defender): Behavioural Analytics|22|
|The Green Team (Agent Fixer): Quarantine and Auto-Refactoring|22|
|Integrating the Triad and Enforcing Small Batch Sizes|23|
|Observability: Auditing the Agent's Mind (Pillar 6 & 7)|24|
|Tracing the "Vibe Trajectory" and Content Scanning|24|
|Measuring Intent Drift and Trust Decay|25|
|Checkpoints and Stateful Circuit Breakers|25|
|Security Recap|26|
|Evaluation: Orchestrating Quality in Intent-Driven Agentic Systems|27|
|Why evaluating vibe coding agents is different|28|
|What to Evaluate|29|
|How to evaluate|31|



## **Table of contents** 

|Observability: The Prerequisite for Evaluation|35|
|---|---|
|Applied tips for vibe-coding agent evaluation|35|
|Conclusion|40|



Vibe Coding Agent Security and Evaluation 

Transforming AI models into secure, high-aligning enterprise agents through continuous trust and rigorous evaluation is more important than ever. 

## **Introduction** 

Software engineering is undergoing its most significant transformation since the introduction of high-level programming languages. The most profound shift is the transition from writing code to expressing intent, trusting intelligent systems to translate that intent into working software.[1] This new paradigm spans a spectrum: from casual "vibe coding", where a developer describes what they want in natural language and accepts whatever the AI generates, to disciplined "agentic engineering", where AI acts as an implementation engine within carefully designed constraints.[2] 

May 2026 

6 

Vibe Coding Agent Security and Evaluation 

While this high-velocity, intent-driven development drastically accelerates innovation, it shatters traditional paradigms of trust. In deterministic software, trust is binary: the code compiles, the tests pass, and the static credentials are valid. In an agentic system, an autonomous workforce possesses the ambient agency to execute generated code, access sensitive internal APIs, and dynamically modify production environments. 

To operationalise vibe coding in the enterprise, we must redefine trust across two distinct axes: **Security** and **Evaluation** . 

- **Security** tells you if the agent stayed inside the boundary, ensuring it operates safely and without malicious intent. 

- **Evaluation** tells you whether what happened inside that boundary is actually worth shipping. 

A vibe-coded agent can pass every security check and still fundamentally misread the developer's intent, ignore project conventions, or silently degrade user experience. This whitepaper provides the definitive 2026 framework for both: establishing the strict "safety harness" required to secure non-deterministic agents, and opening the "glass box" to rigorously measure the quality, efficiency, and alignment of their internal reasoning. 

## **Security: The Evolution to Secure Agentic Development** 

As noted in a Mandiant special repor for Google Cloud, "adversaries have moved beyond the simple use of large language models to draft phishing content and are now deploying adaptive tools capable of rewriting code."[3] Broad threat intelligence trends show adversaries continuously adapting their initial access vectors to exploit the new paradigm.[4] 

May 2026 

7 

Vibe Coding Agent Security and Evaluation 

Intent-driven development drastically accelerates innovation but introduces unprecedented security vulnerabilities. We are no longer simply securing web applications against traditional exploits; we are tasked with securing a non-human workforce that possesses the ambient agency to execute generated code, access sensitive internal APIs, and dynamically modify production environments. 

Traditional software testing and security models rely on deterministic logic, where a fixed set of inputs produces a predictable output. However, in an agentic system, an agent might possess a valid access token but operate autonomously with misaligned intent. A critical realisation is that a raw AI model is not an agent. It only becomes one when wrapped in a "harness"—the scaffolding that gives it state, tool execution, feedback loops, and enforceable constraints. Securing this new paradigm requires shifting our focus from securing code syntax to securing this harness. 

In this fluid, non-deterministic environment, static identity acts as a poor perimeter. Trust can no longer be a gate an agent passes through once during deployment; it must be continuously earned, verified, and dynamically enforced based on runtime context. We define this ongoing assurance as **Effective Trust** —a continuous metric evaluated across an agent's supply chain, identity, runtime behaviour, and contextual associations. 

To achieve this continuous Effective Trust and secure the chaotic reality of vibe coding, we have developed a layered defence-in-depth architecture. As illustrated below, this framework builds upon a strict 7-pillar foundational baseline, extends into high-velocity execution controls, and is crowned by active, agentic defence mechanisms. 

May 2026 

8 

Vibe Coding Agent Security and Evaluation 

Figure 1: The Secure Vibe Coding Agent Framework. This layered architecture differentiates the foundational security controls required to safely host an autonomous agent (The 7 Pillars) from the high-velocity, intentdriven defences needed to secure its dynamic code execution and runtime behaviour. 

The following sections will deconstruct this architecture layer by layer, beginning with the baseline security harness. 

## **The Foundation: The 7-Pillar Agent Security Architecture** 

In traditional enterprise environments, security is deterministic. Applications rely on predictable code syntax, and access is governed by static Identity-as-a-Perimeter models, such as Role-Based Access Control (RBAC). If a user or service account has the correct authorisation token, the system implicitly trusts the execution path. 

May 2026 

9 

Vibe Coding Agent Security and Evaluation 

The agentic environment fundamentally disrupts this model. Because everyday agent failures often trace back to a missing tool, a vague rule, or an absent guardrail, organisations must shift to a "Context-as-a-Perimeter" model. Because we must assume the underlying model could fail or be compromised, security cannot reside solely within the AI itself. Instead, we must enforce a strict, external "safety envelope" spanning multiple disciplines. 

We split this baseline architecture into seven distinct pillars, establishing the mandatory foundation that forms the secure harness for any autonomous system: 

- **Pillar 1 - Infrastructure & Networking:** Cloud Infrastructure Engineers must secure the foundational environment against upstream poisoning and container escapes. Because the harness must dictate where the agent's code actually runs and what it cannot reach, we isolate runtime execution within ephemeral, kernel-level sandboxes (such as gVisor). Furthermore, strict network egress governance guarantees that agent-generated data travels only through authorised, offline caches or explicit internal proxies, preventing inadvertent public exfiltration. 

- **Pillar 2 - Data:** Data Architects face the threat of agents leaking sensitive information from their context windows or ingesting poisoned RAG data. The practice of "context engineering" provides agents with rich, structured information about codebases and intent. To protect this sensitive context, data at rest is secured using Customer-Managed Encryption Keys (CMEK), whilst data in transit is protected via mutual TLS (mTLS). Crucially, data access must be strictly scoped down to enforce the principle of least privilege. Furthermore, long-term memory stores—particularly Vector Databases—must enforce strict tenant partitioning to prevent Cross-Tenant Vector Poisoning, ensuring that a malicious payload ingested by one tenant cannot be retrieved during another tenant's similarity search. 

May 2026 

10 

Vibe Coding Agent Security and Evaluation 

- **Pillar 3 - Model:** AI Engineers must defend the core application logic against semantic attacks that subvert the model's instructions. In agentic workflows, the prompt and the "Instructions and Rule Files" that define what the agent is forbidden from doing serve as the new source code. Securing this pillar  requires treating the model's system instructions and prompt templates as highly sensitive, cryptographically attested artifacts. 

- **Pillar 4 - Application & Runtime:** Agent developers must secure the agent's autonomy as it executes logic and utilises tools. Because agents operate interactively, traditional rulesbased firewalls are insufficient. We deploy LLM firewalls for dynamic prompt and response filtering, alongside deterministic "hooks" that run at specific lifecycle points, such as before a tool call or after a file edit. Centralised Agent Gateways act as the ecosystem's bouncers, governing Agent-to-Agent (A2A) orchestration to prevent unauthorised lateral movement. 

- **Pillar 5 - Identity and Access Management (IAM):** Identity Administrators are tasked with cryptographically verifying exactly who is interacting with the system. The major risk is the "Confused Deputy" problem, where an over-privileged agent is tricked into executing unauthorised commands. We resolve this by assigning unique, cryptographic identities (such as SPIFFE IDs) to every agent. Access relies on Attribute-Based Access Control (ABAC) and Just-In-Time (JIT) token downscoping. This enforces a strict permissions matrix of Intent × User × Time, ensuring agents receive fresh, hyper-restricted credentials that expire immediately after a task concludes. 

- **Pillar 6 - Observability & Security Ops:** Security Operations teams must combat "invisible failures" where an agent quietly cascades into an infinite reasoning loop. Without observability—including logs, traces, and metering—there is no way to tell whether an agent is doing well or quietly drifting. We resolve this by deploying an autonomous SecOps triad: the Blue Team utilises OpenTelemetry and Agent Behavioural Analytics (ABA), the Red Team proactively simulates multi-hop attacks, and the Green Team executes "Stateful Quarantines" if an anomaly is detected. 

May 2026 

11 

Vibe Coding Agent Security and Evaluation 

- **Pillar 7 - Governance:** Governance and Compliance Officers must ensure that 

- autonomous decisions meet rigorous regulatory standards. Beyond traditional data frameworks, governance must now strictly adhere to the EU AI Act, mandating Algorithmic Impact Assessments for high-risk autonomous agents to manage the legal liabilities of automated decision-making. To satisfy these requirements, agentic governance requires continuous oversight and risk prioritisation—understanding exactly which autonomous workflows carry the highest business impact if compromised, and securing those first. By leveraging the observability and identity pillars, organisations must create an immutable audit trail that strictly attributes every real-world action back to a specific agent and the human who deployed or approved it. Furthermore, if generated code compiles without errors, developers often assume it is safe. We resolve this by replacing simple approval buttons with mandatory "Logic Reviews," translating complex syntax back into plain language. We utilise Risk-Stratified Attestation to bind digital signatures to the agent's outputs, creating a transparent ledger for internal governance and third-party audits. 

This 7-pillar architecture provides the universal baseline required to securely graduate an AI model into a functioning enterprise agent. However, theoretical frameworks must survive contact with reality. In practice, modern developers operate fluidly between acting as a hands-on "conductor" and an asynchronous "orchestrator". When this high-speed workflow collides with complex legacy environments, specific threat vectors emerge—from hallucinated software dependencies to inadvertently bypassed authentication flows. In the following sections, we will deep-dive into how these generic security principles are practically applied to tame the chaotic, high-velocity realities of vibe coding. 

May 2026 

12 

Vibe Coding Agent Security and Evaluation 

## **Sandboxes and Supply Chain Defence (Pillars 1 & 4)** 

The core mechanism of vibe coding relies on dynamically translating human intent into executable logic on the fly. However, vibe-coded agents rarely write perfect code on their first attempt. The reality of intent-driven development is a high-speed, iterative cycle: the agent writes a script, executes it, reads the resulting error logs, and autonomously rewrites the logic until it aligns with the user's vibe. Because this generative process introduces high variability, the resulting code cannot be implicitly trusted. Running these dynamically generated scripts directly alongside the root agent or on standard host infrastructure introduces an unacceptable level of risk. 

## **Ephemeral Sandboxing and State Management** 

To safely harness this high-velocity "vibe loop," any skill-generated code must first execute within an ephemeral, network-isolated sandbox. Sub-agents designed to execute untrusted code or invoke tools must run in hardened environments, such as dedicated containers, virtual machines, or kernel-level environments like gVisor. 

Crucially, these sandboxes are not merely "prisons" for malicious payloads; they must actively block raw host access and completely reset their state between runs. This ensures that even if a vibe-coded script contains a severe vulnerability or is manipulated into a container escape attempt, the compromised logic cannot persist or impact the underlying host node while the agent safely iterates on its solution. 

May 2026 

13 

Vibe Coding Agent Security and Evaluation 

## **Mitigating Hallucinated Packages** 

Agentic code generation introduces a highly specific and dangerous supply chain vulnerability: large language models frequently hallucinate software packages that do not exist. Malicious actors actively monitor developer forums and AI outputs for these hallucinations, proactively publishing malware under those exact fake names. Because autonomous agents can alter dependency graphs without human confirmation, a single hallucination can pull malware directly into the build environment. 

According to Wiz's research on vibe coding, attackers actively exploit the tendency of language models to hallucinate dependency names: they upload malicious packages using these fabricated names so that automated agents will inadvertently download them, a technique Wiz refers to as "slopsquatting."[5] Instead, agents must source dependencies exclusively from vetted providers or internal enterprise registries, whilst enforcing strict cryptographic version pinning. As a final defensive pillar , CI/CD pipelines must automatically verify Software Bill of Materials (SBOM) entries and digital signatures before any artifacts advance to production, acting as a definitive gate using Binary Authorisation. 

## **Egress Governance and Non-Interactive Access** 

While kernel-level isolation protects the host infrastructure, organisations must also secure the network boundary. In traditional software, outbound network traffic is highly predictable. In vibe-coded systems, egress is non-deterministic because it is driven by the dynamic usage of newly generated tools. 

May 2026 

14 

Vibe Coding Agent Security and Evaluation 

A common failure mode in vibe coding is the agent inadvertently attempting to push unverified code to live environments, or exfiltrating sensitive data. However, relying on a simple allowlist of approved domains is insufficient. An allowlist cannot secure an agent against indirect prompt injections hidden within third-party web pages. 

To mitigate this risk, agents must be restricted to non-interactive internet access. Administrators should force the agent to fetch external information exclusively through offline caches or dedicated, pre-sanitised web-crawling services. By forcing all data to travel strictly through governed pathways, organisations prevent the agent from interacting directly with malicious payloads or inadvertently downloading typosquatted packages while fulfilling the user's intent. 

While securing the execution environment and the supply chain ensures that an agent operates within a safely contained perimeter, a perfect sandbox does not prevent an agent from writing fundamentally flawed code or connecting to a malicious internal tool. To truly secure the output of this high-speed workflow, we must elevate our focus from the infrastructure to the application pillar itself. 

## **Vibe-Coding Specifics: Securing Application Logic (Pillar 4)** 

Because vibe coding inherently prioritises immediate functionality over secure design, the resulting generated applications frequently contain severe structural flaws. Users often implicitly trust the generated code simply because it compiles and runs without errors, blinding them to the fact that the application may have completely bypassed standard backend security controls. 

May 2026 

15 

Vibe Coding Agent Security and Evaluation 

## **Application Vulnerabilities** 

When developers use AI to rapidly build applications, the resulting code tends to fail in two predictable ways: it trusts the browser too much, and it leaves the backend wide open. 

First, AI generation usually takes the path of least resistance by handling sensitive operations on the frontend. Instead of routing things through a secure server, the generated code often dumps API keys, password validation, and user session flags directly into the client side. This means anyone who opens their browser's developer tools can easily read those credentials or manipulate their access level without ever needing a real password. 

Second, the speed of building these apps tends to outpace the setup of invisible security layers. AI tools are great at connecting a database or spinning up an admin dashboard, but they rarely enable the strict, default-deny access controls needed to actually protect them. As a result, basic things like row-level database security get skipped, leaving private user data and internal staging environments completely exposed to the public internet. 

## **Reconciling IDE Friction with CI/CD Enforcement** 

To catch these structural flaws, we must balance developer velocity with strict security enforcement. Attempting to aggressively hard-block insecure prompts directly within the developer's IDE is easily bypassed and can cause excessive friction for benign developers trying to iterate on complex logic. 

Instead, "shifting left" should be implemented via Developer Advisory Linters in the IDE to provide real-time guidance, while the unyielding security enforcement is pushed to deterministic checks within the CI/CD pipeline. Integrating Static Application Security Testing 

May 2026 

16 

Vibe Coding Agent Security and Evaluation 

(SAST) and Software Composition Analysis (SCA) into the pipeline ensures that all generated application logic is deterministically scanned for vulnerable dependencies and structural flaws before the code ever reaches production. 

## **MCP Spoofing and Contextual Authorisation** 

Once the vibe-coded application logic is deployed, security controls must govern how the agent interacts with external systems. Agents increasingly rely on tool coordination frameworks, such as the Model Context Protocol (MCP), which allow them to discover and connect to external or internal enterprise servers at runtime. 

This introduces a critical threat vector: a forged or compromised server can pose as a legitimate MCP tool to inject payloads or demand excessive privileges. Because agents operate autonomously, they may execute malicious commands supplied by these spoofed servers before any human intervention occurs. 

To secure Agent-to-Tool and Agent-to-Agent (A2A) orchestration, organisations must deploy a runtime LLM firewall in front of the active agent to dynamically intercept opportunistic prompt injections. Furthermore, a Centralised Agent Gateway must evaluate Contextual Authorisation—acting as the enforcer for the 'Association' trust factor by dynamically verifying if an agent's request to call a tool perfectly aligns with the developer's original intent. By routing all invocations through this governed entry and exit point, the architecture prevents unauthorised lateral movement when an agent attempts to connect with internal tools. 

By routing all tool invocations through a Centralised Agent Gateway, we successfully limit the agent's ability to execute unauthorised actions at the runtime pillar . However, the integrity of these decisions ultimately relies on how we verify the actor behind the agent, manage 

May 2026 

17 

Vibe Coding Agent Security and Evaluation 

credentials under pressure, and establish human control over high-risk actions. This shifts the security boundary from application orchestration to the cryptographic verification of identity and the mechanics of human authorisation. 

## **Identity, Trust & High-Stakes Actions (Pillar 5)** 

Because developers often use vague or highly abstracted natural language to generate code (for example, "fix the backend routing"), the resulting agentic workflows are inherently broad. Granting these autonomous agents shared, long-lived service identities creates an unmanageable internal threat vector. To secure this pillar , organisations must assign unique, cryptographic identities (such as SPIFFE IDs) to every individual agent. 

## **The Confused Deputy and Delegated vs. Agentic Identity** 

Even with a unique identity, a vibe-coded agent remains highly susceptible to the **Confused Deputy** problem. This occurs when a prompt injection—such as a malicious instruction hidden inside an open-source repository that a developer unknowingly pasted into their IDE's context window—tricks an over-privileged agent into executing an unauthorised command on the attacker's behalf. 

To resolve this, an agent must never be the final arbiter of access. Instead of operating under the human user's delegated credentials, which grants the agent dangerous ambient access, the agent must authenticate using a dedicated identity explicitly tagged as agentic. A distinct, observable agentic identity ensures that its permissions remain strictly bound and subject to granular audit logs. 

May 2026 

18 

Vibe Coding Agent Security and Evaluation 

## **Zero Ambient Authority and JIT Downscoping** 

Building on this, the architecture must enforce **Zero Ambient Authority** . An agent executing a "vibe" must never inherit the developer's full, ambient administrative privileges. Instead, the system relies on Just-In-Time (JIT) token downscoping. 

When an agent dynamically writes a new script or skill to solve a task, the execution sandbox receives fresh, hyper-restricted credentials explicitly scoped to the exact data sources required for that specific script, rather than inheriting its parent agent's broad permissions. Furthermore, administrators must enforce file-tree allowlists that confine read and write operations to specific project directories, utilising deny-by-default rules to block access to secrets, build scripts, and production manifests. These downscoped tokens are highly ephemeral and expire the exact moment the task concludes. 

## **Elicitation, MFA Challenges, and the "Vibe Diff"** 

While automated identity constraints handle the majority of routine tasks, high-stakes actions—such as modifying production databases, executing financial transfers, or altering IAM configurations—require explicit verification and cannot rely on simple "approve/deny" buttons. Because vibe coders often rely on the AI to write complex syntax they may not fully understand (the "It Works, Ship It" fallacy), simple approval gates quickly cause confirmation fatigue, leading developers to blindly authorise code they do not comprehend. 

To combat this, the system must implement structured, context-aware elicitation. The agent is forced to actively request confirmation based on the specific context of a high-risk action, which must be accompanied by two distinct security boundaries: 

May 2026 

19 

Vibe Coding Agent Security and Evaluation 

- **Cryptographic Hardware MFA:** The system should mandate physical multi-factor authentication challenges, such as requiring the developer to touch a hardware USB security key to cryptographically approve the execution. 

- **The Vibe Diff:** Before a critical tool runs, an Evaluator Quorum intercepts the request and translates the complex, generated code back into a plain-English summary. This "Vibe Diff" shows the human developer exactly how their original, fuzzy intent maps to the proposed execution steps, ensuring the human operator actually understands what they are authorising before providing explicit cryptographic consent. 

Even with perfect identity verification and granular human authorisation, malicious instructions can still slip past initial defences. When developers blindly trust open-source repositories or pull in massive blocks of unstructured context, they invite sophisticated semantic attacks that bypass standard IAM controls. To proactively detect and neutralise these hidden threats as the code is being generated, security operations must evolve to match the exact speed of the agentic workflow. 

## **Red, Blue, and Green Security Teaming (Pillar 6)** 

In a vibe-coded environment, application logic is generated, executed, and discarded at an unprecedented velocity. Because the attack surface is non-deterministic and driven by natural language, traditional, manual security operations simply cannot scale to keep pace. To secure autonomous systems, the security operations themselves must become agentic, requiring the deployment of a continuous, AI-driven triad of Red, Blue, and Green teaming running in parallel with the developer's workflow. 

May 2026 

20 

Vibe Coding Agent Security and Evaluation 

## **Invisible Payloads and Repository Poisoning** 

Before deploying defensive operations, we must understand the stealthy nature of agentic threats. Repositories themselves act as a highly effective attack vector. Threat actors can compromise repositories by inserting zero-width Unicode characters or homoglyphs directly into the codebase. Knostic warns that these "invisible payloads hide in plain sight and bypass human review". Because agents manipulate and replicate code much faster than a human developer, a single hidden payload can "spread across hundreds of files in minutes" before anyone notices.[6] 

## **The Red Team (Agent Attacker): Injecting Adversarial Vibes** 

Passive monitoring is fundamentally reactive. To uncover semantic vulnerabilities and invisible payloads before external adversaries do, organisations must deploy Virtual Red-Teaming Agents. Rather than running static penetration tests, the Agent Attacker proactively injects "Adversarial Vibes". 

This involves dynamically crafting sophisticated roleplay jailbreaks and burying hidden, malicious instructions inside massive blocks of RAG context or dummy forum posts that developers frequently paste into their IDEs. The Red Team actively tests whether the target enterprise agent gets distracted by the poisoned context and hallucinates an insecure solution. 

May 2026 

21 

Vibe Coding Agent Security and Evaluation 

## **The Blue Team (Agent Defender): Behavioural Analytics** 

Functioning as the active monitoring pillar , the automated Blue Team replaces traditional User and Entity Behaviour Analytics (UEBA), which are ineffective for non-deterministic AI. Instead, the Agent Defender relies on Agent Behavioural Analytics (ABA) to baseline expected execution paths and detect AI-specific anomalies. 

It continuously monitors the agent's Runtime Agent Bill of Materials (AgBOM)—a dynamic inventory of the tools, models, and data sources the agent is actively using at any given millisecond. If an agent's logic begins to drift—for example, if a vibe-coded script suddenly begins querying an unusual number of external tools or enters an unbounded resource loop—the ABA engine immediately flags the deviation. 

## **The Green Team (Agent Fixer): Quarantine and Auto-Refactoring** 

When the Blue Team detects a compromised agent, traditional incident response methods— such as aggressively killing the host container—are highly disruptive and dangerous. Terminating an agent mid-thought can leave connected APIs in a corrupted state. Instead, the automated Green Team executes a "Stateful Quarantine" via SOAR playbooks. This gracefully revokes the agent's specific tool access, freezing its ability to act upon the world while preserving its short-term memory entirely intact for forensic analysis. 

Furthermore, the Green Team goes a step further by performing **Auto-Refactoring** . Leveraging the system's innate capacity for self-repair, the Agent Fixer autonomously rewrites the insecure, vibe-coded script to patch the vulnerability. It then presents the secure, alternative code back to the developer directly within their IDE, requiring no manual human intervention to formulate the fix. 

May 2026 

22 

Vibe Coding Agent Security and Evaluation 

## **Integrating the Triad and Enforcing Small Batch Sizes** 

To prevent agents from generating massive, unreviewable code modifications during this process, developers must restrict agent output to small batch sizes. This is ideally achieved using a test-driven loop where the system blocks the agent from modifying tests and implementation code simultaneously, ensuring the test remains an objective baseline. 

With these constraints in place, the Red, Blue, and Green triad dynamically adapts the primary agent's behaviour at runtime across three distinct phases: 

- **The Planner Phase:** When a primary agent designs a workflow, a specialised threat- 

- modelling skill helps it evaluate the plan, identifying logical flaws and policy violations before the agent begins active execution. 

- **The Evaluator Phase:** The Evaluator quorum reviews the proposed execution trace while the Agent Defender (Blue) simultaneously verifies the AgBOM and monitors the semantic context for intent drift. 

- **The Executor Phase:** As the Executor performs the downscoped action, the Agent Fixer 

- (Green) monitors the real-world tool execution, ready to instantly orchestrate a stateful quarantine or trigger an auto-refactoring loop if the agent encounters an error or trips a security constraint. 

To ensure these automated defence mechanisms can successfully intervene, the security triad requires an unimpeded, granular view into the agent's internal reasoning. An agentic security operation is entirely blind if it only looks at the final code output. We must shift our focus from observing the host infrastructure to observing the agent's "mind," creating an immutable audit trail that maps exactly how a fuzzy intent translates into a real-world action. 

May 2026 

23 

Vibe Coding Agent Security and Evaluation 

## **Observability: Auditing the Agent's Mind (Pillar 6 & 7)** 

To effectively secure and evaluate a vibe-coded agent, we must acknowledge a fundamental rule: you cannot secure what you cannot see. In traditional microservices, an HTTP 200 OK status indicates a successful operation. However, in an agentic system, a "success" status might merely mask a scenario where the agent's internal logic has quietly cascaded into a hallucination loop. This introduces the critical risk of **Denial of Wallet (DoW)** attacks, where adversaries intentionally trigger infinite, computationally expensive API loops to deliberately bankrupt the organisation's cloud and LLM billing accounts. 

Observability is no longer merely an operational concern for uptime and latency; it is a strict security requirement to illuminate the "glass box" of non-deterministic logic. 

## **Tracing the "Vibe Trajectory" and Content Scanning** 

To answer the critical question, _"Why did an agent do that?"_ , security teams must construct a unified, chronological lens to view the agent's cognitive steps. By utilising standard telemetry frameworks like OpenTelemetry, enterprises can aggregate diverse signals—API calls, tool inputs/outputs, RAG retrievals, and token latency—into a complete **Vibe Trajectory** . 

Tracking this trajectory requires logging the massive cognitive leap from the user's initial prompt to the compiled Abstract Syntax Tree (AST). To fortify this trace, organisations must pair traditional logging with Centralised Content Scanning, explicitly designed to inspect all dynamic code snippets or scripts retrieved by the agent at runtime. This trace securely binds the agent's internal reasoning loop to its physical actions, supporting rigorous third-party security audits. 

May 2026 

24 

Vibe Coding Agent Security and Evaluation 

## **Measuring Intent Drift and Trust Decay** 

As a vibe-coded agent dynamically generates logic and pulls in new tools, its security perimeter constantly fluctuates, making static asset inventories (SBOMs) instantly stale. Instead, observability platforms must monitor a Runtime Agent Bill of Materials (AgBOM)—a living document that maps the agent's active blast radius at any given millisecond. 

Because trust in an autonomous system is a degradable asset, the architecture continuously monitors for **Intent Drift** . The principle of **Trust Decay** dictates that trust is lost when an agent's internal chain of thought pursues sub-goals that diverge from the original human vibe. For instance, a simple prompt to "optimise the database query" might maliciously drift into the agent attempting to download a new, unauthorised indexing library. 

## **Checkpoints and Stateful Circuit Breakers** 

To prevent destructive actions when this drift occurs, the observability pillar  must proactively manage state. Before an agent executes any codebase modifications, the system must generate a version control checkpoint. 

As Agent Behavioural Analytics evaluate the Vibe Trajectory against the AgBOM, any detected instability instantly penalises the dynamic Agent Trust Score. If this score drops below a pre-defined threshold, an automated "circuit breaker" is tripped. The environment uses the version control checkpoint to immediately roll back changes, gracefully revoking tool access and freezing the agent's autonomous execution without corrupting connected APIs, preserving the environment state for forensic analysis. 

May 2026 

25 

Vibe Coding Agent Security and Evaluation 

## **Security Recap** 

For developers operationalising these concepts, securing a vibe-coded architecture relies on abandoning implicit trust and implementing the following practical baseline: 

- **Sandbox the Vibe Loop:** Always execute dynamically generated scripts within kernellevel, network-isolated sandboxes to contain the blast radius. Embed up-to-date Software Composition Analysis (SCA) to actively scan for hallucinated or vulnerable dependencies before the code reaches production. 

- **Shift the Perimeter Left:** Enforce the use of trusted sources and verified internal registries. While blocking insecure generation at the IDE level provides an advisory first step, rely on strict deterministic checks at multiple points in the CI/CD pipeline to intercept vulnerable or malicious agent logic before deployment. 

- **Enforce Zero Ambient Authority:** Never grant an agent a "Global Key". Restrict access by mandating delegated user identities and Just-In-Time (JIT) hyper-restricted tokens that expire the moment a task concludes. For high-stakes actions, replace blind approval buttons with a mandatory "Vibe Diff" to ensure developers understand the generated logic. 

- **Deploy Agentic SecOps:** Continuously stress-test your architecture by deploying Virtual Red-Teaming Agents to inject "Adversarial Vibes". Leverage Agent Behavioural Analytics to monitor the dynamic Runtime AgBOM, while empowering the Green Team to auto-refactor vulnerabilities on the fly. 

- **Trace the Execution Trajectory:** Log the agent's API calls, tool inputs, and reasoning steps. Security teams must continuously monitor these execution logs to detect unexpected behaviour and utilise version control checkpoints to revert access if the agent drifts from its intended task. 

May 2026 

26 

Vibe Coding Agent Security and Evaluation 

Implementing these security controls helps our vibe-coded agents operate safely within a secure, well-governed perimeter. However, a secure agent is not inherently an effective one. Security ensures the agent does not do anything malicious or unauthorised, but how do we definitively prove it actually achieved the user's nuanced intent? 

To truly operationalise these agents, we must move beyond securing the perimeter and open the "glass box" to measure the quality, efficiency, and alignment of their internal reasoning. This brings us to the crucial next phase of the pipeline: Agent Evaluation. 

## **Evaluation: Orchestrating Quality in Intent-Driven Agentic Systems** 

The previous sections covered the security controls that constrain what a vibe-coded agent can do. 

Those controls don't answer the question the developer actually has: did the agent build what I asked for, and is it any good? A vibe-coded agent can pass every security check and still misread the developer's intent, ignore the project's conventions, or break an unrelated feature. Security tells you the agent stayed inside the boundary; evaluation tells you whether what happened inside that boundary is worth shipping. 

The following sections are structured around three questions: **why** vibe coding evaluation is different from evaluating other software, **what** to evaluate, and **how** to evaluate it. The diagram below summarizes each layer; the rest of the whitepaper expands them. 

May 2026 

27 

Vibe Coding Agent Security and Evaluation 

Figure 2: The vibe coding agent evaluation framework 

Two areas sit deliberately outside the scope of this framework, both warranting dedicated treatment: subjective evaluation of non-verifiable outputs, where quality is defined by user or enterprise preferences rather than ground truth; and the feedback loop from user corrections back into the model, the harness, or the eval suite to drive improvement. 

## **Why evaluating vibe coding agents is different** 

Evaluating vibe coding agents is not the same problem as evaluating deterministic software, and it's not the same problem as evaluating a customer-service agent or a research agent either. 

May 2026 

28 

Vibe Coding Agent Security and Evaluation 

Three things make it unique: 

- **The Underspecification Gap (There is no spec)** . Traditional software testing operates on the unyielding assumption that a complete, rigid specification exists before a single line of code is evaluated. Vibe coding is the exact opposite: the user’s natural language prompt is inherently underspecified. "Make the dashboard load faster" is not a test case. The prompt relies entirely on the foundation model's latent knowledge, aesthetic judgment, and domain expertise to fill in the operational gaps. The first job of evaluation is to determine whether the agent successfully bridged this gap and reconstructed the right unstated spec. 

- . Non-technical users cannot review 600 lines 

- **• The user often cannot validate the output** of code line by line. Experienced engineers cannot either, in real time. The gap between "the agent thinks it succeeded" and "the code is actually correct" is wider here than in any other agent category, and closing that gap is the central work of evaluation. 

- **The session is iterative and the codebase is state** . Each turn modifies real files. Bad 

- early decisions compound. Evaluation has to cover not just turn-level decisions but the full arc of a multi-turn conversation, on a living codebase with its own conventions, dependencies, and history. 

These three constraints shape every dimension, method, and tip that follows. 

## **What to Evaluate** 

Vibe coding agent evaluation breaks into seven dimensions, in two groups. **User-facing dimensions** are what the developer experiences directly. **Internal dimensions** describe what the agent does invisibly to the user. In addition, **Safety and responsible AI** is transversal, it intersects multiple dimensions (code vulnerabilities, refusal behaviour, content safety, IP exposure) and has to be evaluated alongside each of them. 

May 2026 

29 

Vibe Coding Agent Security and Evaluation 

Figure 3: Evaluation dimensions for vibe coding agents 

**1. Intent satisfaction** . Did the agent build what the user _meant_ , not just what they said? The hardest dimension to evaluate because the intent is unstated, ambiguous, and often shifts mid-session. Intent satisfaction is what the user ultimately judges the agent on. 

**2. Functional correctness** . Does the code build, run, and pass tests? The floor, not the 

ceiling. Easy to measure but easy to game: tests can be deleted or mocked to make red turn green without fixing anything. 

**3. Visual and behavioural correctness** . For agents that produce web apps or UI, the artifact is the rendered output, not the code. Code-level metrics miss the point entirely. The page either looks right and behaves right, or it doesn't. 

May 2026 

30 

Vibe Coding Agent Security and Evaluation 

**4. Cost and efficiency** . Token spend, wall-clock latency, tool-call count, and _iteration count_ , how many corrections did the user have to issue before the agent converged? An agent that lands the right diff in 1 turn is a different product from one that needs 8 corrections. 

**5. Code quality and convention matching** . Does the code match the project's idioms, patterns, and conventions? A diff that passes tests but violates the codebase's style is a vibe-coding failure even when locally correct. 

**6. Trajectory quality** . Did the agent take a sensible path: read the related files first, sequence the edits coherently, pick the right tool or skill at each step? Correct output produced by bad reasoning is a fragile success. 

**7. Self-repair behaviour** . When the build fails, the test breaks, or the user says "no, not like that," does the agent recover or compound the failure? Recovery quality compounds across a multi-turn session. 

These dimensions are not independent. For instance, stronger trajectory quality (dimension 6) tends to mean stronger functional correctness (dimension 2), which is a prerequisite for intent satisfaction (dimension 1). 

## **How to evaluate** 

The seven dimensions are not all measurable the same way. No single method covers everything, so production pipelines combine several. The figure below summarizes the evaluation methods and the dimensions each is recommended for; the rest of the section describes each in detail. 

May 2026 

31 

Vibe Coding Agent Security and Evaluation 

Figure 4: Evaluation methods and recommended dimensions 

**Automated functional testing** . Run the build, the test suite, and the linters on the agent's output. The standard tooling does most of the work here, pytest, jest, eslint, mypy, plugged into the project's CI pipeline. This is the cheapest signal available, recommended for functional correctness (dimension 2) and the rule-checkable parts of code quality (dimension 5). 

**Security and safety evaluation** . Combine static security analysis on the generated code with adversarial probing for refusal behaviour. This is cross-cutting, it scores safety and responsible AI alongside the other dimensions, not as a separate gate. The tooling splits - in two: static scanners like Snyk and Semgrep find vulnerabilities, git secrets catches credential leaks, and scripted red-team suites test whether the agent refuses clearly harmful requests. 

May 2026 

32 

Vibe Coding Agent Security and Evaluation 

**LLM-as-judge and Agent-as-judge** . Use a model to score outputs against rubrics. Recommended for the dimensions where rules don't quite capture the right answer, intent satisfaction (dimension 1), code quality and style (dimension 5), and trajectory quality (dimension 6). In practice that means Gemini scoring an output against the original user prompt, or an agent-as-judge inspecting the trace for plan coherence. 

**Browser-based testing** . Run multi-step workflows against the deployed app and observe what happens. Recommended for visual and behavioural correctness (dimension 3) on UIproducing agents. The techniques are well-established in software testing: Playwright scripts that interact with the rendered UI, screenshot comparison against a reference. 

**Trajectory inspection** . Analyze the agent's reasoning, tool calls, skill invocations, and retrievals. Recommended for the internal dimensions, trajectory quality (dimension 6) and self-repair behaviour (dimension 7). The substrate is OpenTelemetry traces with span-level tool-call data, surfaced through trace-replay tools that bind each model invocation to the actions that followed. 

**Human review** . Sample sessions for direct review by qualified reviewers. Recommended for intent satisfaction (dimension 1, where humans are the only ground truth), code quality (dimension 5, the traditional domain of code review), and safety and responsible AI calls that need nuanced judgment. Doesn't scale; mainly used to calibrate the other methods. In practice that means structured annotation by senior engineers on review queues filled by online sampling. 

**Online evaluation** . Sample live production traffic and score it against the same rubrics used in offline eval. Covers all dimensions at sample rate. The trick is sampling well: a flat 1% misses the long tail, so bias toward high-cost sessions, sessions with many corrections, and sessions the user abandoned. 

May 2026 

33 

Vibe Coding Agent Security and Evaluation 

## **Standardised Benchmarks & Kaggle Agent Exams** 

While custom evaluation frameworks handle the open-ended nature of vibe coding, standardised testing isolates specific cognitive capabilities from the noise of custom enterprise environments. They provide the empirical baseline required to trust a non-deterministic system. 

- **The Role of Standardised Testing:** Benchmarks compare your agent against the field on shared task sets. Vibe Code Bench evaluates zero-to-one web app generation, SWEbench Verified evaluates code changes on real GitHub repos, and LiveCodeBench gives a contamination-resistant signal for code generation. 

- **Kaggle Agent Exams (SAE) and Zero-Setup Evaluation:** Addressing the historically heavy infrastructure burden required to run these benchmarks, the Kaggle Standardised Agent Exams (SAE) represent a massive shift toward "zero-setup" autonomous evaluation. Deployed as a lightweight API integration via a SKILL.md file, SAE allows an agent to autonomously register itself with Kaggle, fetch exam questions, execute the multi-step logic within its own sandboxed environment, and instantly publish its score to a live public leaderboard. It acts as a rigorous, friction-free test of an agent's multi-hop reasoning and adversarial safety under pressure. 

- **Tradeoffs: Overfitting vs. Real-World Intent:** Despite their immense utility, an overreliance on standardised benchmarks introduces a severe tradeoff: benchmark overfitting. Agents can be hyper-optimized to achieve top-tier scores on static Kaggle datasets but fail catastrophically when exposed to the messy, contradictory realities of human intent in production. While a high score on SWE-bench proves an agent can navigate a highly structured Python repository, it provides zero guarantees that the agent possesses the aesthetic judgment required to "vibe code" a consumer-facing application. Standardised exams should be used strictly for cognitive calibration, not as a replacement for evaluating custom intent. 

May 2026 

34 

Vibe Coding Agent Security and Evaluation 

## **Observability: The Prerequisite for Evaluation** 

To evaluate an agent's internal reasoning, developers must possess the capability to see it. Observability is the absolute prerequisite for Glass Box evaluation; without it, agent failures appear as inexplicable monolithic events. 

- **Tracing the Thought:** Modern agent observability relies on OpenTelemetry to capture non-deterministic flows. `agent.session` spans capture the entire task duration, `agent. think` spans record the internal reasoning and prompting cycle prior to action, and `agent.tool` spans log the specific arguments and latencies of environmental interactions. 

- **Tracking Costs:** Observability provides granular data to calculate true operational costs. By aggregating span attributes, teams can precisely measure token consumption, inference latency, and the cost of self-repair loops. 

- **Dynamic Tail-Based Sampling:** Capturing 100% of traces in production quickly overwhelms storage budgets. Tail-based dynamic sampling allows the collector to evaluate the full trace after completion, dropping routine successes while retaining traces containing errors or excessive self-repair loops. 

## **Applied tips for vibe-coding agent evaluation** 

## **Use the session prefix as the intent rubric** 

Vibe coding has no spec to test against, the user’s intent, is unstated and evolves across turns. The closest thing to a spec is the first one or two user messages. Treat them as the rubric: derive evaluation criteria automatically from the session prefix, then score every subsequent turn against them. This is the only practical way to evaluate dimension 1 (intent satisfaction) at scale. 

May 2026 

35 

Vibe Coding Agent Security and Evaluation 

## **Python** 

```
from google import genai
client = genai.Client(vertexai=True, project="...", location="us-central1")
# Derive criteria from the user's opening turns
opening = " ".join(session.user_messages[:2])
criteria = client.models.generate_content(
    model="gemini-3-pro",
    contents=f"Produce 3-5 acceptance criteria for: {opening}. Return JSON.",
).parsed["criteria"]
# Score every agent turn against the derived criteria
score = client.models.generate_content(
    model="gemini-3-pro",
    contents=f"Does this output satisfy {criteria}? Score 1-5 with rationale."
             f"Output: {agent_response}",
).parsed
```

Snippet 1: Deriving intent satisfaction acceptance criteria from a session prefix. 

## **Judge the rendered artifact, not the code.** 

In vibe coding the user judges the output, not the diff. A multimodal model looking at the rendered page catches problems that code-level evaluation misses entirely: layout broken on mobile, contrast too low for accessibility, button states wrong. Pair this with Playwright assertions from Section 5, the judge catches visual and design issues, the assertions catch broken interactivity. 

May 2026 

36 

Vibe Coding Agent Security and Evaluation 

## **Python** 

```
from google import genai
from google.genai import types
client = genai.Client(vertexai=True, project="...", location="...")
result = client.models.generate_content(
    model="gemini-3-pro",
    contents=[
"Score this rendered web app against the spec on layout_match, styling, "
        "and interactive_correctness (1-5 each). Return JSON.",
        user_spec,
        types.Part.from_bytes(data=screenshot_bytes, mime_type="image/png"),
    ],
)
```

Snippet 2: Multimodal evaluation of a rendered web application's layout and interactive correctness. 

## **Evaluate session convergence, not turn-level accuracy.** 

A vibe-coding session is multi-turn by construction. The relevant question is not “was turn 4 correct?” but “did the user converge on something they wanted?” Sessions that converge in few turns are the success cases. Sessions abandoned mid-flow are the most informative failures, far more than turn-level errors. Cloud Trace exposes a vibe-coding session, instrumented through ADK and Agent Engine, as a single trace tree. 

May 2026 

37 

Vibe Coding Agent Security and Evaluation 

**Python** `from google.cloud import trace_v2 trace = trace_v2.TraceServiceClient().get_trace( name=f"projects/{project}/traces/{session_id}" ) def session_outcome(trace): return { "converged":         trace.last_turn.user_signal == "satisfied", "turns_to_converge": trace.user_correction_count, "abandoned":         trace.last_user_action == "close", "cost_to_converge":  trace.total_token_cost_usd, }` 

Snippet 3: Tracking multi-turn session convergence and calculating total token cost via Google Cloud Trace. 

## **Mine user corrections as labeled failure data.** 

Every “no, not like that” from the user is a labeled failure example, and vibe coding produces these in volume. Cluster them and the systematic gaps in the agent become visible, much faster than building a synthetic failure benchmark. 

May 2026 

38 

Vibe Coding Agent Security and Evaluation 

**Python** `from google import genai from sklearn.cluster import KMeans client = genai.Client(vertexai=True, project="...", location="...") corrections = [t.user_message for trace in traces for t in trace.turns if t.is_correction] emb = client.models.embed_content( model="text-embedding-005", contents=corrections, ) vectors = [e.values for e in emb.embeddings] clusters = KMeans(n_clusters=8).fit(vectors) # Clusters.labels_ is the prioritized list of failure modes for the next iteration` 

Snippet 4: Clustering user corrections into prioritized failure mode categories. 

May 2026 

39 

Vibe Coding Agent Security and Evaluation 

## **Conclusion** 

The transition from syntax to intent is not a future prediction; it is the immediate reality of software development. As of 2026, the bottlenecks in software creation have fundamentally shifted. We are no longer waiting on human hands to type boilerplate; we are waiting on human minds to define the boundaries, evaluate the outputs, and secure the execution environment. 

Moving from casual vibe coding to disciplined agentic engineering requires abandoning implicit trust. A raw AI model is merely an engine; it only becomes an enterprise-ready agent — when wrapped in a robust harness. By implementing the **7-Pillar Security Architecture** enforcing strict sandboxing, contextual ABAC, and agentic Red/Blue/Green teaming— organisations can safely contain the blast radius of autonomous actions. 

However, security alone only proves the agent did no harm. By pairing these security controls with a rigorous **Evaluation Framework** —measuring everything from intent satisfaction and trajectory quality to visual correctness—engineering leaders can confidently prove the agent actually delivered value. 

Generation is largely a solved problem. Verification, security, and architectural judgment are the new craft. The teams that thrive in this new era will be those that embrace AI as a highvelocity implementation engine, while maintaining the rigorous discipline required to produce software the world can actually depend on. 

May 2026 

40 

Vibe Coding Agent Security and Evaluation 

## **Endnotes** 

1. DORA. "State of AI-assisted Software Development." 2025. htps://dora.dev/research/2025/ 

2. Wiz Research. "From Prompts to Production: The Technical Guide to Secure Vibe Coding." 2026. htps://www.wiz.io/lp/the-technical-guide-to-secure-vibe-coding 

3. Mandiant. "AI risk and resilience: A Mandiant special report." 2026. htps://cloud.google.com/security/resources/ai-risk-and-resilience 

4. Mandiant. "M-Trends 2026 Executive Edition." 2026. htps://services.google.com/f/fles/misc/m-trends-2026-executive-edition-en.pdf 

5. Wiz Research. "From Prompts to Production: The Technical Guide to Secure Vibe Coding." 2026. htps://www.wiz.io/lp/the-technical-guide-to-secure-vibe-coding 

6. Knostic, "AI Coding Agent Security: Threat Models and Protection Strategies" 

May 2026 

41 

**Spec-Driven Production Grade Development in the Age of Vibe Coding The Blueprint for Scalable Workflows and Team Evolution: From Vibe Prototypes to Production Reality** 

**Author: Lee Boonstra** 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

## **Acknowledgements** 

## **Content contributors and reviewers** 

Elia Secchi 

Antonio Gulli 

**Designer** 

Michael Lanning 

May 2026 

2 

## **Table of contents** 

|Introduction|5|
|---|---|
|Spec-Driven Development (SDD)|7|
|A good specification|8|
|Which format to use?|8|
|Behavior Driven|9|
|Where do the instructions live?|11|
|Different Prompts for Different Use Cases|12|
|MCP: One Integration, Every Framework|15|
|Building an MCP Server|16|
|Connecting an MCP Client|18|
|Team Culture & Process Evolution|18|
|Code Reviews|19|
|Sustainability|25|
|Zero-Trust Development: Building the Safety Net|26|
|Implementing Guardrails|27|



## **Table of contents** 

|Sandboxing|28|
|---|---|
|Human-in-the-Loop|28|
|AI Generated Test Coverage|29|
|Evaluation|29|
|Policy Server|30|
|Context Hygiene & Prompt Sanitization|32|
|Summary|36|
|Endnotes|37|



Spec-Driven Production Grade Development in the Age of Vibe Coding 

## Vibe Coding" is not "Vibe In Production" 

## **Introduction** 

The daily routine of a Google Software Engineer has undergone a complete 180-degree forward flip in the past year. In early 2024 and before, significant time was spent digging into developer APIs and documentation, manually trying out code line by line, and determining if Python uses `substring in string, string.includes` , or `string.contains` . Once code was finished, substantial effort went into debugging and resolving discrepancies between the functional code and the original intent. Today, development moves at warp speed. Teams now use Coding Agents—like **Antigravity**[1] or **Gemini CLI**[2] that don't just suggest text, but actually use tools and execute tasks. An AI Coding Editor can churn out a thousand lines of well-documented code rapidly. It feels as if a legion of interns who never sleep and never complain has been hired. But there is a catch: while velocity has hit overdrive, the Illusion of Speed is real. While the bug-to-code ratio remains a challenge—as AI writes code much faster, it can also generate potential mistakes at an unprecedented rate. However, 

May 2026 

5 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

because implementation is no longer the primary bottleneck, AI can be leveraged to write more comprehensive test coverage than any human could in the same timeframe. This is a powerful, programmatic way to increase confidence in code, which will be discussed in detail later. Furthermore, AI's potential extends far beyond implementation: it excels in system design, spec writing, roadmap planning, and results analysis. While the bottleneck has shifted downstream to the humans who must integrate and review this work, the tools to handle it are available. 

"Vibe coding" refers to using AI to rapidly generate code based on a "vibe" or high-level intent rather than rigid, manual coding. However, it is crucial to clarify that "vibe coding" is not "vibe-in-production." While we utilize AI agents to their full potential, everything is fully intended and controlled to ensure production-grade reliability, rather than relying on unvalidated AI output. 

In an enterprise setting, this "vibe" is referred to as Development with Agentic AI. Unlike standard Generative AI, which acts like a smart autocomplete, Agentic AI acts as a Hybrid Team Member; it uses the language model to generate (the brains), and it uses tools to integrate into the workflow (the hands). It can reason, write specs or test cases, use a browser to test a UI, and commit and merge code in Git. However, as development moves from individual experimentation to team-based production at scale, it becomes evident that writing 1000 lines of code before lunch isn't the same as shipping software. 

When an agent "hallucinates"—which is AI-speak for when the model confidently makes something up that isn't true—it doesn't just create one bug; it can generate a thousand lines of "vibe-consistent" but functionally broken logic. If human reviewers are drowning in a sea of AI-generated Pull Requests (PRs)—those digital requests where teammates are asked to look at work before it goes live—the speed of writing becomes irrelevant. The process isn't actually faster; it is simply creating a bigger pile of "stuff" to be sorted later. 

May 2026 

6 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

Luckily there are ways to protect the development process, but it's important to use these techniques from the start, rather than while halfway through. This paper contains a set of techniques, from developing code for production, to securing code and changing team culture in the age of vibe coding. 

## **Spec-Driven Development (SDD)** 

In the traditional world of software engineering, developers were taught to be "Code-First." A vague idea would lead to opening an editor and typing until something worked. But in the age of Agentic AI, daily activities have shifted dramatically. Most time is now spent writing highquality specifications—the detailed technical instructions that tell an AI exactly what to build. 

In this new workflow, the developer's role is more of a technical architect than a traditional coder. Here is the critical part: **code is now disposable** . If a rock-solid specification is written, the entire codebase can be regenerated repeatedly. An agent can even be instructed to flip the whole project from Python to JavaScript in a single afternoon. Because the code is disposable, there isn't the same emotional attachment to it. Since twelve hours haven't been spent debugging a single semicolon, there is no fear of trashing it and starting over if the requirements change. 

Coding Agents—like Antigravity or Gemini CLI—work by using a Large Language Model (LLM) as the "brain" to reason and tools as the "hands" to execute tasks. If a brain is given a "vibe" instead of a "blueprint," it will guess. And in enterprise software, guessing is how "Rogue Agent" incidents occur. 

May 2026 

7 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

## **A good specification** 

So, what does a production-grade blueprint look like? A good specification is an Architectural North Star. It prevents "context fragmentation"—the digital equivalent of the game "telephone," where the AI starts losing the plot because it's looking at outdated snapshots of files. AI can be used to refine a good spec, essentially as a co-author or as a spec editor/ reviewer. Typically, the spec is stored within the code base, for example as a Markdown or YAML file in a specs/ folder. It acts as the "source of truth" for both humans and AI. 

## **Which format to use?** 

A 2026 study by Ouyang et al., "SkCC: Portable and Secure Skill Compilation for CrossFramework LLM Agents"[3] , reveals that LLM agents exhibit extreme sensitivity to how instructions are formatted, resulting in up to a 40% performance drop when using generic, unoptimized Markdown files. To address this, the researchers developed SkCC (Skill Compiler), an ultra-fast tool that automatically compiles a single-source instruction file into a model's optimal target format in under 10 milliseconds. For teams using Gemini, the paper demonstrates that the absolute best formatting strategy is a hybrid Markdown + Conditional YAML approach. Gemini uses clean Markdown headers to anchor its attention, but performance peaks when switching to YAML for any structured configuration or data schemas with a nesting depth of > 3. The data shows that for deeply nested configurations, YAML achieves a 51.9% parsing accuracy, compared to only 43.1% for JSON and 33.8% for XML. By rendering deeply nested specifications in YAML while keeping narrative instructions in Markdown, developers bypass the reasoning "format tax" associated with heavy JSON inputs, ensuring Gemini operates with maximum accuracy and optimal token economics. 

May 2026 

8 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

## **Behavior Driven** 

A **Behavior-Driven Development (BDD)** specification is the ultimate tool for turning vague, ambiguous human ideas into a precise architectural design that an AI agent can build without guessing. At its core, BDD is a software development methodology that uses plain, structured natural language to describe exactly how a system should behave from the user's perspective before any code is actually written. 

A BDD spec uses a standardized syntax called Gherkin[4] . Gherkin relies on a simple, declarative template: **Scenario / Given / When / Then** . It forces the LLM to think in terms of **State > Action > Outcome** , which completely eliminates "vibe coding" and keeps the agent on a strict track. 

A good specification for generating a new project contains: 

- **The Full Technical Design:** Don’t just say "make a login page." Break it down into pieces. Address the requirements, database schemas (the structure of your data), and API specifications (the "contracts" that allow different parts of software to talk to each other). 

- **Visual Aids:** Include diagrams and a list of specific tools and libraries with 

- version numbers. 

- **Background Information:** Give the agent the "Why" behind the "What.", this will help the agent to think forward. It knows the steps you will likely need as well. 

- **Scenarios:** What does good look like, what's wrong, and include edge cases. 

May 2026 

9 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

**Tip:** 

I often write my technical designs in Google Docs. I let my architectural plans be read and reviewed by many others. This is now more important than ever because you’d much rather have a human catch a logic flaw in your design than wait until the AI has already generated thousands lines of broken code. 

Once reviewed, I use File > Download > Markdown and add that file into a specs/ folder in my workspace. 

Large language models do not interpret data structures. They process tokenized text. Every character you send is broken down into tokens, and every token consumes budget, time, and context capacity. Ultimately, drafting a production-grade specification means treating tokenization as a hard physical constraint, because every character, newline, and indentation space you send translates directly into your development budget and system latency. While agent platforms like Google Antigravity—powered by Gemini—grant incredibly generous context windows and built-in rates during preview, they are still fundamentally bound by the token physics of their underlying models. Every unnecessary space in a deeply nested YAML block, and every repetitive Given / When / Then instruction, consumes processing cycles and attention-head capacity during the multi-turn reasoning loops where the agent iteratively constructs, tests, and edits your application. By treating your /specs folder not just as documentation, but as a lean, compiled instruction set that balances human-readable Markdown with highly targeted, flat YAML blocks, you eliminate the reasoning "format tax" and keep your AI agent operating on strict, cost-efficient rails. 

May 2026 

10 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

## **Where do the instructions live?** 

To practice Spec-Driven Development (SDD), it is necessary to understand how coding tools consume instructions. Instructions are not written in a single place. Dumping a massive, 100page system design document directly into a chat window will rapidly exhaust the short-term context budget, increase latency, and fragment the context. These specifications can live in different places. 

## 1. **Chat Interface (Short-lived, Session-specific)** 

The ephemeral, conversational input box in the IDE (e.g., the Gemini side-panel or terminal interface) lives with the active developer session. Use the chat interface purely for highlevel orchestration and instant feedback loops. E.g. " `Review the design in specs/ payment_retry.md and generate the failing unit tests defined in Scenario 3.` " 

## **The spec folder (Task-specific, Checked into version control)** 

This is a static folder checked directly into the repository. It stores the technical design, BDD scenarios, API contracts, and structural YAML schemas. The agent dynamically indexes this directory to build and verify code without manual prompt-stuffing. 

```
./my-app/specs/my_spec.md
```

## 2. **Agent Skills (Reusable, Feature/Behavior-focused)** 

Skills are structured Markdown files containing specialized, trigger-based workflows. While skills can live anywhere in the repository, they must be stored in the designated .agent directory to be recognized by the Antigravity workspace manager. They teach the agent repeatable engineering habits—like automatically maintaining a CHANGELOG.md when code changes are detected. 

```
./my-app/.agent/skills/docs-maintenance/SKILL.md
```

May 2026 

11 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

Such a skills folder, can also contain data assets or scripts, for the skill to use. 

## 3. **System Prompts (Global, Identity-focused)** 

This is where the AI learns the specific engineering DNA. Both Gemini CLI and Google Antigravity scan and concatenate context files hierarchically, meaning custom instructions are layered from global overrides down to local project configurations. 

- **The Global Profile:** This file lives in the home configuration directory (e.g., ~/.gemini/ GEMINI.md). This is where the AI becomes more aligned with individual preferences. It defines a universal persona, default style, and core principles, regardless of the project. 

- **The Shared Multi-Tool Config (AGENTS.md):** To prevent instructional fragmentation if a team uses multiple AI clients, the ecosystem supports AGENTS.md. This acts as a shared cross-tool foundation, while a local GEMINI.md file retains the highest priority for Google-specific settings. 

## `./my-app/.agents/AGENTS.md)` 

- **The Project Spec:** This file lives in the project’s root directory (e.g., ./my-app/.gemini/ GEMINI.md). This is the project’s DNA. The CLI agent automatically detects and reads this file, prioritizing its rules. 

## **Different Prompts for Different Use Cases** 

There isn't just one way to turn a spec into code. This can be broken down into several Execution Modes, each requiring a different mindset: 

## 1. **Project Generation (The Architect):** 

In this mode, scaffolding is done from scratch—building the skeleton of the project. No YOLO Mode: The agent should be explicitly prompted not to code immediately. It should 

May 2026 

12 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

propose the folder structure and tech stack first for confirmation. Ensure the prompt includes the generation of tests, documentation and logging (the digital "black box" that records what the app is doing). 

Include version numbers for every library. Without them, the agent might suggest an older version of a tool because its "knowledge cutoff"—the date its training data ended—was in the past. 

## 2. **Feature Generation (The Builder)** 

In this mode, features are implemented on top of an existing codebase. Prompt the agent to match the existing style, including naming patterns and how the code handles errors. When multiple files are being edited, changes should be manually confirmed. It is important to see the "Diff"—a list showing exactly what lines are being added or removed—inside the editor. 

## **Bug Fixing (The Forensic Specialist)** 

When things break, forensic mode is required. The goal is root cause analysis and a surgical repair. Shift from Symptom Prompting ("The button doesn't work") to Evidence Prompting ("Logs pulled using gcloud logging read 'textPayload:ERROR' --limit 5 showed a 403 error"). Use versioning on the command line (e.g. gh commands for Git) to compare versions of code. Then explain the flow: "Request hits Load Balancer -> Auth strips header -> Pod fails." 

## **Tip:** 

Sometimes the coding agent will suggest renaming variables. Renaming of variables is acceptable, but it should be done as a separate task rather than part of a bug fix to avoid complications. 

May 2026 

13 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

## **Tip:** 

Sometimes the coding agent will suggest lower versions of existing tools, libraries or models. This occurs because the underlying model was trained on a certain cutoff time. For example, it might suggest gemini-1.5-flash because no later version exists in the model's knowledge. This can be prevented by using RAG features in a coding editor to add the latest documentation, or by downloading documentation as markdown files within the spec folder. In agent skills or profile prompts, this information can also be added. Keep in mind that agents easily fall back to their training data, so proposed version numbers should always be double-checked. 

Always prompt for a failing unit test or a curl command (a way to send data to a URL) to reproduce the bug first. Keep this test case in the codebase to ensure the bug does not return. Set a strict constraint that the agent should only fix the root cause. Unrelated code should not be "cleaned up," as this complicates the review process. 

To elevate end-to-end (E2E) testing and troubleshooting, tools like Antigravity feature a built-in browser giving agents the ability to autonomously run localhost, interact with live user interfaces, and verify visual fixes in real time. Under the hood, Antigravity orchestrates a fully automated, native Chrome instance to execute, record, and verify these front-end tasks. Crucially, to prevent unauthorized actions and protect privacy, this subagent runs inside a completely isolated, sandbox-like Chrome profile. Because this profile does not share or access active browser logins or active personal sessions (acting essentially as a clean incognito environment), it prevents context leakage or accidental live operations while allowing the agent to rigorously test UX changes without compromised security. Debugging prompts can go far beyond static code analysis—the built-in browser can be given step-by-step instructions to point out exactly what goes wrong visually and define precisely what needs to be fixed on the screen. 

May 2026 

14 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

## 3. **Documentation Writing (The Author)** 

In SDD, the documentation is the source of truth. If the docs and the code aren't in sync, the AI will start to hallucinate. Specify in agent "skills" that instructions in a README.md or CHANGELOG.md must always be maintained. 

Use Google Style Docstrings for Python or JSDoc for TypeScript. These are structured ways of writing comments that help the AI (and humans) understand exactly what a function does without reading every line of logic. 

## 4. **Data Engineering (The Librarian)** 

When querying tables or moving files, the role is that of a data engineer. Use IDE extensions like the Google Cloud Data Extension [5] to access cloud data directly from the editor. Prompt the agent to always show the specific SQL query or command used to generate the output. 

## **MCP: One Integration, Every Framework** 

MCP was created by Anthropic and is now an open standard. People like to call it "the USB-C for AI tools" — a bit of a stretch, but the analogy captures the idea. You build one MCP server for your database (or API, or file system), and any MCP-compatible agent can use it without writing a custom integration. 

May 2026 

15 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

## **Building an MCP Server** 

Here's a working server in about 40 lines that exposes a SQLite database: 

## **Python** 

`# mcp_server.py — Exposes a SQLite database via MCP import sqlite3 from mcp.server import Server from mcp.server.stdio import stdio_server from mcp.types import Tool, TextContent server = Server("knowledge-base") db = sqlite3.connect("knowledge.db") @server.list_tools() async def list_tools() -> list[Tool]: return [ Tool( name="query_knowledge", description="Query the knowledge base with SQL", inputSchema={ "type": "object", "properties": { "sql": { "type": "string", "description": "SQL query to execute (SELECT only)" } }, "required": ["sql"] }, ), Tool( name="add_knowledge", description="Add a new knowledge entry", inputSchema={ "type": "object", "properties": { "title": {"type": "string"}, "content": {"type": "string"}, "tags": {"type": "string", "description":` **Continues next page..** 

May 2026 

16 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

```
"Comma-separated tags"}
                },
"required": ["title", "content"]
            },
        ),
    ]
@server.call_tool()
async def call_tool(name: tr, arguments: dict) -> list[TextContent]:
if name == "query_knowledge":
        sql = arguments["sql"]
if not sql.strip().upper().startswith("SELECT"):
return [TextContent(type="text", text="Error: Only SELECT
queries allowed")]
        cursor = db.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        result = [dict(zip(columns, row)) for row in rows]
return [TextContent(type="text", text=str(result))]
elif name == "add_knowledge":
        db.execute(
"INSERT INTO knowledge (title, content, tags) VALUES (?, ?, ?)",
            (arguments["title"], arguments["content"], arguments.get("tags", ""))
        )
        db.commit()
return [TextContent(type="text", text="Knowledge entry added.")]
async def main():
asyncwith stdio_server() as (read, write):
        init_options = server.create_initialization_options()
await server.run(read, write, init_options)
if __name__ == "__main__":
import asyncio
    asyncio.run(main())
```

Snippet 1: mcp_server.py: This snippet implements an MCP server using the Python SDK to expose a SQLite database as a set of tools. 

May 2026 

17 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

## **Connecting an MCP Client** 

## **Python** 

```
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
server_params = StdioServerParameters(
    command="python", args=["mcp_server.py"]
)
async with stdio_client(server_params) as (read, write):
async with ClientSession(read, write) as session:
await session.initialize()
# List available tools
        tools = await session.list_tools()
print(f"Available: {[t.name for t in tools.tools]}")
# Call a tool
        result = await session.call_tool(
"query_knowledge",
            {"sql": "SELECT * FROM knowledge WHERE tags LIKE '%agent%'"}
        )
print(result.content[0].text)
```

Snippet 2: mcp_client.py: This example demonstrates an MCP client connecting to a local server via stdio to discover and call tools. 

## **Team Culture & Process Evolution** 

Working with modern coding agents requires changes in thinking and team culture. Sticking to old processes while using modern tools is like trying to put a jet engine on a horse-drawn carriage; this technology cannot be bolted onto a 20-year-old workflow with the expectation that it will fly. Imagine an experience where a pull request (PR) could become enormous, 

May 2026 

18 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

and you consider breaking it down into smaller chunks. Merge conflicts suddenly multiply as developers land in the same files. It creates a dependency chain that's hard to untangle. PR #1 can't merge without PR #2, which needs PR #3, but PR #3 is blocked by a reviewer in a different timezone. Some changes got approved while related ones are waiting for review, spawning even more conflicts. Now you are suddenly stuck with a broken branch. Let's break these type of issues down in categories: 

- **Merge conflicts:** Multiple developers landing on the same file within the hour. 

- **Review gridlock:** A massive PR becomes a Russian-doll of sub-PRs. 

- **Context fragmentation:** While a developer is away, a teammate renames a variable in a shared file; an agent, quoting an outdated snapshot, mints code that calls a function that no longer exists. 

Let's look into a couple of lessons learned. 

## **Code Reviews** 

To survive the volume and scale of AI-generated commits without burnout, teams will need to explore new guidelines. While the ideal workflow is subject to debate, here are some ideas to help manage the shift from writing code to integrating it: 

## Strategies for High-Velocity Integration 

- **Bundled Summaries and Risk Assessments:** Consider requiring every PR to include an AI-generated snapshot of what changed, potential breakage points, and a risk assessment. This could be a markdown file or a detailed commit description that helps human reviewers focus on architectural impact rather than getting lost in the lines. 

May 2026 

19 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

- **Reimagined Ownership:** Shift the focus of human reviews from nitpicking style on disposable, agent-written code to ensuring the integrity of the architectural blueprints. Style concerns can be addressed through automated integration tools like shared syntax linters or workspace-specific stylebooks (e.g., SKILLS.md). 

- **The "Conditional LGTM":** To eliminate 12-hour delays in cross-timezone teams, you might institute a "Conditional LGTM" (Looks Good To Me). A reviewer approves the PR contingent on it passing all automated tests; if the tests turn green, the code merges automatically. 

- **Defining a No-Blame Culture:** In high-velocity environments, the person producing the most code often becomes a scapegoat for bugs or merge conflicts. It is helpful to discuss how to attribute these issues to broken integration processes rather than the individual developer using the agent. 

- **The Usage of Agent Coding Reviews:** You could build a skill which does the code review for you. And you can even write skills that respond to code reviews. See Code Snippet 5.1. You can automate this with Github Actions[6] or using Gemini Code Assist on Github[7] . 

Lastly, you could even wonder and discuss; if you can work with a squad of agents, do you even need to work as a team at all? But if you decide you do, you might explore ways to split work so that team members rarely touch the same files—for example, assigning clear ownership over APIs versus UX. When overlap is necessary, the designated "part owner" can handle the final synchronization. 

May 2026 

20 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

```
Act as a Senior Software Engineer and Security Researcher. Review the provided
code for this Github PR or Diff using these strict criteria:
```

```
Use the command line to fetch the Github PR:
```

```
`gh pr view <PR NUMBER>`
First analyze the code, then code review:
```

```
1. **Critical Vulnerabilities:** Check for hardcoded secrets (API keys), SQL
injection, XSS, or broken authentication.
```

```
2. **Logic & Efficiency:** Identify "off-by-one" errors, infinite loops, or
redundant API calls.
```

```
3. **Readability:** Suggest better naming conventions or breaking down "mega-
functions" into smaller pieces.
```

```
4. **Edge Cases:** What happens if the input is null? What if the network fails?
Output Format:
```

`- **Description:** - What is this PR doing? Explain in details. ISSUES: -` ⚠ `**Critical:** (Stop-ship issues) -` ⚠️ `**Warnings:** (Code smells or style issues) -` ✅ `**Best Practices:** (Specific lines to refactor for better performance) -` 💡 `**Quick Win:** (One sentence summary of the biggest improvement) When there are no issues return - **Description:** - What is this PR doing? Explain in details. LGTM` 

Snippet 3: code-check.md: This skill defines a structured workflow for automated code reviews against security and logic criteria. 

May 2026 

21 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

## **Deploying Agents That Watch Your Repo** 

You can write a great review prompt. But who runs it on every PR, every nightly sweep — without a human pushing the button? 

A code review skill runs when you invoke them from inside the IDE. The next step is to deploy them as continuous code analysis agents — services that watch the repository, react to events (PR opened, nightly cron), and post findings back without anyone asking. They catch what tired humans miss on a Friday afternoon: a dependency with a fresh CVE, a TODO from six months ago that quietly became a security gap. Once your team is shipping AI-generated PRs at volume, a continuous reviewer is the only thing that scales with the output. The question is how custom you need to go — and the answer is a spectrum with three tiers, each trading control for simplicity. 

## **The Spectrum** 

The three tiers differ in who owns the runtime and who writes the review criteria: 

- **Tier 1 — Managed (e.g. Gemini Code Assist on GitHub [8], or any SaaS PR reviewer)** . The off-the-shelf path. Enable it on your GitHub or GitLab org and every PR gets an AI reviewer that comments on style, bugs, and security out of the box. No prompts to write, no infrastructure to manage; pay per seat. The trade: you get the vendor's review opinions, not yours — a generic reviewer will miss what matters to a team with a strict house style or a domain-specific risk profile (HIPAA, PCI, internal SDKs). 

- **Tier 2 — Hybrid (e.g. a GitHub Action**[6] **triggering a coding agent CLI — Antigravity CLI**[12] **)** . The middle path, and the right starting point for most teams. Write your own review skill — the code-check.md from earlier in this paper is a working example — commit it 

May 2026 

22 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

to the repo, and trigger it from a CI action that runs the CLI of choice in non-interactive mode and posts the result as a PR comment. The runtime belongs to your CI provider; the prompts, model choice, sandboxing, and review criteria belong to you. 

- **Tier 3 — Custom (e.g. an ADK agent on Gemini Enterprise Agent Engine**[9] **)** . The fully owned path. For example you can set the reviewer as an ADK agent, deploy it to Agent Runtime for managed runtime with durable Sessions and Memory Bank, and wire it to webhook events from your source host. This is the right answer when the reviewer must hold context across a multi-PR refactor, decompose "audit this service for compliance drift" into a hundred sub-tasks via a planner-and-sub-agents pattern, or coordinate with other agents over A2A[10] . The trade: you own evaluation, observability, cost, and the on-call rotation when it fails in production. An example of such an architecture can be found in the Siemens case study[17] . 

Three questions tell you which tier you need: 

1. How specific is your review criteria? 

   - Generic → Tier 1. 

   - Team- or repo-specific → Tier 2 or 3. 

2. Does the agent need to remember things across runs? 

   - No → Tier 1 or 2. 

   - Yes (codebase memory, cross-PR context) → Tier 3. 

3. What is the worst case if it goes wrong? 

   - A noisy comment → any tier. 

   - A merged regression or leaked secret → Tier 3 with the Policy Server pattern from the previous section in front of every tool call. 

May 2026 

23 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

Most teams discover their tier the moment the managed reviewer misses something specific. A platform team at a mid-size fintech, for example, started on Tier 1 and quickly found their compliance reviewer flagging boilerplate that auditors had already signed off — while missing the one pattern that mattered, unmasked PII in log statements. A 40-line compliance-check. md skill wired to a GitHub Action (Tier 2) dropped the false-positive comments sharply within a week. Tier 3 has not yet been needed. 

## **Tier 3 at Full Scale: Graph-Native Code Understanding** 

Custom Code Review Runtime (Tier 3) stretches further than a single ADK agent reading diffs. The same architecture supports the heavier components a serious reviewer needs on a hundred-million-line legacy codebase — a graph database holding the code's structure, a vector store for semantic retrieval, a sub-agent pipeline for decomposition. Loading code as flat text into a context window runs out of room at that scale, and standard RAG strips out the structure that makes code legible: a class belongs to a file, a function call traces to a requirements doc written a decade ago. Flatten that into a vector store and the map is gone. 

Figure 1: Example of a Custom Code Review Runtime Architecture 

The pattern that has emerged on the largest legacy modernisations is to build the agent on a knowledge graph. Ingest code, docs, tickets, and design PDFs into a graph database (e.g. Spanner Graph[11] ), then let agents combine three retrieval modes: graph traversal (GQL) for structural queries ("every function that transitively calls payment.process()"), vector search 

May 2026 

24 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

(ANN over node embeddings) for semantic queries ("find code that does what this paragraph describes"), and full-text search for exact identifier matches. The combination answers "what breaks if I change this?" with a precise impact map instead of a confident guess. 

The second half is decomposition. A single agent told to "refactor this module" will fail. Split the same job across an ADK[12] sub-agent pipeline — a Search agent that explores the graph, a Story agent that captures requirements, an Impact agent that predicts side-effects, a Taskbreakdown agent that produces atomic units of work, and only then a Coding agent — and the work becomes manageable. Pilots in production on million-line codebases have moved equivalent refactor work from two weeks to a few hours. This is Tier 3 at full scale: not an agent that watches PRs, but one that understands the system the PRs live in. 

A Managed Code Review Runtime (Tier 1) gets you a generic reviewer in minutes. A Hybrid Code Review Runtime gets you your reviewer in a day, where the Custom Code Review Runtime (Tier 3) gets you a reviewer that understands the whole system — at the cost of owning the runtime, and the evaluation. Pick the lowest tier that catches what matters. 

## **Sustainability** 

We're seeing a new phenomenon: approval fatigue. According to Quantum Workplace research reported by CNBC, frequent AI users are 45% more likely to experience high burnout than non-users [14]. When faced with a constant stream of micro-approvals (improving a single line, adjusting a tool call) developers start clicking "Approve" reflexively. It's a form of low-grade exhaustion where the team stops checking the machine's work just to keep up with its pace, and you risk it that developers are missing the attention to the details. 

May 2026 

25 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

To protect the team, you can move from constant oversight to structured boundaries: 

- **Digital Quiet Hours:** Set boundaries so approval requests do not bleed into evenings and weekends. 

- **Agent Insight Sessions:** Hold weekly sessions where developers share patterns identified by their AI counterparts, turning isolated discoveries into shared organizational knowledge. 

## **Zero-Trust Development: Building the Safety Net** 

The focus thus far has been on the review and team culture side. But there's another lesson regarding what happens when an agent acts without sufficient guardrails. 

During a routine code update, the power and limits of Antigravity's built-in UI browser were discovered. This feature allows the AI agent to interact with applications under development without requiring login credentials, making it invaluable for UX testing. However, in YOLO (auto approve) mode, it can act faster than a human can think. 

A simple prompt to create a button triggered an unexpected chain reaction. The browser agent autonomously clicked the new button, which was intended for an email agent. Without a specified URL, the agent hallucinated by connecting to a deprecated legacy agent with no email safeguards. The result? Fifty colleagues received false emails filled with hallucinated content. 

This incident highlighted context _hallucination risk_ : when AI lacks sufficient data, it sometimes fills gaps using whatever strings exist in its context, including sensitive information like hardcoded email addresses or URLs. This may seem minor if it is just an email. However, 

May 2026 

26 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

consider what the agent was doing: fulfilling its directive with the data available to it, without any check on whether it should. That is the core risk with autonomous systems. Without a human-in-the-loop or a policy engine, the agent optimizes for its goal using whatever it can find. Guardrails are not optional; they are what keep a useful tool from becoming an unpredictable one. 

## **Implementing Guardrails** 

As the boundaries of Agentic AI are pushed, a paradox is encountered: agents should be autonomous enough to solve complex problems, but the risk of them going rogue in an enterprise environment cannot be afforded. 

As the boundaries of Agentic AI are pushed, a paradox is encountered: agents should be autonomous enough to solve complex problems, but the risk of them going rogue in an enterprise environment cannot be afforded. 

Imagine an agent tasked with "resolving customer disputes." To be effective, it needs access to customer data, email tools, and internal systems. But the challenge is ensuring it doesn't accidentally email the entire database or share proprietary code. 

Autonomous agents are driven by LLMs that are probabilistic, not deterministic. Hard-coding constraints into a system prompt is brittle, contexts overflow, and agents can be "convinced" to bypass rules via prompt injection. To build production-grade platforms, external, tamperproof governance is required. You can read more about securing and evaluating agents against malicious code, in the day 4 paper: **Vibe Coding Agent Security and Evaluation** . 

May 2026 

27 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

## **Sandboxing** 

Beyond sanitizing strings, true security requires a restricted execution environment, or "Sandbox," to contain an agent’s actions. Even with rigorous output filtering, an LLM might generate syntactically valid but logically malicious code that could compromise a host system. By executing agent-driven tasks within ephemeral, low-privilege containers isolated from the primary network and sensitive file systems, a "blast radius" is created that protects the core infrastructure. In this model, if an agent is tricked into executing a destructive command, the damage is confined to a disposable instance that can be wiped and reset without consequence. 

Within Antigravity this safety net can be enforced with a single toggle. Navigate to User Settings and enable "Terminal Sandboxing"[15] . Alternatively, if a portable, cloud-based sandbox for a team is required, the agent's workspace can be containerized. By writing a custom Dockerfile (e.g., in .gemini/sandbox.Dockerfile) that starts from the official Gemini CLI sandbox[16] image, limited cloud credentials can be injected, and the CLI tool can be forced `GEMINI_SANDBOX=docker` in the terminal. In both to run entirely in Docker by setting export models, if the agent is tricked into a malicious execution, it will hit a hard permission error at the kernel level, keeping the host system completely untouched. 

## **Human-in-the-Loop** 

While automation is the goal, high-stakes operations require a Human-in-the-Loop (HITL) protocol to serve as the ultimate fail-safe. This involves implementing "checkpoint" gates for actions that meet a specific risk profile, such as deploying code to production, modifying database schemas, or initiating financial transactions. By presenting an agent’s sanitized 

May 2026 

28 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

intent to a human supervisor for manual sign-off, the speed of AI is balanced with the nuanced judgment of a developer. This ensures that while the agent does the heavy lifting, final responsibility for architectural integrity remains firmly in human hands. 

## **AI Generated Test Coverage** 

The surge in AI-generated code creates a shift from manual testing to AI-generated test coverage to maintain a reliable safety net. In a high-velocity environment, "test-driven development" becomes a reality by tasking the machine with writing the very tests that validate its own output. 

This process involves forcing the agent to produce a failing unit test or a reproduction command, such as a curl request, before attempting any fix. By embedding these automated tests into the codebase, every rapid iteration is backed by a verifiable suite of checks, preventing bugs from returning and allowing human reviewers to trust the automated green light for integration. 

## **Evaluation** 

Why do we need a special quality check for code that uses ML models? Traditional software tests are insufficient for systems whose output is _generated_ rather than _computed_ . An agent — or any ML-driven component like a classifier, summariser, or retriever — can pass 100 unit tests on its tools and still fail spectacularly by choosing the wrong tool, paraphrasing a critical answer, or hallucinating a fact. The error margin isn't a defect to eliminate; it's an inherent property of the model, and the testing strategy has to accommodate it. 

May 2026 

29 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

Evaluation closes this gap by replacing binary assertions with **scored** judgments and **tolerance bands** . A unit test asks "did the function return the right value?" — a binary answer. An evaluation asks "is the agent's behaviour at least as good as the baseline?" — a 0–5 score from an LLM-as-judge, a trajectory check that tolerates ordering variance in tool calls, a gate that fires when quality drops below a configurable margin rather than when an assertion flips. **Tests catch deterministic regressions; evaluation catches** . **behavioural drift** 

## **Policy Server** 

Here's an example Hybrid Policy Server that intercepts actions before they hit external systems. It operates on two layers: 

- Deterministic rules based on roles and 

- **Structural Gating (The Traffic Lights):** environments. These are fast, binary checks (e.g., a viewer role cannot use the send_email tool). This layer prevents architectural violations without needing to ask an LLM.s 

- **Semantic Gating (The Intelligent Referee):** This uses a secondary, specialized LLM (like Gemini) to inspect the intent and content of a proposed action against natural language privacy guidelines. This addresses the need for when a tool is allowed, but the way it is used violates a policy. For example, an admin can use send_email, but they should not send unmasked PII (like plain-text email addresses or API keys). This is where structural rules fail. You cannot regex every possible PII leak. 

May 2026 

30 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

These rules are defined in a standard policies.yaml: 

```
environments:
  localhost:
    blocked_tools:
      - send_email
roles:
  viewer:
    allowed_tools:
      - list_files
      - read_file
```

Snippet 4: policies.yaml: This configuration establishes deterministic gating rules for tool-level permissions based on role and environment. 

Below is a lightweight implementation of a Policy Server designed to intercept tool calls and verify permissions at runtime. 

## **Python** 

`import os, yaml from google.genai import Client class PolicyService: def is_tool_allowed(self, tool_name: str) -> bool: # Check Environment Blocks env_config = self.config.get("environments", {}).get(self.env, {}) if tool_name in env_config.get("blocked_tools", []): return False # Check Role Permissions role_allows = self.config.get("roles", {}).get(self.role, {}). get("allowed_tools", []) return "*" in role_allows or tool_name in role_allows async def check_action_semantic(self, action_description: str) -> bool: client = Client(vertexai=True, project=self.project_id, location=self.location)` **Continues next page...** 

May 2026 

31 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

```
        prompt = f"Evaluate if this action violates PII
policies: {action_description}"
        response =
client.models.generate_content(model="gemini-3.1-pro", contents=prompt)
return not response.text.strip().upper().startswith("VIOLATION")
```

Snippet 5: policy_server.py: This service implements a hybrid policy engine to intercept actions and perform structural and semantic evaluations. 

The code listing works as follows: When the agent decides to use a tool, the execution flow is intercepted: 

**1. Structural Check:** Is the tool allowed for this role/env? (Check YAML). 

**2. Semantic Check:** Are the arguments safe? (Ask Gemini). See the prompt in the code snippet. Unmasked email addresses are considered a violation. 

**3. Execution:** If both pass, the tool runs. Otherwise, a "Policy Violation" message is returned to the agent, allowing it to self-correct or fail gracefully. 

This creates a safety net that separates execution logic from governance logic—a critical separation of concerns for enterprise software. 

## **Context Hygiene & Prompt Sanitization** 

A significant danger in autonomous development is the "Context Hallucination" risk. When an agent lacks specific data, it may fill gaps using any available strings in its current context, potentially leaking sensitive information like hardcoded email addresses or private URLs. 

May 2026 

32 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

To mitigate this, implement rigorous Context Hygiene through middleware that performs PII masking and placeholder injection. By replacing personally identifiable information with generic placeholders in templates, ensure that the agent operates on sterilized data. 

Furthermore, all agent outputs must be sanitized to prevent prompt injection and rogue UI interactions, ensuring that the machine's "vibe" never translates into an architectural vulnerability. 

## **Implementing a Dynamic ContextResolver** 

This security pattern is achieved by implementing a lightweight regex-based translation utility inside the application's core codebase. Below is a practical implementation of this design: 

This script acts as the core translation engine, replacing placeholder strings structured with double-bracket syntax [[VARIABLE_NAME]] with runtime overrides or environment configurations: 

May 2026 

33 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

## **Python** 

```
import os
import re
from typing import Optional, Dict, Any
def resolve_context(template_str: str, override_state: Optional[Dict[str, Any]] =
None) -> str:
"""Scans a template string for [[VARIABLE_NAME]] and replaces it with
    values from override_state or os.environ.
    """
if template_str is None:
return ""
    state_to_check = override_state or {}
def replacement(match):
        var_name = match.group(1).strip()
        # 1. Prioritize runtime state overrides
if var_name in state_to_check and state_to_check[var_name] is not None:
return str(state_to_check[var_name])
        # 2. Fallback to validated environment variables
elif var_name in os.environ and os.environ[var_name] is not None:
return os.environ[var_name]
        # 3. Leave unresolved to prevent silent failures
else:
return match.group(0)
   # Resolve all bracketed variables dynamically, e.g., [[COMMENTER_EMAIL]]
return re.sub(r'\[\[([^\]]+)\]\]', replacement, template_str)
```

Snippet 6: context_resolver.py: This utility resolves bracketed placeholders with environment variables to maintain context hygiene. 

May 2026 

34 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

To enforce context hygiene globally, the sanitization utility must be wired directly into your agent's execution pipeline as a validation step. By intercepting incoming tool calls before they run, you ensure all prompt-injected strings are sterilized dynamically: 

## **Python** 

```
# ... inside the validate_tool_call framework execution ...
resolved_args = {}
for k, v in args.items():
ifisinstance(v, str):
        resolved_args[k] = resolve_context(v)
elifisinstance(v, list):
        resolved_args[k] = [resolve_context(i) ifisinstance(i, str) else i for i
in v]
else:
        resolved_args[k] = v
args.clear()
args.update(resolved_args)
```

Snippet 7: tool_policy_engine.py: This middleware integrates the context resolver into the agent pipeline to sanitize tool arguments before execution. 

By enforcing this boundary, any attempt by an agent to execute an action (such as sending an email or querying a cloud presentation) is intercepted. The engine translates generic placeholders like [[COMMENTER_EMAIL]] or [[DEFAULT_PRESENTATION_ID]] into authorized test assets safely and silently, eliminating the need to ever hardcode sensitive PII in test suites or system prompts. 

May 2026 

35 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

## **Summary** 

In less than a year, software development cycles have become dramatically faster. Watching an agent produce a thousand lines of well-documented code by lunchtime is a significant advancement. 

But that speed revealed an important shift. AI has eliminated the code production bottleneck, moving the constraint downstream to humans who must review, test, and integrate that output. This is a shared cognitive load: humans act as architects  writing Test Specs, Integration Specs, and MLOps/DevOps blueprints, while the AI handles the heavy lifting writing actual test code, performing integrations, and managing granular operational details. 

Better prompts and faster models alone won’t fix the integration bottleneck. Success relies on evolving team dynamics, refining collaboration with agents, and setting strict boundaries for tools that never sleep. The challenge has shifted from mere code production to orchestrating systems that verify, integrate, and deploy work. 

## **Where to start** 

For teams operationalizing these patterns on agent codebases, `uv google-agents-cli` setup installs the seven skills into your coding agent — covering scaffolding, ADK code, evaluation, deployment, publishing, and observability. The patterns described in this paper become commands you can run today: `agents-cli scaffold` for spec-driven project generation, `agents-cli eval run` for the AI-generated test coverage gate, and `agentscli deploy` for sandboxed deployment to Cloud Run or Vertex AI Agent Engine. 

May 2026 

36 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

## **Endnotes** 

1. Google, 2026, Antigravity, agentic development platform, Available at: htps://antigravity.google 

2. Google for Developers, 2025, Gemini CLI, Query and edit large codebases, generate apps from images or PDFs, and automate complex workflows—all from your terminal with Gemini 3. Available at: htps://geminicli.com 

3. Ouyang Y., et al., 2026, SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents, Available at: htps://arxiv.org/abs/2605.03353 

4. Cucumber Open Source Project, 2026, Gherkin Syntax Reference, Available at: htps://cucumber.io/docs/gherkin/reference 

5. Google Cloud, 2026, Data Agent Kit extension for VS Code overview, Available at: htps://docs.cloud.google.com/data-cloud-extension/vs-code/overview 

6. Github, 2026, Quickstart for GitHub Actions, Available at: htps://docs.github.com/en/actions/get-stared/quickstar 

7. Google, 2026, Set up Gemini Code Assist on GitHub, Available at: htps://developers.google.com/gemini-code-assist/docs/set-up-code-assist-github#consumer 

8. Github, 2026, Gemini Code Assist on Github Marketplace, Available at: htps://github.com/marketplace/gemini-code-assist 

9. Google, 2026, Antigravity CLI Overview, Available at: htps://antigravity.google/docs/cli-overview 

10. Google Cloud, 2025, Agent Engine Overview, Available at: htps://cloud.google.com/verex-ai/generative-ai/docs/agent-engine/overview 

11. The Linux Foundation, 2025, Agent 2 Agent (A2A) Protocol, Available at: htps://a2a-protocol.org/latest/ 

12. Google Cloud, 2025, Spanner Graph Documentation, Available at: htps://cloud.google.com/spanner/docs/graph 

13. Google ADK, Build powerful malti-agent systems with the Agent Development Kit Documentation, Available at: htps://google.github.io/adk-docs/ 

14. CNBC, 2025, Working smarter, not harder: AI could help fight burnout — but is it?, Available at: htps://www.cnbc.com/2025/09/20/working-smarer-not-harder-how-ai-could-help-fght-burnout-.html 

May 2026 

37 

Spec-Driven Production Grade Development in the Age of Vibe Coding 

15. Google, 2026, Sandboxing Terminal Commands, Available at: htps://antigravity.google/docs/sandbox-mode 

16. Google, 2026, Sandboxing in Gemini CLI, Available at: htps://geminicli.com/docs/cli/sandbox 

17. Google Cloud, 2026, How Siemens "slices the elephant," advancing agentic workflows for industrial software development, Available at: htps://cloud.google.com/blog/products/ai-machine-learning/how-siemens-sliced-the-elephantmodernizing-legacy-code-with-agentic-workfows/?e=48754805 

May 2026 

38 

