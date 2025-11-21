# Zhang–Shen Bound Score

## Summary

The Zhang–Shen Bound Score is a specialized criterion inspired by theoretical
bounds on causal discovery or structure learning performance, associated with
work by Zhang and Shen and collaborators. In Tetrad, it serves as an
experimental or research-focused score to evaluate graphs under such bounds.

## When to use

- You are experimenting with **theoretical guarantees** or bounds-based
  selection criteria.
- You are working with algorithms or studies that directly reference the
  Zhang–Shen framework.
- You want to compare standard BIC-like selection with a more theory-driven
  bound-based metric.

## Model class

- Depends on the specific bound and setting; often continuous or discrete DAGs
  with certain regularity assumptions.

## Score form (conceptual)

The score encodes either:

- An upper or lower bound on risk or error associated with a structure, or
- A surrogate objective motivated by such a bound,

and is used as a scalar criterion for comparing candidate graphs.

## Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `zsRiskBound`           | Double in [0, 1]. Risk bound used in the Zhang–Shen criterion. This is the probability of getting a model whose score is worse than the score of the true model, conditional on the true model being among the candidates. Smaller values enforce a stricter bound (more protection against overfitting but more risk of underfitting); larger values relax the bound. Default is 0.1. |
| `precomputeCovariances` | Boolean. If `true`, precomputes and caches covariance (and possibly cross-covariance) matrices used by the score. This speeds up repeated scoring at the cost of additional memory. If `false`, these quantities are recomputed on the fly, which saves memory but can be slower for large graphs or many score evaluations. |
| `singularityLambda`     | Double. Handles singular or nearly singular covariance matrices. If `singularityLambda > 0`, that value is added to the diagonal (a ridge term) to stabilize matrix inverses. If `singularityLambda < 0`, a pseudoinverse is used instead. Default is 0.0. Use a small positive value if you encounter numerical-singularity warnings. |
| `effectiveSampleSize`   | Double > 0, or `-1`. If `-1` (default), the actual sample size N is used in the log(N) penalty or tail-bound terms. If set to a positive value, the score behaves as if that were the sample size (for example, when treating weighted or subsampled data as having a different effective N). |

## Strengths

- Grounded in theoretical performance bounds.
- Encourages exploration of criteria beyond classical likelihood penalties.

## Limitations

- More specialized and less standard than BIC/EBIC; interpretation may be less
  familiar.
- Theoretical assumptions behind the bound may not hold in all applied
  settings.
