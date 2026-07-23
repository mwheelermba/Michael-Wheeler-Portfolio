"""Alert budget-aware threshold calibration.

The model risk threshold is set dynamically against a simulated daily alert
budget (max reviewable cases per analyst team per day). When the queue would
overflow, highest-loss-risk cases are prioritized.
"""

import pandas as pd

# Simulated operational constraints
ANALYSTS = 5
CASES_PER_ANALYST_PER_DAY = 20
DAILY_ALERT_BUDGET = ANALYSTS * CASES_PER_ANALYST_PER_DAY


def expected_loss(score: pd.Series, amount: pd.Series) -> pd.Series:
    """Expected dollar loss if unreviewed: P(fraud) * (amount + remediation)."""
    raise NotImplementedError("TODO")


def optimize_threshold(scores: pd.Series, amounts: pd.Series,
                       budget: int = DAILY_ALERT_BUDGET) -> float:
    """Find the daily threshold that stays within budget while maximizing
    expected loss captured. Returns the calibrated risk threshold."""
    raise NotImplementedError("TODO")


def queue_utilization(scores: pd.Series, thresholds: list[float],
                      budget: int = DAILY_ALERT_BUDGET) -> pd.DataFrame:
    """Report alert queue utilization at various threshold settings."""
    raise NotImplementedError("TODO")
