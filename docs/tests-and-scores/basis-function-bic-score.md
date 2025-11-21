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

## Parameters in Tetrad

Typical parameters include:

- `penaltyDiscount` — Scales the complexity penalty.
- Basis-related settings:
  - truncation order (maximum basis degree),
  - basis family (Legendre, Chebyshev, etc.).
- `standardize` — Whether to rescale variables before expansion.

## Strengths

- Captures a wide range of nonlinear functional relationships while retaining a
  finite parameterization.
- Integrates directly with nonlinear independence tests such as Basis Function
  LRT.

## Limitations

- Requires careful choice of basis and truncation level.
- Overly rich bases can overfit, while too simple bases may underfit.
- Computational cost grows with number of basis terms.

