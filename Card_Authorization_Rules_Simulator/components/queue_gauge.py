"""Alert budget utilization gauge.

Visualizes manual review queue load against team capacity and surfaces
suggested threshold adjustments when the queue exceeds budget.
"""

import streamlit as st

from app.budget import BudgetStatus


def render_queue_gauge(status: BudgetStatus, suggestions: list[str] | None = None) -> None:
    """Render the queue utilization gauge.

    TODO:
    - Progress-style gauge of queue_size vs. budget with clear
      over-budget state (utilization > 100%).
    - When over budget, list suggested threshold adjustments.
    """
    raise NotImplementedError
