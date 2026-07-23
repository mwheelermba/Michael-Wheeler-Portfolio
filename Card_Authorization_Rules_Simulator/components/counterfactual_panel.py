"""Educational explainer panel: the counterfactual feedback problem.

When a transaction is declined by a rule, it never generates a ground
truth label — the transaction never completes, so you never observe
whether it would have been fraudulent. Rule performance metrics are
therefore biased toward the observable population of approved
transactions, and declined transactions create a blind spot in training
data: the rule is constantly "grading its own homework."

Standard mitigation: pass a small randomized slice of flagged
transactions through to completion to maintain an unbiased training
distribution.
"""

import streamlit as st


def render_counterfactual_panel() -> None:
    """Render the counterfactual feedback problem explainer.

    TODO:
    - Expandable panel (st.expander) with the explanation above.
    - Optional illustrative diagram of the label blind spot and the
      randomized holdout mitigation.
    """
    raise NotImplementedError
