# Level 1 SPEC — Single-Agent Claim Verifier

## Problem Statement
Build a single-agent system that reads a short input file with factual claims about a product and produces a concise, evidence-oriented verification report. The system should be easy to understand, reproducible, and focused on prompt engineering plus basic tool usage.

## Functional Requirements
- Ingest a plain-text file containing multiple claims.
- Extract claims into a structured list.
- For each claim, generate a brief verification attempt with a confidence rating.
- Output a JSON file and a Markdown report.
- Support a simple search/lookup tool interface (can be mocked).

## Non-Functional Requirements
- Deterministic output format (stable JSON schema).
- Clear error handling for empty inputs or timeouts.
- Reproducible runs with explicit parameters.
- Easy to run locally with Python 3.10+.

## Architecture
Agents:
- Single verifier agent that performs claim extraction, evidence lookup, and verdict generation.

Orchestration:
- Linear single-agent workflow with explicit steps.

Memory:
- Stateless (no long-term memory). Use prompt context only.

Tools:
- One lookup tool abstraction for evidence retrieval (can be a stub).

## In Scope
- Prompt engineering for extraction and verification.
- Structured outputs (JSON + Markdown).
- Basic tool call integration.

## Out of Scope
- Multi-agent coordination.
- Long-term memory or vector databases.
- Full production observability.
- Complex RAG pipelines.
