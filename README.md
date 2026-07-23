# Michael Wheeler — Analytics Portfolio

**Vancouver, WA** | mikewheeler.ind@gmail.com | linkedin.com/in/mwheelermba

---

## About

I am a senior analytics professional with six years of experience designing
analytical systems, building data infrastructure, and delivering findings to
executive audiences across SaaS, edtech, and independent consulting. My current
work at Risepoint includes ETL architecture in Databricks, forecasting and
segmentation systems serving a 150-university portfolio, and a GenAI-powered
knowledge system that replaced a manual workflow and saves 25% of my team's weekly labor hours.
Most of that work lives in private repositories.

The projects here are built on my own time, on publicly available data, to
investigate problems I find interesting. The current focus is forensic data
analysis: fraud detection, financial statement anomaly detection, transaction
monitoring, and audit tooling. These projects reflect how I actually think about
data problems, starting from the investigative question, building toward a
documented finding, and producing something a non-technical stakeholder can act
on.

Outside of my portfolio, I also built SettlementScan, a free and open source class action lawsuit matching app that helps the busy person (like myself) keep up with all the settlements they qualify for.

Earlier exploratory work and IBM certification capstones from 2022 to 2023 are
in the `/archive` folder. They reflect an earlier stage of my technical
development and are kept for continuity.

---

## Forensic Analytics Projects

The projects in this section are built around a consistent methodology: take a
real investigative problem, work with real or realistic data at realistic scale,
and produce output that looks like what an actual analyst would hand to a
decision-maker, not a notebook with a model accuracy score at the bottom.

### Card Authorization Rules Engine & Loss-Friction Simulator

An interactive simulation tool that models a card-not-present transaction
authorization funnel, allowing a fraud analyst or strategy professional to
explore the tradeoffs between fraud loss mitigation and customer friction in
real time. The tool is not a detection model on real data; it is a decision
support and communication tool that makes the core tension of fraud operations
tangible and quantifiable. Adjustable rule thresholds, alert budget constraints,
and a counterfactual feedback explainer are all included. Built in Python and
Streamlit.

### PaySim Transaction Monitoring & Compliance Engine

An end-to-end transaction monitoring pipeline on the PaySim synthetic financial
dataset, built to simulate the architecture of a real compliance detection stack.
The emphasis is on the operational tradeoffs that fraud and compliance teams
actually face: class imbalance handling via SMOTE-Tomek, a cost-optimized loss
function that weights misclassification by dollar impact rather than count,
deterministic rule layering running in parallel with the probabilistic model, and
automated SAR draft generation following FinCEN narrative guidelines. Built in
PySpark, XGBoost, and SHAP.

### More in progress

Additional forensic projects covering financial statement anomaly detection,
healthcare claims audit, general ledger integrity testing, and systems
reconciliation are in development and will be added as they are completed.

---

## Skills

**Languages and Platforms:** Python, SQL, Databricks, Snowflake, Power BI,
Power Query, dbt

**Methods:** ETL/ELT pipeline design, predictive modeling, forecasting,
statistical analysis, hypothesis testing, A/B testing, anomaly detection,
exploratory data analysis

**Tools:** Python, SQL, Databricks, Snowflake, Power BI, Power Query, MCP, GenAI tooling 

**Business:** Executive reporting, KPI framework design, cross-functional
stakeholder management, data governance, forensic investigation methodology

---

## Personal Interests

Mindfulness and meditation, hiking and outdoor activities, reading and writing,
video games.

---

## Contact

mikewheeler.ind@gmail.com | linkedin.com/in/mwheelermba
