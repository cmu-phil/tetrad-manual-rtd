# Basis Function BIC Score

## Summary

The Basis Function BIC Score is a BIC-type score for **nonlinear additive
models** built using basis expansions (e.g., polynomial or orthogonal basis
functions). It evaluates DAG structures where each node is modeled as a
basis-function regression on its parents.

## When to use

- You believe the causal relationships are **nonlinear** but smooth.
- You use basis expansions (e.g., Legendre polynomials) to approximate
  conditional means.
- You are running score-based or hybrid algorithms designed for nonlinear
  settings.

## Model class

- Additive or general nonlinear models with basis expansions at each node.
- Errors typically assumed independent with finite variance (often Gaussian
  for scoring).

## Score form (conceptual)

As with other BIC scores:

    BIC = 2 * logL − k * ln(N)

where `logL` is the log-likelihood under the fitted basis-function model and
`k` is the number of basis coefficients.

## Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `truncationLimit`       | Integer ≥ 1. Truncation level for the basis expansion. Basis functions with indices from 1 up to this value are included for each continuous variable (for example, the first 3 Legendre polynomials). Larger values allow more flexible nonlinear fits but increase the number of parameters and the risk of overfitting. Default is 3. |
| `penaltyDiscount`       | Double ≥ 0. The penalty multiplier “c” in the modified BIC-type criterion (for example, a score of the form 2·log-likelihood − c·k·log(N), where k is the number of free parameters and N is the sample size). Larger values impose a stronger complexity penalty and yield sparser graphs; smaller values allow denser graphs. Typical defaults are around 1–2. |
| `regularizationLambda`  | Double ≥ 0. Small nonnegative ridge term added to the diagonal of covariance or Gram matrices used in the regression / basis-function fitting. Default is 1e−8. Increasing this can improve numerical stability when matrices are nearly singular, at the cost of slightly biasing coefficients toward zero. |

## Strengths

- Captures a wide range of nonlinear functional relationships while retaining a
  finite parameterization.
- Integrates directly with nonlinear independence tests such as Basis Function
  LRT.

## Limitations

- Requires careful choice of basis and truncation level.
- Overly rich bases can overfit, while too simple bases may underfit.
- Computational cost grows with number of basis terms.

