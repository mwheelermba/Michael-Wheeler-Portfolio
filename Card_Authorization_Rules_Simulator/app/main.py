"""Streamlit application entry point.

Card Authorization Rules Engine & Loss-Friction Simulator.

Run with:
    streamlit run app/main.py

Layout:
- Sidebar: sliders and toggles for every rule threshold, risk score
  thresholds, alert budget, and friction cost assumptions.
- Main pane: real-time metrics (updates on slider movement, no submit
  button), fraud-vs-friction charts, alert queue gauge, net loss impact
  chart, counterfactual explainer, and exportable summary report.
"""

import streamlit as st

from app.simulator import SimulationConfig, generate_population
from app.rules import RuleConfig, apply_rules, AMOUNT_RANGE, ACCOUNT_AGE_RANGE, VELOCITY_RANGE
from app.scoring import ScoreConfig, compute_risk_scores, score_decisions
from app.metrics import FrictionAssumptions, compute_metrics
from app.budget import DEFAULT_ALERT_BUDGET, evaluate_budget, suggest_adjustments
from components.fraud_chart import render_fraud_chart
from components.friction_chart import render_friction_chart
from components.queue_gauge import render_queue_gauge
from components.counterfactual_panel import render_counterfactual_panel

st.set_page_config(
    page_title="Card Authorization Rules Simulator",
    page_icon="🛡️",
    layout="wide",
)


@st.cache_data
def load_population(population_size: int, fraud_rate: float, seed: int):
    """Generate (and cache) the synthetic transaction population."""
    config = SimulationConfig(population_size, fraud_rate, seed)
    return generate_population(config)


def build_sidebar() -> tuple[RuleConfig, ScoreConfig, FrictionAssumptions, int]:
    """Render sidebar controls and return the selected configuration.

    TODO:
    - Simulation controls: population size, fraud prevalence, seed.
    - Rule sliders with independent enable toggles:
        amount ($100-$10,000), account age (0-90 days), velocity (1-50).
    - Risk score thresholds: review and decline cutoffs.
    - Alert budget number input.
    - Friction cost assumption inputs.
    """
    raise NotImplementedError


def render_metrics_row(results) -> None:
    """Render the headline metric tiles (st.metric row).

    TODO: display fraud blocked/missed, legit declined, FPR,
    queue load, and net loss impact from MetricResults.
    """
    raise NotImplementedError


def render_export_section(rule_config, score_config, results) -> None:
    """Render the exportable rule configuration summary.

    TODO: fill output/rule_config_report_template.md with the current
    configuration and metrics; offer via st.download_button.
    """
    raise NotImplementedError


def main() -> None:
    st.title("Card Authorization Rules Engine & Loss-Friction Simulator")
    st.caption(
        "Synthetic card-not-present authorization funnel — explore the tradeoff "
        "between fraud loss and customer friction. No real data; all "
        "transactions are generated at runtime."
    )

    # TODO: wire the full pipeline once modules are implemented:
    # 1. rule_config, score_config, assumptions, budget = build_sidebar()
    # 2. df = load_population(...)
    # 3. df = apply_rules(df, rule_config)
    # 4. scores = compute_risk_scores(df, score_config)
    # 5. df = df.join(score_decisions(scores, score_config))
    # 6. results = compute_metrics(df, assumptions)
    # 7. render_metrics_row(results)
    # 8. render_fraud_chart(df); render_friction_chart(df)
    # 9. render_queue_gauge(evaluate_budget(df, budget))
    # 10. render_counterfactual_panel()
    # 11. render_export_section(rule_config, score_config, results)
    st.info("Skeleton build — simulation pipeline not yet implemented.")


if __name__ == "__main__":
    main()
