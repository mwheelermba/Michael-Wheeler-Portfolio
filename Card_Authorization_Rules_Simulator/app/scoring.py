"""Risk score calculation layer.

Calculates a lightweight risk score for each transaction from a weighted
combination of the input signals. The score is used as an additional
threshold control alongside the deterministic rules, letting the
simulation model the interaction between rule-based and score-based
authorization logic.

Score semantics: 0.0 (lowest risk) to 1.0 (highest risk). Transactions
score higher for larger amounts, younger accounts, lower device trust,
larger geo distance, and higher 24h velocity.
"""

from dataclasses import dataclass, field

import pandas as pd

DEFAULT_WEIGHTS = {
    "amount": 0.20,
    "account_age_days": 0.20,
    "device_trust_score": 0.25,
    "geo_distance_km": 0.15,
    "txn_count_24h": 0.20,
}


@dataclass
class ScoreConfig:
    """Weights and decision thresholds for the risk score layer."""

    weights: dict = field(default_factory=lambda: dict(DEFAULT_WEIGHTS))
    # Score >= review_threshold -> manual review; >= decline_threshold -> auto-decline
    review_threshold: float = 0.6
    decline_threshold: float = 0.85
    enabled: bool = True


def compute_risk_scores(df: pd.DataFrame, config: ScoreConfig) -> pd.Series:
    """Compute a 0-1 risk score for each transaction.

    TODO:
    - Normalize each signal to 0-1 (min-max or logistic squashing;
      invert device_trust_score and account_age_days so higher = riskier).
    - Return the weighted sum, clipped to [0, 1].
    """
    raise NotImplementedError


def score_decisions(scores: pd.Series, config: ScoreConfig) -> pd.DataFrame:
    """Map scores to decision bands: approve / review / decline.

    TODO: return boolean columns ``score_review`` and ``score_decline``.
    """
    raise NotImplementedError
