"""Output metric calculation.

For any combination of rule and score settings, calculates the real-time
metrics displayed by the UI:

- Fraud blocked: count and dollar value of fraudulent transactions declined
- Fraud missed: count and dollar value of fraudulent transactions approved
- Legitimate declined: count and dollar value of good transactions blocked
  (false positives)
- False Positive Rate: % of legitimate transactions declined
- Alert queue load: transactions routed to manual review rather than
  auto-approve or auto-decline
- Net loss impact: fraud losses avoided minus the friction cost of
  declining legitimate customers (configurable friction cost assumptions)

Extending the simulator
-----------------------
Add a new metric by implementing its calculation here and registering it
in ``METRIC_REGISTRY`` so the UI picks it up for display.
"""

from dataclasses import dataclass

import pandas as pd


@dataclass
class FrictionAssumptions:
    """Configurable cost assumptions for the net loss impact metric."""

    # Expected lifetime-value cost of falsely declining a good customer,
    # expressed as a multiple of the declined transaction amount.
    friction_cost_multiplier: float = 0.25
    # Cost per manual review case (analyst time).
    review_cost_per_case: float = 3.50


@dataclass
class MetricResults:
    """Computed metrics for one rule/score configuration."""

    fraud_blocked_count: int = 0
    fraud_blocked_value: float = 0.0
    fraud_missed_count: int = 0
    fraud_missed_value: float = 0.0
    legit_declined_count: int = 0
    legit_declined_value: float = 0.0
    false_positive_rate: float = 0.0
    alert_queue_load: int = 0
    net_loss_impact: float = 0.0


def compute_metrics(
    df: pd.DataFrame,
    assumptions: FrictionAssumptions | None = None,
) -> MetricResults:
    """Compute all output metrics from a decisioned transaction frame.

    Expects ``df`` to carry the decision columns produced by rules.py and
    scoring.py plus the ground-truth ``is_fraud`` label.

    TODO:
    - Derive final decision per transaction (approve / review / decline)
      from rule flags and score bands.
    - Cross-tabulate decisions against ``is_fraud`` for counts and values.
    - Compute FPR over the legitimate population only.
    - Net loss impact = fraud value blocked
        - fraud value missed
        - friction cost of legitimate declines
        - review queue processing cost.
    """
    assumptions = assumptions or FrictionAssumptions()
    raise NotImplementedError


# Registry consumed by the UI layer for metric display ordering/labels.
METRIC_REGISTRY = {
    "fraud_blocked_count": "Fraud blocked (count)",
    "fraud_blocked_value": "Fraud blocked ($)",
    "fraud_missed_count": "Fraud missed (count)",
    "fraud_missed_value": "Fraud missed ($)",
    "legit_declined_count": "Legitimate declined (count)",
    "legit_declined_value": "Legitimate declined ($)",
    "false_positive_rate": "False positive rate",
    "alert_queue_load": "Alert queue load",
    "net_loss_impact": "Net loss impact ($)",
}
