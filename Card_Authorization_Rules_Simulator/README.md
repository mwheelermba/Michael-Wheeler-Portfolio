# Card Authorization Rules Simulator

Python and Streamlit. All data is synthetic and generated at runtime, so there are no API keys, no databases, and nothing to configure. Clone it, install two or three packages, and run it.

**Status: work in progress.** The project structure is in place and I am building out the simulation logic module by module.

## The question I am exploring

Every fraud rule has two costs. Tighten a velocity threshold and you block more fraud, but you also decline more legitimate customers who happen to shop in bursts. Loosen it and the customers are happy, but fraud losses climb. Fraud teams live inside this tradeoff, and it is surprisingly hard to communicate with static reports or threshold tables.

So I wanted a tool where you can move a slider and watch both sides react at once. Tighten the account age gate and see the fraud number drop while the false positive number rises. The idea is that the conversation stops being "the threshold feels too strict" and becomes "this setting saves $40k in fraud but costs us 300 good customers, is that worth it?"

To be clear, this is not a fraud detection model and there is no real transaction data anywhere in it. It simulates a card-not-present authorization funnel so you can reason about how rules behave, not predict anything.

## What the tool does

The simulator generates a population of synthetic card-not-present transactions with a realistic fraud rate (somewhere between 0.1% and 1%, which is typical for CNP depending on the merchant). Each transaction gets a handful of risk signals: amount, account age, a device trust score, distance from the registered address, time since the last transaction, and how many transactions the account has made in the past 24 hours.

Three rules sit on top of that, each with its own slider and on/off toggle:

- a transaction amount threshold ($100 to $10,000)
- an account age gate (0 to 90 days)
- a 24 hour velocity limit (1 to 50 transactions)

There is also a simple weighted risk score with review and decline cutoffs, since real authorization stacks usually mix rules with scores and I wanted to see how the two layers interact.

Whenever you change a setting, the metrics update: fraud blocked and missed (count and dollars), good customers declined, false positive rate, how many transactions land in the manual review queue, and an estimated net loss figure that nets fraud savings against the cost of declining legitimate customers.

Two pieces I care about most, because they are the parts that make fraud strategy different from just running a model:

**The alert budget.** A review team can only work so many cases a day. If your rule settings flag 2,000 transactions and the team can handle 200, the other 1,800 are not actually getting reviewed no matter what your dashboard says. The simulator treats review capacity as a hard constraint and flags when a configuration blows past it.

**The counterfactual feedback problem.** When a rule declines a transaction, you never find out whether it was actually fraud. The transaction never happened, so there is no label. Your performance metrics only reflect the transactions you approved, which means every rule is grading its own homework. The app includes a panel explaining this and the standard fix (letting a small random slice of flagged transactions through so you keep an honest sample). This one took me a while to fully wrap my head around and I think it is one of the most underappreciated problems in fraud analytics.

## Running it

```bash
pip install -r requirements.txt
streamlit run app/main.py
```

Opens in your browser and runs entirely on your machine.

## How it is organized

```
app/            core simulation logic
  main.py       Streamlit entry point
  simulator.py  builds the synthetic transaction population
  rules.py      the three adjustable rules
  scoring.py    weighted risk score and decision cutoffs
  metrics.py    fraud blocked/missed, false positives, net loss
  budget.py     alert queue capacity checks
components/     the charts and panels on the Streamlit page
output/         template for the exportable rule config summary
notebooks/      static threshold sweep analysis
```

I kept the pieces separate on purpose. Adding a new risk signal means touching simulator.py, a new rule goes in rules.py, and a new metric goes in metrics.py. I did not want to untangle one big script every time I had a new idea to test.

## Ideas for later

- More rule types (geo distance rules, device trust cutoffs)
- Letting the friction cost assumptions vary by customer segment
- A side by side comparison view for two rule configurations
