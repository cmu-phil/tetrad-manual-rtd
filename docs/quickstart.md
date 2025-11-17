# Quickstart

A **five-minute walkthrough**: load data → run a search → view your first causal graph.

This guide assumes the **Tetrad GUI is already running**. (If not see the [**Tetrad GUI setup page**](https://www.cmu.edu/dietrich/philosophy/tetrad/use-tetrad/tetrad-application.html).)

---

## 1. Add a Data or Simulation Box

### Option A — Load data
1. Add a **Data** box from the left toolbar.
2. Double-click it → **Load Data…**
3. Choose a CSV/TSV/whitespace file (or a covariance matrix).
4. Confirm variable types if prompted.

Your dataset now appears in the Data box.

### Option B — Simulate data
1. Add a **Simulation** box.
2. Choose a generator (linear SEM, nonlinear SEM, etc.).
3. Enter number of variables and sample size.
4. Click **Simulate**.

A graph and dataset appear inside the Simulation box.

---

## 2. (Optional) Add Prior Knowledge

If you have background knowledge:
1. Add a **Knowledge** box.
2. Draw an arrow **from the Data/Simulation box → to the Knowledge box**.
3. Specify required edges, forbidden edges, or tiers.

You may skip this step for your first run.

---

## 3. Run a Causal Search

1. Add a **Search** box.
2. Draw an arrow **from the Data box → to the Search box**  
   (and from the Knowledge box if you're using one).
3. Double-click the Search box and choose an algorithm:
    - **PC**, **FGES**, **BOSS** — if no hidden confounders (DAG/CPDAG)
    - **FCI**, **GFCI**, **BOSS-FCI** — if hidden confounders are possible
4. Set parameters if needed.
5. Click **Run Search and Generate Graph**.

A completed **Search box** now contains the learned graph.

---

## 4. View and Edit the Graph

To work with the graph directly:

1. Add a **Graph** box to the workbench.
2. Draw an arrow **from the Search box → to the Graph box**.

Double-click the Graph box to view the graph.

Here you can:
- Add/remove/orient edges
- Highlight colliders or paths
- Check whether it's a DAG/CPDAG/PAG
- Inspect properties and adjustment sets

(You *can* preview the graph inside the Search box, but the **Graph box** is where full interaction happens.)

---

## 5. Save and Export

- **Save** the project (File → Save Project)
- **Export** graphs (PNG, SVG, PDF, or structural formats)

---

You now have a full causal workflow:  
**data → search → editable graph**.

Explore the **User Guide** for more features,  
or the **Algorithms** page for details on each search method.