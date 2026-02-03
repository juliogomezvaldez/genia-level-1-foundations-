# Level 2 Mock Interviews — Multi-Agent RAG Verifier

## Interview 1 — Multi-Agent Design
- Why did you choose these agent roles, and what do they own?
- Show me an example where the Retriever and Verifier disagree. What happens?
- How do you avoid compounding errors across agents?
- What would you change if latency doubled?
- Trade-off: more agents vs. clearer responsibilities. Defend your decision.

## Interview 2 — RAG and Evidence Quality
- How do you decide what to retrieve for a claim?
- What happens if your top-k retrieval is wrong?
- How do you prevent the Verifier from ignoring evidence?
- What metrics would you track for RAG quality?
- Trade-off: precision vs. recall in retrieval. Which matters more here?

## Interview 3 — Reliability and Governance
- Where do you add responsible AI checks in the flow?
- What risks exist when agents cite sources incorrectly?
- If a client wants deterministic answers, how do you adapt?
- What would you log for later audits?
- Trade-off: strict guardrails vs. user flexibility. Which do you prefer and why?
