"""Legitimate declines (customer friction) visualization.

Shows how many good customers the current configuration blocks —
the false-positive side of every rule tightening.
"""

import pandas as pd
import streamlit as st


def render_friction_chart(df: pd.DataFrame) -> None:
    """Render the legitimate-transactions-declined chart.

    TODO:
    - Aggregate legitimate transactions by final decision.
    - Show declined count/value and the false positive rate alongside
      the fraud chart for direct visual comparison.
    """
    raise NotImplementedError
