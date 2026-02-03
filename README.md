# Fact-Checking Auditor (Single-Agent)

## Overview
A lightweight, reproducible starter project for verifying factual claims with a single agent and a single search/lookup tool. This repo is part of the Agentic AI Level 1 foundations track.

**Key techniques:** Prompt engineering, structured reasoning, tool use (search/lookup)

## Features
- Claim/task extraction
- Evidence retrieval (tool or RAG depending on level)
- Structured outputs (JSON) + Markdown report
- Basic failure handling (timeouts, retries)

## Requirements
- Python 3.10+

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

## How It Works (High Level)
1. Parse the input file to extract claims/tasks.
2. Retrieve evidence using the search tool.
3. Produce a structured JSON verdict and a human‑readable Markdown report.

## Project Structure
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

## Course Materials
- `COURSE_GUIDE.md`: Week‑by‑week implementation guide
- `SPEC.md`: Requirements + architecture
- `agentic-ai-syllabus.md`: 4‑week plan for this level
- `reviews/`: Peer review templates

## Roadmap (Suggested)
- Add caching for search results
- Improve evidence scoring and ranking
- Expand to multi‑agent verification

## License
Add your license here.
