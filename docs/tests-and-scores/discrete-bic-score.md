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

## Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `penaltyDiscount`       | Double ≥ 0.0. The penalty multiplier “c” in a BIC-type criterion (for example, a score of the form 2·log-likelihood minus c·k·log(N), where k is the number of free parameters and N is the sample size). Larger values impose a stronger complexity penalty and yield sparser graphs; smaller values allow denser graphs. Typical defaults are around 1–2. |
| `structurePrior`        | Double ≥ 0.0. Structure prior coefficient controlling a binomial-style prior on the number of parents per node. When 0.0 (default), the score uses essentially a flat structure prior. Increasing this value encodes a stronger preference for a particular expected in-degree and can bias the search toward graphs whose parent counts match that prior. |

## Strengths

- Standard score for discrete Bayesian networks.
- Easy to compute from counts and CPT cardinalities.

## Limitations

- Sensitive to sparse contingency tables; can be unstable when many cells have
  low counts.
- Assumes multinomial sampling and no model misspecification.
