# Example: Auto MPG Analysis with Grid Search

This page walks through a complete causal analysis workflow in Tetrad using the **Auto MPG** dataset.  
It illustrates how to move from data exploration to model selection using **Grid Search** and **Markov checking**, following the default workflow recommended in this manual.

The goal is not to identify a single “true” causal graph, but to show how to arrive at a **minimal, Markov-consistent model** under clearly stated assumptions.

---

## 1. The Auto MPG Dataset

We use the Auto MPG dataset from the CMU causal datasets repository:

- Repository:  
  https://github.com/cmu-phil/example-causal-datasets
- Data file used:  

  `real/auto-mpg/data/auto-mpg.data.mixed.max.3.categories.txt`

### Data Preparation

Before loading the data into Tetrad, we made two simple preprocessing decisions:

1. **Removed the car name field**, which serves as an identifier and is not meaningful for causal modeling.
2. **Removed rows with missing values**, to keep the example focused on the core workflow rather than missing-data handling.

The resulting dataset contains:

- Several continuous variables (e.g., `mpg`, `weight`, `horsepower`)
- One discrete variable (`origin`) with **three categories**

Because of this mixture, the data should be loaded as **mixed data** with a maximum of **3 categories**, as indicated in the file name.

---

## 2. Loading and Exploring the Data in Tetrad

1. Load the dataset into a **Data box**.
2. Specify that the data are **mixed**, with a maximum of 3 categories.

### Visual Exploration

![Plot matrix for the Auto MPG data.](../../_static/images/tetrad-interface/box-by-box/example-data-plotmatrix.png)

Using the **Plot Matrix** tool in the Data box, we observe:

- Strong, approximately **linear relationships** among many pairs of variables
- No obvious nonlinear clusters or sharp discontinuities
- Patterns consistent with additive, roughly Gaussian noise

These observations suggest that **linear-Gaussian modeling assumptions** are reasonable for this dataset, even though one variable is discrete.

---

## 3. Algorithm Choice and Assumptions

### Causal Sufficiency

For this example, we **assume causal sufficiency**:

- All major common causes of the measured variables are assumed to be observed.
- We therefore search for a **CPDAG** (a Markov equivalence class of DAGs), rather than a PAG.

This is a modeling assumption made for illustration purposes; it simplifies the workflow and is reasonable for this dataset.

---

### Algorithm: BOSS

We choose **BOSS**, a score-based search algorithm, because:

- It performs well in linear settings
- It scales well for systematic exploration
- It integrates naturally with score-based model comparison

---

### Score: Degenerate Gaussian BIC

Based on data exploration, we select the **Degenerate Gaussian BIC** score:

- It is appropriate for **mixed data**
- It aligns with the approximately linear structure seen in the plot matrix
- It supports Markov checking via the **DG-LRT** test

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

At this point, leave parameter ranges unchanged.

---

### Step 3: Table Columns Tab

1. Go to the **Table Columns** tab.
2. Click **Add Table Column(s)**.
3. In the dialog, click **Markov Check Columns**.

> **Note:** At present, there is a UI issue that requires scrolling to the bottom of the dialog to ensure all relevant columns are selected.  
> (This will be addressed in a future release.)

4. Click **Add**.

The selected Markov-check statistics should now appear in the table-columns list.

---

### Step 4: Comparison Tab (Initial Setup)

In the **Comparison** tab:

- Set **Comparison Graph Type** to **CPDAG**
- Set **Sort by Utility** to **Yes**
- Set **Markov Checker Test** to  
  **DG-LRT (Degenerate Gaussian Likelihood Ratio Test)**

If you open **Edit Utilities**, you will see that default utilities for the Markov-check statistics are already configured.

---

### Step 5: Set Parameter Ranges

Return to the **Algorithms** tab:

1. Click **Edit Parameters**
2. Open the **Scores** section
3. For **Penalty Discount**, enter:

```
1, 1.2, 1.4, 1.6, 1.8, 2, 2.2, 2.4, 2.6, 2.8, 3, 3.2, 3.4, 3.6
```

This range spans models from relatively dense to relatively sparse.

---

## 5. Running the Comparison

1. Go back to the **Comparison** tab.
2. Click **Run Comparison**.

Grid Search will:

- Run BOSS for each penalty-discount value
- Compute Markov-check statistics for each resulting CPDAG
- Summarize the results in a comparison table

![Grid Search comparison results for the Auto MPG data.](../../_static/images/tetrad-interface/box-by-box/example-data-comparison.png)

---

## 6. Interpreting the Comparison Results

In the comparison table, two columns are especially informative:

- **MC-KSPass**  
  Indicates whether the model passes the Markov check
- **#EdgesEst**  
  Indicates model complexity

A common pattern is visible:

- Very sparse models fail Markov checking
- Very dense models pass but are difficult to interpret
- Several intermediate models pass Markov checks

---

### Choosing a Model

Among the rows where **MC-KSPass = 1**, select the model with the **fewest edges**.

In this example, that corresponds to:

- **Algorithm = 8**

This choice represents a **minimal Markov-consistent CPDAG** under the stated assumptions.

![Selected CPDAG for the Auto MPG example.](../../_static/images/tetrad-interface/box-by-box/example-data-graph8.png)

---

## 7. Viewing the Selected Graph

1. Open the **View Graphs** tab.
2. Select **Algorithm = 6**.

The displayed graph is the final candidate model for this analysis.

---

## 8. What This Example Illustrates

This worked example demonstrates a **complete default workflow** in Tetrad:

1. Explore the data visually
2. Make assumptions explicit
3. Use Grid Search to explore parameter sensitivity
4. Evaluate models using Markov checking
5. Select a minimal model that passes diagnostics

---

## 9. Next Steps

From here, you might:

- Explore alternative assumptions (e.g., allowing latent variables)
- Inspect Markov-check violations in more detail
- Incorporate background knowledge and rerun the analysis
- Use the selected structure for causal effect estimation

---

## Extension: Parameter Estimation with Mixed Data (Hybrid CG)

The analysis above focuses on **structure discovery**—identifying a Markov-consistent CPDAG for the Auto MPG data.
Tetrad also supports **parameter estimation** for *mixed discrete/continuous models*, allowing us to move beyond
graph structure and estimate quantitative causal relationships.

Because the Auto MPG dataset contains both continuous variables and a discrete variable (`origin`),
we use the **Hybrid Conditional Gaussian (Hybrid CG) estimator**.

### Hybrid CG Estimation Workflow

1. Add a **Hybrid CG Estimator** box.
2. Connect:
   - The selected DAG (PM) from the previous section
   - The Auto MPG data set
3. Use default settings:
   - Equal-frequency binning for continuous parents of discrete variables
   - Dirichlet pseudocount α = 1
4. Click **Estimate & Preview**.

The estimator fits:
- Linear-Gaussian regression models for continuous children
- Conditional probability tables for discrete children

[Hybrid CG estimator table image goes here]

---

## Example: Horsepower → Acceleration

One edge of interest in the selected DAG is:

```
horsepower → acceleration
```

The Hybrid CG estimator produces a regression coefficient of approximately:

```
-0.84
```

At first glance, the negative sign may seem surprising. However, interpreting this result correctly
requires understanding the semantics of the `acceleration` variable in this dataset.

---

## Interpreting the Acceleration Variable

In the Auto MPG dataset, **acceleration does not mean dv/dt**, as it would in physics.

Instead, it is defined as:

> **The time (in seconds) required to accelerate from 0 to 60 miles per hour.**

Under this definition:
- Larger values correspond to *slower* acceleration
- Smaller values correspond to *faster* acceleration

Therefore, a negative coefficient for horsepower → acceleration means:

> Increasing horsepower reduces the time required to reach 60 mph.

A scatterplot of acceleration versus horsepower confirms this relationship:

[Acceleration vs. horsepower scatterplot image goes here]

---

## Extension: Adjustment and Total Causal Effects

To cross-check the Hybrid CG estimate, we compute the **total causal effect**
of horsepower on acceleration using the **Adjustment / Total Effects** tool.

### Adjustment Workflow

1. Add an **Adjustment / Total Effects** box.
2. Use the same DAG (or CPDAG) identified earlier.
3. Set:
   - Treatment variable X = `horsepower`
   - Outcome variable Y = `acceleration`
4. Let Tetrad compute valid adjustment sets and estimate the total effect.

The estimated total causal effect is again approximately:

```
-0.84
```

[Adjustment total effects image goes here]

Because there is only a single directed path from horsepower to acceleration in the selected model,
the **direct effect and total effect coincide**, and the two independent estimation methods agree.

---

## What These Extensions Demonstrate

These extensions illustrate that Tetrad supports a **complete causal workflow** for mixed data:

- Structure discovery using Grid Search
- Parameter estimation using Hybrid CG models
- Causal effect estimation via adjustment
- Cross-validation of conclusions using independent tools

They also highlight an important practical lesson:

> **Correct causal interpretation depends on understanding variable definitions, not just algorithms.**

