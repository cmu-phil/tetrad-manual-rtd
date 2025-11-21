# Basis Function BIC Score

## Summary

The Basis Function BIC Score is a BIC-type score for **nonlinear additive or partially nonlinear models** built using finite basis expansions. It supports **continuous variables** (using polynomial or orthogonal basis functions) and **discrete variables** (expanded into indicator bases). This makes it suitable for **mixed continuous/discrete datasets**.

The score evaluates DAG structures where each node is modeled via a basis-function regression on its parents, regardless of whether they are continuous or discrete.

## When to use

- Data may include **nonlinear continuous** relationships and/or **categorical variables**.
- You want a **single unified scoring approach** that handles mixed data without discretization.
- You are using hybrid or score-based algorithms such as **BOSS**, **GES/FGES**, **GRaSP**, or **FCIT**.

## Model class

- Each variable is modeled using a **basis expansion** of its parents:
    - Continuous parents use orthogonal/polynomial basis functions truncated at some order.
    - Discrete parents use **indicator basis functions** (all categories except one).
- This allows the conditional mean to approximate smooth nonlinear functions and interactions.

Residuals are assumed independent with finite variance (often Gaussian for scoring).

## Score form (conceptual)

As with other BIC scores:

    BIC = 2 * logL − k * ln(N)

where:

- `logL` = log-likelihood under the fitted basis-function model
- `k` = number of basis coefficients
- `N` = sample size

## Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `truncationLimit`       | Integer ≥ 1. Truncation level for continuous-variable basis expansions. Larger values fit more complex nonlinearities but increase dimensionality. |
| `penaltyDiscount`       | Double ≥ 0. Multiplier for the BIC penalty term. Higher values encourage sparser graphs. |
| `regularizationLambda`  | Ridge regularization parameter for basis regression. Helps with nearly singular Gram matrices. |

## Strengths

- Handles **mixed continuous + discrete** datasets in a unified framework.
- Captures **smooth but nonlinear** functional dependencies.
- Integrates directly with BOSS, GRaSP, and nonlinear constraint-based tests.

## Limitations

- Must choose basis family and truncation limit.
- Too many basis terms can overfit without sufficient sample size.
- Assumes finite-parameter expansions, not arbitrary nonparametric functions.

## References

- Ramsey, J., Andrews, B., & Spirtes, P. (2025). *Scalable causal discovery from recursive nonlinear data via truncated basis function scores and tests.* arXiv:2510.04276.