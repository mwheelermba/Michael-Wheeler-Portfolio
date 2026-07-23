"""Deterministic rule layer.

Runs in parallel with the probabilistic model. Transactions meeting any hard
criterion are flagged regardless of model score. Rules and model serve
different functions: rules encode known typologies and regulatory triggers;
the model catches novel patterns.
"""

from dataclasses import dataclass

import pandas as pd

# Round-number thresholds historically associated with structuring
STRUCTURING_THRESHOLDS = (9000, 9500, 10000)
NEW_ACCOUNT_WINDOW_HOURS = 48


@dataclass
class RuleHit:
    rule_id: str
    description: str


def rule_dest_balance_zeroed(df: pd.DataFrame) -> pd.Series:
    """Destination account balance zeroed immediately post-transfer."""
    raise NotImplementedError("TODO")


def rule_structuring_amount(df: pd.DataFrame) -> pd.Series:
    """Amount at/above round-number structuring thresholds."""
    raise NotImplementedError("TODO")


def rule_new_account_max_limit(df: pd.DataFrame) -> pd.Series:
    """New account executing maximum-limit transaction within first 48 hours."""
    raise NotImplementedError("TODO")


def apply_rules(df: pd.DataFrame) -> pd.DataFrame:
    """Apply all rules; return df with `rule_flagged` bool and `rule_hits` list."""
    raise NotImplementedError("TODO: combine individual rule outputs")
