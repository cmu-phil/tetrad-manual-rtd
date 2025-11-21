# MVP BIC Score

## Summary

The MVP BIC Score is a BIC-type score tailored to **multivariate Poisson** or
related count-valued models. It evaluates DAGs or graphical structures where
nodes represent count variables with Poisson-like dependencies.

## When to use

- Variables are **counts** that may have multivariate Poisson structure.
- You are using specialized models or algorithms for count-valued causal
  discovery.
- You want a BIC-like score that respects the Poisson nature of the data.

## Model class

- Multivariate Poisson or related count models used in MVP-style structures.

## Score form (conceptual)

As a BIC-type score:

    BIC = 2 * logL − k * ln(N)

with `logL` computed under a multivariate Poisson model and `k` the number of
free parameters.

## Parameters

| Parameter (camelCase)    | Description |
|--------------------------|-------------|
| `structurePrior`         | Double ≥ 0.0. Structure prior coefficient controlling a binomial-style prior on the number of parents per node (or, more generally, on edge density). When 0.0 (default), the score uses essentially a flat structure prior. Increasing this value encodes a stronger preference for a particular expected in-degree and can bias the search toward graphs whose parent counts match that prior. |
| `fDegree`                | Integer ≥ 1. Degree parameter for the MVP projection model (for example, the degree of the polynomial or basis expansion used in the projection step). Higher values allow more flexible functional forms in the projection but increase the number of parameters and the risk of overfitting. Typical values are small integers such as 1, 2, or 3. |
| `discretize`             | Boolean. If `true`, continuous variables may be discretized in situations where the MVP likelihood or projection model would otherwise be unstable or poorly supported (for example, very sparse configurations). If `false`, the score uses the continuous MVP projection model directly, which can be less robust when cell counts are small. Default is typically `true`. |
| `effectiveSampleSize`    | Double > 0, or `-1`. If `-1` (default), the actual sample size N is used in the log(N) penalty term. If set to a positive value, the score behaves as if that were the sample size (for example, when treating weighted or subsampled data as having a different effective N). |

## Strengths

- Tailored to **count data** beyond simple univariate Poisson assumptions.
- Integrates with Poisson-based tests and priors.

## Limitations

- Requires a suitable multivariate Poisson model and estimation routine.
- May be sensitive to overdispersion and zero inflation.
