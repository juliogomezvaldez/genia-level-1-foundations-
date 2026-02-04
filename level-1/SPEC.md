# Level 1 SPEC — Single-Agent Claim Verifier

## Problem Definition
Financial teams (audit, compliance, and risk) continuously consume statements from reports, press releases, analyst notes, and internal summaries. Many of these statements are factual claims, often numerical, such as revenue growth percentages, headcount changes, dates, or regulatory assertions.

Today, verifying these claims is manual, slow, inconsistent, and error-prone—especially when multiple sources disagree, claims are underspecified, or evidence is fragmented across documents.

This project builds a Fact-Checking Auditor: a focused single-agent system that ingests a batch of factual claims, retrieves supporting or contradicting evidence from trusted sources (real or simulated), and produces a concise audit report. Each claim is classified as Verified, Unverified, or False, including citations and a confidence score.

The primary goal is not absolute truth, but reproducible and evidence-grounded verification behavior with explicit failure modes such as insufficient evidence, ambiguous claims, or tool timeouts.

## Claim Data Generation (Required)

To enable deterministic testing and reproducible end-to-end execution, the system must include a claim data generator that produces structured input data for the agent.

### Requirements
- Generate synthetic datasets of factual claims (e.g., 10–50 claims) including:
  - Mixed outcomes: verified, false, and unverifiable claims.
  - Multiple claim types:
    - Numeric (revenue, margins, growth percentages).
    - Categorical (CEO name, company attributes).
    - Temporal (year, quarter).
    - Comparative (e.g., “higher than last year”).
  - Controlled difficulty:
    - Simple claims with direct evidence matches.
    - Tricky claims involving missing context, unit mismatches, or ambiguous periods.

- Output formats:
  - `claims.json` as the canonical structured input.
  - Optional `claims.txt` generated from the JSON for human readability.

- Provide a matching evidence corpus:
  - `evidence.json` or a local document set containing evidence snippets and source metadata.

- Support a `seed` parameter to ensure deterministic and reproducible dataset generation.

### Rationale

This approach enables reproducible demos, automated evaluation against known ground truth, and a clear separation between LLM reasoning quality and evidence or tool quality.
## Example Claim and Evidence Schema (Reference)

### Claim Object
- `id`: Unique identifier.
- `text`: Natural language claim.
- `entities`: Structured fields (company, metric, period, value, unit).
- `expected_label`: verified | false | unverified (evaluation only).

### Evidence Object
- `claim_id`: Associated claim ID.
- `sources`: List of evidence snippets with title, publisher, date, snippet, and URL.


## Functional Requirements

FR-1. The system shall ingest a structured input file (`claims.json`) containing a batch of factual claims.

FR-2. The system shall extract and normalize each claim into a structured internal representation (e.g., claim ID, text, entities).

FR-3. The system shall include a claim data generator capable of producing synthetic claim datasets with deterministic behavior using a configurable seed.

FR-4. The system shall support multiple claim types, including numeric, categorical, temporal, and comparative claims.

FR-5. For each claim, the system shall retrieve supporting or contradicting evidence using a search or retrieval tool (real or simulated).

FR-6. The system shall evaluate each claim against the retrieved evidence and classify it as `verified`, `false`, or `unverified`.

FR-7. The system shall produce a structured output file (`results.json`) containing the classification, evidence citations, and a confidence score for each claim.

FR-8. The system shall generate a human-readable audit report (`audit_report.md`) summarizing the verification results and rationale per claim.

FR-9. The system shall explicitly handle failure cases, including missing evidence, ambiguous claims, and tool execution errors.

FR-10. The system shall operate as a single-agent system with deterministic inputs and reproducible outputs.


## Non-Functional Requirements

NFR-1. Determinism  
Given the same input files, configuration, and random seed, the system shall produce identical outputs across executions.

NFR-2. Reproducibility  
All datasets (claims and evidence) shall be locally generated or stored to allow fully offline and reproducible runs.

NFR-3. Explainability  
For each claim classification, the system shall provide an explicit rationale referencing the supporting or contradicting evidence.

NFR-4. Failure Transparency  
When a claim cannot be verified, the system shall clearly indicate whether the cause is insufficient evidence, ambiguity, or tool failure.

NFR-5. Simplicity  
The system shall remain easy to understand, configure, and run locally by a single developer.

NFR-6. Performance  
The system shall be able to process small batches of claims (≤50) within a reasonable execution time on a local machine.

NFR-7. Extensibility  
The design shall allow future extensions such as RAG, multi-agent workflows, or additional tools without major refactoring.

NFR-8. Observability (Basic)  
The system shall log key steps of execution, including claim ingestion, evidence retrieval, classification decisions, and errors.


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
