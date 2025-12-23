# Model Evaluation and Markov Checking

After running causal searches (including Grid Search) and collecting candidate models, the next crucial step is **model evaluation**.

Causal discovery algorithms propose graphs based on assumptions and search criteria — but those graphs still need to be **checked against the data**.  
In Tetrad, the primary tool for this purpose is the **Markov Checker**.

Rather than accepting a model at face value, causal analysis benefits from *criticism and testing*. The Markov Checker is designed to address a question that often matters most in practice:

> **Is this graph plausible given the data we have?**

---

## Why Model Evaluation Matters

Search algorithms will always return a graph, even when their assumptions are poorly matched to the data.

Without evaluation, it is easy to:
- Overfit noise
- Accept graphs that contradict observed conditional independences
- Prefer unnecessarily complex models

Model evaluation helps separate models that are:
- **compatible with the data**, from
- models that are **statistically contradicted** by it.

The Markov Checker plays a central role in this screening process.

---

## What the Markov Checker Does

Every causal graph implies a set of **conditional independence (CI) relations** via the Markov property. The Markov Checker:

1. Takes a candidate graph
2. Extracts the CI relations implied by that graph
3. Tests those implications against the data using a chosen independence test

If many implied independences are not supported by the data, the model **fails** the Markov check.

### Intuition

You can think of the Markov Checker as asking:

> *If this graph were correct, which independences should we observe — and do we actually observe them?*

If the answer is “no,” then something is inconsistent: the assumptions, the graph, the test choice, or the data.

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

When using Grid Search, Markov Checker results are typically recorded automatically for each candidate model.

---

## Interpreting Markov Checker Output

### Key Outputs

- Overall consistency statistic
- Pass / fail decision (relative to a threshold)
- List of violated conditional independences

### How to Read the Results

- **Few or no violations**  
  The model is *not ruled out* by the data.

- **Many violations**  
  The model is likely inconsistent with observed conditional independences.

- **Borderline results**  
  Consider revisiting assumptions, test choice, or model complexity.

Passing a Markov check does *not* prove a model is correct — it only indicates that the model is **compatible with the data** under the chosen assumptions.

---

## Minimal Markov-Consistent Models

In practice, useful candidate models usually satisfy two criteria:

1. They **pass the Markov check**
2. They are **relatively simple**

This leads to the idea of **minimal Markov-consistent models**.

Among models that pass Markov checking:
- Prefer graphs with fewer edges
- Avoid added complexity unless it improves consistency or interpretability

Grid Search is especially helpful for identifying this balance between **fit and simplicity**.

---

## Comparing Models from Grid Search

When evaluating multiple candidates:

- Rank or inspect models by:
    - Markov consistency statistics
    - Number of edges or degrees of freedom
- Look for:
    - Adjacencies that appear across many settings
    - Orientations that persist across algorithms or tests
    - Clear gains in consistency with modest increases in complexity

A common pattern is:
- Very sparse models fail Markov checks
- Very dense models pass but offer little insight
- **Intermediate models** often provide the most useful structure

---

## Important Caveats

### Markov Checking Is Not a Proof
Passing a Markov check does not establish causal truth. It only rules out models that contradict observed independences.

### Test Choice Matters
Using a test poorly matched to the data (e.g., linear-Gaussian tests on strongly nonlinear data) can distort conclusions.

### Sampling Variability Exists
Some violations may arise from finite samples or marginal effects. Interpretation should be guided by patterns, not rigid thresholds.

---

## Beyond Markov Checking

For deeper evaluation, you may also:

- Use **resampling or stability analysis**
    - Identify edges that appear consistently
- Compare **different tests or scores**
    - Assess robustness to modeling assumptions
- Incorporate **domain knowledge**
    - Known causal constraints, interventions, or temporal orderings

These approaches complement Markov checking rather than replace it.

---

## Practical Tips

✔ Use Markov checking early and throughout the workflow  
✔ Combine it with Grid Search rather than isolated runs  
✔ Prefer simpler models that pass diagnostics  
✔ Treat unstable edges with caution  
✔ Document evaluation decisions carefully

---

## Summary

Model evaluation is a central part of causal analysis:

- The **Markov Checker** screens candidate graphs for consistency with the data
- **Minimal Markov-consistent models** offer a principled balance of fit and simplicity
- Combined with Grid Search, evaluation supports a disciplined, transparent workflow

---

## 🧭 Next Step

After identifying plausible models, proceed to **Interpreting Results**, where you’ll focus on communicating findings, assessing robustness, and understanding remaining uncertainty.