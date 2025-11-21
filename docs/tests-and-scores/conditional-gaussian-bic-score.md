# Conditional Gaussian BIC Score

## Summary

The Conditional Gaussian BIC Score is a BIC-type score for **conditional
Gaussian (CG) models** with mixed continuous and discrete variables. It
evaluates a DAG or CG structure by combining CG log-likelihood with a penalty
on the number of parameters.

## When to use

- Data are a mix of continuous and discrete variables.
- You assume a CG model: given the discrete variables, continuous variables are
  multivariate normal with means and covariances that may depend on discrete
  configurations.
- You are using score-based or hybrid algorithms that support CG models.

## Model class

- Conditional Gaussian Bayesian networks with discrete parents and linear-
  Gaussian continuous components.

## Score form (conceptual)

As with other BIC scores:

    BIC = 2 * logL − k * ln(N)

where `logL` is the CG log-likelihood and `k` is the number of free parameters
(conditional means, covariances, and discrete probabilities).

## Parameters

| Parameter (camelCase)           | Description |
|---------------------------------|-------------|
| `penaltyDiscount`               | Double ≥ 0.0. The penalty multiplier “c” in the modified BIC-type criterion (for example, a score of the form 2·log-likelihood − c·k·log(N), where k is the number of free parameters and N is the sample size). Larger values impose a stronger complexity penalty and yield sparser graphs; smaller values allow denser graphs. Default is 2.0. |
| `structurePrior`                | Double ≥ 0.0. Structure prior coefficient controlling a binomial-style prior on the number of parents per node. When 0.0 (default), the score uses essentially a flat structure prior. Larger values encode a stronger preference for a particular expected parent count and can bias the search toward graphs with that typical in-degree. |
| `discretize`                    | Boolean. If `true`, continuous variables are discretized when a conditional Gaussian likelihood would require integrating over a continuous parent with a discrete child (a backup “discretize X” strategy). If `false`, the score uses the exact conditional Gaussian integration whenever possible. Default is `true`. |
| `numCategoriesToDiscretize`     | Integer ≥ 2. Number of categories used when discretizing continuous variables in the backup discretization step. Default is 3. Larger values give a finer discretization but increase the size of the conditional tables and the number of parameters. |
| `minSampleSizePerCell`         | Integer ≥ 2. Minimum required sample size per configuration (cell) in the conditional Gaussian model. If the per-cell sample size is too small, the exact CG calculations become unstable, and the score may fall back to the discretization strategy. Default is 4. |

## Strengths

- Properly accounts for **mixed** data types without discretizing continuous
  variables.
- Integrates naturally with CG independence tests and CG learning algorithms.

## Limitations

- Requires enough data per discrete configuration.
- Assumes linear-Gaussian behavior for continuous components.

## References

- Andrews, B., Ramsey, J., & Cooper, G. F. (2018). *Scoring Bayesian networks of mixed variables.* International Journal of Data Science and Analytics, 6(1), 3–18.