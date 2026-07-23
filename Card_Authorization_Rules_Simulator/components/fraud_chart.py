"""Fraud blocked vs. missed visualization.

Side-by-side view of fraudulent transactions declined versus approved
under the current rule configuration, by count and dollar value.
"""

import pandas as pd
import streamlit as st


def render_fraud_chart(df: pd.DataFrame) -> None:
    """Render the fraud blocked vs. missed chart.

    TODO:
    - Aggregate fraud transactions by final decision (blocked / missed).
    - Render paired bars for count and dollar value.
    """
    raise NotImplementedError
