# Zhang–Shen Bound Score

## Summary

The Zhang–Shen Bound Score is an experimental score for linear Gaussian
models that uses a risk bound derived from Theorem 1 of Zhang and Shen (2010)
to choose a penalty for the number of parents of each node.

For each variable, and for each possible maximum number of parents (called
m0), the score numerically solves for a penalty value lambda(m0) such that
the probability of selecting a model whose score is worse than the true model
is bounded above by a user-specified risk bound in the interval [0, 1].
Intuitively, the risk-bound parameter controls an upper bound on the local
false positive probability for parent edges.

The score is designed to be conservative, especially for large, dense models,
and to give a risk parameter that is directly interpretable.

## When to use

Use the Zhang–Shen Bound Score when:

- You want a theory-guided criterion based on an explicit risk bound for local
  false positive decisions.
- You are working with linear Gaussian SEMs and want an alternative to
  standard BIC/EBIC-style penalties.
- You are exploring large or moderately dense models where a conservative
  score is preferable and you want a tunable risk parameter.
- You are using FGES, GRaSP, or similar search algorithms and are willing to
  let the score refine its internal estimates as nodes are revisited during
  search.

## Model class

- Linear Gaussian DAG / SEM over a set of continuous variables.
- Implemented on top of a covariance matrix (or raw data converted to a
  covariance matrix).
- As with other SEM-based scores in Tetrad, higher scores indicate stronger
  dependence or better fit; negative scores indicate independence.

## Score form (conceptual)

For a given target node i and candidate parent set Pa(i), the local score has
the form:

> score(i | Pa(i)) = -0.5 * nEff * log(varRy) - lambda(m0) * numberOfParents

where:

- varRy is the residual variance of node i given its current parents,
- nEff is the effective sample size (either the actual sample size or a
  user-specified value),
- numberOfParents is the size of the current parent set Pa(i),
- lambda(m0) is the penalty derived from Zhang–Shen’s bound for the current
  estimate of the maximum number of parents m0 for that node.

The score maintains, for each node:

- an estimate of the maximum number of parents in the (unknown) minimal true
  model m0,
- the best local score observed so far, and
- the corresponding residual variance.

Each time a better local score is observed for that node, these estimates are
updated. As search algorithms such as FGES or GRaSP revisit the node, the
bound becomes sharper and the resulting scores tend to improve over time.
In practice, starting with m0 = 0 for all variables already gives reasonable
behavior.

## Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `zsRiskBound`           | Double in [0, 1]. Risk bound used in the Zhang–Shen criterion. This is the probability of getting a model whose score is worse than the score of the true model, conditional on the true model being among the candidates. Smaller values enforce a stricter bound (more protection against overfitting but more risk of underfitting); larger values relax the bound. Default is 0.1. |
| `precomputeCovariances` | Boolean. If `true`, precomputes and caches covariance (and possibly cross-covariance) matrices used by the score. This speeds up repeated scoring at the cost of additional memory. If `false`, these quantities are recomputed on the fly, which saves memory but can be slower for large graphs or many score evaluations. |
| `singularityLambda`     | Double. Handles singular or nearly singular covariance matrices. If `singularityLambda > 0`, that value is added to the diagonal (a ridge term) to stabilize matrix inverses. If `singularityLambda < 0`, a pseudoinverse is used instead. Default is 0.0. Use a small positive value if you encounter numerical-singularity warnings. |
| `effectiveSampleSize`   | Double > 0, or `-1`. If `-1` (default), the actual sample size N is used in the log(N) penalty or tail-bound terms. If set to a positive value, the score behaves as if that were the sample size (for example, when treating weighted or subsampled data as having a different effective N). |

## Strengths

- Provides a directly interpretable risk parameter (`zsRiskBound`), linking
  model selection to a bound on the probability of choosing a model worse than
  the true one.
- Tends to be conservative for large, dense models, making it useful when
  false positives are a major concern.
- Can be computationally faster than some alternative scores in the same
  package, while still being grounded in a theoretical risk bound.
- Adapts as search proceeds: nodes revisited by FGES or GRaSP get progressively
  refined estimates of m0 and lambda(m0).

## Limitations

- Specialized to linear Gaussian SEMs; it is not intended for discrete or
  highly non-Gaussian settings.
- More complex and less standard than BIC or EBIC; the behavior and
  interpretation may be less familiar to many users.
- The performance depends on how often nodes are revisited during search, since
  the estimates of m0 and lambda(m0) improve over time.
- The theoretical assumptions of Zhang and Shen (2010) are asymptotic and may
  not hold perfectly in small samples or strongly misspecified models.

## References

- Zhang, Y., & Shen, X. (2010). *Model selection procedure for high-dimensional data.* Statistical Analysis and Data Mining: The ASA Data Science Journal, 3(5), 350–358.