# PaySim Transaction Monitoring & Compliance Engine

**Type:** Fraud Detection | Compliance Automation
**Stack:** PySpark, Python, XGBoost, SHAP, LLM (SAR generation)
**Data:** [PaySim Synthetic Financial Transactions](https://www.kaggle.com/datasets/ealaxi/paysim1) (Kaggle)

An end-to-end transaction monitoring engine built on the PaySim synthetic dataset, simulating the architecture of a real compliance detection stack. The emphasis is not on maximizing model accuracy but on replicating the operational tradeoffs fraud and compliance teams actually face: minimizing financial losses from missed fraud without flooding the review queue with false positives.

> **Status:** 🚧 Skeleton / in progress. Module structure is in place; implementation is underway.

## Pipeline

Raw transaction ingestion → class-imbalance handling (SMOTE-Tomek) → cost-optimized XGBoost classification → deterministic rule layer → SHAP explainability → alert budget-aware threshold calibration → automated SAR draft generation.

## Repository Structure

```
├── data/
│   └── download_instructions.md         # PaySim is on Kaggle; download instructions here
├── pipeline/
│   ├── preprocess.py                    # Data cleaning and feature engineering
│   ├── resample.py                      # SMOTE-Tomek implementation
│   ├── train.py                         # XGBoost with custom cost-weighted loss
│   ├── rules.py                         # Deterministic rule layer
│   ├── explain.py                       # SHAP value computation and formatting
│   └── sar_draft.py                     # LLM-assisted SAR narrative generation
├── calibration/
│   └── threshold_optimizer.py           # Alert budget-aware threshold calibration
├── output/
│   ├── flagged_transactions.csv         # Review queue output with SHAP explanations
│   └── sample_sar_draft.md              # Example SAR narrative output
└── notebooks/
    └── investigation_walkthrough.ipynb  # Full pipeline walkthrough with commentary
```

## Design Principles

- **Fraud detection is a cost optimization problem, not a classification accuracy problem.** The model minimizes expected dollar loss: a missed fraud costs the full transaction amount plus remediation; a false positive costs analyst time and customer friction.
- **Accuracy is not reported.** A model that flags nothing achieves 99.87% accuracy on this dataset and catches zero fraud. Metrics used instead: PR-AUC, dollar-weighted false negative rate, alert queue utilization, and false positive rate by transaction type.
- **Rules and models run in parallel.** Deterministic rules encode known typologies (balance-zeroing transfers, structuring-threshold amounts, new-account max-limit activity); the model catches novel patterns. Either can route a transaction to review.
- **Alert budgets are real.** The risk threshold is calibrated dynamically against a simulated daily analyst review capacity, prioritizing highest-loss-risk cases when the queue is full.
- **Compliance output, not just scores.** High-risk transactions get SHAP-based analyst-readable explanations and an LLM-drafted SAR narrative following FinCEN guidelines — always human-reviewed, never auto-filed.

## Setup

```bash
pip install -r requirements.txt
```

Then follow [data/download_instructions.md](data/download_instructions.md) to obtain the dataset.

## Dataset Limitations

PaySim is a simulation. Its fraud patterns are more deterministic than real-world fraud, so performance metrics here overstate real-world detection rates. The value of this implementation is the pipeline architecture, the cost-optimization framing, and the compliance output layer — not the specific numbers achieved on synthetic data.
