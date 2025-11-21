# Degenerate Gaussian BIC Score

## Summary

The Degenerate Gaussian BIC Score extends the SEM BIC score to settings where
the covariance matrix may be **singular or nearly singular**. It uses
regularization or pseudo-inverse techniques to evaluate the likelihood for
high-dimensional or degenerate Gaussian models.

## When to use

- You are working with **high-dimensional continuous data**.
- Standard SEM BIC becomes unstable due to rank deficiency of the covariance
  matrix.
- You want a BIC-like score that is more robust to degeneracy.

## Model class

- Linear Gaussian models, but with potential degeneracies (e.g., more
  variables than samples or strong collinearities).

## Score form (conceptual)

Similar to SEM BIC:

    BIC ≈ 2 * logL_reg − k_eff * ln(N)

where `logL_reg` is a regularized or pseudo-inverse-based log-likelihood, and
`k_eff` reflects the effective number of parameters given degeneracy.

## Parameters in Tetrad

Typical parameters include:

- `penaltyDiscount` — Scales the complexity penalty.
- Regularization or rank thresholds used to stabilize covariance estimates.
- `verbose` — Logging of rank, condition numbers, and warnings.

## Strengths

- More stable than standard SEM BIC in high-dimensional or nearly singular
  settings.
- Can be used with GRaSP or other high-dimensional search algorithms.

## Limitations

- Approximate nature of the likelihood and degrees of freedom.
- Behavior depends on the chosen regularization scheme.
