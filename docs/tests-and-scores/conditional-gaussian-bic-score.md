# Conditional Gaussian BIC Score

## Summary

The Conditional Gaussian BIC Score is a BIC-type score for **conditional
Gaussian (CG) models** with mixed continuous and discrete variables. It
evaluates a DAG or CG structure by combining CG log-likelihood with a penalty
on the number of parameters.

## When to use

- Data are a mix of continuous and discrete variables.
- You assume a CG model: given the discrete variables, continuous variables are
  multivariate normal with means and covariances that may depend on discrete
  configurations.
- You are using score-based or hybrid algorithms that support CG models.

## Model class

- Conditional Gaussian Bayesian networks with discrete parents and linear-
  Gaussian continuous components.

## Score form (conceptual)

As with other BIC scores:

    BIC = 2 * logL − k * ln(N)

where `logL` is the CG log-likelihood and `k` is the number of free parameters
(conditional means, covariances, and discrete probabilities).

## Parameters in Tetrad

Typical parameters include:

- `penaltyDiscount` — Adjusts the strength of the complexity penalty.
- Options related to handling sparse discrete configurations or regularizing
  covariance estimates.
- `verbose` — Whether to log local scores.

## Strengths

- Properly accounts for **mixed** data types without discretizing continuous
  variables.
- Integrates naturally with CG independence tests and CG learning algorithms.

## Limitations

- Requires enough data per discrete configuration.
- Assumes linear-Gaussian behavior for continuous components.
