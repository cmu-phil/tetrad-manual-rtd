# Quickstart

A **five-minute tour** of Tetrad: from loading data to seeing your first causal graph.

This guide assumes you have already **launched the Tetrad GUI**.

For installation instructions, see the  
**[official Tetrad GUI setup page](https://www.cmu.edu/dietrich/philosophy/tetrad/use-tetrad/tetrad-application.html)**.

---

## 1. Load or Simulate Data

### **Option A — Load a dataset from file**
1. Open the **Data box**.
2. Click **Load Data…**
3. Select your file:
    - Tabular data (CSV, TSV, whitespace-delimited)
    - Covariance matrix (with sample size)
4. Confirm variable types if prompted.

Your dataset will now appear in the Data box.

---

### **Option B — Simulate data from a causal model**
1. Open **Simulation Tools**.
2. Choose a generator:
    - Linear SEM
    - Nonlinear SEM
    - User-defined models
3. Specify:
    - Number of variables
    - Sample size
    - Noise/error settings
4. Click **Generate**.

Your simulated dataset will appear alongside any loaded datasets.

---

## 2. (Optional) Add Prior Knowledge

Prior knowledge helps constrain the search and improve interpretability.

Open the **Knowledge box** to define:

- **Required edges**
- **Forbidden edges**
- **Tiers / background knowledge** (“X must come before Y”)
- **Selection variables** or **interventions**

You can save knowledge for reuse across multiple algorithms.

> Tip: Try searches *with* and *without* knowledge to see how it affects the output graph.

---

## 3. Run a Causal Search

Open the **Search box** and choose:

### **If you assume *no hidden confounders* (target: DAG/CPDAG):**
- **PC** (classic constraint-based)
- **FGES** (fast, score-based)
- **BOSS** (order-based; often sharp orientations)

### **If hidden confounders may be present (target: PAG):**
- **FCI** (canonical method)
- **BOSS-FCI** (score-assisted hybrid)
- **FCIT** (targeted-testing hybrid; fewer spurious independences; experimental)

These are the **recommended first-try algorithms**.  
More algorithms are available in the full list.

---

### Configure and run
1. Choose the dataset.
2. Select the algorithm.
3. (Optional) Attach **Knowledge**.
4. Adjust key parameters:
    - `alpha` (for CI tests)
    - score penalty (e.g., BIC `c`)
    - depth
    - number of threads
5. Click **Run**.

A causal graph (DAG, CPDAG, or PAG) appears in the **Graph box**.

---

## 4. Inspect and Interact with the Graph

In the **Graph box**, you can:

- Hover/click nodes and edges to view details
- Compute:
    - Paths
    - Subgraphs
    - Edge frequencies (with resampling)
- Manually:
    - Add or remove edges
    - Orient edges
    - Highlight colliders / definite structures
- Run **legality checks** to ensure the graph is a valid DAG/MAG/PAG

This is where you interpret and refine the structure.

---

## 5. (Optional) Compare Graphs & Estimate Effects

### **Compare graphs**
Open the **Compare box** to assess:

- Adjacency differences
- Orientation differences
- Precision/recall-style metrics
- Algorithm-vs-algorithm or sample-size-vs-sample-size comparisons

Useful for:
- Evaluating multiple algorithms
- Stability analysis
- Checking effect of prior knowledge

---

### **Estimate causal effects**

With the estimated graph, you can:

- Compute **adjustment sets**
- Estimate **total effects** (IDA + PAG-IDA variants)
- Explore **edge-specific** or **path-specific** effects (where supported)

These tools appear in various dialogs under **Graph**, **Search**, or dedicated effect estimation interfaces.

---

## 6. Save, Export, and Iterate

Once satisfied:

- **Save** the project to preserve datasets, graphs, and knowledge.
- **Export**:
    - Graph images (PNG, SVG, PDF)
    - Graph structures (various formats)
    - Parameter tables or CSV summaries

Then iterate—adjust parameters, try alternative algorithms, or refine knowledge.

---

## 📦 Screens & GUI Reference

These links point to the structured HTML pages bundled with the manual:

- **What’s New**  
  👉 [`whats-new.html`](./_static/manual/whats-new.html)

- **Graph Box**  
  👉 [`graph-box.rewrite.html`](./_static/manual/graph-box.rewrite.html)

- **Compare Box**  
  👉 [`compare-box.rewrite.html`](./_static/manual/compare-box.rewrite.html)

- **Search Box**  
  👉 [`search-box.rewrite.html`](./_static/manual/search-box.rewrite.html)

- **Knowledge Box**  
  👉 [`knowledge-box.rewrite.html`](./_static/manual/knowledge-box.rewrite.html)

---

From here, continue to the **User Guide** for detailed explanations of each GUI component,  
or the **Algorithms** page for deeper discussion of algorithm behavior.