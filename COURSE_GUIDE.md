# COURSE GUIDE – Fact-Checking Auditor (Single-Agent)

This guide maps the 4 weeks of the level to concrete implementation milestones.

## Week 1
- Implement `schemas.py` (input/output contracts)
- Create initial prompts in `prompts.py`
- Add a golden set in `data/` and a tiny test runner

## Week 2
- Implement `tools/search_tool.py` with timeouts + retries
- Add `src/main.py` to run the pipeline end-to-end

## Week 3
- Add robust parsing (atomic claims/tasks)
- Add Markdown report formatting
- Add unit tests for critical components


## Week 4 (Capstone)
- Validate against the golden set and improve failure modes
- Run peer reviews using `/reviews` templates
- Finalize README + SPEC + sample outputs
