# Running Searches and Grid Search Tips

Once you have explored your data and chosen a starting set of assumptions and methods (see *Algorithm Selection and Assumptions*), the next step is to **run causal searches systematically**.

Rather than treating causal discovery as a one-shot operation, Tetrad is designed to support exploring how results change across reasonable choices of algorithms, tests or scores, and tuning parameters. The **Grid Search** tool provides a structured way to do this.

---

## Why Use Grid Search?

Grid Search is particularly useful when you want to:

- Explore **multiple parameter settings** for a given algorithm
- Compare **different algorithms** under similar assumptions
- Understand how sensitive results are to tuning choices
- Identify **simple models that are consistent with the data**
- Apply diagnostics such as the **Markov Checker** in a systematic way

For many analyses, Grid Search serves as the main workflow for causal discovery in Tetrad.

---

## From Single Runs to Systematic Search

It is often helpful to begin with a single exploratory run to confirm that an algorithm behaves sensibly on your data. However, interpretation usually benefits from going beyond a single configuration.

A single run answers:

> *What happens for this specific choice of parameters?*

Grid Search helps address a broader question:

> *Which results remain stable across reasonable choices?*

---

## Running a Basic Search

Before using Grid Search, it helps to understand the components of an individual search.

In the Tetrad interface:

1. Select a **causal discovery algorithm** (e.g., PC, FCI, GES).
2. Choose an appropriate **test or score** based on your data type.
3. Set key parameters:
   - Significance level (α) for test-based methods
   - Penalty or discount for score-based methods
4. Run the search and inspect the resulting graph.

If the output appears implausible, overly dense, or unstable, that is often a sign that **systematic exploration** will be useful.

---

## What to Sweep in Grid Search

When using Grid Search, it is usually best to vary **only a small number of meaningful parameters** at a time. This keeps the results easier to interpret.

### 1. Significance Level (α) — Test-Based Methods

Common values include:

- 0.01  
- 0.05  
- 0.10  

Lower α values tend to produce sparser graphs; higher values allow more edges. Sweeping α can reveal how strongly the data support particular connections.

---

### 2. Penalty or Discount — Score-Based Methods

Penalty parameters control the balance between model fit and complexity.

- Higher penalties favor simpler models  
- Lower penalties allow more complex graphs  

Sweeping this parameter often reveals a region where graphs remain Markov-consistent while increasing gradually in complexity.

---

### 3. Algorithm Choice

Grid Search makes it straightforward to compare:

- Constraint-based methods (e.g., PC, FCI)
- Score-based methods (e.g., GES, BOSS, GRaSP)
- Hybrid approaches

Comparing across algorithm families helps distinguish robust features from method-specific behavior.

---

### 4. Tests and Scores

Different tests and scores can respond differently to:

- Non-Gaussianity  
- Nonlinearity  
- Mixed data types  

Exploring a small set of compatible options can clarify how sensitive results are to modeling assumptions.

---

## Interpreting Grid Search Results

A Grid Search produces a table where each row corresponds to a specific algorithm and parameter combination.

Two aspects are especially informative:

### 1. Markov Consistency

- Does the graph’s implied conditional independence structure agree with the data?
- Diagnostics such as the **Markov Checker** are designed to assess this.

Graphs that consistently fail Markov diagnostics typically warrant closer scrutiny or revised assumptions.

---

### 2. Model Complexity

- Number of edges  
- Degrees of freedom (when available)

Among models that pass diagnostics, simpler graphs are often preferred unless there is a clear reason to accept additional complexity.

---

## A Practical Starter Pattern

A commonly effective approach is:

1. Choose **one algorithm family** (e.g., PC or FCI).
2. Sweep **one key parameter** (α or penalty).
3. Evaluate results using:
   - Markov Checker statistics
   - Visual inspection of graphs
4. Identify **minimal models** that pass diagnostics.
5. Optionally repeat with a second algorithm family.

This balances systematic exploration with interpretability.

---

## Reading Grid Search Output

When examining the results table:

- Each row corresponds to a distinct model.
- Selecting a row allows you to inspect the associated graph.
- Pay attention to:
  - Adjacencies that appear across many settings
  - Orientations that remain stable
  - Edges that appear or disappear easily (these are typically less robust)

The aim is not to identify a single “best” graph, but to understand which features are consistently supported.

---

## Common Pitfalls to Avoid

### Sweeping Too Many Parameters at Once

Large grids can become difficult to interpret. Starting with a small, focused sweep is usually more productive.

---

### Changing Background Knowledge Too Early

It can be helpful to first see what the data suggest before adding strong constraints.

---

### Delaying Diagnostics

If many models fail Markov diagnostics, it may be worth revisiting assumptions, tests, or parameter ranges early.

---

### Not Recording What Was Tried

Keeping brief notes on parameter choices and outcomes can greatly simplify interpretation and reporting.

---

## Where Grid Search Fits in the Workflow

Grid Search sits at the center of the causal analysis workflow:

- After **choosing assumptions and methods**
- Before **final interpretation and reporting**

It turns causal discovery from a single run into a structured, evidence-based exploration.

---

## 🧭 Next Step

Once you have identified promising candidate models, continue to **Model Evaluation and Markov Checking** to assess consistency, robustness, and plausibility in greater detail.
