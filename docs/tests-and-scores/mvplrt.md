# Multivariate Polynomial Likelihood Ratio Test (MVPLRT)

## Summary

The Multivariate Polynomial Likelihood Ratio Test (MVPLRT) is a **nonlinear
parametric CI test** that uses multivariate polynomial regression models. It
compares models for X with and without Y (given S) using a likelihood ratio
statistic based on polynomial expansions.

## When to use

- Data are continuous, and relationships are suspected to be **smooth but
  nonlinear**.
- You are willing to approximate conditional means using polynomial expansions.
- Sample size is sufficient to estimate polynomial terms stably.

## Assumptions

- Conditional expectations can be well approximated by multivariate polynomials
  up to a chosen degree.
- Residuals are approximately independent with finite variance.
- Polynomial order and interactions are chosen in a way that balances bias and
  variance.

## Test details (conceptual)

For each X ⟂ Y | S query:

1. Fit a polynomial regression model for X on S and Y up to a truncation degree.
2. Fit a reduced polynomial model for X on S only.
3. Compute the likelihood ratio statistic for the difference between full and
   reduced models.
4. Use a chi-square approximation for the difference in degrees of freedom to
   obtain a p-value.

## Parameters in Tetrad

Typical parameters include:

- `alpha` — Significance level.
- `maxDegree` — Maximum polynomial degree (truncation order).
- Possibly options for including or excluding interaction terms.
- `verbose` — Whether to report fitted polynomial terms and diagnostics.

## Strengths

- Can capture flexible **nonlinear** dependencies using a finite set of
  polynomial terms.
- Provides a parametric likelihood ratio framework with interpretable degrees
  of freedom.

## Limitations

- Polynomial models can become unstable or overfit if degree is too high
  relative to sample size.
- Performance is sensitive to scaling of variables and choice of degree.
- May not capture highly non-smooth relationships efficiently.

