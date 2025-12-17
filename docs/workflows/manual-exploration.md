# Manual Exploration: Try Searches Interactively

Before diving into systematic *Grid Search* sweeps, it’s helpful to get a feel for how causal search algorithms behave — especially how different choices of tests, scores, and parameters affect the graphs you see.  
The **Manual Exploration** page shows how to use Tetrad’s **Pipelines** interface to experiment interactively, one step at a time.

Manual exploration is less systematic than grid search, but it helps build **intuition** about:
- How tests and scores influence output
- How constraints (e.g., time tiers) shape graphs
- How search results change with parameter adjustments

Once you understand these patterns, you’ll be better prepared to run more exhaustive sweeps in Grid Search.

---

## When to Do Manual Exploration

Perform manual exploration after you:

- **Explored the data** (see *Data Exploration*)
- **Formed initial assumptions** about causal sufficiency and functional form
- **Have a sense** of which algorithm families might be sensible

Manual exploration is great for getting comfortable with:
- Pipelines and modular workflows in the Tetrad UI
- Running a small number of searches with variation
- Inspecting and comparing graph outputs interactively

---

## Building a Pipeline

In Tetrad, a **Pipeline** connects:
- A **Data node** (your dataset)
- One or more **Search nodes** (search algorithms / methods)
- Optional **Diagnostic nodes** (Markov Checker, Graph Metrics, etc.)

### Step-by-Step

1. Open the **Pipelines** menu.
2. Drag in a **Data node** and select your dataset.
3. Add a **Search node** (e.g., PC, FCI, GES, etc.)
4. Connect the Data node to the Search node.
5. Configure the Search node:
    - Choose a test or score
    - Set parameters (α, penalty, etc.)
6. Optionally add a **Markov Checker** node
    - Connect the Search node output to the Markov Checker input
7. Run the pipeline

This lets you experiment with one algorithm and one set of choices at a time.

---

## Examples of Manual Exploration

Here are several exploration paths you can try:

### A. Varying Test Sensitivity

1. Fix the algorithm to **PC**.
2. Run with:
    - α = 0.01
    - α = 0.05
    - α = 0.10

Inspect how the skeleton and orientations change as you loosen or tighten conditional independence thresholds.

---

### B. Comparing Algorithms

1. Build two pipelines:
    - PC with Fisher-Z
    - FCI with the same test
2. Run both and compare results:
    - Does allowing latents (with FCI) change adjacencies?
    - Do orientations agree where they overlap?

This gives a hands-on sense of algorithmic differences.

---

### C. Adding Background Knowledge

1. Start with a base search (PC / FCI).
2. Add **tiered time-order constraints**.
3. Rerun and observe:
    - How many forbidden edges are removed?
    - What orientations become identifiable?

This helps reinforce how background knowledge interacts with search logic.

---

### D. Nonlinear / Non-Gaussian Tests

1. Load your data.
2. Apply a **nonparametric test** (e.g., KCI/RCIT) with PC/FCI.
3. Compare to the same algorithm using Fisher-Z.

See how different assumptions about functional form affect outputs.

---

## Inspecting and Comparing Outputs

After running a pipeline:

- Use the **Graph viewer** to visually inspect results.
- Expand nodes to see adjacencies and marks.
- For each run:
    - Note the number of edges
    - Check orientations
    - See if results violate known constraints

Manual exploration is qualitative — you’re developing pattern recognition before turning to quantitative comparison in Grid Search.

---

## How This Prepares You for Grid Search

Manual exploration helps you answer:

- *Which parameters matter most?*
- *Which tests or scores seem sensible?*
- *Which algorithms are worth comparing systematically?*

Once you’ve built this intuition, Grid Search lets you **formalize** the exploration:

- Sweep across a range of settings
- Collect consistent diagnostics
- Compare models quantitatively

---

## Tips for Effective Manual Exploration

✔ Change **one thing at a time** — this isolates effects.  
✔ Keep track of each run’s settings and results.  
✔ Combine pipelines with lightweight documentation (notes or screenshots).  
✔ Use visual comparison before moving to systematic sweeps.

---

## Summary

Manual exploration is an **interactive first pass** that helps you:

- Understand algorithm behavior with your data
- See how assumptions and parameters influence results
- Decide what to sweep and compare in Grid Search

After this stage, you’ll be ready to use Grid Search to *systematize* intuition into defensible model comparisons.

---

## Next Step

→ Follow with **Running Searches and Grid Search Tips** to turn intuition into systematic analysis.