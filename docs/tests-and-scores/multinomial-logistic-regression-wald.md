# Multinomial Logistic Regression Wald Test

## Summary

The Multinomial Logistic Regression Wald Test is a CI test based on fitting a
multinomial logistic model for a **categorical outcome** and using Wald
statistics to test whether a predictor Y contributes significantly beyond a set
of covariates S.

## When to use

- You have a **multiclass categorical** response variable.
- You want a regression-based CI test where independence corresponds to the
  absence of certain regression coefficients.
- Sample sizes are large enough for asymptotic Wald approximations.

## Assumptions

- A multinomial logistic regression model is appropriate for the outcome.
- Independence X ⟂ Y | S corresponds to zero coefficients for Y in the model
  for X given S (or vice versa, depending on how test is set up).
- Standard regularity conditions for Wald tests hold.

## Test details (conceptual)

For each X ⟂ Y | S query, the test:

1. Treats X (or Y) as the categorical response.
2. Fits a multinomial logistic regression with predictors S and Y.
3. Checks whether the coefficients associated with Y differ significantly from
   zero using a **Wald statistic**.
4. Converts the Wald statistic to a p-value using a chi-square approximation.

## Parameters in Tetrad

Typical parameters include:

- `alpha` — Significance level for rejecting independence.
- Regularization options or penalties in the multinomial model (if exposed).
- `verbose` — Whether to print coefficient estimates and test statistics.

## Strengths

- Regression-based and flexible for multi-category outcomes.
- Can handle multiple predictors simultaneously in S.
- Integrates naturally with generalized linear model workflows.

## Limitations

- Model fitting can be expensive for large graphs and many CI queries.
- Results depend on multinomial logistic model assumptions.
- May be unstable when some categories are rare.

