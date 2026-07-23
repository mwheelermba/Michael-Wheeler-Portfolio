"""Deterministic authorization rule implementations.

Each rule follows a common signature so new rules can be added without
modifying the core application logic:

    def rule(df: pd.DataFrame, threshold: <numeric>) -> pd.Series

The returned boolean Series is True where the rule FLAGS the transaction
(enhanced review / decline), False where the transaction passes.

Rules implemented (all independently toggleable in the UI):

- Transaction Amount Threshold — flag transactions above a configurable
  dollar limit. Slider range: $100 to $10,000.
- Account Age Gate — flag transactions on accounts younger than a
  configurable age. Slider range: 0 to 90 days.
- Velocity Threshold — flag accounts exceeding a configurable number of
  transactions in the past 24 hours. Slider range: 1 to 50.
"""

from dataclasses import dataclass

import pandas as pd

# Slider ranges surfaced by the Streamlit sidebar
AMOUNT_RANGE = (100, 10_000)
ACCOUNT_AGE_RANGE = (0, 90)
VELOCITY_RANGE = (1, 50)


@dataclass
class RuleConfig:
    """Active thresholds and toggles for the rule layer."""

    amount_enabled: bool = True
    amount_threshold: float = 2_500.0

    account_age_enabled: bool = True
    account_age_threshold_days: int = 14

    velocity_enabled: bool = True
    velocity_threshold_24h: int = 10


def amount_rule(df: pd.DataFrame, threshold: float) -> pd.Series:
    """Flag transactions with ``amount`` above ``threshold``."""
    raise NotImplementedError


def account_age_rule(df: pd.DataFrame, threshold_days: int) -> pd.Series:
    """Flag transactions on accounts younger than ``threshold_days``."""
    raise NotImplementedError


def velocity_rule(df: pd.DataFrame, threshold_24h: int) -> pd.Series:
    """Flag transactions where ``txn_count_24h`` exceeds ``threshold_24h``."""
    raise NotImplementedError


def apply_rules(df: pd.DataFrame, config: RuleConfig) -> pd.DataFrame:
    """Apply all enabled rules and return per-rule and combined flags.

    TODO:
    - Evaluate each enabled rule into its own boolean column
      (``flag_amount``, ``flag_account_age``, ``flag_velocity``).
    - Add a combined ``flag_any_rule`` column (logical OR).
    - Leave disabled rules as all-False so per-rule impact can be isolated.
    """
    raise NotImplementedError
