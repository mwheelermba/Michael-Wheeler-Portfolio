"""LLM-assisted SAR (Suspicious Activity Report) draft generation.

For transactions above the high-risk threshold, generates a structured SAR
draft narrative from transaction details, the SHAP explanation, and account
history context. Drafts follow FinCEN narrative guidelines and are formatted
for human review before filing — this pipeline never auto-files.
"""

import pandas as pd

SAR_SYSTEM_PROMPT = """\
You are drafting a Suspicious Activity Report narrative for human compliance
review. Follow FinCEN narrative guidelines: state who, what, when, where, why
the activity is suspicious, and how it occurred. Use only the facts provided.
Do not speculate beyond the evidence. Mark the draft clearly as DRAFT —
PENDING HUMAN REVIEW.
"""


def build_context(txn: pd.Series, shap_explanation: str, account_history: pd.DataFrame) -> dict:
    """Assemble the factual context passed to the LLM."""
    raise NotImplementedError("TODO")


def generate_sar_draft(context: dict) -> str:
    """Call the LLM and return a structured SAR draft narrative (markdown)."""
    raise NotImplementedError("TODO: implement Anthropic API call")
