# Grid Search

The **Grid Search** tool automates running a search algorithm over a **grid of parameter settings**, so you can
compare performance across many configurations without manually re-running the algorithm.

[//]: # (```{note})

[//]: # (Suggested screenshot:)

[//]: # ()
[//]: # (- The Grid Search configuration dialog, showing choice of algorithm, parameters, and value grid.)

[//]: # (  Save as: ``../../_static/images/tetrad-interface/overview/grid-search-dialog.png``.)

[//]: # (```)

![](../../_static/images/tetrad-interface/overview/grid-search-dialog.png)

## Purpose

Grid Search is useful when:

- You want to tune **hyperparameters** such as penalty discounts, depth limits, or alpha levels.
- You are not sure which test/score or parameter combination works best for your data.
- You want to explore the trade-offs between **sparsity**, **fit**, and **orientation quality** in a systematic way.

Rather than setting parameters by hand and re-running the algorithm, Grid Search lets you define a **parameter grid**
and then runs all combinations automatically.

## Basic workflow

1. Open the Grid Search tool from the **Tools** or **Algorithms** menu.
2. Choose:
    - A **data node**.
    - A **base algorithm** (e.g., FGES, GFCI, BOSS, etc.).
3. Specify the **parameter grid**:
    - Select parameters to vary.
    - Enter a list of values for each parameter (e.g., `alpha ∈ {0.01, 0.05, 0.1}`).
4. Optionally specify:
    - How results should be summarized (scores, edge counts, fit indices).
    - Whether to run in parallel (if available).
5. Run the grid search.

Tetrad will run the chosen algorithm once for **every combination** of parameter values in the grid.

## Outputs

Grid Search typically produces:

- A **table** summarizing each run, with columns including:
    - Parameter values (one column per parameter).
    - Key metrics (e.g., score value, number of edges, run time).
- A collection of **result graphs**, one per parameter combination (or per subset, depending on configuration).

You can:

- Sort the table to find the best-scoring configurations.
- Inspect graphs corresponding to promising parameter settings.
- Export the summary table for further analysis in R or Python.

## Notes and tips

- Start with a **coarse grid** (few values per parameter) to identify promising regions.
- For expensive algorithms, be cautious about grids that produce too many combinations.
- Combine Grid Search with **domain knowledge**: prioritize parameter ranges that make scientific sense, not just
  purely data-driven optima.
