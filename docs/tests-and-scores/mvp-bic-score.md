# MVP BIC Score

## Summary

The MVP BIC Score is a BIC-type score tailored to **multivariate Poisson** or
related count-valued models. It evaluates DAGs or graphical structures where
nodes represent count variables with Poisson-like dependencies.

## When to use

- Variables are **counts** that may have multivariate Poisson structure.
- You are using specialized models or algorithms for count-valued causal
  discovery.
- You want a BIC-like score that respects the Poisson nature of the data.

## Model class

- Multivariate Poisson or related count models used in MVP-style structures.

## Score form (conceptual)

As a BIC-type score:

    BIC = 2 * logL − k * ln(N)

with `logL` computed under a multivariate Poisson model and `k` the number of
free parameters.

## Parameters in Tetrad

Typical parameters include:

- `penaltyDiscount` — Scales the BIC penalty term.
- Model-specific hyperparameters for the multivariate Poisson formulation.
- `verbose` — Logging of local MVP BIC contributions.

## Strengths

- Tailored to **count data** beyond simple univariate Poisson assumptions.
- Integrates with Poisson-based tests and priors.

## Limitations

- Requires a suitable multivariate Poisson model and estimation routine.
- May be sensitive to overdispersion and zero inflation.
