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

## Parameters

| Parameter (camelCase) | Description |
|-----------------------|-------------|
| `alpha`               | Significance level (p-value cutoff) for the likelihood-ratio test of conditional independence. The null hypothesis is that the variables are conditionally independent given the conditioning set. P-values below `alpha` lead to rejection. Smaller values make the test more conservative (fewer edges); larger values make the graph denser. Typical range: 0.0–1.0. |
| `fDegree`             | Integer ≥ 1. Degree parameter for the MVP projection model (for example, the degree of the polynomial or other basis used in the projection step). Higher values allow more flexible functional forms in the projections but increase the number of parameters and the risk of overfitting. Typical values are small integers such as 1, 2, or 3. |
| `discretize`          | Boolean. If `true`, continuous variables may be discretized in situations where the MVP likelihood-ratio test would otherwise be unstable or poorly supported (for example, very sparse configurations). If `false`, the test uses the continuous MVP projection model directly, which can be less robust when effective cell counts are small. Default is typically `true`. |

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

