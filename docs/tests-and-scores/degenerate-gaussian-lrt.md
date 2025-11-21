# Degenerate Gaussian Likelihood Ratio Test

## Summary

The Degenerate Gaussian Likelihood Ratio Test is a variant of Gaussian LRT
designed for settings where the covariance matrix may be **singular or nearly
singular** (for example, when the number of variables is large relative to the
sample size, or when strong linear constraints exist).

## When to use

- You are working with **high-dimensional continuous data** where standard
  covariance estimation is unstable.
- Some variables may be exactly or nearly linear combinations of others.
- You still want a parametric Gaussian-style test with adjustments for
  degeneracy.

## Assumptions

- Data are approximately multivariate Gaussian (or at least elliptically
  distributed).
- A suitable regularized or pseudo-inverse covariance estimator is available.
- The degeneracy can be handled without introducing severe bias.

## Test details (conceptual)

For each X ⟂ Y | S query, the test:

1. Constructs covariance and cross-covariance matrices involving X, Y, and S.
2. Uses a **degeneracy-aware** estimator (for example, pseudo-inverse,
   regularization, or dimension reduction) to fit full and restricted models.
3. Forms a likelihood ratio statistic comparing models with and without
   dependence between X and Y given S.
4. Uses an approximate chi-square distribution or alternative calibration to
   obtain a p-value.

## Parameters in Tetrad

Typical parameters include:

- `alpha` — Significance level.
- Regularization-related settings (if exposed), such as ridge parameters or
  rank thresholds.
- `depth` — Maximum conditioning-set size for the algorithms that use this
  test.
- `verbose` — Whether to log degeneracy warnings and rank information.

## Strengths

- More robust than standard Gaussian tests in **high-dimensional** or nearly
  singular settings.
- Can be used as a drop-in replacement for Fisher Z when degeneracy is an
  issue.

## Limitations

- Exact null distribution may be approximate; calibration can be more complex.
- Behavior depends on the choice of regularization or pseudo-inverse.
- Still relies on approximate Gaussian assumptions.
