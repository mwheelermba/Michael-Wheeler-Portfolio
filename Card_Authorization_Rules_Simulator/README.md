# Card Authorization Rules Engine & Loss-Friction Simulator

**Type:** Fraud Strategy | Decision Engine Simulation
**Stack:** Python, Streamlit
**Data:** Synthetic card-not-present transaction simulation — no real data, no external services

An interactive simulation of a real-time card-not-present (CNP) authorization funnel. Move a slider to tighten a velocity threshold and immediately see how much fraud gets blocked — and how many legitimate customers get declined alongside it. The tool makes the core tension of fraud operations tangible: **every rule that blocks fraud also risks blocking good customers**, and finding the right threshold is a business optimization problem, not a technical accuracy problem.

This is not a detection model. It is a decision-support and strategy-communication tool — the kind of interactive analysis fraud strategy analysts build to move stakeholder conversations from abstract threshold debates to specific, quantified business decisions.

## What It Does

- **Synthetic CNP population** generated at runtime with realistic fraud prevalence (0.1%–1.0%) and six risk signals per transaction: amount, account age, device trust score, geolocation distance, time since last transaction, and 24-hour velocity
- **Three adjustable rules** with independent toggles — transaction amount threshold ($100–$10,000), account age gate (0–90 days), and 24h velocity threshold (1–50 txns)
- **Risk score layer** — a weighted-signal score with review/decline cutoffs, modeling the interaction between rule-based and score-based authorization logic
- **Real-time metrics** on every slider move: fraud blocked/missed (count and $), legitimate declines, false positive rate, alert queue load, and net loss impact under configurable friction-cost assumptions
- **Alert budget constraint** — when rule settings flag more transactions than the review team can work, the simulator surfaces the capacity breach and suggests threshold adjustments that fit the queue to budget with minimal fraud impact
- **Counterfactual feedback explainer** — an educational panel on why declined transactions never produce ground-truth labels, how that biases rule performance metrics, and the randomized-holdout mitigation used in production fraud systems

## Running the Application

```bash
pip install -r requirements.txt
streamlit run app/main.py
```

Runs locally in a browser. No API keys, database connections, or cloud services required — all data is generated synthetically at runtime.

## Project Structure

```
/
├── app/
│   ├── main.py                     # Streamlit application entry point
│   ├── simulator.py                # Transaction population generation
│   ├── rules.py                    # Deterministic rule implementations
│   ├── scoring.py                  # Risk score calculation
│   ├── metrics.py                  # Output metric calculation
│   └── budget.py                   # Alert budget constraint logic
├── components/
│   ├── fraud_chart.py              # Fraud blocked vs missed visualization
│   ├── friction_chart.py           # Legitimate declines visualization
│   ├── queue_gauge.py              # Alert budget utilization gauge
│   └── counterfactual_panel.py     # Educational explainer panel
├── output/
│   └── rule_config_report_template.md  # Exportable rule configuration summary
├── notebooks/
│   └── threshold_analysis.ipynb    # Static analysis of threshold tradeoffs
└── README.md
```

## What This Demonstrates

Fraud strategy roles require understanding not just that fraud exists in the data, but how detection rules interact with business operations, customer experience, and analyst capacity:

- **Alert budgets as an operational constraint** that shapes rule design, not an afterthought
- **Quantifying customer friction cost**, not just fraud loss prevented
- **The counterfactual feedback problem** — a core challenge in maintaining production fraud models
- **Interactive tool design** that serves the communication function fraud strategy analysts actually perform for product and business stakeholders

## Extending the Simulator

The modular architecture is intentional — extend it without touching the core application logic:

- **New risk signals:** extend the transaction generation schema in `app/simulator.py`
- **New rules:** add to `app/rules.py` following the existing rule function signature
- **New metrics:** implement the calculation in `app/metrics.py` and register it in `METRIC_REGISTRY` for display
