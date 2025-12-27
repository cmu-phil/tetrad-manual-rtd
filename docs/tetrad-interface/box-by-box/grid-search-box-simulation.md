# Grid Search (Simulation)

This page describes how to use **Grid Search** in Tetrad when working from a **simulation** rather than a fixed dataset.

In simulation-based Grid Search, Tetrad repeatedly generates data from a specified simulation model and evaluates causal discovery algorithms across multiple parameter settings. This workflow is especially useful for **method comparison**, **sensitivity analysis**, and **benchmarking** under controlled conditions.

---

## When to Use Simulation-Based Grid Search

Simulation-based Grid Search is appropriate when:

- You want to compare algorithms under **known ground truth**
- You want to understand how performance changes with:
  - sample size,
  - noise level,
  - graph density,
  - functional form,
  - or latent structure
- You are evaluating **robustness or failure modes** of algorithms
- You are developing or testing new methods

Unlike data-based Grid Search, simulation-based Grid Search is **stochastic**: results depend on random draws unless otherwise fixed.

---

## Key Difference from Data-Based Grid Search

| Aspect | Data-Based | Simulation-Based |
|------|-----------|------------------|
| Data source | Fixed dataset | Generated repeatedly |
| Randomness | None | Yes (unless seeded) |
| Ground truth | Unknown | Known |
| Truth-based statistics | Hidden | Available |
| Typical use | Applied analysis | Method evaluation |

---

## Step 1: Select a Simulation

1. Add a **Grid Search** box to the workspace.
2. Connect it to a **Simulation** box.
3. In the **Simulation** editor:
   - Choose a **graph type** (e.g., random DAG, scale-free)
   - Choose a **simulation model** (e.g., linear Gaussian, nonlinear)
   - Set simulation parameters (number of variables, sample size, noise level, etc.)

Only **one simulation** may be active at a time.

---

## Step 2: Algorithms Tab

In the **Algorithms** tab:

1. Click **Add Algorithm**
2. Select one or more causal discovery algorithms
3. Choose compatible tests or scores
4. Optionally edit algorithm, test, or score parameters

As with data-based Grid Search, parameters may be specified as **comma-separated lists**, and all combinations will be explored.

---

## Step 3: Table Columns Tab

In the **Table Columns** tab, select statistics and parameters to report.

Because the true graph is known in simulation mode, you may include:

- Adjacency precision / recall
- Arrowhead precision / recall
- Structural Hamming Distance (SHD)
- Other truth-based performance measures

You may also include:
- Markov checking statistics
- Estimated graph properties (e.g., number of edges)
- Parameter values

Choose a **small, interpretable set** of columns to keep comparisons readable.

---

## Step 4: Comparison Tab

In the **Comparison** tab:

- Choose a **comparison graph type** (e.g., DAG, CPDAG, PAG)
- Select a **truth graph** or derived graph for evaluation
- Configure utilities for truth-based statistics if sorting by utility
- Choose Markov checking options if desired

Truth-based utilities are meaningful here because the ground truth is known.

---

## Step 5: Run Counts and Randomness

Simulation-based Grid Search allows you to specify how many times each configuration is run.

Key options include:

- **Number of runs per configuration**
- **Random seed** (if reproducibility is desired)
- **Aggregation method** (e.g., mean statistics across runs)

Increasing the number of runs improves stability but increases computation time.

---

## Running the Comparison

Click **Run Comparison** to begin.

For each algorithm and parameter combination, Grid Search will:

1. Generate data from the simulation
2. Run the algorithm
3. Compute selected statistics
4. Aggregate results across runs

Progress and detailed logs appear in the **Verbose Output** tab.

---

## Interpreting Simulation Results

Simulation-based Grid Search is best interpreted comparatively:

- Compare algorithms under identical conditions
- Examine trade-offs between:
  - accuracy,
  - complexity,
  - robustness,
  - and consistency
- Identify regimes where methods perform well or fail

Avoid focusing on single rows; patterns across conditions are more informative.

---

## Common Pitfalls

- Sweeping too many parameters at once
- Using too few simulation runs
- Over-interpreting small differences
- Ignoring failure cases

Simulation studies are most valuable when they reveal **limitations**, not just successes.

---

## Summary

Simulation-based Grid Search allows you to:

- Evaluate causal discovery methods under controlled conditions
- Use truth-based performance metrics responsibly
- Understand sensitivity to modeling choices
- Compare algorithms systematically

It complements data-based Grid Search by answering *methodological* questions rather than applied ones.

---

## 🧭 Next Steps

- Compare results across multiple simulations
- Vary assumptions systematically
- Use insights to guide applied analyses on real data
