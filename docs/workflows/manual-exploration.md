# Manual Exploration: Try Searches Interactively

Before running systematic **Grid Search** sweeps, it can be useful to explore causal discovery methods interactively.  
Manual exploration helps you build intuition about how algorithms behave, how assumptions matter, and which choices are worth comparing more carefully.

This page shows how to use Tetrad’s **Pipelines** interface to experiment step by step — one algorithm, one parameter setting, one result at a time.

> Manual exploration is *optional*.  
> Many users can go directly to Grid Search, but this stage can be helpful for understanding and confidence-building.

---

## Why Do Manual Exploration?

Manual exploration is especially helpful for:

- Seeing how **tests and scores** influence graph structure
- Understanding how **parameter changes** affect sparsity and orientation
- Learning how **constraints and background knowledge** shape results
- Getting comfortable with Tetrad’s modular workflow

It is intentionally **lightweight and qualitative** — the goal is intuition, not final answers.

---

## When Manual Exploration Is Useful

Manual exploration is most helpful when you:

- Have explored your data (see *Data Exploration*)
- Have rough assumptions but want to see how sensitive results are
- Are unfamiliar with a particular algorithm or test
- Want to sanity-check behavior before a Grid Search

If you already know what you want to compare, you can skip directly to Grid Search.

---

## Pipelines: The Interactive Workflow

In Tetrad, a **Pipeline** is a visual workflow connecting:

- A **Data node** (your dataset)
- One or more **Search nodes** (algorithms)
- Optional **Diagnostic nodes** (e.g., Markov Checker)

Pipelines let you run and inspect individual searches interactively.

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

Each run produces a graph you can inspect visually.

---

## Examples of Manual Exploration

Below are common exploratory exercises that help build intuition.

---

### A. Varying Test Sensitivity

1. Fix the algorithm (e.g., **PC**).
2. Run with different significance levels:
    - α = 0.01
    - α = 0.05
    - α = 0.10

Observe:
- How edge density changes
- Which orientations remain stable
- Whether the graph becomes implausibly dense or sparse

---

### B. Comparing Algorithms

1. Build two pipelines:
    - PC with Fisher-Z
    - FCI with the same test
2. Run both.
3. Compare:
    - Adjacencies
    - Orientations
    - Whether allowing latent confounders changes conclusions

This helps clarify what different algorithm families are doing.

---

### C. Adding Background Knowledge

1. Start with a baseline search.
2. Add **time-order or tier constraints**.
3. Rerun the pipeline.

Observe:
- Which edges are forbidden
- How orientations become more constrained
- Whether results better align with domain knowledge

---

### D. Exploring Nonlinearity or Non-Gaussianity

1. Run a search using a linear-Gaussian test (e.g., Fisher-Z).
2. Rerun using a nonparametric test (e.g., KCI or RCIT).
3. Compare the resulting graphs.

This can reveal whether linear assumptions are distorting results.

---

## Inspecting Results

After each run:

- Use the **Graph Viewer** to inspect the output.
- Note:
    - Number of edges
    - Orientation patterns
    - Any violations of known constraints
- Compare results visually rather than numerically.

Manual exploration is about *pattern recognition*, not optimization.

---

## How Manual Exploration Leads to Grid Search

Manual exploration helps answer practical questions such as:

- Which parameters matter most?
- Which algorithms seem plausible for this data?
- Which diagnostics are worth emphasizing?

Once you have rough answers, **Grid Search** lets you:

- Systematically sweep parameters
- Compare algorithms side by side
- Evaluate results quantitatively
- Identify minimal models that pass diagnostics

---

## Tips for Effective Manual Exploration

✔ Change only **one thing at a time**  
✔ Keep notes or screenshots of runs  
✔ Use visual comparison, not just intuition  
✔ Stop early — this is preparation, not the main analysis

---

## Summary

Manual exploration is a **low-cost way to build intuition** about causal discovery:

- It helps you understand algorithm behavior
- It reveals parameter sensitivity
- It prepares you for systematic comparison

Once you know what to explore, Grid Search turns intuition into structured, defensible analysis.

---

## 🧭 Next Step

Proceed to **Running Searches and Grid Search Tips** to learn how to turn exploratory insights into systematic comparisons.