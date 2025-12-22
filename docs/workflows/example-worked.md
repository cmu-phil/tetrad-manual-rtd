# Example: Auto MPG Analysis with Grid Search

This page walks through a complete causal analysis workflow in Tetrad using the **Auto MPG** dataset.  
It illustrates how to move from data exploration to model selection using **Grid Search** and **Markov checking**, following the default workflow recommended in this manual.

The goal is not to assert a single “true” causal graph, but to show how to identify a **minimal, Markov-consistent model** under clearly stated assumptions.

---

## 1. The Auto MPG Dataset

We use the Auto MPG dataset available from the CMU causal datasets repository:

- Repository:  
  https://github.com/cmu-phil/example-causal-datasets
- Data file used:  

real/auto-mpg/data/auto-mpg.data.mixed.max.3.categories.txt

### Data Preparation

Before loading the data into Tetrad, we made two preprocessing decisions:

1. **Removed the car name field**, which is an identifier and not suitable for causal modeling.
2. **Removed rows with missing values**, to simplify the analysis and avoid complications from missing-data handling.

The resulting dataset contains:

- Continuous variables such as `mpg`, `weight`, `horsepower`, etc.
- One discrete variable (`origin`) with **three categories**.

Because of this mixture, the data should be loaded as **mixed data** with a maximum of **3 categories**, as indicated in the file name.

---

## 2. Loading and Exploring the Data in Tetrad

1. Load the dataset into a **Data box**.
2. Specify that the data are **mixed**, with a maximum of 3 categories.

### Visual Exploration

```{figure} ../../_static/images/tetrad-interface/box-by-box/example-data-plotmatrix.png
:name: tetrad-grid-search-box-screenshot
:alt: Plot matrix for the Auto-MPG data.
```

Using the **Plot Matrix** tool in the Data box, we observe:

- Strong approximately **linear trends** among many pairs of variables
- No obvious nonlinear clusters or discontinuities
- Reasonable support for linear-Gaussian modeling assumptions

This visual evidence suggests that **linear Gaussian methods** are appropriate, even in the presence of one discrete variable.

---

## 3. Algorithm Choice and Assumptions

### Causal Sufficiency

For this example, we **assume causal sufficiency**:

- All major common causes of the measured variables are assumed to be observed.
- We therefore search for a **CPDAG** (a Markov equivalence class of DAGs), rather than a PAG.

This is a modeling assumption, not a fact — but it is reasonable for this example and keeps the workflow simple.

### Algorithm: BOSS

We choose **BOSS**, a score-based search algorithm, because:

- It performs well in linear settings
- It scales well for systematic exploration
- It integrates naturally with score-based model comparison

### Score: Degenerate Gaussian BIC

Based on data exploration, we select the **Degenerate Gaussian BIC score**, which:

- Is appropriate for **mixed data**
- Matches the approximately linear structure seen in the plot matrix
- Is compatible with BOSS and Markov checking using DG-LRT

---

## 4. Setting Up the Grid Search

### Step 1: Connect the Data

- Draw an edge from the **Auto MPG Data box** to a **Grid Search** box.

This configures Grid Search to operate directly on the dataset.

---

### Step 2: Algorithms Tab

1. Go to the **Algorithms** tab.
2. Click **Add Algorithm**.
3. Select **BOSS**.
4. Choose **Degenerate Gaussian BIC** as the score.

At this point, do *not* yet enter parameter ranges.

---

### Step 3: Table Columns Tab

1. Go to the **Table Columns** tab.
2. Click **Add Table Column(s)**.
3. In the dialog, click **Markov Check Columns**.

> **Note:** At present, there is a UI bug where you must scroll all the way down to ensure all relevant columns are selected.  
> (This will be fixed in a future release.)

4. Click **Add**.

The selected Markov check statistics should now appear in the table columns list.

---

### Step 4: Comparison Tab (Initial Setup)

In the **Comparison** tab:

- Set **Comparison Graph Type** to **CPDAG**
- Set **Sort by Utility** to **Yes**
- Set **Markov Checker Test** to  
  **DG-LRT (Degenerate Gaussian Likelihood Ratio Test)**

If you click **Edit Utilities**, you will see that utilities have already been configured for the default Markov check statistics.

---

### Step 5: Set Parameter Ranges

Now return to the **Algorithms** tab:

1. Click **Edit Parameters**
2. Open the **Scores** section
3. For **Penalty Discount**, enter the following range:

1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6

This range explores a spectrum from relatively dense to relatively sparse models.

---

## 5. Running the Comparison

1. Return to the **Comparison** tab.
2. Click **Run Comparison**.

Grid Search will now:

- Run BOSS for each penalty discount value
- Compute Markov check statistics for each resulting CPDAG
- Summarize results in the comparison table

```{figure} ../../_static/images/tetrad-interface/box-by-box/example-data-comparison.png
:name: tetrad-grid-search-box-screenshot
:alt: Comparison result for the Auto-MPG data.
```

---

## 6. Interpreting the Comparison Results

In the comparison table, focus on two columns:

- **MC-KSPass**  
  Indicates whether the model passes the Markov check
- **#EdgesEst**  
  Indicates model complexity

You will typically observe that:

- Very sparse models fail Markov
- Very dense models pass but are unnecessarily complex
- Several intermediate models pass Markov

### Choosing a Model

Among the rows where **MC-KSPass = 1**, select the model with the **fewest edges**.

In this example, that corresponds to:

- **Algorithm = 6**

This represents a **minimal Markov-consistent CPDAG** under the chosen assumptions.

```{figure} ../../_static/images/tetrad-interface/box-by-box/example-data-graph6.png
:name: tetrad-grid-search-box-screenshot
:alt: Comparison result for the Auto-MPG data.
```

---

## 7. Viewing the Selected Graph

1. Go to the **View Graphs** tab.
2. Select **Algorithm = 6**.

The displayed graph is the final candidate model for this analysis.

This graph:

- Is consistent with observed conditional independences
- Is relatively sparse
- Reflects the assumptions made (causal sufficiency, linearity, DG score)

---

## 8. What This Example Demonstrates

This worked example illustrates a **complete default workflow** in Tetrad:

1. Explore the data visually
2. Choose assumptions explicitly
3. Use Grid Search to explore parameter sensitivity
4. Evaluate candidates using Markov checking
5. Select a minimal model that passes diagnostics

Rather than producing a single opaque output, this workflow emphasizes **justified model selection**.

---

## 9. Next Steps

From here, you may:

- Examine alternative assumptions (e.g., allowing latent variables)
- Feed the selected graph into the **Markov Checker** tool for deeper inspection
- Incorporate background knowledge and rerun the analysis
- Use the selected structure for causal effect estimation

This concludes the Auto MPG Grid Search example.