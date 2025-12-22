# Model Evaluation and Markov Checking

After running causal searches (including Grid Search) and collecting candidate models, the next crucial step is **model evaluation**.

Causal discovery algorithms propose graphs based on assumptions and search criteria — but those graphs still need to be **checked against the data**.  
In Tetrad, the primary tool for this purpose is the **Markov Checker**.

Rather than accepting a model at face value, causal analysis should involve *criticism and testing*. The Markov Checker helps answer the question many users ultimately care about:

> **“Is this graph even plausible given the data we have?”**

---

## Why Model Evaluation Matters

Search algorithms will *always* return a graph — even when the assumptions behind the method are poorly matched to the data.

Without evaluation, it is easy to:
- Overfit noise
- Accept graphs that violate observed conditional independences
- Prefer overly complex models without empirical justification

Model evaluation helps you distinguish between models that are:
- **compatible with the data**, and
- those that are **statistically contradicted** by it.

The Markov Checker plays a central role in this screening process.

---

## What the Markov Checker Does

Every causal graph implies a set of **conditional independence (CI) relations** via the Markov property. The Markov Checker:

1. Takes a candidate graph
2. Extracts its implied CI relations
3. Tests those implications against the data using an independence test

If the implied independences are not supported by the data, the model **fails** the Markov check.

### Intuition

You can think of the Markov Checker as asking:

> “If this graph were correct, which independences should we observe — and do we actually observe them?”

If not, then *something is wrong*: the assumptions, the graph, the test choice, or the data.

---

## Running the Markov Checker in Tetrad

To evaluate a candidate graph:

1. Select the graph you want to evaluate
2. Open the **Markov Checker**
3. Choose an independence test compatible with your data:
    - Continuous data: Fisher-Z, rank-based tests, etc.
    - Discrete data: appropriate discrete tests
4. Run the checker

Tetrad reports:
- A **summary statistic** or pass/fail indicator
- A list of **violated** and **non-violated** CI implications

In Grid Search workflows, these results are typically recorded automatically for each candidate model.

---

## Interpreting Markov Checker Output

### Key Outputs

- **Overall consistency statistic**
- **Pass / fail decision** (relative to a threshold)
- **List of violated conditional independences**

### How to Read the Results

- **Few or no violations**
    - The model is *not ruled out* by the data
- **Many violations**
    - The model is likely inconsistent with observed conditional independences
- **Marginal or borderline results**
    - Consider revising assumptions, test choice, or model complexity

Importantly, *passing the Markov check does not prove the model is correct* — it only means the model is **compatible with the data** under the chosen assumptions.

---

## Minimal Markov-Consistent Models

In practice, you usually want models that satisfy **two criteria**:

1. They **pass the Markov check**, and
2. They are **as simple as possible**

This motivates the idea of **minimal Markov-consistent models**.

Among models that pass Markov checking:
- Prefer graphs with fewer edges
- Avoid unnecessary complexity unless strongly supported

Grid Search is especially helpful for identifying this trade-off between **fit and simplicity**.

---

## Comparing Models from Grid Search

When evaluating multiple candidates:

- Rank or visualize models by:
    - Markov consistency statistic
    - Number of edges (or degrees of freedom)
- Look for:
    - Stable adjacencies across parameter choices
    - Orientations that persist across tests or algorithms
    - Clear improvements in consistency with modest increases in complexity

A common pattern is:
- Very sparse models fail Markov checks
- Very dense models pass but are uninformative
- **Intermediate models** are often the most useful

---

## Important Caveats

### Markov Checking Is Not a Proof
Passing a Markov check does *not* establish causality. It only rules out models that contradict observed independences.

### Test Choice Matters
Using a test poorly matched to the data (e.g., linear-Gaussian tests on strongly nonlinear data) can produce misleading results.

### Sampling Variability Exists
Some violations may arise from finite samples or borderline effects. Use judgment, not rigid thresholds.

---

## Beyond Markov Checking

For deeper analysis, you may also:

- Use **resampling or stability analysis**
    - Identify edges that appear consistently
- Compare **different tests or scores**
    - Assess robustness to assumptions
- Incorporate **domain knowledge**
    - Known causal constraints, interventions, or temporal orderings

These methods complement Markov checking rather than replace it.

---

## Practical Tips

✔ Use Markov checking *early and often*  
✔ Combine it with Grid Search rather than isolated runs  
✔ Prefer simple models that pass diagnostics  
✔ Treat fragile edges with caution  
✔ Document evaluation decisions carefully

---

## Summary

Model evaluation is a critical step in causal analysis:

- The **Markov Checker** screens candidate graphs for consistency with data
- **Minimal Markov-consistent models** offer a principled balance of fit and simplicity
- Combined with Grid Search, evaluation turns causal discovery into a disciplined scientific workflow

---

## 🧭 Next Step

After identifying plausible models:

→ Proceed to **Interpreting Results**, where you’ll learn how to communicate findings, assess robustness, and distinguish solid conclusions from remaining uncertainty.