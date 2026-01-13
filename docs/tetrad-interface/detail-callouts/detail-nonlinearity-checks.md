# Detail: Nonlinearity Checks

## Purpose

The **Nonlinearity Checks** tool provides a systematic way to assess whether the conditional expectation E(Y | X) appears to be linear or nonlinear, using several complementary statistical tests.

This tool is intended to help users:
- diagnose whether linear modeling assumptions are reasonable,
- decide whether nonlinear causal discovery methods (e.g., RFF-BIC, KCV-BIC, BF-based methods) are warranted,
- understand *why* certain algorithms succeed or fail on a given dataset.

The tool is **descriptive and diagnostic**, not a causal discovery algorithm by itself.

---

## Conceptual Background

Most classical causal discovery methods rely (explicitly or implicitly) on **linear conditional expectations**:
E(Y | X) = β₀ + βᵀX.

However, many real-world mechanisms violate this assumption. In particular:

- **Additive nonlinear mechanisms**:  
  Y = f₁(X₁) + ··· + fₖ(Xₖ) + e  
  (also known as generalized additive or additive-noise models)

- **Non-additive nonlinear mechanisms**:  
  Y = f(X₁, …, Xₖ) + e

- **Fully general mechanisms**:  
  Y = f(X₁, …, Xₖ, e)

The Nonlinearity Checks tool evaluates evidence against linearity of E(Y | X) using multiple, complementary tests.

---

## Modes of Operation

The interface supports two modes:

### 1. Pairwise Mode
Each treatment X is tested individually against each outcome Y.

This answers questions such as:
- “Is the relationship between X and Y linear?”
- “Does X have a nonlinear marginal effect on Y?”

### 2. Conditional Mode
Each outcome Y is tested conditional on **all specified treatments X₁,…,Xₖ**.

This answers questions such as:
- “Is E(Y | X₁,…,Xₖ) linear in the predictors?”
- “Does a linear multivariate regression adequately describe the conditional mean?”

---

## Implemented Tests

Each row in the results table reports the outcome of the following tests.

### 1. Ramsey RESET Test

**Idea:**  
Tests whether nonlinear functions of the fitted values improve a linear regression.

**Method:**  
- Fit a linear model Y ~ X.
- Augment the model with powers of the fitted values (e.g., Ŷ², Ŷ³).
- Perform an F-test for the additional terms.

**Interpretation:**  
- Rejecting suggests misspecification of the linear functional form.

**Strengths:**  
- Simple, classical, fast.

**Limitations:**  
- Detects only certain types of nonlinearity.
- Power depends on chosen polynomial order.

**Reference:**  
Ramsey, J. B. (1969). *Tests for specification errors in classical linear least-squares regression analysis.*  
Journal of the Royal Statistical Society, Series B.

---

### 2. Spline vs Linear Likelihood Ratio Test

**Idea:**  
Compare a linear model to a flexible spline-based regression.

**Method:**  
- Fit a linear regression.
- Fit a regression using spline basis expansions of X.
- Perform a likelihood ratio (or approximate chi-square) test.

**Interpretation:**  
- Rejection indicates evidence for smooth nonlinear structure.

**Strengths:**  
- Sensitive to smooth nonlinearities.
- Interpretable as a nested model comparison.

**Limitations:**  
- Requires choice of spline basis and degrees of freedom.

**Reference:**  
Hastie, T., Tibshirani, R., & Friedman, J. (2009).  
*The Elements of Statistical Learning*, Section 5.4.

---

### 3. Kernel Regression Linearity Test

**Idea:**  
Test whether a nonparametric kernel regression significantly improves predictive performance over linear regression.

**Method:**  
- Fit a linear regression.
- Fit a kernel regression (e.g., Nadaraya–Watson).
- Compare cross-validated prediction error.

**Interpretation:**  
- Improved predictive performance suggests nonlinear conditional expectation.

**Strengths:**  
- Nonparametric and flexible.
- Sensitive to a wide range of nonlinearities.

**Limitations:**  
- Computationally heavier.
- Requires bandwidth selection.

**Reference:**  
Härdle, W., Müller, M., Sperlich, S., & Werwatz, A. (2004).  
*Nonparametric and Semiparametric Models.*

---

### 4. Random Fourier Feature (RFF) Regression Test

**Idea:**  
Approximate an RBF-kernel regression using random Fourier features and compare against linear regression.

**Method:**  
- Map X into random Fourier feature space Φ(X).
- Fit ridge regression Y ~ Φ(X).
- Compare fit or cross-validated error against linear regression.

**Interpretation:**  
- Significant improvement indicates nonlinear structure in E(Y | X).

**Strengths:**  
- Scales to larger datasets.
- Closely related to methods used in RFF-BIC.

**Limitations:**  
- Randomized (though averaged for stability).
- Requires tuning number of features.

**References:**  
Rahimi, A., & Recht, B. (2007). *Random features for large-scale kernel machines.*  
Gretton et al. (2005). *Measuring statistical dependence with Hilbert-Schmidt norms.*

---

## Output Interpretation

For each test, the tool reports:

- **Statistic**: test-specific measure of nonlinearity.
- **p-value** (when applicable).
- **Decision**: labeled as *Linear* or *Nonlinear* for clarity.

Disagreement between tests is expected and informative:
- Some nonlinearities are local, smooth, or interaction-driven.
- No single test dominates in all regimes.

---

## Practical Guidance

- Consistent rejection across multiple tests strongly suggests nonlinear structure.
- Pairwise nonlinearity does **not** imply conditional nonlinearity.
- Conditional nonlinearity is most relevant for causal discovery algorithms.

This tool is best used as a **diagnostic companion** to causal modeling and search.

---

## Summary

The Nonlinearity Checks tool fills a long-standing gap in Tetrad by providing a principled, multi-test assessment of linearity assumptions. It helps explain when and why nonlinear causal discovery methods are needed—and when simpler linear approaches may suffice.
