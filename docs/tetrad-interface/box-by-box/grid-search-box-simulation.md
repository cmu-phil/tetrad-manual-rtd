# Grid Search (Simulation Studies)

The **Grid Search** tool can also be used to run **simulation studies**, where data are generated from known models and causal discovery algorithms are evaluated systematically.

This mode is intended for:
- methodological research,
- benchmarking algorithms,
- sensitivity analysis,
- and teaching causal discovery under controlled assumptions.

This page describes how Grid Search behaves when **no Data box is connected** and simulations are explicitly selected.

```{figure} ../../_static/images/tetrad-interface/box-by-box/grid-search-box-simulation.png
:name: tetrad-grid-search-box-screenshot
:alt: Grid Search Box in the Tetrad interface.

Grid Search Box in the Tetrad interface sidebar and main panel.
```

---

## When to Use Simulation-Based Grid Search

Simulation-based Grid Search is appropriate when:

- you want to compare algorithms against **known ground truth**,
- you want to study the effects of:
    - graph density,
    - sample size,
    - noise distributions,
    - nonlinearity,
    - latent variables,
- or you want to reproduce or extend results from the literature.

If you already have real data, use the **data-driven Grid Search workflow** instead.

---

## Overview of the Workflow

A typical simulation study proceeds as follows:

1. **Select one or more simulations** (Simulation tab)
2. **Choose algorithms** to evaluate (Algorithms tab)
3. **Choose table columns** to summarize performance (Table Columns tab)
4. **Configure and run the comparison** (Comparison tab)
5. **Inspect estimated graphs and statistics** (View Graphs tab)

Each step may involve parameter sweeps, producing a large number of runs.

---

## Simulation Tab

### Selecting Simulations

Click **Select Simulation** to define a simulation by choosing:

- a **graph type** (e.g., Erdős–Rényi, Scale-Free, MIM),
- a **simulation model** (e.g., Linear SEM, Additive Noise, General Noise).

Each selected simulation represents a *family* of data-generating processes.

### Multiple Simulations

In simulation mode, Grid Search supports **multiple simulations**:

- each simulation is run independently,
- results are grouped by simulation index,
- comparisons aggregate over runs within each simulation.

This is useful for comparing algorithm performance across regimes.

### Editing Simulation Parameters

Click **Edit Parameters** to set simulation parameters such as:

- number of variables,
- expected degree,
- sample size,
- noise distribution parameters.

Comma-separated values trigger **parameter sweeps**, producing multiple datasets per simulation.

---

## Algorithms Tab

Algorithm selection works the same way as in data-driven Grid Search:

- choose algorithms,
- choose compatible independence tests and/or scores,
- edit algorithm parameters via **Edit Parameters**.

In simulation studies, it is common to:

- sweep penalty parameters,
- compare constraint-based vs score-based methods,
- compare algorithms under model misspecification.

The **Manage...** dialog lets you remove or reorder algorithms.

---

## Table Columns Tab

Table columns define how algorithm performance is summarized.

In simulation studies, common columns include:

- adjacency precision / recall,
- arrowhead precision / recall,
- structural Hamming distance (SHD),
- number of edges,
- elapsed time.

Parameter columns can be included to track experimental settings.

Use **Manage...** to remove or reorder columns.

---

## Comparison Tab

### Setup Panel

The setup panel exposes key comparison controls:

- **Comparison Graph Type**
    - DAG, CPDAG, PAG, etc., depending on assumptions.
- **# Runs**
    - Number of independent datasets generated per parameter setting.
- **Parallelism**
    - Number of threads used during comparison.
- **Sort by Utility**
    - Useful when aggregating multiple statistics.

### Running the Comparison

Click **Run Comparison** to execute the study.

Grid Search will:

- generate data,
- run all algorithm/parameter combinations,
- compute statistics,
- aggregate results over runs.

Progress and diagnostics appear in **Verbose Output**.

---

## View Graphs Tab

This tab allows inspection of individual estimated graphs:

- select a simulation index,
- select an algorithm index,
- select a graph index.

Graphs are laid out automatically and can be sent to other tools for inspection.

---

## Interpreting Results

Simulation-based Grid Search enables principled conclusions such as:

- which algorithms recover structure most accurately,
- how performance degrades under misspecification,
- which assumptions matter most in practice.

Because ground truth is known, simulation studies provide insight that is **impossible with real data alone**.

---

## Saved Output

Grid Search saves:

- generated datasets,
- true graphs,
- estimated graphs,
- comparison tables,
- verbose logs.

These files support reproducibility and downstream analysis in R or Python.

---

## Relationship to Data-Driven Grid Search

- **Simulation Grid Search** answers:  
  *“Which methods work well under known assumptions?”*

- **Data-Driven Grid Search** answers:  
  *“Which methods produce models consistent with this data?”*

Both workflows share the same interface but serve different scientific goals.

---

## Reference

Ramsey, J. D., Malinsky, D., & Bui, K. V. (2020).  
*Algcomparison: Comparing the performance of graphical structure learning algorithms with Tetrad.*  
Journal of Machine Learning Research, 21(238), 1–6.