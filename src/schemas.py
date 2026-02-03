from pydantic import BaseModel, Field
from typing import List, Literal

Verdict = Literal["SUPPORTED","NOT_SUPPORTED","UNCLEAR"]

class AuditItem(BaseModel):
    claim: str
    verdict: Verdict
    citations: List[str] = Field(default_factory=list)
    rationale: str

class AuditReport(BaseModel):
    items: List[AuditItem]

    def to_markdown(self) -> str:
        lines = ["# Audit Report", ""]
        for i, it in enumerate(self.items, 1):
            lines.append(f"## {i}. {it.claim}")
            lines.append(f"- **Verdict:** {it.verdict}")
            if it.citations:
                lines.append(f"- **Citations:** " + ", ".join(it.citations))
            lines.append(f"- **Rationale:** {it.rationale}")
            lines.append("")
        return "\n".join(lines)
