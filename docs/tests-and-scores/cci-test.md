# CCI Test

## Summary

The CCI (Conditional Correlation Independence) Test is a flexible CI test that relies on **correlation-based or regression-based residual checks**. It is intended for use when relationships may be nonlinear but still exhibit structures detectable through transformed or residualized correlations.

## When to use

- Data are continuous or can be reasonably treated as such.
- Relationships may be **nonlinear**, but you prefer a lower-cost alternative to fully nonparametric tests.
- You want a test that can exploit regression or residualization schemes combined with correlation checks.

## Assumptions

- Conditional relationships can be captured or approximated by regression plus correlation checks.
- Residuals are not too heavy-tailed or pathological.
- The regression model used internally is at least a reasonable approximation to the conditional mean.

## Test details (conceptual)

Conceptually, the CCI test:

1. Regresses X on S and Y on S (possibly using nonlinear or flexible regressors, depending on the implementation).
2. Examines the **residuals** r_X and r_Y for remaining dependence.
3. Uses correlation-type measures (possibly rank- or kernel-enhanced) on the residuals to test conditional independence of X and Y.
4. Calibrates a p-value using asymptotic or resampling-based approximations, depending on settings.

## Parameters

| Parameter (camelCase) | Description |
|-----------------------|-------------|
| `alpha`               | Significance level (p-value cutoff). The null is conditional independence; p-values below `alpha` lead to rejection. Default is 0.01. Range: 0.0–1.0. |
| `scalingFactor`       | Gaussian-kernel scaling factor used inside the CCI test. Larger values broaden the kernel; smaller values make it more localized. Default: 1.0. |
| `basisType`           | Integer code for basis functions used for nonlinear approximation: `0 = Polynomial`, `1 = Legendre`, `2 = Hermite`, `3 = Chebyshev`. |
| `truncationLimit`     | Number of basis terms to include (1 through truncationLimit). Default: 3. Allowed: 1–1000. Higher values allow more nonlinear flexibility, with increased risk of overfitting. |
| `basisScale`          | Rescaling parameter b for mapping variables into [-b, b]. If `basisScale = 0`, variables are standardized instead. Default: 1. Typical useful values: 0–5. |

## Strengths

- More powerful than linear-Gaussian tests when relationships are mildly nonlinear.
- Less computationally demanding than fully nonparametric kernel CI tests.

## Limitations

- Performance depends heavily on the **regression model** used.
- May miss complex nonlinear dependencies if the regression model is mis-specified.
- Calibration may be more heuristic than classical tests.

## References

- Zhang, K., Peters, J., Janzing, D., & Schölkopf, B. (2012).  
  *Kernel-based conditional independence test and application in causal discovery.*  
  arXiv preprint arXiv:1202.3775.

- Ramsey, J. D. (2014).  
  *A scalable conditional correlation-based independence test.*  
  CMU Technical Report, Department of Philosophy.

- Runge, J. (2018).  
  *Conditional independence testing based on nearest-neighbor estimators.*  
  In *Proceedings of the 34th Conference on Uncertainty in Artificial Intelligence (UAI)*.

- Pfister, N., Bühlmann, P., Schölkopf, B., & Peters, J. (2018).  
  *Kernel-based tests for joint independence.*  
  *Journal of the Royal Statistical Society, Series B*, 80(1), 5–31.