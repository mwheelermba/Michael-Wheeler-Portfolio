# PaySim Transaction Monitoring and Compliance Engine

Fraud detection and compliance automation on the [PaySim synthetic transactions dataset](https://www.kaggle.com/datasets/ealaxi/paysim1) from Kaggle. Built with Python, XGBoost, SHAP, and an LLM step for drafting SAR narratives.

**Status: work in progress.** The structure is laid out and I'm building the pieces one at a time.

## What I'm trying to do here

PaySim has about 6.3 million simulated mobile money transactions, and roughly 0.13% of them are fraud. The interesting problem isn't training a model that scores well. It's the operational question underneath: missed fraud costs the full transaction amount plus cleanup, while a false positive costs analyst review time and annoys a legitimate customer. Those costs are wildly different, and a review team can only work so many cases per day.

So instead of chasing accuracy, this project treats detection as a cost problem. The plan:

1. Clean the data and build behavioral features (balance movement errors, zeroed-out destination accounts, that kind of thing)
2. Handle the class imbalance with SMOTE-Tomek, but keep fraud rare in the training data rather than forcing a 50/50 split that doesn't resemble reality
3. Train XGBoost with a loss function weighted by actual dollar costs, not misclassification counts
4. Run a plain rule layer alongside the model for the obvious stuff (destination balance zeroed right after a transfer, amounts sitting at structuring thresholds, brand new accounts maxing out limits). Rules catch known patterns; the model is there for everything else
5. Explain every flagged transaction with SHAP so a reviewer can see why it was flagged, in plain language
6. Calibrate the alert threshold against a daily review budget. If the queue would overflow, the highest expected-loss cases go first
7. Generate a draft SAR narrative for high-risk cases following FinCEN guidelines. A human reviews every draft. Nothing gets filed automatically

## Folder layout

```
data/          Download instructions for the Kaggle dataset (too big to commit)
pipeline/      Preprocessing, resampling, training, rules, SHAP, SAR drafting
calibration/   Alert budget and threshold tuning
output/        Review queue output and a sample SAR draft
notebooks/     Walkthrough notebook with commentary
```

## On metrics

I'm deliberately not reporting accuracy. A model that flags nothing at all gets 99.87% accuracy on this dataset and catches zero fraud. Instead I'm tracking:

- Precision-recall AUC, which actually means something when the positive class is this rare
- Dollar-weighted false negative rate, meaning fraud missed as a share of fraud value, not fraud count
- Alert queue utilization at different thresholds
- False positive rate broken out by transaction type, to see where the friction lands

## Setup

```bash
pip install -r requirements.txt
```

Then grab the dataset following [data/download_instructions.md](data/download_instructions.md).

## A caveat worth stating up front

PaySim is a simulation, and its fraud patterns are cleaner than anything you'd see in real transaction data. Whatever numbers come out of this will overstate real-world performance. The point of the project is the pipeline design, the cost framing, and the compliance output, not the scores on synthetic data.
