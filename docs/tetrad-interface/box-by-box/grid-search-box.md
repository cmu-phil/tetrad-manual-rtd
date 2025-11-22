# Grid Search Box

```{figure} ../../_static/images/tetrad-interface/box-by-box/grid-search-box.png
:name: tetrad-grid-search-box-screenshot
:alt: Grid Search Box in the Tetrad interface.

Grid Search Box in the Tetrad interface sidebar and main panel.
```

## Purpose

The **Grid Search** box is where you run **parameter sweeps** over one or more algorithms or models.
It lets you define a grid of parameter values, run many configurations automatically, and inspect
how performance or scores change across the grid.

Typical uses include:

- Tuning penalty parameters, significance thresholds, or regularization strengths.
- Comparing different settings of a search algorithm on the same dataset.
- Exploring robustness of results with respect to key hyperparameters.

## Typical workflow

1. **Choose a base algorithm or model**
   - Make sure the algorithm or model you want to tune is already configured in its
     own box (for example, in *Search*, *Estimator*, or another relevant box).
   - In the Grid Search box, select this as the target of the grid search.

2. **Define the parameter grid**
   - Specify which parameters to vary (e.g., penalty discount, alpha level).
   - For each parameter, define:
     - A list of discrete values **or**
     - A range and step size (if supported).
   - Optionally set constraints on combinations (e.g., skip some combinations that you
     know are not meaningful).

3. **Specify evaluation criteria**
   - Choose what you want to record for each grid point, for example:
     - Graph scores (e.g., BIC, log-likelihood).
     - Edge counts or sparsity.
     - Custom statistics, where available.
   - Optionally specify a primary criterion to highlight the “best” configuration.

4. **Run the grid search**
   - Click **Run** to execute the algorithm over all parameter combinations in the grid.
   - Progress may be shown in a log or progress bar.

5. **Inspect and export results**
   - Review the resulting table summarizing each parameter combination and its associated
     metrics.
   - Sort or filter by a particular metric to find promising configurations.
   - Export the table for offline analysis (e.g., CSV) if supported.

## Key controls

- **Toolbar**
  - **New / Configure** – create or edit a grid search specification.
  - **Run** – execute the grid search over all defined parameter combinations.
  - **Stop** – interrupt a long-running grid search.
  - **Export** – save the results table to a file.

- **Grid definition panel**
  - Lists all parameters included in the grid.
  - Columns for parameter name, type (discrete/range), and values.
  - Controls to add, remove, or modify parameters and their value sets.

- **Results panel**
  - A table with one row per parameter combination.
  - Columns for:
    - Parameter values
    - Scores or evaluation metrics
    - Optional flags (e.g., success/failure, warnings)

## Common patterns & tips

- Start with a **coarse grid** over a wide range of values to locate interesting regions;
  follow up with a **finer grid** in a narrower range if necessary.
- Be mindful of the **combinatorial explosion**: the number of runs grows as the product
  of the number of values for each parameter.
- If runs are expensive, consider:
  - Reducing the number of parameters varied at once.
  - Using a smaller dataset or subset of variables for preliminary tuning.
- Keep clear, descriptive names for grid search configurations so you can recognize them
  in saved projects.

## Related pages

- `Tetrad Interface → Overview` – high-level tour of the GUI.
- Other boxes that commonly interact with **Grid Search**:
  - *Search* and *Estimator* (provide algorithms whose parameters you tune).
  - *Compare* (to compare selected “best” configurations from different grid searches).
