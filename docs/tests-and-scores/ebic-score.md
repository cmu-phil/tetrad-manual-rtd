# Extended BIC (EBIC) Score

## Summary

The Extended BIC (EBIC) Score is a generalization of BIC intended for
**high-dimensional settings**. It adds an extra penalty term that depends on
the number of possible edges, favoring sparser graphs more strongly than
standard BIC.

## When to use

- Number of variables is large relative to the sample size.
- You want stronger sparsity encouragement than standard BIC provides.
- You are using score-based methods (FGES, BOSS, GRaSP) in high-dimensional
  regimes.

## Model class

- Typically applied to linear Gaussian or discrete DAGs, but the EBIC form is
  generic.

## Score form (conceptual)

A common EBIC form is:

    EBIC = 2 * logL − k * ln(N) − 2 * γ * ln(choose(p, k_edges))

where γ is a parameter in [0, 1], `p` is the number of variables, and
`k_edges` is the number of edges.

## Parameters

| Parameter (camelCase)     | Description |
|---------------------------|-------------|
| `ebicGamma`               | Double in [0, 1]. The gamma parameter for Extended BIC (EBIC). Values closer to 0 reduce EBIC to ordinary BIC; values closer to 1 add a strong extra penalty for models with many predictors (useful in high-dimensional settings). Default is 0.8. |
| `precomputeCovariances`   | Boolean. If `true`, precomputes and caches covariance (and possibly cross-covariance) matrices used by the score. This speeds up repeated scoring at the cost of additional memory. If `false`, these quantities are recomputed on the fly, which saves memory but can be slower for large graphs or many score evaluations. |
| `singularityLambda`       | Double. Handles singular or nearly singular covariance matrices. If `singularityLambda > 0`, that value is added to the diagonal (a ridge term) to stabilize matrix inverses. If `singularityLambda < 0`, a pseudoinverse is used instead. Default is 0.0. Use a small positive value if you encounter numerical-singularity warnings. |
| `effectiveSampleSize`     | Double > 0, or `-1`. If `-1` (default), the actual sample size N is used in the log(N) penalty term. If set to a positive value, the score behaves as if that were the sample size (for example, when treating weighted or subsampled data as having a different effective N). |

## Strengths

- More conservative than BIC, tending to select **sparser** graphs in high-
  dimensional settings.
- Supported by theory in some sparse regression and graphical model contexts.

## Limitations

- Choice of γ is somewhat problem-dependent.
- May penalize edges too strongly when N is not extremely small compared to p.
