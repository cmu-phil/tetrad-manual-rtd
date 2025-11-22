# Running Algorithms

Tetrad’s interface provides a unified way to configure and run many different **search algorithms** and related
procedures (e.g., adjustment, IDA, stability methods).

[//]: # (```{note})

[//]: # (Suggested screenshots:)

[//]: # ()
[//]: # (1. The dialog or panel for configuring a search algorithm &#40;e.g., FGES or PC&#41;.)

[//]: # (   Save as: ``../../_static/images/tetrad-interface/overview/algorithm-config-dialog.png``.)

[//]: # (2. A parameter table or panel showing the algorithm’s tunable settings.)

[//]: # (   Save as: ``../../_static/images/tetrad-interface/overview/algorithm-parameters.png``.)

[//]: # (```)

![](../../_static/images/tetrad-interface/overview/algorithm-config-dialog.png)

![](../../_static/images/tetrad-interface/overview/algorithm-parameters.png)

## Launching a search

Typical steps:

1. Ensure you have a **data node** (and optionally an initial graph or background knowledge).
2. Choose an algorithm from the **Search / Algorithms** menu or a dedicated toolbar button.
3. A configuration dialog appears where you select:
    - The **data set** to use.
    - A **test and/or score** (depending on the algorithm).
    - The **graph type** to produce (e.g., DAG, CPDAG, PAG) if configurable.
    - Algorithm-specific **parameters**.

After clicking **Run** (or equivalent), Tetrad will:

- Execute the algorithm.
- Create one or more **result graphs** (and possibly tables) in the project tree.
- Optionally open the main result graph immediately in the work area.

## Choosing tests and scores

The configuration dialog typically restricts the available tests and scores to those compatible with your data:

- For **continuous** data: SEM-BIC, Gaussian BIC, Fisher Z test, etc.
- For **discrete** data: discrete BIC, G-square, chi-square-based tests.
- For **mixed or nonlinear** cases: basis-function scores, kernel tests, and more.

For details on individual tests/scores and their parameters, see the **Tests & Scores** section of the manual.

## Setting parameters

Each algorithm has a set of named parameters (e.g., `alpha`, `penaltyDiscount`, `maxDegree`). In the GUI:

- These are typically shown in a **table or form**.
- Default values are provided.
- Some parameters accept integer or real values; others are booleans, enums, or lists.

The **Parameters** section of the manual lists and explains these settings in detail. The GUI’s goal is to present
them in a consistent way and remember your choices between runs (within the current session).

## Running and monitoring

When you click **Run**:

- The status bar shows that the algorithm is executing.
- For some algorithms, a **progress bar** or approximate progress indicator is shown.
- Long-running algorithms may be cancellable from the status bar or dialog.

Upon completion:

- New result nodes (graphs, tables, reports) appear under a dedicated branch in the project tree.
- The primary result graph often opens automatically in the editor.

## Re-running with modified settings

You can usually:

- **Re-open** a previously configured algorithm node.
- Adjust parameters, tests, or scores.
- Run again to generate a new set of results.

This makes it easy to do small parameter sweeps manually, or to try different assumptions (e.g., with vs. without
selection bias, different background knowledge, etc.).

For larger parameter grids, see the **Grid Search** page in this section.
