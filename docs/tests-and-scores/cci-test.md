# CCI Test

## Summary

The CCI (Conditional Correlation Independence) Test is a flexible CI test that
relies on **correlation-based or regression-based residual checks**. It is
intended for use when relationships may be nonlinear but still exhibit
structures detectable through transformed or residualized correlations.

## When to use

- Data are continuous or can be reasonably treated as such.
- Relationships may be **nonlinear**, but you prefer a lower-cost alternative
  to fully nonparametric tests.
- You want a test that can exploit regression or residualization schemes
  combined with correlation checks.

## Assumptions

- Conditional relationships can be captured or approximated by regression plus
  correlation checks.
- Residuals are not too heavy-tailed or pathological.
- The regression model used internally is at least a reasonable approximation
  to the conditional mean.

## Test details (conceptual)

Conceptually, the CCI test:

1. Regresses X on S and Y on S (possibly using nonlinear or flexible
   regressors, depending on the implementation).
2. Examines the **residuals** r_X and r_Y for remaining dependence.
3. Uses correlation-type measures (possibly rank- or kernel-enhanced) on the
   residuals to test X ⟂ Y | S.
4. Calibrates a p-value using asymptotic or resampling-based approximations,
   depending on settings.

## Parameters

| Parameter (camelCase) | Description |
|-----------------------|-------------|
| `alpha`               | Significance level (p-value cutoff) for the conditional independence test. The null is conditional independence; p-values below `alpha` lead to rejection. Default is 0.01. Allowed range: 0.0–1.0. |
| `scalingFactor`       | Scaling factor for the Gaussian kernel used inside the CCI test. Larger values broaden the kernel (smoother similarity), smaller values make it more localized. Default is 1.0. |
| `basisType`           | Integer code for the type of basis functions used to approximate nonlinear relationships: `0 = Polynomial`, `1 = Legendre`, `2 = Hermite`, `3 = Chebyshev`. This controls which orthogonal (or polynomial) system is used in the expansion. |
| `truncationLimit`     | Truncation limit for the basis expansion. Basis functions with indices from 1 up to this value are included for each variable. Default is 3; minimum is 1; maximum is 1000. Larger values allow more flexible nonlinear fits but increase the number of parameters and the risk of overfitting. |
| `basisScale`          | Scaling parameter `b` used to rescale variables into the interval `[-b, b]` before applying the basis functions. If `basisScale = 0`, variables are standardized instead. Default is 1. Typical range is 0–500000, but values near 0–5 are most reasonable for real data. |

## Strengths

- Potentially more powerful than strictly linear-Gaussian tests when
  relationships are mildly nonlinear.
- Can be less computationally expensive than fully nonparametric kernel
  methods.

## Limitations

- Performance depends strongly on the **choice of regression model**.
- May miss complex conditional independences if the regression model is
  mis-specified.
- Behavior and calibration can be more heuristic than classical tests.
