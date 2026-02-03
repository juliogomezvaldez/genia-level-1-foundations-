# Level 1 Mock Interviews — Single-Agent Claim Verifier

## Interview 1 — Prompting and Verification Logic
- Walk me through your end-to-end agent flow. Why is it structured this way?
- How do you prevent the model from hallucinating evidence?
- Show me a case where your extraction fails. What would you change?
- What would you do if the tool call returns no results?
- Trade-off: deterministic output vs. model creativity. How did you choose?

## Interview 2 — Tooling and Reliability
- Your lookup tool is mocked. How would you harden it for real usage?
- How do you handle timeouts and retries without duplicating work?
- What is the smallest change that would make this system unsafe or unreliable?
- If the model returns malformed JSON, what happens next?
- Trade-off: strict schemas vs. speed of development. Defend your choice.

## Interview 3 — Practical Deployment Considerations
- What parameters do you log for reproducibility?
- Suppose you need to run this on 10,000 claims. What breaks first?
- How would you test the quality of the model’s reasoning without ground truth?
- What are the top two risks in production for this agent?
- Trade-off: higher cost model vs. weaker reasoning. How do you decide?
