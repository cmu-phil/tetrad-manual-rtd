# Grid Search Box (Data)

This page describes how the **Grid Search** box behaves when it is connected to a **Data box**.  
In this mode, Grid Search performs **systematic comparison of causal discovery methods on a fixed dataset**.

No simulations are run in this mode. All results are deterministic and fully reproducible.

---

## Purpose of Data-Based Grid Search

When operating on supplied data, Grid Search is designed to help you:

- Compare **algorithms, tests, scores, and parameter settings**
- Evaluate candidate models using **diagnostics** (e.g., Markov checking)
- Identify **simple, Markov-consistent models**
- Assess **robustness** of features across reasonable modeling choices

This is the recommended default workflow for causal discovery in Tetrad.

---

## When This Mode Is Used

Grid Search automatically enters **data mode** when:

- A **Data box** is connected to the Grid Search box, and
- No simulation is selected.

In this case:

- Simulation controls are hidden or disabled
- Each algorithm–parameter combination is evaluated **once**
- Results reflect only variation across modeling choices, not random variation

---

## Basic Setup

To use Grid Search with data:

1. Load your dataset into a **Data box**
2. Draw an edge from the Data box to the **Grid Search** box
3. Open the Grid Search editor

The editor will configure itself for data-based comparison.

---

## Algorithms Tab

In the **Algorithms** tab, you select:

- One or more **causal discovery algorithms**
- Required **independence tests** and/or **scores**
- Parameter ranges for algorithms, tests, and scores

Parameter values may be entered as comma-separated lists.  
Grid Search will evaluate **all combinations** of the selected parameters.

Only tests and scores compatible with the data type (continuous, discrete, mixed) are shown.

---

## Table Columns Tab

In the **Table Columns** tab, you choose which quantities appear in the comparison table.

Available columns include:

- Algorithm and parameter values
- Model complexity measures (e.g., number of edges)
- Diagnostic statistics (e.g., Markov check results)

When working from data, **statistics that require knowledge of the true graph are not shown**, since no ground truth is available.

Columns may be added, reordered, or removed using the **Add** and **Manage** buttons.

---

## Comparison Tab

The **Comparison** tab controls how results are evaluated and displayed.

Key options include:

- **Comparison graph type** (e.g., CPDAG or PAG)
- **Markov Checker test**
- **Utility settings** for ranking models

When you click **Run Comparison**, Grid Search:

1. Runs each selected algorithm for every parameter combination
2. Evaluates resulting graphs using selected diagnostics
3. Populates the comparison table with results

Progress and detailed output are shown in the **Verbose Output** tab.

---

## Interpreting Results

Each row in the comparison table corresponds to a distinct model.

Typical analysis focuses on:

- Whether the model **passes Markov checking**
- Model **complexity** (e.g., number of edges)
- Stability of features across nearby parameter settings

Rather than selecting the single highest-utility model, it is usually more informative to identify **minimal models that pass diagnostics**.

---

## View Graphs Tab

After a comparison is complete, the **View Graphs** tab allows you to inspect individual output graphs.

- Selecting a row in the table highlights the corresponding graph
- Graph selections are remembered when the editor is reopened

This makes it easy to compare candidate models visually.

---

## Notes and Best Practices

- Sweep only a small number of meaningful parameters at a time
- Prefer systematic comparison over isolated runs
- Use diagnostics early to detect mismatched assumptions
- Treat fragile edges and orientations with caution

---

## Summary

When connected to data, the Grid Search box provides a structured, reproducible way to:

- Explore algorithm and parameter sensitivity
- Evaluate candidate causal models
- Identify parsimonious models consistent with the data

This mode forms the backbone of Tetrad’s recommended causal discovery workflow.
