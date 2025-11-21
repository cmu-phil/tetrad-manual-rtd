# Discrete BIC Score

## Summary

The Discrete BIC Score is a BIC-type score for **discrete Bayesian network
structures**. It evaluates DAGs where each node has a multinomial conditional
probability table (CPT) given its parents.

## When to use

- All variables are **discrete** (categorical).
- You are learning a DAG using FGES, BOSS, GRaSP, or similar algorithms on
  discrete data.
- You want a score derived from the multinomial likelihood with a BIC
  penalty.

## Model class

- Discrete Bayes nets with CPTs for each node given its parents.
- No latent variables (unless explicitly modeled in a more complex framework).

## Score form (conceptual)

The score has the form:

    BIC = 2 * logL − k * ln(N)

where `logL` is the log-likelihood under the multinomial parameter estimates,
`k` is the number of free CPT parameters, and `N` is the sample size.

## Parameters in Tetrad

Typical parameters include:

- `penaltyDiscount` — Scales the complexity penalty term.
- `ess` or equivalent sample size parameters may be used in related scores
  but not in pure Discrete BIC.
- `verbose` — Whether to log local scores and structure updates.

## Strengths

- Standard score for discrete Bayesian networks.
- Easy to compute from counts and CPT cardinalities.

## Limitations

- Sensitive to sparse contingency tables; can be unstable when many cells have
  low counts.
- Assumes multinomial sampling and no model misspecification.
