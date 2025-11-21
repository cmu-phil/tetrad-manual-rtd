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

## Parameters

| Parameter (camelCase)        | Description |
|-----------------------------|-------------|
| `kciUseApproximation`       | Boolean. If `true`, uses the **Gamma approximation** algorithm from Zhang et al. (2012); if `false`, uses the exact (more computationally intensive) procedure. |
| `alpha`                     | Significance level for the test. The null hypothesis is conditional independence; smaller values make the test more conservative (fewer rejections). |
| `scalingFactor`             | Scaling factor for the **Gaussian kernel**. Larger values effectively broaden the kernel; smaller values make it more localized.  [oai_citation:0‡parameter.definitions.md](sediment://file_00000000984c71f78b5770ce8355167d) |
| `kciNumBootstraps`          | Number of bootstrap samples used for the KCI null distribution (Theorem 4 and Proposition 5 in Zhang et al. 2012). Must be a positive integer.  [oai_citation:1‡parameter.definitions.md](sediment://file_00000000984c71f78b5770ce8355167d) |
| `kciEpsilon`                | Small positive epsilon used in Proposition 5 of Zhang et al. (2012) to regularize the test statistic. Typically left at its default unless you know you need to tune it.  [oai_citation:2‡parameter.definitions.md](sediment://file_00000000984c71f78b5770ce8355167d) |
| `kernelType`                | Which kernel to use: `1 = Gaussian`, `2 = Linear`, `3 = Polynomial`. Controls the feature space in which independence is tested.  [oai_citation:3‡parameter.definitions.md](sediment://file_00000000984c71f78b5770ce8355167d) |
| `polynomialDegree`          | For the **polynomial kernel**: the degree (order) of the polynomial feature map. Higher degree emphasizes higher-order interactions.  [oai_citation:4‡parameter.definitions.md](sediment://file_00000000984c71f78b5770ce8355167d) |
| `polynomialConstant`        | For the **polynomial kernel**: the additive constant term controlling the tradeoff between lower-order and higher-order terms.  [oai_citation:5‡parameter.definitions.txt](sediment://file_00000000083c71f59a73102e9b5b9ccc) |

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
