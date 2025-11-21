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

## Parameters

| Parameter (camelCase)       | Description |
|-----------------------------|-------------|
| `penaltyDiscount`           | Double ≥ 0.0. The penalty multiplier “c” in the modified BIC-type criterion (for example, a score of the form 2·log-likelihood − c·k·log(N), where k is the number of free parameters and N is the sample size). Larger values impose a stronger complexity penalty and yield sparser graphs; smaller values allow denser graphs. Default is 2.0. |
| `structurePrior`            | Double ≥ 0.0. Structure prior coefficient controlling a binomial-style prior on the number of parents per node. When 0.0 (default), the score uses essentially a flat structure prior. Increasing this value encodes a stronger preference for a particular expected parent count and can bias the search toward graphs with that typical in-degree. |
| `precomputeCovariances`     | Boolean. If `true`, precomputes and caches covariance (and possibly cross-covariance) matrices used by the score. This speeds up repeated scoring at the cost of additional memory. If `false`, covariance quantities are recomputed on the fly, which saves memory but can be slower for large graphs or many score evaluations. |
| `singularityLambda`         | Double. Handles singular or nearly singular covariance matrices. If `singularityLambda > 0`, that value is added to the diagonal (a ridge term) to stabilize inverses. If `singularityLambda < 0`, a pseudoinverse is used instead. Default is 0.0. Use a small positive value when you see numerical-singularity warnings. |
| `effectiveSampleSize`       | Double > 0, or `-1`. If `-1` (default), the actual sample size N is used in the log(N) penalty term. If set to a positive value, the score behaves as if that were the sample size (for example, when you want to treat weighted or subsampled data as having a different effective N). |

## Strengths

- More stable than standard SEM BIC in high-dimensional or nearly singular
  settings.
- Can be used with GRaSP or other high-dimensional search algorithms.

## Limitations

- Approximate nature of the likelihood and degrees of freedom.
- Behavior depends on the chosen regularization scheme.

## References

- Ramsey, J. D., Andrews, B., & Spirtes, P. (2024). *Choosing DAG models using Markov and minimal edge count in the absence of ground truth.* arXiv:2409.20187.
