# Level 3 Mock Interviews — Production-Grade Agentic Auditor

## Interview 1 — Production Architecture
- Describe your agent roles and why each is necessary.
- What happens if the Retriever fails or returns conflicting evidence?
- How do you choose the supervisor routing logic?
- If you had to cut latency by 50%, what would you remove first?
- Trade-off: more agents vs. simpler orchestration. Argue your position.

## Interview 2 — Observability and Reliability
- What logs, traces, and metrics do you capture at each step?
- How do you detect silent failures or degraded reasoning quality?
- What’s your strategy for sampling and alerting at scale?
- Suppose your evaluation harness flags 30% regressions overnight. What do you do?
- Trade-off: richer telemetry vs. privacy and cost. How do you balance?

## Interview 3 — Guardrails and Governance
- Where do guardrails live in the flow, and why there?
- How do you handle conflicting responsible AI requirements?
- What would you do if a high-confidence output is later shown to be wrong?
- How do you ensure auditability for regulators or compliance teams?
- Trade-off: strict guardrails vs. user autonomy. Defend your choice.
