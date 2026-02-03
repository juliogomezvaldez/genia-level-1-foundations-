# Fact-Checking Auditor (Single-Agent)
## Overview
Domain: verification of factual claims (starter)

**Key Techniques:** Prompt engineering, single-agent reasoning, one tool (search/lookup)

This repository follows a simple, reproducible structure:
- **README.md** – what it is and how to run it
- **COURSE_GUIDE.md** – week-by-week implementation guide
- **SPEC.md** – requirements + architecture
- **agentic-ai-syllabus.md** – 4-week plan for this level
- **/reviews** – peer review templates

---

## Features
- Claim/task extraction
- Evidence retrieval (tool or RAG depending on level)
- Structured outputs (JSON) + Markdown report
- Basic failure handling (timeouts, retries)

## Installation
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Quickstart
```bash
python src/main.py --input data/sample_input.txt --output out/report.md
```

## Project structure
```
.
├── COURSE_GUIDE.md
├── README.md
├── SPEC.md
├── agentic-ai-syllabus.md
├── requirements.txt
├── data/
│   └── sample_input.txt
├── out/            # generated reports
├── reviews/
│   ├── peer_review.md
│   └── mock_interview_review_template.md
└── src/
    ├── main.py
    ├── prompts.py
    ├── schemas.py
    └── tools/
        └── search_tool.py
```
