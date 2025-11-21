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

## Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `alpha`                 | Significance level (p-value cutoff) for the likelihood-ratio test of conditional independence. The null hypothesis is that the variables are conditionally independent given the conditioning set. P-values below `alpha` lead to rejection. Smaller values make the test more conservative (fewer edges); larger values make the graph denser. Typical range: 0.0–1.0. |
| `singularityLambda`     | Double used to handle singular or nearly singular covariance matrices. If `singularityLambda > 0`, this value is added to the diagonal (ridge regularization) to stabilize matrix inverses. If `singularityLambda < 0`, a pseudoinverse is used instead. Default is 0.0; use a small positive value if you encounter numerical-singularity warnings. |
| `effectiveSampleSize`   | Double > 0, or `-1`. If `-1` (default), the actual sample size is used in computing the test statistic and p-values. If set to a positive value, the test behaves as if that were the sample size (for example, when treating weighted or subsampled data as having a different effective N). |

## Strengths

- More robust than standard Gaussian tests in **high-dimensional** or nearly
  singular settings.
- Can be used as a drop-in replacement for Fisher Z when degeneracy is an
  issue.

## Limitations

- Exact null distribution may be approximate; calibration can be more complex.
- Behavior depends on the choice of regularization or pseudo-inverse.
- Still relies on approximate Gaussian assumptions.

## References

- Ramsey, J. D., Andrews, B., & Spirtes, P. (2024). *Choosing DAG models using Markov and minimal edge count in the absence of ground truth.* arXiv:2409.20187.
