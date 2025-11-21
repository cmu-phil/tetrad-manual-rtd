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

## Parameters in Tetrad

Typical parameters include:

- `alpha` — Significance level.
- Regression-related hyperparameters (e.g., basis order, regularization) if
  exposed by the implementation.
- `verbose` — Whether to log internal regression fits and residual diagnostics.

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
