# Algorithm Selection and Assumptions

After exploring your data (see *Data Exploration*), the next step in the causal analysis workflow is to choose appropriate discovery methods and clarify the assumptions you are willing to make.

There is no single “best” algorithm for all problems. Different methods rely on different assumptions, emphasize different aspects of the data, and produce different kinds of output. The goal at this stage is to make **reasonable starting choices**, not final commitments.

---

## What This Page Covers

This page is intended to help you:

- Identify the assumptions that matter most for causal discovery
- Understand how those assumptions map to families of algorithms
- Choose sensible starting methods
- Recognize when and how to revise choices using diagnostics and Grid Search

---

## 1. Which Assumptions Matter?

Causal discovery uses statistical patterns to infer aspects of causal structure. Because different algorithms depend on different assumptions, it is useful to be explicit—at least provisionally—about what you are assuming.

### 1.1. Causal Sufficiency

**Question:** Do you believe that all relevant common causes of your measured variables have been observed?

- **Yes:** You may assume causal sufficiency and search for a **DAG or CPDAG**.
- **No or Unsure:** You should allow for latent confounders and search for a **PAG**.

> Causal sufficiency is a strong assumption.  
> If it does not hold, methods that rely on it can yield misleading orientations.

When in doubt, allowing for latent variables is often the more cautious starting point.

---

### 1.2. Functional Form and Distribution

**Question:** Are relationships roughly linear and Gaussian?

- **Yes:** Linear methods (e.g., PC with Fisher-Z, GES/BIC) are often effective.
- **No or Unclear:** Nonparametric or rank-based methods may be more appropriate, though they can be slower or require larger samples.

Visual inspection during the Data Exploration step is often more informative than formal tests at this stage.

---

### 1.3. Modeling Goal

**Question:** What do you want to learn from the analysis?

- **Adjacency structure:** Which variables are connected.
- **Partial orientation:** Some causal directions where identifiable.
- **Full orientation or effect estimation:** Requires stronger assumptions and more careful interpretation.

Different goals justify different levels of modeling complexity and diagnostic scrutiny.

---

### 1.4. Sample Size and Dimensionality

- **Small sample sizes:** Favor simpler models and more conservative assumptions.
- **Large samples:** Support more flexible tests and scores.
- **Many variables:** Regularization and sparsity penalties become increasingly important.

These considerations affect both the stability and interpretability of results.

---

## 2. Major Algorithm Families in Tetrad

Tetrad includes several families of causal discovery methods. The purpose here is not to catalog them exhaustively, but to suggest reasonable entry points.

---

### 2.1. Constraint-Based Methods

**Examples:** PC, FCI  
**Core idea:** Use conditional independence tests to remove and orient edges.

These methods are often useful when:
- An appropriate independence test can be chosen for the data.
- You want models that closely reflect observed conditional independencies.

Typical choices include:
- **PC** when assuming causal sufficiency.
- **FCI** when allowing for latent confounders and selection bias.

Notes:
- The significance level (α) controls sparsity.
- Smaller α values generally produce sparser graphs.

---

### 2.2. Score-Based Methods

**Examples:** GES, BOSS, GRaSP  
**Core idea:** Optimize a global score that balances goodness-of-fit and model complexity.

These methods are often useful when:
- A global objective is preferred over local independence decisions.
- Suitable scores exist for the data type.

Notes:
- Scores naturally penalize overly complex graphs.
- Results can be sensitive to the choice of penalty strength.

---

### 2.3. Hybrid and Global Methods

**Examples:** ARGES, hybrid PC variants

Hybrid approaches combine ideas from constraint-based and score-based methods. They can be helpful when:

- Conditioning sets become large
- Pure constraint-based methods are unstable
- Pure score-based methods risk local optima

They often provide a practical middle ground.

---

## 3. Mapping Assumptions to Starting Choices

The table below summarizes common starting points:

| Assumptions / Goals | Suggested Methods | Notes |
|--------------------|------------------|-------|
| Causal sufficiency, linear-Gaussian | PC, GES, BOSS, GRaSP | Standard baseline |
| Latents possible, linear-Gaussian | FCI, BOSS-FCI, GRaSP-FCI | Produces PAGs |
| Nonlinear or non-Gaussian | PC/FCI with nonparametric tests | More flexible, often slower |
| Mixed data types | Mixed tests or score-based methods | Check compatibility carefully |
| High-dimensional data | Penalized scores, hybrid methods | Regularization is helpful |

This table is meant as guidance rather than prescription.  
Grid Search is designed to let you evaluate alternatives directly.

---

## 4. Choosing Tests and Scores

For detailed reference information, see the **Tests and Scores** section of the manual.

### 4.1. Independence Tests

- **Fisher-Z:** Continuous, approximately Gaussian data.
- **Rank-based tests:** More robust to non-Gaussianity and outliers.
- **Discrete tests:** Fully discrete data.

When unsure, conservative choices combined with diagnostics are often a reasonable starting point.

---

### 4.2. Scores

- **BIC / SEM-BIC:** Common choices for continuous data.
- **Discrete BIC / AIC:** Used in discrete or mixed settings.

Score choice affects both sparsity and sensitivity to noise.

---

## 5. What If You’re Unsure?

Uncertainty is normal—and expected.

A common and productive strategy is to:

1. Start with conservative assumptions (e.g., allow latent variables).
2. Run a simple search.
3. Use diagnostics (especially the Markov Checker).
4. Revise assumptions, parameters, or methods.
5. Repeat.

This **search → diagnose → revise** cycle is central to the causal analysis workflow.

---

## 6. Using Grid Search Effectively

Grid Search allows you to:

- Compare multiple algorithms
- Sweep over key parameters (e.g., α levels, penalty discounts)
- Evaluate models using diagnostics
- Identify **minimal models that pass Markov checks**

Rather than committing to a single method, Grid Search helps clarify **which assumptions and settings are supported by the data**.

---

## 7. Summary

Algorithm selection in Tetrad is less about finding the “right” method upfront and more about:

- Making assumptions explicit
- Choosing sensible starting points
- Evaluating outputs systematically
- Refining choices based on evidence

This approach tends to produce results that are more interpretable and defensible.

---

## 🧭 Next Step

Proceed to **Workflow: Running Searches and Grid Search Tips** to learn how to run searches systematically and evaluate them using Grid Search.
