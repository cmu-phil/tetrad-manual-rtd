# Algorithm Selection and Assumptions

After exploring your data (see *Data Exploration*), the next step in the causal analysis workflow is to choose appropriate search methods and articulate the assumptions you’re willing to make. No single algorithm is universally best; different methods make different assumptions and have different strengths.

This page provides a decision guide to help you choose methods based on data characteristics, your modeling goals, and what you’re willing to assume.

---

## What This Page Covers

- A checklist of key assumptions
- How those assumptions map to algorithm families
- Simple recipes to get started
- Notes on algorithm parameters and diagnostics

---

## 1. What Assumptions Matter?

Causal discovery is fundamentally about using statistical patterns to learn about causal structure. Different methods rely on different assumptions. Here are the key assumptions you should consider:

### 1.1. Causal Sufficiency
**Question:** Do you believe all relevant common causes of the variables in your dataset have been measured?

- **Yes:** You may assume causal sufficiency and search for a DAG or CPDAG.
- **No / Unsure:** You should allow for latent confounders and search for a PAG.

> *Causal sufficiency is a strong assumption: if it’s wrong, methods that assume it can give misleading orientations.*

### 1.2. Functional Form and Distribution
**Question:** Are relationships roughly linear and Gaussian?

- **Yes:** Linear methods (e.g., PC with Fisher-Z, GES/BIC) are good starting points.
- **No / Unclear or Non-Gaussian:** Consider nonparametric or rank-based tests; these are more flexible but may be slower or less powerful in small samples.

### 1.3. Goal of Causal Inquiry
**Question:** What do you *need* from the analysis?

- **Adjacency structure (who’s connected to whom):** Many methods suffice.
- **Partial orientation (some directions):** Some assumption about functional form or stronger constraints may be needed.
- **Specific causal effect estimation:** You may need to combine structure learning with further modeling and adjust for confounders.

### 1.4. Sample Size and Dimensionality
- **Small n, large p:** Be cautious — high-dimensional methods exist but results may be unstable.
- **Large n:** More flexible tests/scores become practical.

Assumptions shape which algorithms are sensible and how their outputs should be interpreted.

---

## 2. Algorithm Families and When to Use Them

Here’s a simplified guide to Tetrad’s major discovery algorithm families.

### 2.1. Constraint-Based Methods

**Examples:** *PC, FCI*  
**What they use:** Conditional independence tests

Use when:
- You have reasonable sample size and can articulate appropriate tests for your data type.
- You want models that are defensible in terms of conditional independence patterns.

Choose:
- **PC** when assuming causal sufficiency.
- **FCI** (or later variants) when allowing for latent variables.

Notes:
- You’ll select a significance level (e.g., α). Smaller values yield sparser graphs.

---

### 2.2. Score-Based Methods

**Examples:** *GES, BOSS, GRaSP*  
**What they use:** A global score (e.g., BIC) to compare models

Use when:
- You want a global optimization objective.
- You have continuous or discrete data for which appropriate scores are available.

Notes:
- Score-based methods can be robust to certain distributional issues if scores match data characteristics.
- They naturally balance fit and complexity.

---

### 2.3. Hybrid and Global Methods

**Examples:** *ARGES, Hybrid-PC*  
Combine ideas from both constraint-based and score-based approaches. Useful when:
- Pure constraint-based methods struggle due to conditioning set size
- Score-based methods alone are prone to local optima

These methods often offer a practical balance.

---

## 3. Mapping Assumptions to Practical Choices

Here’s a compact decision guide:

| Assumptions / Goals | Recommended Method(s)                            | Notes |
|---------------------|--------------------------------------------------|-------|
| Causal sufficiency, linear-Gaussian | PC, GES, BOSS, GRaSP                             | Standard baseline |
| Latents possible, linear-Gaussian | FCI, BOSS-FCI, GRaSP-FCI                         | Captures PAG structures |
| Nonlinear / non-Gaussian patterns | Nonparametric tests (KCI / RCIT) with PC/FCI     | More flexible but computationally heavier |
| Mixed continuous & discrete | Mixed-test variants or score-based mixed scores  | Be careful with test choice |
| High-dimensional | Penalized scores (e.g., BIC/MDL), hybrid methods | Regularization helps complexity |

This table gives starting points; use the *Grid Search* page to explore parameter choices and diagnostics.
See the [algorithms](../algorithms) section for a complete listing of algorithms available in Tetrad.

---

## 4. Choosing Tests and Scores

See the [test and scores](../tests-and-scores) section for a complete listing of tests and scores available in Tetrad.


### 4.1. Tests for Constraint-Based Methods
- **Fisher-Z:** For continuous, approximately Gaussian data.
- **Rank-based tests:** For non-Gaussian continuous data (less sensitive to outliers).
- **Discrete tests:** For fully discrete data.

When in doubt, inspect residuals, scatterplots, and distributions to guide test selection.

---

### 4.2. Scores for Score-Based Methods

- **BIC / SEM-BIC:** Balances model fit and complexity; works well for many continuous settings.
- **Discrete BIC / AIC:** Use for discrete or mixed data when appropriate.

**Note:** Score choice influences sparsity and sensitivity to noise.

---

## 5. What to Do When You’re Unsure

It’s okay to *not know* which assumptions hold perfectly. In that case:

1. **Start with a conservative assumption** (e.g., allow latents).
2. **Run a simple search** (e.g., PC or FCI).
3. **Use diagnostics** (e.g., Markov Checker) to evaluate whether the output is consistent with data.
4. **Iterate:** Adjust assumptions, algorithms, or test/score settings.

This iterative process — *search → diagnose → revise* — is the heart of causal analysis.

---

## 6. Integration with Grid Search

The *Grid Search* tool in Tetrad lets you:

- Sweep key parameters (e.g., α, penalty/discount)
- Compare algorithms side-by-side
- Explore models under different assumptions

Use **Grid Search** after you’ve chosen a plausible family of methods to evaluate how sensitive results are to parameter choices.

---

## 7. Summary

Choosing algorithms in Tetrad is less about selecting a single “best” method up front and more about:

- Understanding your data
- Making explicit assumptions
- Picking a sensible starting method
- Evaluating outputs systematically

This guides you toward defensible causal models rather than a “one-size-fits-all” solution.

---

## 🧭 Next Step

After you’ve chosen initial methods and assumptions, continue with **Workflow: Running Searches and Grid Search Tips** to systematically explore models and evaluate them with diagnostics.