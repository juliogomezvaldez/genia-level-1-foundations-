def build_verification_prompt(claim: str, evidence: str) -> str:
    return f"""You are a verification agent. You MUST rely only on the provided evidence.
If evidence is insufficient, answer UNCLEAR.

Claim:
{claim}

Evidence:
{evidence}

Return JSON:
{{
  "verdict": "SUPPORTED|NOT_SUPPORTED|UNCLEAR",
  "citations": ["..."],
  "rationale": "..."
}}
"""
