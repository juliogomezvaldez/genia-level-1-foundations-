# Level 3 SPEC — Production-Grade Agentic Compliance Auditor

## 1. Problem Statement (Easy to Understand)

In a real company, teams constantly make statements and decisions that must follow rules, such as:
- internal security and privacy policies,
- data retention rules,
- acceptable use guidelines,
- and external guidance (industry standards or regulator guidance).

Examples of “compliance claims”:
- “We do not store any personal data.”
- “User deletion requests are fulfilled within 24 hours.”
- “We keep audit logs for 5 years.”

Auditing these claims is hard because:
- policies are long and spread across many documents,
- some claims require context (what data, where, how long, who can access),
- risk is not binary (some cases must be escalated),
- decisions must be explainable and reviewable later (audit trail).

This project builds a **production-grade agentic system** that:
1. reads compliance claims,
2. retrieves relevant policies as evidence (RAG),
3. decides whether the claim is compliant,
4. assigns risk and escalation decisions,
5. applies guardrails (safety + bias + format/policy adherence),
6. outputs auditable results plus observability artifacts (logs, traces, metrics).

**Key idea:** This is not just a “verifier”. It is an **auditor**: evidence-backed, risk-aware, and traceable.

---

## 2. Student-Generated Inputs (Required)

To keep the capstone reproducible and self-contained, the student must generate these inputs locally:

### 2.1 Compliance Claims Dataset
**File:** `compliance_claims.json`

**Requirements**
- 15–40 claims.
- Each claim includes:
  - `id`
  - `text` (the compliance claim)
  - `domain` (privacy | security | retention | marketing | HR | etc.)
  - `context` (short scenario; 2–5 sentences)
  - `sensitivity` (low | medium | high)
  - Optional `expected_outcome` (for evaluation only; not visible to agents)

### 2.2 Policy Corpus (Internal + External)
**Folder:** `/policies/` (markdown/text) OR **File:** `policies.json`

**Requirements**
- 10–30 documents total.
- Must include:
  - internal policies (synthetic, authored by the student),
  - external guidance (synthetic summaries authored by the student).
- Each document includes metadata:
  - `doc_id`, `title`, `owner`, `version`, `effective_date`,
  - `domain`, `confidentiality`,
  - `source_type` (internal | external)

### 2.3 Risk Rubric (How to Assign Risk & Escalate)
**File:** `risk_rubric.json`

**Requirements**
- risk levels: `low | medium | high`
- escalation rules, e.g.:
  - high sensitivity + unclear evidence → escalate
  - conflicting policies → escalate
  - missing required controls → high risk

### 2.4 System Configuration
**File:** `config.yaml`

**Requirements**
- model selection (primary + fallback)
- cost limits per run (token/call cap)
- retrieval settings (top_k, filters)
- retry/fallback rules
- redaction settings for sensitive logs

---

## 3. Outputs (What the System Produces)

### 3.1 Structured Results
**File:** `results.json`

Each claim output includes:
- `verdict`: `compliant | non_compliant | unclear`
- `risk_level`: `low | medium | high`
- `escalate`: `true | false`
- `confidence`: 0–1 (or low/medium/high)
- `evidence`: list of cited policy snippets:
  - `doc_id`, `title`, `quote/snippet`, `effective_date`
- `explanation`: short reasoning (no hallucinations, evidence-grounded)
- `trace_id`: link to trace entry

### 3.2 Human Report
**File:** `audit_report.md`

A readable summary including:
- high-risk findings,
- escalations and why,
- per-claim verdict with citations.

### 3.3 Observability Artifacts
**Folder:** `/observability/`
- `logs.jsonl` (structured logs)
- `traces.json` (per-agent step timing + retries)
- `metrics.json` (latency, retrieval hit rate, fallback rate, estimated token usage)

---

## 4. Functional Requirements (Detailed)

FR-1. The system shall ingest `compliance_claims.json`.

FR-2. The system shall ingest and index the policy corpus to enable RAG retrieval.

FR-3. The system shall implement a multi-agent pipeline with these roles:
- Retriever
- Verifier
- Risk Reviewer
- Reporter

FR-4. The Retriever agent shall retrieve relevant policy evidence per claim using a retrieval tool.

FR-5. The Verifier agent shall produce a compliance verdict:
- `compliant`, `non_compliant`, or `unclear`,
strictly based on retrieved evidence.

FR-6. The Risk Reviewer agent shall assign:
- `risk_level` (low/medium/high),
- `escalate` flag (true/false),
using the `risk_rubric.json` and verification confidence.

FR-7. The system shall run guardrail checks:
- **Safety**: prevent unsafe or disallowed outputs.
- **Bias**: detect obvious discriminatory or unfair conclusions.
- **Policy adherence**: ensure outputs follow schema and cite evidence.

FR-8. The Reporter agent shall generate `results.json` and `audit_report.md`.

FR-9. The system shall emit observability outputs (logs, traces, metrics) for every run.

FR-10. The system shall support retries and fallbacks:
- retrieval retry (if no results or tool errors),
- model fallback (if cost/latency limits exceeded),
- degraded mode (`unclear` + escalate) when evidence is missing.

---

## 5. Non-Functional Requirements (Detailed)

NFR-1. **High Availability & Graceful Degradation**  
The system should still produce an auditable output even when retrieval or models fail.

NFR-2. **Cost Controls**  
The system shall enforce configurable per-run cost limits and support cheaper fallbacks.

NFR-3. **Auditability**  
All verdicts must include evidence references and a traceable decision path.

NFR-4. **Security & Sensitive Inputs**  
The system shall avoid logging raw sensitive data and support redaction/hashing in logs.

NFR-5. **Reproducibility**  
Given the same inputs and configuration, the output schema must remain stable and rerunnable.

NFR-6. **Maintainability**  
Agent roles, tool interfaces, and handoff contracts must be clearly documented.

---

## 6. Architecture (Simple View)

### Agents
- **Retriever Agent**: finds relevant policy passages (RAG).
- **Verifier Agent**: decides compliance status using retrieved passages.
- **Risk Reviewer Agent**: assigns risk and escalation using rubric.
- **Reporter Agent**: formats structured results and final report.

### Orchestration
- A **Supervisor** controls the flow:
  - routes tasks to agents,
  - handles retries,
  - applies fallbacks,
  - enforces guardrails pre/post generation.

### Memory
- **Short-term**: session context passed between agents.
- **Long-term**: retrieval index built from policies.

### Tools
- Retrieval/search tool (RAG)
- Evaluation tool (schema checks, citation checks, rubric checks)
- Guardrail tool (safety + bias + output policy constraints)

---

## 7. In Scope
- Multi-agent orchestration with specialized roles.
- RAG-based policy grounding.
- Guardrails and automated evaluation hooks.
- Observability artifacts (logs/traces/metrics) per run.

## 8. Out of Scope
- Training or fine-tuning base models.
- Non-GenAI ML pipelines.
- Large-scale data engineering beyond retrieval indexing.
