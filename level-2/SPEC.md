# Level 2 SPEC — Multi-Agent RAG Claim Verifier

## 1. Problem Statement

In Level 1, claims were verified using a single agent and a small, local evidence set. While effective for simple scenarios, this approach does not scale when:

- The number of claims increases.
- Evidence is spread across many documents.
- Different reasoning steps require different skills (retrieval vs. verification).
- Knowledge must be searched rather than hardcoded.

In real-world systems, claim verification is not a single-step task. It requires:
- searching across document collections,
- selecting relevant evidence,
- reasoning over retrieved context,
- and coordinating multiple responsibilities.

This project builds a **Multi-Agent Claim Verification System** that verifies factual claims against a **curated document corpus** using **Retrieval-Augmented Generation (RAG)**.

The system must demonstrate:
- collaboration between **specialized agents**,
- grounding of LLM reasoning in **retrieved external knowledge**,
- and the use of a simple **orchestration layer** to coordinate agents.

The core problem (claim verification) remains the same as Level 1; the focus is on increasing architectural realism and technical depth.

---

## 2. Student-Generated Inputs (Required)

To keep the project self-contained, reproducible, and easy to evaluate, **all inputs must be generated locally by the student**.

### 2.1 Claims Dataset

The student must generate a synthetic dataset of factual claims.

**Requirements**
- 10–30 claims.
- Mixed outcomes:
  - Verifiable claims.
  - False claims.
  - Unverifiable claims.
- Claim types:
  - Numeric (e.g., revenue, growth percentage).
  - Temporal (year, quarter).
  - Categorical (CEO name, product launch).
  - Comparative (e.g., “higher than last year”).

**Output**
- `claims.json` (canonical input file).

**Example fields**
- `id`
- `text`
- `entities`
- `expected_label` *(for evaluation only; not shown to agents at runtime)*

---

### 2.2 Document Corpus

The student must generate a **curated document set** that will be used for retrieval.

**Requirements**
- 5–20 documents.
- Each document should:
  - Contain factual information relevant to some claims.
  - Include basic metadata (title, source, date).
- The corpus should include:
  - Documents that support some claims.
  - Documents that contradict some claims.
  - Missing coverage for some claims (to force `unverified` outcomes).

**Output**
- A `/documents/` directory containing text or Markdown files  
  **or**
- A single `documents.json` file with document text and metadata.

---

### 2.3 Retrieval Index

From the document corpus, the system must:
- Build a **retrieval index** (vector-based or keyword-based).
- Use this index during execution to ground agent reasoning.

The index must be:
- Generated locally.
- Rebuilt deterministically when configuration is unchanged.

---

## 3. Functional Requirements

FR-1. The system shall ingest a student-generated `claims.json` file.

FR-2. The system shall ingest and index a student-generated document corpus.

FR-3. The system shall use **at least two specialized agents** with distinct responsibilities.

FR-4. The system shall retrieve relevant documents for each claim using a RAG-based approach.

FR-5. The system shall explicitly pass retrieved context between agents.

FR-6. The system shall evaluate each claim using retrieved evidence.

FR-7. The system shall classify each claim as `verified`, `false`, or `unverified`.

FR-8. The system shall cite specific documents used as evidence.

FR-9. The system shall produce:
- `results.json` with structured verdicts.
- `report.md` with human-readable explanations.

FR-10. The system shall use an explicit orchestration layer to coordinate agent execution.

---

## 4. Non-Functional Requirements

NFR-1. **Clear Agent Contracts**  
Each agent must have clearly defined inputs and outputs.

NFR-2. **Deterministic Output Schema**  
Given the same inputs and configuration, the output structure must remain stable.

NFR-3. **Traceability**  
Each verdict must be traceable to retrieved documents.

NFR-4. **Reproducibility**  
The system shall run end-to-end using only locally generated files.

NFR-5. **Simplicity Over Scale**  
The focus is correctness and clarity, not performance or scalability.

---

## 5. Architecture

### Agents

- **Retriever Agent**
  - Receives a claim.
  - Queries the retrieval index.
  - Returns ranked evidence snippets.

- **Verifier Agent**
  - Receives the claim and retrieved context.
  - Reasons over evidence.
  - Produces a verdict and rationale.

- **Optional Summarizer Agent**
  - Formats final explanations and reports.

---

### Orchestration

- A lightweight router coordinates:
  - agent execution order,
  - retries on retrieval failure,
  - context handoff between agents.

---

### Memory

- **Short-term memory**
  - Shared context within a single execution.
- **Long-term memory**
  - Retrieval index built from the document corpus.

---

### Tools

- Retrieval tool (vector or keyword search).
- Optional metadata filtering tool (e.g., date, source).

---

## 6. In Scope

- Multi-agent collaboration patterns.
- RAG-based evidence retrieval.
- Explicit agent roles and orchestration.
- Traceable reasoning grounded in documents.

---

## 7. Out of Scope

- Production-scale observability pipelines.
- Distributed orchestration frameworks.
- Advanced model fine-tuning.
- Cost and latency optimization.

---

## 8. Key Learning Outcome

> In Level 2, the student learns how to evolve a simple LLM script into a **coordinated agentic system** that retrieves knowledge, shares context, and reasons collaboratively.
