"""Data cleaning and feature engineering for the PaySim dataset.

Loads the raw PaySim CSV, cleans known artifacts, and engineers behavioral
features used downstream by the model and rule layers.
"""

from pathlib import Path

import pandas as pd

RAW_DATA_PATH = Path("data/PS_20174392719_1491204439457_log.csv")

# Only TRANSFER and CASH_OUT contain fraud in PaySim; other types are retained
# for the rule layer but excluded from model training.
FRAUD_ELIGIBLE_TYPES = ("TRANSFER", "CASH_OUT")


def load_raw(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load the raw PaySim CSV."""
    raise NotImplementedError("TODO: implement raw load with dtype spec")


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Clean known PaySim artifacts.

    - Normalize transaction type labels (CASH-OUT -> CASH_OUT)
    - Drop isFlaggedFraud (leaky / trivial built-in rule)
    - Handle zero-balance placeholder values on merchant accounts
    """
    raise NotImplementedError("TODO: implement cleaning steps")


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Engineer behavioral features.

    Planned features:
    - balance delta errors (amount vs. observed balance movement)
    - origin/destination balance zeroed flags
    - transaction amount relative to originator balance
    - hour-of-day / day-of-simulation from `step`
    - account age proxies for new-account rules
    """
    raise NotImplementedError("TODO: implement feature engineering")


def run(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Full preprocess: load -> clean -> engineer features."""
    return engineer_features(clean(load_raw(path)))


if __name__ == "__main__":
    run()
