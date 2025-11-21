# Extended BIC (EBIC) Score

## Summary

The Extended BIC (EBIC) Score is a generalization of BIC intended for
**high-dimensional settings**. It adds an extra penalty term that depends on
the number of possible edges, favoring sparser graphs more strongly than
standard BIC.

## When to use

- Number of variables is large relative to the sample size.
- You want stronger sparsity encouragement than standard BIC provides.
- You are using score-based methods (FGES, BOSS, GRaSP) in high-dimensional
  regimes.

## Model class

- Typically applied to linear Gaussian or discrete DAGs, but the EBIC form is
  generic.

## Score form (conceptual)

A common EBIC form is:

    EBIC = 2 * logL − k * ln(N) − 2 * γ * ln(choose(p, k_edges))

where γ is a parameter in [0, 1], `p` is the number of variables, and
`k_edges` is the number of edges.

## Parameters in Tetrad

Typical parameters include:

- `gamma` — Strength of the extra EBIC penalty term.
- `penaltyDiscount` — May co-exist with γ in some implementations.
- `verbose` — Whether to log EBIC contributions.

## Strengths

- More conservative than BIC, tending to select **sparser** graphs in high-
  dimensional settings.
- Supported by theory in some sparse regression and graphical model contexts.

## Limitations

- Choice of γ is somewhat problem-dependent.
- May penalize edges too strongly when N is not extremely small compared to p.
