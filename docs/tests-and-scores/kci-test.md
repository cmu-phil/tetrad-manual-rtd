# Kernel Conditional Independence Test (KCI)

## Summary

The Kernel Conditional Independence (KCI) test is a **nonparametric CI test**
based on reproducing kernel Hilbert spaces (RKHS). It detects whether X is
independent of Y given S by embedding the joint distributions into RKHSs and
measuring conditional cross-covariances.

## When to use

- Data may involve **complex nonlinear relationships** and **non-Gaussian
  distributions**.
- You want a general-purpose nonparametric CI test, without assuming a specific
  parametric model.
- Sample sizes are moderate (KCI is computationally more intensive than
  simple parametric tests).

## Assumptions

- Data are i.i.d. samples from a joint distribution over (X, Y, S).
- The chosen kernels (e.g., Gaussian RBF) are characteristic enough to capture
  dependencies.
- Kernel bandwidths and regularization parameters are reasonably tuned.

## Test details (conceptual)

For each X ⟂ Y | S query, the KCI test:

1. Constructs kernel matrices for X, Y, and S using a chosen kernel (such as
   Gaussian RBF).
2. Forms an estimator of the **conditional cross-covariance operator** of X
   and Y given S in the RKHS.
3. Uses a trace or norm of this operator as the test statistic.
4. Calibrates the null distribution using asymptotic approximations,
   permutations, or resampling to obtain a p-value.

## Parameters in Tetrad

Typical parameters include:

- `alpha` — Significance level.
- Kernel parameters (e.g., bandwidths) and regularization strengths.
- `numResamples` — Number of resampling iterations for calibration (if
  applicable).
- `verbose` — Whether to log kernel statistics and timing information.

## Strengths

- Very flexible: can capture highly **nonlinear** and **non-Gaussian** patterns
  of dependence.
- Suitable as a gold-standard nonparametric CI test for small- to moderate-
  sized problems.

## Limitations

- Computationally expensive for large sample sizes (N) or many CI tests.
- Requires kernel and hyperparameter choices; performance can be sensitive to
  bandwidth settings.
- Less scalable than basis-function or parametric tests for large-scale
  graph discovery.

## References

- Zhang, K., Peters, J., Janzing, D., & Schölkopf, B. (2012).
  Kernel-based conditional independence test.
  *Journal of Machine Learning Research*, 13, 555–587.
