# Manual Exploration: Try Searches Interactively

Before running systematic **Grid Search** sweeps, it can be useful to explore causal discovery methods interactively.
Manual exploration helps you understand how algorithms behave, how assumptions influence results, and which choices are worth examining more carefully.

This page describes how to use Tetrad’s **Pipelines** interface to experiment step by step — one algorithm, one parameter setting, and one result at a time.

> Manual exploration is optional.
> Many users can proceed directly to Grid Search, but this stage can be helpful for building intuition and confidence.

---

## Why Use Manual Exploration?

Manual exploration can be helpful for:

- Seeing how **tests and scores** influence graph structure
- Understanding how **parameter changes** affect sparsity and orientation
- Observing how **constraints and background knowledge** shape results
- Becoming familiar with Tetrad’s modular workflow

The emphasis here is **qualitative rather than definitive**. The goal is insight and orientation, not final conclusions.

---

## When Manual Exploration Is Useful

Manual exploration is most useful when you:

- Have explored your data (see *Data Exploration*)
- Have provisional assumptions and want to understand sensitivity
- Are unfamiliar with a particular algorithm or test
- Want to sanity-check behavior before committing to a Grid Search

If you already know what you want to compare, you can proceed directly to Grid Search without this step.

---

## Pipelines: The Interactive Workflow

In Tetrad, a **Pipeline** is a visual workflow connecting:

- A **Data** node (your dataset)
- One or more **Search** nodes (causal discovery algorithms)
- Optional **Diagnostic** nodes (e.g., Markov Checker)

Pipelines allow you to run and inspect individual searches interactively, making it easier to see how results are produced.

---

## Building a Simple Pipeline

1. Open the **Pipelines** workspace.
2. Drag in a **Data** node and select your dataset.
3. Add a **Search** node (e.g., PC, FCI, GES).
4. Connect the Data node to the Search node.
5. Configure the Search node:
   - Choose a test or score
   - Set key parameters (α, penalty, etc.)
6. (Optional) Add a **Markov Checker** node.
7. Run the pipeline.

Each run produces a graph that can be inspected visually.

---

## Examples of Manual Exploration

The following exercises illustrate common ways to build intuition about algorithm behavior.

### A. Varying Test Sensitivity

1. Fix the algorithm (e.g., **PC**).
2. Run with different significance levels:
   - α = 0.01
   - α = 0.05
   - α = 0.10

Observe:

- How edge density changes
- Which orientations remain stable
- Whether the graph becomes implausibly sparse or dense

---

### B. Comparing Algorithms

1. Build two pipelines:
   - PC with Fisher-Z
   - FCI with the same test
2. Run both.
3. Compare:
   - Adjacencies
   - Orientations
   - The effect of allowing latent confounders

This helps clarify how different algorithm families behave on the same data.

---

### C. Adding Background Knowledge

1. Start with a baseline search.
2. Add **time-order or tier constraints**.
3. Rerun the pipeline.

Observe:

- Which edges are forbidden
- How orientations become more constrained
- Whether results align more closely with domain knowledge

---

### D. Exploring Nonlinearity or Non-Gaussianity

1. Run a search using a linear-Gaussian test (e.g., Fisher-Z).
2. Rerun using a nonparametric test (e.g., KCI or RCIT).
3. Compare the resulting graphs.

This can indicate whether linear assumptions are strongly influencing the results.

---

## Inspecting Results

After each run:

- Use the **Graph Viewer** to inspect the output.
- Note:
  - The number of edges
  - Orientation patterns
  - Any apparent conflicts with prior knowledge

Focus on visual and structural differences rather than numeric optimization. Manual exploration is about recognizing patterns, not selecting a final model.

---

## How Manual Exploration Leads to Grid Search

Manual exploration helps answer practical questions such as:

- Which parameters appear most influential?
- Which algorithms seem appropriate for this data?
- Which diagnostics are likely to be informative?

Once you have provisional answers, **Grid Search** allows you to:

- Systematically sweep parameters
- Compare algorithms side by side
- Evaluate results quantitatively
- Identify models that perform well under diagnostics

---

## Tips for Effective Manual Exploration

- Change only **one element at a time**
- Keep brief notes or screenshots of runs
- Use side-by-side visual comparisons
- Stop early — this step is preparatory, not exhaustive

---

## Summary

Manual exploration provides a low-overhead way to understand how causal discovery methods behave:

- It builds intuition about algorithms and parameters
- It highlights sensitivity to assumptions
- It prepares you for systematic comparison

Once you have a sense of what matters, Grid Search supports a more structured and defensible analysis.

---

## 🧭 Next Step

Proceed to **Running Searches and Grid Search Tips** to learn how to turn exploratory insights into systematic comparisons.
