import argparse
from pathlib import Path
from src.prompts import build_verification_prompt
from src.schemas import AuditItem, AuditReport
from src.tools.search_tool import SearchTool

def extract_claims(text: str) -> list[str]:
    # Simple baseline extractor: one claim per line
    return [ln.strip() for ln in text.splitlines() if ln.strip()]

def verify_claim(claim: str, tool: SearchTool) -> AuditItem:
    evidence = tool.search(claim)
    prompt = build_verification_prompt(claim, evidence)
    # Placeholder: this is where you'd call your LLM provider
    # For now, we return an "UNCLEAR" result to keep the repo runnable without keys.
    return AuditItem(claim=claim, verdict="UNCLEAR", citations=[], rationale="LLM call not implemented in template repo.")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    text = Path(args.input).read_text(encoding="utf-8")
    claims = extract_claims(text)

    tool = SearchTool()
    items = [verify_claim(c, tool) for c in claims]
    report = AuditReport(items=items)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(report.to_markdown(), encoding="utf-8")
    print(f"Wrote report to: {args.output}")

if __name__ == "__main__":
    main()
