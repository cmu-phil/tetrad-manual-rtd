# Example: Auto MPG Analysis with Grid Search (Extended)

This page walks through a complete causal analysis workflow in Tetrad using the **Auto MPG** dataset.
It illustrates how to move from data exploration to model selection using **Grid Search**, and then how to **estimate causal effects in mixed discrete/continuous models** using tools built into Tetrad.

The goal is not to identify a single “true” causal graph, but to show how to arrive at a **minimal, Markov-consistent model** under clearly stated assumptions, and then to **interpret causal effects quantitatively**.

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

- Several continuous variables (e.g., `mpg`, `weight`, `horsepower`, `acceleration`)
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

This assumption simplifies the workflow and is reasonable for this dataset.

### Algorithm: BOSS

We choose **BOSS**, a score-based search algorithm, because:

- It performs well in linear settings
- It scales well for systematic exploration
- It integrates naturally with score-based model comparison

### Score: Degenerate Gaussian BIC

Based on data exploration, we select the **Degenerate Gaussian BIC** score:

- It is appropriate for **mixed data**
- It aligns with the approximately linear structure seen in the plot matrix
- It supports Markov checking via the **DG-LRT** test

---

## 4. Setting Up and Running the Grid Search

(Setup steps omitted here for brevity; they are unchanged from the original example.)

After running Grid Search and examining the Markov-check results, we select a **minimal CPDAG** that passes diagnostics.

[Selected CPDAG image goes here]

---

## 5. Choosing a Representative DAG

To estimate causal effects, we select a **representative DAG** from the CPDAG:

- One undirected edge is oriented based on background knowledge
- Meek’s orientation rules are then applied

This yields a fully directed acyclic graph suitable for parameter estimation.

[Chosen DAG image goes here]

---

## 6. Parameter Estimation with the Hybrid CG Estimator

Because the dataset contains both discrete and continuous variables, we use the **Hybrid Conditional Gaussian (Hybrid CG) Estimator**.

1. Add a **Hybrid CG Estimator** box.
2. Connect the selected DAG (PM) and the data to the estimator.
3. Use default settings (equal-frequency binning, Dirichlet alpha = 1).
4. Click **Estimate & Preview**.

The estimator fits:

- Conditional probability tables for discrete children
- Linear-Gaussian regression models for continuous children

### Example: Horsepower → Acceleration

An edge of particular interest is:

```
horsepower → acceleration
```

The estimated regression coefficient for this edge is:

```
-0.084
```

[Hybrid CG regression table image goes here]

At first glance, the negative sign may seem surprising. However, this interpretation depends critically on the meaning of the variable **acceleration** in this dataset.

---

## 7. Interpreting “Acceleration” in the Auto MPG Data

In the Auto MPG dataset, **acceleration is not the physical quantity dv/dt**.

Instead, it is defined as:

> **The time (in seconds) required to accelerate from 0 to 60 mph.**

Under this definition:

- Larger values mean **slower acceleration**
- Smaller values mean **faster acceleration**

Therefore, a negative coefficient for horsepower → acceleration means:

> Increasing horsepower reduces the time needed to reach 60 mph.

This is exactly what we would expect.

A scatterplot of acceleration versus horsepower confirms this negative relationship:

[Scatterplot image goes here]

---

## 8. Cross-Checking with Adjustment Total Effects

To validate the estimated coefficient, we compute the **total causal effect** of horsepower on acceleration using the **Adjustment / Total Effects** tool.

1. Use the same DAG (or CPDAG).
2. Set:
   - Treatment X = `horsepower`
   - Outcome Y = `acceleration`
3. Compute adjustment sets and total effects.

The total effect estimate is again:

```
-0.084
```

[Adjustment total effects image goes here]

Because there is only a single directed path from horsepower to acceleration in the graph, the **direct effect and total effect coincide**, and the two independent estimation methods agree.

---

## 9. What This Extended Example Illustrates

This extended Auto MPG example demonstrates that Tetrad supports:

- **Mixed discrete/continuous data**
- **Hybrid CG parameter estimation**
- **Adjustment-based causal effect estimation**
- **Cross-validation of causal conclusions using independent tools**

It also highlights an important practical lesson:

> **Correct causal interpretation depends on understanding variable semantics, not just algorithms.**

Examining the data, inspecting scatterplots, and verifying variable definitions are essential parts of a sound causal workflow.

---

## 10. Summary

In this example, we:

1. Identified a minimal Markov-consistent CPDAG using Grid Search
2. Selected a representative DAG
3. Estimated parameters using the Hybrid CG Estimator
4. Computed total causal effects via adjustment
5. Resolved an apparent sign paradox by carefully interpreting the data

This workflow illustrates how Tetrad’s mixed-data tools can be used together to produce **coherent, interpretable causal conclusions on real datasets**.
