# Poisson BIC Test

## Summary

The Poisson BIC Test is a model-comparison-based CI test for **count data**,
assuming a Poisson or Poisson-regression model. It evaluates whether including
a predictor Y significantly improves the model for X given S, using **BIC**
differences as a proxy for a hypothesis test.

## When to use

- The response variable is a **count** (non-negative integer).
- A Poisson (or Poisson-like) model is a reasonable approximation.
- You are using score-based or hybrid methods for **count-valued** data and
  want a consistent CI test.

## Assumptions

- Conditional on predictors, counts follow a Poisson distribution with mean
  modeled (typically) via a log link.
- Independence corresponds to the absence of Y in the Poisson regression for X
  given S (and vice versa).
- BIC differences can reasonably approximate evidence for or against
  independence.

## Test details (conceptual)

For each X ⟂ Y | S query, the test:

1. Fits a Poisson regression model for X ~ Y + S and a restricted model
   X ~ S.
2. Computes BIC for both models.
3. Translates the **difference in BIC** into a decision about independence:
   if including Y does not significantly improve BIC, X and Y are treated as
   independent given S.
4. Uses a threshold linked to the alpha level or a fixed BIC difference
   criterion.

## Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `precomputeCovariances` | Boolean. If `true`, precomputes and caches covariance (and possibly cross-covariance) matrices or related sufficient statistics used by the Poisson BIC-based test. This speeds up repeated evaluations at the cost of additional memory. If `false`, these quantities are recomputed on the fly, which saves memory but may slow down large runs. |
| `poissonLambda`         | Double > 0. Lambda parameter for the Poisson distribution used in the underlying likelihood. Controls the expected rate of counts under the Poisson model. Default is 1.0; minimum is about 1e-10. In most applications you can leave this at the default unless you have a specific reason to encode a different expected rate. |
| `singularityLambda`     | Double. Handles singular or nearly singular covariance or information matrices in the Poisson modeling step. If `singularityLambda > 0`, that value is added to the diagonal (a ridge term) to stabilize matrix inverses. If `singularityLambda < 0`, a pseudoinverse is used instead. Default is 0.0. Use a small positive value if you encounter numerical-singularity warnings. |

## Strengths

- Tailored to **count data** and Poisson-like processes.
- Integrates naturally with Poisson-based scores used in causal discovery.

## Limitations

- Poisson assumptions may be violated (overdispersion, zero-inflation).
- Requires model fitting for each CI query, which is more expensive than simple
  correlation-based tests.
- Calibration from BIC differences to p-values is approximate.

