# Grid Search Box (Data-Driven)

The **Grid Search** tool helps you compare causal discovery algorithms on a *single dataset* in a systematic, reproducible way. It is designed to reduce cognitive load while still supporting careful methodological choices—especially around **Markov checking**.

This page describes the **current** Grid Search interface and recommended workflow when a **Data box** is connected. The tool can also be used **without** a Data box, for example, to compare algorithms on simulated data. In both cases, knowledge (a Knowledge box) may be used as an additional input.

```{figure} ../../_static/images/tetrad-interface/box-by-box/grid-search-box-data.png
:name: tetrad-grid-search-box-screenshot
:alt: Grid Search Box in the Tetrad interface.

Grid Search Box in the Tetrad interface sidebar and main panel.
```

## What Grid Search Is (and Is Not)

**Grid Search is for model selection, not deep diagnosis.**

- It lets you **compare algorithms and parameterizations** on the same data.
- It helps you **eliminate bad models** and **identify promising ones** using principled statistics.
- It is *not* a replacement for the standalone **Markov Checker** tool, which provides deeper diagnostics.

Think of Grid Search as a **front-end filter**: it narrows the space of models so that detailed analysis becomes feasible.

---

## Overview of the Workflow

When Grid Search is driven by data, the workflow is intentionally linear:

1. **Review the data summary** (Data tab)
2. **Choose algorithms** appropriate for the data (Algorithms tab)
3. **Choose table columns** to summarize results (Table Columns tab)
4. **Configure and run the comparison** (Comparison tab)
5. **Inspect candidate graphs** (View Graphs tab)
6. *(Optional)* Send selected graphs to the **Markov Checker** for deeper analysis

Each step is designed to be minimal, explicit, and reversible.

---

## Data Tab

When a dataset is connected:

- The dataset is treated as the **single fixed simulation**.
- Controls for adding simulations or setting simulation parameters are **hidden**.
- The tab summarizes:
    - number of variables and rows,
    - variable names,
    - supplied background knowledge (if any).

This ensures that Grid Search remains focused on **algorithm comparison**, not data generation.

---

## Algorithms Tab

### Adding Algorithms

Click **Add Algorithm** to choose:

- a causal discovery algorithm,
- an independence test *and/or* score **compatible with the data type**.

Only tests and scores that make sense for the data (continuous, discrete, or mixed) are shown. Invalid combinations are never offered.

### Managing Algorithms

Click **Manage...** to:

- remove selected algorithms,
- reorder algorithms (the order is preserved in output and saved state).

This replaces the old “Remove Last” behavior and provides precise control.

### Editing Algorithm Parameters

Click **Edit Parameters** to adjust algorithm, test, score, and bootstrapping parameters.

- Parameters are organized into tabs.
- Tabs appear *only if relevant parameters exist*.
- Comma-separated values trigger **parameter sweeps**.

---

## Table Columns Tab

Table columns define what statistics appear in the comparison table.

### Adding Columns

Click **Add Table Column(s)** to select:

- statistics (e.g., number of edges, Markov pass indicators),
- parameter columns (values actually used in the run).

Helpful shortcuts include:

- **Used Parameters** – select all user-set parameters
- **Used Statistics** – select statistics used in the previous run
- **Markov Defaults** – quickly select standard Markov-checking columns

### Managing Columns

Click **Manage...** to:

- remove selected columns,
- reorder columns.

The order you choose is the order shown in results.

---

## Comparison Tab

This is where Grid Search is configured and executed.

### Setup Panel (Top)

The setup panel exposes the most important controls directly:

- **Comparison Graph Type** (e.g., DAG, CPDAG, PAG)
- **Sort by Utility** (recommended when doing Markov-based selection)
- **Markov Checker Test** (filtered to data-compatible tests)
- **Markov Checker Parameters**

If no dataset is supplied (rare), a **# Runs** control is shown; otherwise it is hidden.

### Running the Comparison

Click **Run Comparison** to execute the grid search.

- Results appear in the **Comparison** tab.
- Detailed logs appear in **Verbose Output**.
- All results are saved to disk for reproducibility.

---

## View Graphs Tab

This tab lets you inspect estimated graphs produced by the comparison.

- Select an **algorithm** and **graph index**.
- The selected graph is remembered when the editor is reopened.
- The graph can be connected to other Tetrad tools for further analysis.

Since the simulation is fixed, there is no simulation selector here.

---

## Markov Checking: Recommended Practice

Grid Search uses a **fixed conditioning-set strategy** internally (typically *Ordered Local Markov MAG*).

This is intentional:

- It avoids overwhelming users with rarely-appropriate choices.
- It yields stable, comparable results across algorithms.

If you want to:

- explore alternative conditioning-set strategies,
- diagnose specific violations,
- examine p-value distributions in detail,

**send the selected graph to the standalone Markov Checker tool.**

Grid Search helps you find *good candidates*; the Markov Checker helps you *understand them*.

---

## Saved Output

Grid Search saves:

- the comparison table,
- selected graphs,
- parameter settings,
- verbose logs.

These files can be used for follow-up analysis in Tetrad, R, or Python.

---

## Key Design Principles

- **One dataset → one simulation**
- **Impossible choices are removed** rather than guarded against
- **Management dialogs replace incremental undo**
- **Defaults support Markov-based model selection**
- **Advanced diagnostics live in dedicated tools**

The goal is to make principled causal discovery *approachable without being simplistic*.

---

## Reference

Ramsey, J. D., Malinsky, D., & Bui, K. V. (2020).  
*Algcomparison: Comparing the performance of graphical structure learning algorithms with Tetrad.*  
Journal of Machine Learning Research, 21(238), 1–6.