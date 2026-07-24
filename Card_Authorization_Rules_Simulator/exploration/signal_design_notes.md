# Signal design notes

Early notes to myself before I build the transaction generator. The point of this file is to decide what each risk signal should look like so the synthetic population behaves like real card-not-present traffic instead of a toy. If I skip this and just let the numbers fall out however, the whole simulator stops meaning anything.

## The one rule I do not want to break

Fraud and legitimate transactions have to overlap on every signal. In real life a fraudster and a nervous first-time customer buying an expensive gift look a lot alike. If I let the two groups separate cleanly on any signal, then a single rule catches all the fraud with no false positives, the tradeoff disappears, and the tool has nothing to say. So every signal below is "shifted, not separated." Different centers, overlapping tails.

## Signal by signal

**Transaction amount.** Right-skewed, most purchases small, a long tail of big ones. Fraud sits a little higher on average but not dramatically, because smart fraud stays under the radar. I do not want fraud amounts clustering at some obvious high number. Never zero or negative.

- legit: most spend in the tens to low hundreds
- fraud: shifted up modestly, wider spread

**Account age (days).** Younger accounts carry more risk, but plenty of good customers are brand new too. So fraud leans young, legit spans new to years old.

- legit: broad, long tail of established accounts
- fraud: concentrated in the first few weeks, but with some older compromised accounts mixed in

**Device trust score (0 to 1).** Higher is safer. Legit clusters high, fraud leans low, big overlap in the middle where most of the hard decisions live.

**Geo distance from registered address (km).** Most transactions happen near home. Travel and gifts create a natural long tail for good customers, so distance alone is weak. Fraud leans farther out.

**Time since last transaction / velocity (count in 24h).** Most accounts are quiet. Fraud rings burn a card fast, so fraud should have a heavier tail on the 24h count. This is the signal I expect to carry the most weight, but it still has to overlap because some legit customers genuinely shop in bursts (think holiday season).

## Base rate

Keep fraud prevalence configurable between 0.1 and 1 percent, default around 0.5. This is the number that makes accuracy useless as a metric, so I want it front and center and easy to change.

## What I will check once the generator exists

- fraud rate in the output actually matches the config, and changing the config changes it
- pull a summary table of each signal grouped by fraud label and confirm the centers are shifted but the ranges overlap
- no impossible rows: a 2-day-old account cannot have a long history
- same seed gives the same population every run

## Open questions for later

- should any signals be correlated with each other (young account AND far from home), or keep them independent for the first version? Leaning independent to start, revisit if the tradeoffs look too clean.
- realistic weekday vs weekend or time-of-day effects, probably out of scope for v1 but worth noting.
