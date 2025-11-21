# Generalized Information Criterion (GIC) Scores

## Summary

GIC (Generalized Information Criterion) Scores form a family of criteria that
generalize AIC and BIC by allowing more flexible penalty terms. In Tetrad, GIC
scores provide a tunable framework for balancing fit and complexity beyond the
standard BIC penalty.

## When to use

- You want more flexibility than BIC or EBIC in penalizing model complexity.
- You are exploring alternative trade-offs between fit and sparsity.
- You are running score-based or hybrid algorithms and wish to compare
  different penalty regimes.

## Model class

- Follows the same model classes as the underlying likelihood (SEM, discrete
  BN, etc.), but with a generalized penalty structure.

## Score form (conceptual)

A generic GIC score can be written as:

    GIC = 2 * logL − c(N, p, k)

where `c(N, p, k)` is a user-defined or theory-motivated penalty function
depending on sample size N, dimension p, and parameter count k.

## Parameters in Tetrad

Typical parameters include:

- `penaltyFunction` or hyperparameters specifying the penalty shape.
- Possibly γ-like or λ-like coefficients controlling penalty strength.
- `verbose` — Logging of GIC components.

## Strengths

- Highly flexible; can replicate AIC, BIC, EBIC, and other criteria as special
  cases.
- Useful for sensitivity analysis and method comparison.

## Limitations

- Theoretical guarantees depend on the specific penalty chosen.
- Parameter tuning can be nontrivial.
