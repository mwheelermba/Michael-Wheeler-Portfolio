"""Synthetic card-not-present (CNP) transaction population generation.

Generates a synthetic transaction population at runtime, parameterized to
reflect realistic CNP fraud prevalence rates (typically 0.1% to 1.0%
depending on merchant category and authentication method).

Each transaction carries the risk signals consumed by the rule layer
(rules.py) and the risk score layer (scoring.py):

- ``amount``: transaction amount in USD
- ``account_age_days``: account age in days at time of transaction
- ``device_trust_score``: 0-1 score derived from device fingerprint history
- ``geo_distance_km``: geolocation distance from registered address
- ``hours_since_last_txn``: time since last successful transaction
- ``txn_count_24h``: number of transactions in the last 24 hours
- ``is_fraud``: ground-truth label (known because data is synthetic)

Extending the simulator
-----------------------
Add new risk signals by extending the schema in ``generate_population``.
Fraudulent and legitimate transactions should draw from distinct
distributions for any signal intended to carry predictive value.
"""

from dataclasses import dataclass

import numpy as np
import pandas as pd

DEFAULT_POPULATION_SIZE = 50_000
DEFAULT_FRAUD_RATE = 0.005  # 0.5% — mid-range CNP prevalence
DEFAULT_RANDOM_SEED = 42


@dataclass
class SimulationConfig:
    """Parameters controlling the synthetic population."""

    population_size: int = DEFAULT_POPULATION_SIZE
    fraud_rate: float = DEFAULT_FRAUD_RATE
    random_seed: int = DEFAULT_RANDOM_SEED


def generate_population(config: SimulationConfig | None = None) -> pd.DataFrame:
    """Generate a synthetic CNP transaction population.

    Returns a DataFrame with one row per transaction and the risk-signal
    columns documented in the module docstring. Fraudulent transactions
    draw from shifted distributions (younger accounts, lower device trust,
    higher velocity, larger geo distance) so that rules and scores have
    signal to work with.

    TODO:
    - Sample legitimate transaction signals from baseline distributions
      (lognormal amounts, long-tailed account age, high device trust).
    - Sample fraudulent transaction signals from shifted distributions.
    - Combine, shuffle, and return with a stable ``txn_id`` index.
    """
    config = config or SimulationConfig()
    rng = np.random.default_rng(config.random_seed)
    raise NotImplementedError("Population generation not yet implemented")
