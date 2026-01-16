# Detail: Nonlinearity Checks

## Purpose

The **Nonlinearity Checks** tool provides a systematic, multi-test assessment of whether the conditional expectation

E(Y | X)

is adequately described by a linear model, or whether there is evidence for nonlinear structure.

This tool is intended to help users:

- diagnose whether linear modeling assumptions are reasonable for a given set of variables,
- decide whether nonlinear causal discovery methods (e.g., RFF-BIC, BF-based methods) are warranted,
- understand why linear methods may succeed or fail on a given dataset.

The tool is **descriptive and diagnostic**. It does not perform causal discovery by itself.

---

## Conceptual Background

Many classical causal discovery methods rely, explicitly or implicitly, on the assumption that the conditional mean of a variable is linear in its causes:

E(Y | X) = beta0 + beta^T X

Real-world data often violate this assumption. Common departures include:

- **Additive nonlinear structure**:

  Y = f1(X1) + f2(X2) + ... + fk(Xk) + e

- **Non-additive nonlinear structure** (interactions among predictors):

  Y = f(X1, X2, ..., Xk) + e

The Nonlinearity Checks tool evaluates evidence against linearity of the conditional mean using several complementary statistical tests.

It does not attempt to test independence of noise variables or distinguish causal noise models.

---

## Modes of Operation

The interface supports two modes.

### 1. Pairwise Mode

Each treatment X is tested individually against each outcome Y.

This answers questions such as:
- Is the marginal relationship between X and Y linear?
- Does X have a nonlinear effect on Y by itself?

### 2. Conditional Mode

Each outcome Y is tested conditional on **all specified treatments X1, X2, ..., Xk**.

This answers questions such as:
- Is E(Y | X1, ..., Xk) linear in the predictors?
- Does a multivariate linear regression adequately describe the conditional mean?

Conditional mode is generally more relevant for causal discovery.

---

## Implemented Tests

Each row in the results table reports the outcome of the following tests.

### 1. Ramsey RESET Test

**Idea:**

Tests whether nonlinear functions of the fitted values improve a linear regression.

**Method:**

- Fit a linear regression Y ~ X.
- Augment the model with powers of the fitted values (for example, Y-hat squared, Y-hat cubed).
- Perform an F-test for the added terms.

**Interpretation:**

Rejecting suggests misspecification of the linear functional form.

**Strengths:**

- Classical, simple, fast.

**Limitations:**

- Detects only certain forms of nonlinearity.
- Power depends on the chosen polynomial order.

**Reference:**  
Ramsey, J. B. (1969). *Tests for specification errors in classical linear least-squares regression analysis.*  
Journal of the Royal Statistical Society, Series B.

---

### 2. Cross-Validated Linear vs Nonlinear Prediction (RFF)

**Idea:**

Test whether a flexible nonlinear predictor improves predictive performance over a linear model.

**Method:**

- Fit a linear ridge regression.
- Fit a nonlinear kernel ridge regression approximated using Random Fourier Features (RFF).
- Compare cross-validated mean squared error.

**Interpretation:**
Rejecting indicates evidence that E(Y | X) is nonlinear.

**Strengths:**

- Sensitive to a wide range of nonlinearities.
- Scales better than full kernel methods.
- Closely related to RFF-BIC.

**Limitations:**

- Computationally heavier than parametric tests.
- Randomized (averaged for stability).

**Note:**
This test is only run when “Include slow tests” is enabled.

---

### 3. Conditional-Moment / Nonlinear-Features LM Test

**Idea:**

Check whether nonlinear transformations of the predictors explain structure left in the residuals of a linear model.

**Method:**

- Fit a linear model Y ~ X.
- Compute residuals.
- Regress residuals on nonlinear features of X (squares, cubes, and pairwise products).
- Use an LM-style test statistic.

**Interpretation:**

Rejecting suggests the linear conditional mean is misspecified.

**Strengths:**

- Targets specific nonlinear structure.
- Fast relative to fully nonparametric methods.

**Limitations:**

- Uses a limited feature set.
- May miss very smooth or high-order nonlinearities.

**Reference:**  

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*, Section 5.4.

---

### 4. Additive-Component (Hinge-Basis) Test

**Idea:**

Assess whether allowing nonlinear but additive effects improves a linear model.

**Method:**

- Fit a linear regression.
- Augment the model with per-predictor hinge-basis functions.
- Perform an F-test comparing the augmented model to the linear model.

**Interpretation:**

Rejecting indicates nonlinear structure consistent with an additive model.

**Strengths:**

- Helps diagnose departures from linearity without introducing interactions.
- Computationally moderate.

**Limitations:**

- Assumes additivity.
- Does not detect interaction effects.

**References:**

Hastie, T., Tibshirani, R., & Friedman, J. (2009). The Elements of Statistical Learning.

---

### 5. Additivity Check: Additive vs Fully Nonparametric (RFF)

**Idea:**

Determine whether interactions among predictors are needed beyond additive nonlinear effects.

**Method:**

- Fit an additive nonlinear model using hinge-basis functions.
- Fit a fully nonparametric model using RFF-based kernel ridge regression.
- Compare cross-validated prediction error.

**Interpretation:**

- Reject: Non-additive. Interactions likely matter.
- Fail to reject: Additive OK. No evidence against additivity.

**Strengths:**

- Directly probes interaction structure.
- Useful for assessing suitability of additive-model algorithms (for example, CAM).

**References:**

Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*
Buja, A., Hastie, T., & Tibshirani, R. (1989). Linear smoothers and additive models.  The Annals of Statistics, 17(2), 453–510.

**Limitations:**
- Computationally expensive.
- Failure to reject does not prove true additivity.

**Note:**
This test is only run when “Include slow tests” is enabled.

---

### Output Interpretation

For each test, the table reports:

- **Statistic**: test-specific measure of nonlinearity (visible via “Show Stats”).
- **Decision:** Linear / Nonlinear, or Additive OK / Non-additive
- **p-value** (when applicable)

Selecting a row and clicking “Show Stats” displays the full test statistics and p-values.

Disagreement between tests is expected and informative:
- Some nonlinearities are smooth,
- others involve interactions,
- no single test dominates in all regimes.

---

## Practical Guidance

- Consistent rejection across multiple tests strongly suggests nonlinear structure.
- Pairwise nonlinearity does **not** imply conditional nonlinearity.
- Conditional nonlinearity is most relevant for causal discovery.
- Additivity checks help decide whether additive-model assumptions are plausible.

This tool is best used as a **diagnostic companion** to causal modeling and search.

---

### Summary

The Nonlinearity Checks tool provides a principled, multi-test diagnostic for assessing linearity assumptions in conditional means. It helps explain when nonlinear causal discovery methods are needed, and when simpler linear approaches may suffice, without making strong assumptions about causal noise structure.
