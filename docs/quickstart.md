# Quickstart

A **five-minute tour** of Tetrad: from loading data to viewing your first causal graph.

This guide assumes you have already **launched the Tetrad GUI**.  
For installation instructions, see the **Tetrad GUI setup page**:
https://www.cmu.edu/dietrich/philosophy/tetrad/use-tetrad/tetrad-application.html

---

You can begin using the Tetrad interface by clicking tools in the left toolbar and then clicking in the workbench (the large white area) to add **session nodes** to your project.

These nodes can be connected to form **flowcharts** representing your causal-discovery workflow.  
To connect two boxes:

1. Select the **arrow tool** in the toolbar.
2. Drag an arrow from one box to another.

If a connection is not permitted (e.g., incompatible box types), the arrow will simply not attach.

Several ready-made workflows (“pipelines”) can be created from the **Pipelines** menu at the top.

---

## 1. Load or Simulate Data

### **Option A — Load a dataset from file**
1. Place a **Data** box on the workbench and double-click it.
2. Click **Load Data…**
3. Select your file:
    - Tabular data: CSV, TSV, or whitespace-delimited
    - Covariance matrix with sample size  
      (see the **Data Formats** page for details)
4. Confirm variable types if prompted.

If the format is valid, your dataset will appear in the Data box.

---

### **Option B — Simulate data from a causal model**
1. Place a **Simulation** box on the workbench.
2. Choose a generator:
    - Multinomial Bayes model
    - Linear SEM
    - Nonlinear SEM
    - Additive nonlinear model
    - etc.
3. Specify:
    - Number of variables
    - Sample size
    - Noise/error settings
    - Any other parameters offered for your generator
4. Click **Simulate**.

The generating graph and the simulated dataset will appear in separate tabs inside the Simulation box.

---

## 2. (Optional) Add Prior Knowledge

Prior knowledge helps constrain the search and improve interpretability.

1. Place a **Knowledge** box on the workbench.
2. Connect your Data or Simulation box to it using an arrow so the Knowledge box knows which variables it applies to.

You may then define:

- **Required edges**
- **Forbidden edges**
- **Temporal tiers / background knowledge**
- Other options exposed in the Knowledge box

Knowledge can be saved and reused.

When running a search, connect your **Data box** and **Knowledge box** to the **Search box**. Any compatible search algorithm will respect the knowledge constraints.

> **Tip:** Try running a search *with* and *without* knowledge to see how it influences the resulting graph.

---

## 3. Run a Causal Search

Place a **Search** box on the workbench.  
Connect your Data box (and Knowledge box, if desired) to it with arrows, then double-click the Search box and choose an algorithm.

Your choice depends on the assumptions you are making about the data.

For a description of the target graph types, see the **Graph Formats** page.

### **If you assume _no hidden confounders_ (target: DAG/CPDAG):**
- **PC** — classic constraint-based
- **FGES** — fast score-based
- **BOSS** — order-based; often produces very sharp orientations

### **If hidden confounders may be present (target: PAG):**
- **FCI** — canonical method
- **GFCI** — hybrid score+test
- **BOSS-FCI** — score-assisted hybrid
- **FCIT** — targeted-testing hybrid; reduces spurious CI calls (experimental)

These are the **recommended first-try algorithms**.  
More algorithms appear in the full list.

---

### Configure and run
1. Select the dataset.
2. Choose the algorithm.
3. (Optional) Attach **Knowledge**.
4. Adjust parameters:
    - `alpha` (significance level for CI tests)
    - Score penalty (e.g., BIC `c`)
    - Depth
    - Number of threads
    - Other algorithm-specific settings
5. Click **Run Search and Generate Graph**.

A causal graph (DAG, CPDAG, or PAG) will appear in a **Graph** box.

You may return to the parameter screen to rerun the search with different settings.

---

## 4. Inspect and Interact with the Graph

Place a **Graph** box on the workbench and double-click it.  
Alternatively, draw an arrow from a Search box to a Graph box.

In the Graph box you can:

- **Manually edit**
    - Add or remove edges
    - Orient edges
    - Highlight colliders or other features
- **Run legality checks** to ensure your graph is a legal DAG/MAG/PAG
- Explore paths, adjustment sets, and graph properties
- Convert graph types (e.g., DAG → PAG equivalence class)
- Use right-click menus for quick editing and inspection

Examples of available tools:

- **Graph → Graph Properties**: summary stats
- **Graph → Paths**: list paths, compute adjustment sets
- **Graph → Highlight**: cycles, colliders, structures
- **Graph → Check Graph Type**: test whether the graph is a DAG/CPDAG/PDAG/MAG/PAG
- **Graph → Manipulate Graph**: convert or simplify graphs

These tools help you interpret and refine the learned structure.

---

## 5. (Optional) Compare Graphs & Estimate Effects

### **Compare graphs**
Add a **Compare** box to the workbench to examine:

- Differences in adjacencies
- Differences in orientations
- Precision/recall metrics
- Algorithm-vs-algorithm comparisons
- Sample-size-vs-sample-size differences

This is useful for:
- Benchmarks
- Stability analysis
- Assessing prior-knowledge impact

---

### **Estimate causal effects**

Add an **Estimate** box and connect a **PM box** (parameter model) and a **Data box** to it.

With these, you can:

- Estimate parameters of a parameterized model
- Compute model fit statistics
- Inspect regression coefficients, noise variances, etc.

PM boxes can be created by connecting a Graph box to a PM box.

---

## 6. Save, Export, and Iterate

Once satisfied:

- **Save** the project to preserve datasets, graphs, and knowledge.
- **Export**:
    - Graph images (PNG, SVG, PDF)
    - Graph files (multiple formats)
    - Parameter tables or CSV summaries

You can then iterate: adjust parameters, explore alternative algorithms, refine knowledge, or simulate additional data.

---

From here, continue to the **User Guide** for in-depth descriptions of each GUI component,  
or the **Algorithms** page for detailed behavior of each causal-discovery method.