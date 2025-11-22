# Search Box

```{figure} ../../_static/images/tetrad-interface/box-by-box/search-box.png
:name: tetrad-search-box-screenshot
:alt: Search Box in the Tetrad interface.

Search Box in the Tetrad interface sidebar and main panel.
```

## Purpose

The **Search** box is where you run **causal discovery algorithms** in Tetrad. It connects:

- one or more **datasets** (from the *Data* box),
- an **independence test** and/or **score** (depending on the algorithm),
- optional **background knowledge** (from the *Knowledge* box),
- and an **algorithm** (e.g., PC, FCI, GFCI, FGES, BOSS, GRaSP),

and produces one or more **graphs** that appear in the *Graph* box.

Typical uses include:

- Learning causal graphs from observational or simulated data.
- Comparing different algorithms or parameter choices on the same dataset.
- Incorporating background knowledge to refine the search.

## Typical workflow

1. **Choose data and (optionally) knowledge**
   - In the *Data* box, load or select the dataset you want to analyze.
   - In the *Knowledge* box, specify any background knowledge (forbidden/required edges, tiers)
     you want to impose.
   - In the Search box, select:
     - The dataset.
     - The (optional) knowledge object.

2. **Select a search algorithm**
   - From the algorithm drop-down, choose an appropriate method, for example:
     - **Constraint-based**: PC, FCI, RFCI, CFCI, FCIT, etc.
     - **Score-based**: FGES, BOSS, GRaSP, etc.
     - **Hybrid**: GFCI, GRaSP-FCI, BOSS-FCI, etc.
   - Once you select an algorithm, its parameter panel appears (e.g., alpha, penalty discount,
     maximum path length).

3. **Configure test and/or score**
   - For constraint-based algorithms:
     - Choose an independence test (e.g., Fisher Z, G², KCI).
     - Set parameters such as significance level (alpha).
   - For score-based algorithms:
     - Choose a score (e.g., SEM BIC, Bayes score).
     - Set score-related parameters (e.g., penalty discount).
   - For hybrid algorithms, configure both as required.

4. **Run the search**
   - Click **Search** or **Run**.
   - Progress and messages (e.g., number of tests, warnings) appear in a log or status area.

5. **Inspect resulting graphs**
   - The search output is one or more graphs added to the *Graph* box.
   - In the Search box, you may also see:
     - A summary of the algorithm’s run.
     - References to the resulting graph objects.
   - Switch to the *Graph* box to edit, visualize, and export the learned graphs.

## Key controls

- **Toolbar**
  - **New / Configure** – set up a new search specification.
  - **Run / Search** – execute the current search.
  - **Stop** – interrupt a long-running search.
  - **Duplicate** – clone an existing search configuration for small variations.
  - **Export log** – save run details, when supported.

- **Search setup panel**
  - Drop-downs for:
    - Dataset.
    - Knowledge (optional).
    - Algorithm.
    - Independence test (if applicable).
    - Score (if applicable).
  - Fields for algorithm parameters:
    - Alpha levels, penalty discounts, maximum depth, etc.
  - Flags for:
    - Allowing latent variables or selection bias (for FCI-style algorithms).
    - Verbose logging or experimental options (depending on version).

- **Results / log panel**
  - Summary of:
    - Which dataset and knowledge were used.
    - Which algorithm, test, and score were chosen.
    - Number of tests or score evaluations performed.
  - References to the resulting graph(s) created in the *Graph* box.

## Common patterns & tips

- Choose algorithms that **match the assumptions** of your setting:
  - Use FCI-style methods when latent confounders or selection bias are plausible.
  - Use PC or FGES when you are comfortable assuming no latent variables or selection.
- Use **background knowledge** (from the *Knowledge* box) whenever you have strong prior
  constraints; this can improve both correctness and efficiency.
- When exploring parameter sensitivity:
  - Duplicate a search configuration and vary one parameter at a time (alpha, penalty, etc.).
  - Use the *Compare* box to contrast the resulting graphs.

## Related pages

- `Tetrad Interface → Overview` – high-level tour of the GUI.
- Other boxes that commonly interact with **Search**:
  - *Data* (provides datasets as input).
  - *Knowledge* (supplies background constraints).
  - *Graph* (receives the learned graphs).
  - *Compare* (compares graphs from different searches).
  - *Grid Search* (runs many searches over parameter grids).
