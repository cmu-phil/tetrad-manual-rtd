# SEM BIC Score

## Summary

The SEM BIC Score is a **BIC-type score** for **linear structural equation
models (SEMs)** with continuous variables and Gaussian errors. It evaluates the
fit of a DAG or SEM structure by combining the log-likelihood of the implied
covariance matrix with a penalty on model complexity.

## When to use

- Data are continuous and reasonably **Gaussian**.
- You are learning a DAG or SEM using algorithms like FGES, BOSS, or GRaSP.
- You want a consistent, likelihood-based score that trades off fit and
  complexity.

## Model class

- Linear structural equation models with Gaussian noise.
- Equivalent to evaluating a DAG with linear regressions at each node.

## Score form (conceptual)

The SEM BIC Score is of the form:

    BIC = 2 * logL − k * ln(N)

where:

- `logL` is the maximized log-likelihood for the model,
- `k` is the number of free parameters (edges and variances),
- `N` is the sample size.

In Tetrad’s convention, **larger BIC values are better**.

## Parameters in Tetrad

Typical parameters include:

- `penaltyDiscount` — Multiplier on the complexity penalty.
- `structurePrior` or related options for prior edge penalties (if enabled).
- `faithfulnessAssumed` or similar flags (algorithm-dependent).

## Strengths

- Well-studied, consistent under standard regularity conditions.
- Efficient to compute using regression or covariance matrix factorizations.
- Natural choice for continuous linear DAG/SEM learning.

## Limitations

- Assumes linear-Gaussian structure; may mis-score strong nonlinear or
  non-Gaussian relationships.
- Sensitive to outliers and heteroskedasticity.
