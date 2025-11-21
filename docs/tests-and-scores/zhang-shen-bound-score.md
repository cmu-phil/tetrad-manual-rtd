# Zhang–Shen Bound Score

## Summary

The Zhang–Shen Bound Score is a specialized criterion inspired by theoretical
bounds on causal discovery or structure learning performance, associated with
work by Zhang and Shen and collaborators. In Tetrad, it serves as an
experimental or research-focused score to evaluate graphs under such bounds.

## When to use

- You are experimenting with **theoretical guarantees** or bounds-based
  selection criteria.
- You are working with algorithms or studies that directly reference the
  Zhang–Shen framework.
- You want to compare standard BIC-like selection with a more theory-driven
  bound-based metric.

## Model class

- Depends on the specific bound and setting; often continuous or discrete DAGs
  with certain regularity assumptions.

## Score form (conceptual)

The score encodes either:

- An upper or lower bound on risk or error associated with a structure, or
- A surrogate objective motivated by such a bound,

and is used as a scalar criterion for comparing candidate graphs.

## Parameters in Tetrad

Typical parameters might include:

- Hyperparameters appearing in the bound or its approximation.
- `penaltyDiscount` – If combined with other terms.
- `verbose` — Logging of bound components and derived scores.

## Strengths

- Grounded in theoretical performance bounds.
- Encourages exploration of criteria beyond classical likelihood penalties.

## Limitations

- More specialized and less standard than BIC/EBIC; interpretation may be less
  familiar.
- Theoretical assumptions behind the bound may not hold in all applied
  settings.
