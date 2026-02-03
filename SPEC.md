# Project SPEC – Fact-Checking Auditor (Single-Agent)

**Level focus:** Foundations & Single-Agent Systems

## 1) Problem statement
Build an agentic system that resolves knowledge-heavy requests by:
- extracting atomic claims/tasks,
- retrieving supporting evidence,
- generating a structured, transparent response,
- refusing when evidence is insufficient.

## 2) Functional requirements
- **FR1 Input:** text request (ticket/email/doc excerpt) or list of claims.
- **FR2 Extraction:** split into atomic claims/tasks.
- **FR3 Retrieval:** fetch evidence via tool or RAG.
- **FR4 Verification/Decision:** classify each claim as Supported / Not Supported / Unclear.
- **FR5 Output:** structured report (JSON + Markdown view) with citations.
- **FR6 Logging:** capture prompts, tool calls, and decisions (traces in Level 3).

## 3) Non-functional requirements
- **Groundedness:** do not assert unverifiable facts as true.
- **Latency:** degrade gracefully; timeouts + partial results.
- **Cost control:** token budgets; caching where appropriate.
- **Security:** redact sensitive inputs in logs.
- **Maintainability:** modular design + tests.

## 4) Architecture
### Agents
- **ClaimVerifierAgent (single agent):** extracts claims, calls a search tool, produces verdicts.


### Orchestration
- **Orchestration:** linear pipeline (extract → search → compare → report).


### Memory
- **Memory:** none (optional session context only).


### Tools
- **Tools:** `SearchTool` (web search or local KB lookup).


## 5) Scope
**In scope:** LLM prompting, agents, tools, memory/RAG (as level), evaluation/guardrails (as level).  
**Out of scope:** traditional ML training, CV, classic NLP, generic data engineering.
