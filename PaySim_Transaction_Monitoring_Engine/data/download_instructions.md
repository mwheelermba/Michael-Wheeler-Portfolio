# PaySim Dataset — Download Instructions

The PaySim synthetic financial transactions dataset is hosted on Kaggle and is **not** committed to this repository (~470 MB uncompressed, ~6.3M rows).

## Option 1: Kaggle CLI (recommended)

```bash
pip install kaggle
kaggle datasets download -d ealaxi/paysim1 -p data/
unzip data/paysim1.zip -d data/
```

Requires a Kaggle API token at `~/.kaggle/kaggle.json` — see [Kaggle API docs](https://www.kaggle.com/docs/api).

## Option 2: Manual download

1. Visit https://www.kaggle.com/datasets/ealaxi/paysim1
2. Download and extract `PS_20174392719_1491204439457_log.csv` into this `data/` directory.

## Expected file

```
data/PS_20174392719_1491204439457_log.csv
```

The pipeline expects this filename by default (configurable in `pipeline/preprocess.py`).

## Schema

| Column | Description |
|---|---|
| step | Hour of simulation (1–744, ~30 days) |
| type | CASH-IN, CASH-OUT, DEBIT, PAYMENT, TRANSFER |
| amount | Transaction amount |
| nameOrig | Originating account |
| oldbalanceOrg / newbalanceOrig | Originator balance before/after |
| nameDest | Destination account |
| oldbalanceDest / newbalanceDest | Destination balance before/after |
| isFraud | Ground-truth fraud label (~0.13% positive) |
| isFlaggedFraud | Naive built-in rule flag (not used as a feature) |
