# Running Searches and Grid Search Tips

Once you have explored your data and chosen a starting set of assumptions and methods (see *Algorithm Selection and Assumptions*), the next step is to **run causal searches systematically**.

Rather than treating causal discovery as a one-shot operation, Tetrad encourages you to explore how results change across reasonable choices of algorithms, tests or scores, and tuning parameters. The **Grid Search** tool is designed to support exactly this kind of structured exploration.

---

## Why Use Grid Search?

Grid Search is especially useful when you want to:

- Explore **multiple parameter settings** for a given algorithm
- Compare **different algorithms** under similar assumptions
- Understand how sensitive results are to tuning choices
- Identify **simple models that are consistent with the data**
- Use diagnostics such as the **Markov Checker** in a systematic way

For many users, Grid Search is the *default workflow* for causal discovery in Tetrad.

---

## From Single Runs to Systematic Search

You may begin with a single exploratory run to confirm that an algorithm behaves sensibly on your data. However, interpretation should rarely stop there.

A single run answers:
> “What happens for *this* choice of parameters?”

Grid Search helps answer:
> “Which results are **stable** across reasonable choices?”

---

## Running a Basic Search

Before using Grid Search, it helps to understand the basic components of a search.

In the Tetrad interface:

1. Select a **causal discovery algorithm** (e.g., PC, FCI, GES).
2. Choose an appropriate **test or score** based on your data type.
3. Set key parameters:
    - Significance level (α) for test-based methods
    - Penalty or discount for score-based methods
4. Run the search and inspect the resulting graph.

If the output looks implausible, overly dense, or unstable, that is a strong signal that **systematic exploration** is needed.

---

## What to Sweep in Grid Search

When using Grid Search, vary **only a small number of meaningful parameters** at a time. This keeps results interpretable.

### 1. Significance Level (α) — Test-Based Methods

Typical values:
- 0.01
- 0.05
- 0.10

Lower α tends to produce sparser graphs; higher α produces denser graphs. Sweeping α reveals how much structure is supported by the data.

---

### 2. Penalty / Discount — Score-Based Methods

Penalty parameters control the trade-off between model fit and complexity.

- Higher penalties favor simpler models
- Lower penalties allow more edges

Sweeping the penalty often reveals a clear region where models remain Markov-consistent while becoming increasingly complex.

---

### 3. Algorithm Choice

Grid Search allows you to compare:

- Constraint-based methods (e.g., PC, FCI)
- Score-based methods (e.g., GES, BOSS, GRaSP)
- Hybrid approaches

Comparing across algorithm families helps distinguish robust features from method-specific artifacts.

---

### 4. Tests and Scores

Different tests and scores respond differently to:

- Non-Gaussianity
- Nonlinearity
- Mixed data types

Sweeping across a small set of compatible tests or scores helps diagnose sensitivity to modeling assumptions.

---

## Interpreting Grid Search Results

A Grid Search produces a table of results, where each row corresponds to a particular algorithm and parameter combination.

Two quantities are especially important:

### 1. Markov Consistency

- Does the graph’s implied conditional independence structure agree with the data?
- Diagnostics such as the **Markov Checker** help answer this question.

Graphs that fail Markov diagnostics should generally be treated with skepticism.

---

### 2. Model Complexity

- Number of edges
- Degrees of freedom (when available)

Among graphs that pass Markov diagnostics, **simpler models are usually preferable** unless there is strong justification for additional complexity.

---

## A Practical Starter Pattern

For many users, the following pattern works well:

1. Select **one algorithm family** (e.g., PC or FCI).
2. Sweep **one key parameter** (α or penalty).
3. Evaluate results using:
    - Markov Checker statistics
    - Visual inspection of graphs
4. Identify **minimal models** that pass diagnostics.
5. Optionally repeat with a second algorithm family.

This approach balances thoroughness with interpretability.

---

## Reading Grid Search Output

When examining results:

- Each row represents a distinct model.
- Clicking a row allows you to inspect the corresponding graph.
- Look for:
    - Adjacencies that appear across many settings
    - Orientations that remain stable
    - Edges that disappear or flip easily (these are less reliable)

The goal is not to find a single “best” graph, but to identify **robust features** of the causal structure.

---

## Common Pitfalls to Avoid

### Don’t Sweep Too Many Parameters at Once
Large parameter grids can become difficult to interpret. Start small.

---

### Keep Background Knowledge Fixed Initially
Explore what the data suggest on their own before adding strong constraints.

---

### Use Diagnostics Early
If most models fail Markov diagnostics, reconsider assumptions, tests, or parameter ranges.

---

### Document What You Tried
Keeping track of what you swept — and why — makes interpretation and reporting much easier.

---

## Where Grid Search Fits in the Workflow

Grid Search sits at the center of the causal analysis workflow:

- After **choosing assumptions and methods**
- Before **final interpretation and reporting**

It transforms causal discovery from a single run into a structured, evidence-based exploration.

---

## 🧭 Next Step

Once you have identified promising candidate models:

→ Continue to **Model Evaluation and Markov Checking** to assess consistency, robustness, and plausibility in greater detail.