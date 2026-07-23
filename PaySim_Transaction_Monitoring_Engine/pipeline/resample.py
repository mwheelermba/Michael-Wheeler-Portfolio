"""SMOTE-Tomek combined resampling for class imbalance handling.

PaySim fraud prevalence is ~0.13%. SMOTE generates synthetic minority samples;
Tomek links remove ambiguous borderline majority samples. The sampling ratio is
tuned to preserve realistic fraud prevalence rather than forcing 50/50 balance.
"""

import pandas as pd

# Target minority proportion after resampling — deliberately far from 0.5 to
# avoid distorting the majority-class behavioral distribution.
TARGET_MINORITY_RATIO = 0.05


def resample(X: pd.DataFrame, y: pd.Series, ratio: float = TARGET_MINORITY_RATIO):
    """Apply SMOTE-Tomek and return (X_resampled, y_resampled).

    Only applied to the training split — never to validation/test data.
    """
    raise NotImplementedError("TODO: implement SMOTETomek from imblearn")
