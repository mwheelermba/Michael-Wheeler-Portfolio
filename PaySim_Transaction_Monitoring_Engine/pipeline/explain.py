"""SHAP value computation and analyst-facing formatting.

Every flagged transaction gets a local explanation of which features drove its
risk score. Output is formatted for analyst consumption, not model validation.
"""

import pandas as pd


def compute_shap(model, X_flagged: pd.DataFrame):
    """Compute SHAP values for the flagged population (TreeExplainer)."""
    raise NotImplementedError("TODO")


def global_importance(shap_values, feature_names: list[str]) -> pd.DataFrame:
    """Rank global feature importance across the full flagged population."""
    raise NotImplementedError("TODO")


def local_explanation(shap_row, features_row: pd.Series, top_n: int = 5) -> str:
    """Human-readable explanation for one flagged transaction.

    Example output:
        Risk driven primarily by: destination balance zeroed post-transfer
        (+0.41), amount 98% of originator balance (+0.22), ...
    """
    raise NotImplementedError("TODO")
