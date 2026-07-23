# PaySim Transaction Monitoring & Compliance Engine

**Type:** Fraud Detection | Compliance Automation  
**Stack:** PySpark, Python, XGBoost, SHAP, LLM (SAR generation)  
**Data:** PaySim Synthetic Financial Transactions (Kaggle)  
**Relevance:** Trust & Safety Data Analyst, Fraud Risk Analyst, Financial Crimes Analyst, Forensic Consulting

---

## Overview

This project builds an end-to-end transaction monitoring engine on the PaySim synthetic financial dataset, designed to simulate the architecture of a real compliance detection stack. The emphasis is not on maximizing model accuracy but on replicating the operational tradeoffs that fraud and compliance teams actually face: how do you minimize financial losses from missed fraud without flooding your review queue with false positives that consume analyst time and degrade legitimate customer experience?

The pipeline runs from raw transaction ingestion through class-imbalance handling, cost-optimized classification, deterministic rule layering, and automated Suspicious Activity Report (SAR) draft generation — covering the full lifecycle from signal to compliance output.

---

## Problem Statement

A financial platform processes millions of transactions daily. A small fraction are fraudulent, but the cost of missed fraud is asymmetric: a missed fraudulent transfer costs the platform the full transaction amount plus remediation costs, while a false positive costs analyst review time and customer friction. Standard accuracy metrics obscure this asymmetry entirely. The challenge is building a detection system that optimizes for business impact, not benchmark performance, and produces compliance-ready outputs when high-risk transactions are identified.

---

## Technical Implementation

### Dataset
PaySim simulates mobile money transactions based on real transaction logs from a mobile money service in an African country. It contains approximately 6.3 million transactions across five transaction types (CASH-IN, CASH-OUT, DEBIT, PAYMENT, TRANSFER) with a fraud rate of approximately 0.13%, representing a highly imbalanced classification problem.

### Class Imbalance Handling
SMOTE-Tomek combined resampling is applied to address class imbalance without distorting the underlying behavioral distributions of the majority class:
- SMOTE generates synthetic minority class samples in feature space
- Tomek links identify and remove borderline majority class samples that create ambiguous decision boundaries
- Resampling ratio is tuned to preserve realistic fraud prevalence rather than achieving artificial balance

### Cost-Optimized Loss Function
A custom loss function weights misclassification costs asymmetrically to reflect actual business impact:
- False Negative cost: full transaction amount plus estimated remediation cost
- False Positive cost: estimated analyst review time (in dollars) plus customer friction proxy
- The model is trained to minimize expected dollar loss rather than classification error

### Deterministic Rule Layer
A deterministic rule layer runs in parallel with the probabilistic model and flags transactions meeting hard criteria regardless of model score:
- Destination account balance zeroed immediately post-transfer (a strong fraud signal in PaySim)
- Transaction amount at or above round-number thresholds historically associated with structuring
- New account executing maximum-limit transaction within first 48 hours

Transactions flagged by either the rule layer or the model above a tuned risk threshold are routed to the review queue.

### Explainability Layer
SHAP values are computed for every flagged transaction, producing a human-readable explanation of which features drove the risk score:
- Global feature importance ranked across the full flagged population
- Local explanation for each individual flagged transaction
- Output formatted for analyst consumption, not model validation

### Automated SAR Draft Generation
When a transaction exceeds the high-risk threshold, an LLM-assisted pipeline generates a structured SAR draft narrative using the transaction details, SHAP explanation, and account history context. The draft follows FinCEN narrative guidelines and is formatted for human review before filing — it does not auto-file.

### Alert Budget Management
The model is calibrated against a simulated daily alert budget (maximum reviewable cases per analyst team per day). The risk threshold is set dynamically to stay within budget while prioritizing highest-loss-risk cases when the queue is full.

---

## Key Metrics

The project reports on metrics relevant to compliance operations rather than standard ML benchmarks:

- **Precision-Recall AUC** rather than ROC-AUC (appropriate for highly imbalanced datasets where the positive class is rare and costly)
- **Dollar-weighted false negative rate** (fraud missed as a percentage of total fraud value, not fraud volume)
- **Alert queue utilization** (what percentage of the daily budget is consumed at various threshold settings)
- **False positive rate by transaction type** (to identify which transaction types generate disproportionate friction)

Note: overall accuracy is not reported. A model that classifies everything as non-fraud achieves 99.87% accuracy on this dataset and catches zero fraud. Accuracy is the wrong metric for imbalanced fraud detection and is treated as such throughout.

---

## What This Demonstrates

This project signals understanding of the operational and compliance dimensions of fraud detection, not just the modeling mechanics. Specifically:

- Knowledge that fraud detection is a cost optimization problem, not a classification accuracy problem
- Understanding of alert budget constraints and the tradeoff between detection rate and analyst capacity
- Familiarity with SAR generation and FinCEN compliance workflow requirements
- Practical application of explainability tools in a compliance context where model decisions must be defensible
- Awareness that deterministic rules and probabilistic models serve different functions and should run in parallel

---

## Relevance by Role

| Target Role | Signal Strength | Primary Reason |
|---|---|---|
| GitHub Trust & Safety Data Analyst | High | Abuse-risk scoring, anomaly detection, and investigation views are explicitly listed in the job description; this project demonstrates all three |
| Fraud Risk Analyst (Fintech) | Very High | Core detection stack architecture; alert budget framing directly mirrors fintech fraud operations |
| Financial Crimes Analyst | High | SAR generation and FinCEN workflow familiarity are directly relevant |
| Forensic Data Analytics Consultant | Moderate | Less directly relevant than reconciliation projects; useful as a technical depth signal |
| Payment Integrity Analyst | Low | Detection model architecture is less relevant than retrospective audit methodology for this track |

---

## Files

```
/
├── data/
│   └── download_instructions.md         # PaySim is available on Kaggle; download instructions here
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
├── notebooks/
│   └── investigation_walkthrough.ipynb  # Full pipeline walkthrough with commentary
└── README.md
```

---

## Notes on Dataset Limitations

PaySim is a simulation, not real transaction data. Its fraud patterns are more deterministic than real-world fraud, which means model performance metrics here will overstate real-world detection rates. This is acknowledged throughout the project. The value of this implementation is in the pipeline architecture, the cost-optimization framing, and the compliance output layer, not in the specific performance numbers achieved on the synthetic dataset.
