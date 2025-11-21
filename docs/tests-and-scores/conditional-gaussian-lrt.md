# Conditional Gaussian Likelihood Ratio Test

## Summary

The Conditional Gaussian Likelihood Ratio Test is designed for **conditional
Gaussian (CG) models**, where some variables are continuous and others are
discrete. It tests independence X ⟂ Y | S under a CG assumption by comparing
nested CG models with and without cross-terms between X and Y.

## When to use

- Data are **mixed**: some continuous, some discrete.
- You want a parametric test that respects the structure of CG models (linear
  Gaussian conditional on discrete configurations).
- You are using CG-capable algorithms or scores in Tetrad.

## Assumptions

- The data generation process is compatible with a **conditional Gaussian**
  distribution: given the discrete variables, the continuous variables follow a
  multivariate normal distribution whose mean and covariance may depend on the
  discrete configuration.
- Sufficient sample size exists within each configuration of the discrete
  variables.
- Relationships are linear in the continuous variables within each discrete
  cell.

## Test details (conceptual)

For each candidate independence X ⟂ Y | S, the CG LRT:

1. Partitions the data according to the discrete variables in X, Y, and S.
2. Fits CG models that either permit or forbid dependence between X and Y
   given S within each partition.
3. Forms a likelihood ratio statistic by comparing the full and restricted
   models.
4. Uses an asymptotic chi-square distribution for the difference in log-
   likelihoods to obtain a p-value.

## Parameters

| Parameter (camelCase)           | Description |
|---------------------------------|-------------|
| `alpha`                         | Significance level (p-value cutoff) for the likelihood-ratio test of conditional independence. The null hypothesis is that the variables are conditionally independent given the conditioning set. P-values below `alpha` lead to rejection. Smaller values make the test more conservative (fewer edges); larger values make the graph denser. Typical range: 0.0–1.0. |
| `discretize`                    | Boolean. If `true`, continuous variables are discretized in cases where the exact conditional Gaussian test would require unstable or poorly supported estimates (for example, when some discrete parent configurations have very small sample size). If `false`, the test attempts to use the exact conditional Gaussian likelihood in all cases and may be less robust when cells are sparse. Default is `true`. |
| `numCategoriesToDiscretize`     | Integer ≥ 2. Number of categories used when discretizing continuous variables in the backup discretization step. Default is 3. Larger values give a finer discretization but increase the number of cells and reduce counts per cell. |
| `minSampleSizePerCell`         | Integer ≥ 2. Minimum required sample size per configuration (cell) in the conditional Gaussian model. If some cells fall below this threshold, the test may fall back to discretization (if `discretize = true`) or produce unstable results. Default is 4. |

## Strengths

- Designed specifically for **mixed continuous/discrete** data.
- Avoids ad hoc discretization of continuous variables.
- Compatible with CG BIC scores and CG-aware search procedures.

## Limitations

- Requires enough samples per discrete configuration; sparse cells can be a
  problem.
- Assumes linear-Gaussian structure for continuous variables within each
  discrete cell.
- More complex and computationally intensive than purely continuous or purely
  discrete tests.

## References

- Lauritzen, S. L. (1996). *Graphical Models*. Oxford University Press.

## References

- Andrews, B., Ramsey, J., & Cooper, G. F. (2018). *Scoring Bayesian networks of mixed variables.* International Journal of Data Science and Analytics, 6(1), 3–18.