# Algorithm Selection and Assumptions

After exploring your data (see *Data Exploration*), the next step in the causal analysis workflow is to choose appropriate discovery methods and clarify the assumptions you are willing to make.

There is no single “best” algorithm for all problems. Different methods rely on different assumptions, emphasize different aspects of the data, and produce different kinds of output. This page helps you make **reasonable starting choices** — not final commitments.

---

## What This Page Covers

This page helps you:

- Identify the assumptions that matter most for causal discovery
- Understand how those assumptions map to families of algorithms
- Choose sensible starting methods
- Know when and how to revise choices using diagnostics and Grid Search

---

## 1. Which Assumptions Matter?

Causal discovery uses statistical patterns to infer causal structure.  
Different algorithms rely on different assumptions, so it is important to be explicit about what you are assuming — even provisionally.

### 1.1. Causal Sufficiency

**Question:** Do you believe that all relevant common causes of your measured variables have been observed?

- **Yes:** You may assume causal sufficiency and search for a **DAG or CPDAG**.
- **No or Unsure:** You should allow for latent confounders and search for a **PAG**.

> Causal sufficiency is a strong assumption.  
> If it is wrong, methods that rely on it can produce misleading orientations.

When unsure, it is usually safer to allow for latent variables and relax the assumption.

---

### 1.2. Functional Form and Distribution

**Question:** Are relationships roughly linear and Gaussian?

- **Yes:** Linear methods (e.g., PC with Fisher-Z, GES/BIC) are often effective.
- **No or Unclear:** Consider nonparametric or rank-based methods, which are more flexible but often slower or less powerful in small samples.

Visual inspection from the Data Exploration step is often more informative than formal tests here.

---

### 1.3. Modeling Goal

**Question:** What do you want to learn from the analysis?

- **Adjacency structure:** Which variables are connected.
- **Partial orientation:** Some causal directions where identifiable.
- **Full orientation or effect estimation:** Requires stronger assumptions and careful interpretation.

Different goals justify different levels of modeling complexity and diagnostic scrutiny.

---

### 1.4. Sample Size and Dimensionality

- **Small sample sizes:** Favor simpler models and conservative assumptions.
- **Large samples:** Support more flexible tests and scores.
- **Many variables:** Regularization and sparsity penalties become more important.

These considerations affect how stable and interpretable results will be.

---

## 2. Major Algorithm Families in Tetrad

Tetrad includes several families of causal discovery methods. The goal here is not to exhaustively catalog them, but to help you choose a reasonable starting point.

---

### 2.1. Constraint-Based Methods

**Examples:** PC, FCI  
**Core idea:** Use conditional independence tests to remove and orient edges.

Use these when:
- You can choose an appropriate independence test for your data.
- You want models that closely reflect observed conditional independencies.

Choose:
- **PC** if assuming causal sufficiency.
- **FCI** if allowing latent confounders and selection bias.

Notes:
- The significance level (α) controls sparsity.
- Smaller α → fewer edges.

---

### 2.2. Score-Based Methods

**Examples:** GES, BOSS, GRaSP  
**Core idea:** Optimize a global score that balances fit and complexity.

Use these when:
- You want a global objective rather than local independence decisions.
- Appropriate scores exist for your data type.

Notes:
- Scores naturally penalize overly complex graphs.
- Results can be sensitive to penalty strength.

---

### 2.3. Hybrid and Global Methods

**Examples:** ARGES, hybrid PC variants

These methods combine constraint-based and score-based ideas and can be useful when:

- Conditioning sets become large
- Pure constraint-based methods are unstable
- Pure score-based methods get stuck in local optima

They often provide a practical compromise.

---

## 3. Mapping Assumptions to Starting Choices

The table below summarizes reasonable starting points:

| Assumptions / Goals | Suggested Methods | Notes |
|--------------------|------------------|-------|
| Causal sufficiency, linear-Gaussian | PC, GES, BOSS, GRaSP | Standard baseline |
| Latents possible, linear-Gaussian | FCI, BOSS-FCI, GRaSP-FCI | Produces PAGs |
| Nonlinear or non-Gaussian | PC/FCI with nonparametric tests | More flexible, slower |
| Mixed data types | Mixed tests or score-based methods | Be careful with compatibility |
| High-dimensional data | Penalized scores, hybrid methods | Regularization helps |

This table is meant as guidance, not prescription.  
Use Grid Search to evaluate alternatives.

---

## 4. Choosing Tests and Scores

See the **Tests and Scores** section of the manual for full reference details.

### 4.1. Independence Tests

- **Fisher-Z:** Continuous, approximately Gaussian data.
- **Rank-based tests:** Robust to non-Gaussianity and outliers.
- **Discrete tests:** Fully discrete data.

When unsure, start with conservative choices and rely on diagnostics.

---

### 4.2. Scores

- **BIC / SEM-BIC:** Widely used for continuous data.
- **Discrete BIC / AIC:** For discrete or mixed settings.

Score choice influences both sparsity and sensitivity to noise.

---

## 5. What If You’re Unsure?

Uncertainty is normal — and expected.

A productive strategy is:

1. Start with conservative assumptions (e.g., allow latents).
2. Run a simple search.
3. Use diagnostics (especially the Markov Checker).
4. Revise assumptions, parameters, or methods.
5. Repeat.

This **search → diagnose → revise** loop is the core causal workflow.

---

## 6. Using Grid Search Effectively

Grid Search allows you to:

- Compare multiple algorithms
- Sweep key parameters (e.g., α, penalty discounts)
- Evaluate models using diagnostics
- Identify **minimal models that pass Markov tests**

Rather than committing to one method, Grid Search helps you understand **which assumptions and settings are supported by your data**.

---

## 7. Summary

Algorithm selection in Tetrad is not about guessing the “right” method upfront. It is about:

- Making assumptions explicit
- Choosing sensible starting points
- Evaluating outputs systematically
- Refining choices based on evidence

This approach leads to models that are more defensible and easier to interpret.

---

## 🧭 Next Step

Proceed to **Workflow: Running Searches and Grid Search Tips** to learn how to run searches systematically and evaluate them using Grid Search.