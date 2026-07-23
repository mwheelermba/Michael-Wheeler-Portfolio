"""XGBoost training with a custom cost-weighted loss.

The model minimizes expected dollar loss, not classification error:
- False Negative cost: full transaction amount + estimated remediation cost
- False Positive cost: analyst review time (in dollars) + customer friction proxy
"""

import pandas as pd

# Business cost assumptions (documented, tunable)
REMEDIATION_COST_FIXED = 150.0   # per missed fraud, on top of transaction amount
ANALYST_REVIEW_COST = 12.0       # per false positive, ~15 min at loaded rate
FRICTION_COST_PROXY = 5.0        # per false positive, customer friction estimate


def fn_cost(amount: float) -> float:
    """Dollar cost of a missed fraudulent transaction."""
    return amount + REMEDIATION_COST_FIXED


def fp_cost() -> float:
    """Dollar cost of a false positive alert."""
    return ANALYST_REVIEW_COST + FRICTION_COST_PROXY


def cost_weighted_objective(preds, dtrain):
    """Custom XGBoost objective: gradient/hessian of asymmetric dollar loss.

    Per-row FN cost is passed via sample weights (transaction amount based).
    """
    raise NotImplementedError("TODO: implement custom objective")


def train(X_train: pd.DataFrame, y_train: pd.Series, amounts: pd.Series):
    """Train the cost-weighted XGBoost classifier and return the fitted model."""
    raise NotImplementedError("TODO: implement training loop with early stopping")


def evaluate(model, X_test: pd.DataFrame, y_test: pd.Series, amounts: pd.Series) -> dict:
    """Report compliance-relevant metrics.

    - PR-AUC (not ROC-AUC; not accuracy)
    - Dollar-weighted false negative rate
    - False positive rate by transaction type
    """
    raise NotImplementedError("TODO: implement evaluation metrics")
