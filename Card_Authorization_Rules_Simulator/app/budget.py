"""Alert budget constraint logic.

The alert budget is the maximum number of transactions the review team
can manually evaluate per day. When rule settings generate more flagged
transactions than the budget allows, the simulator surfaces the
constraint visually and suggests threshold adjustments that bring the
queue within capacity while minimizing the impact on fraud loss
mitigation.
"""

from dataclasses import dataclass

import pandas as pd

DEFAULT_ALERT_BUDGET = 200  # cases per day


@dataclass
class BudgetStatus:
    """Queue load relative to the configured alert budget."""

    queue_size: int
    budget: int

    @property
    def utilization(self) -> float:
        """Queue size as a fraction of budget (may exceed 1.0)."""
        return self.queue_size / self.budget if self.budget else float("inf")

    @property
    def over_budget(self) -> bool:
        return self.queue_size > self.budget


def evaluate_budget(df: pd.DataFrame, budget: int = DEFAULT_ALERT_BUDGET) -> BudgetStatus:
    """Measure current review queue load against the alert budget.

    TODO: count transactions in the manual review band and return a
    BudgetStatus.
    """
    raise NotImplementedError


def suggest_adjustments(df: pd.DataFrame, budget: int) -> list[str]:
    """Suggest threshold adjustments that bring the queue within budget.

    TODO:
    - Rank candidate threshold moves (per rule and score band) by
      queue reduction per dollar of additional fraud missed.
    - Return human-readable suggestions, cheapest fraud impact first.
    """
    raise NotImplementedError
