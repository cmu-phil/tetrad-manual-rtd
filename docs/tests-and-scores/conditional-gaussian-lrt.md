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

## Parameters in Tetrad

Typical parameters include:

- `alpha` — Significance threshold for rejecting independence.
- Options controlling how CG models are regularized or how small cells are
  handled (if implemented).
- `verbose` — Whether to show test counts and warnings about sparse cells.

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
