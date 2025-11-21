# Poisson Prior Score

## Summary

The Poisson Prior Score is an information criterion that combines a likelihood
term with a **Poisson prior** on model features such as the number of edges or
parents per node. It is designed to encourage sparse structures in count-data
settings.

## When to use

- You wish to encode a prior belief that the number of edges or parents per
  node follows a Poisson distribution.
- You are modeling **count data** and want structured priors over graphs.
- You are exploring Bayesian or penalized-likelihood approaches to structure
  learning.

## Model class

- Typically used with count-valued DAGs or Poisson-based models, but in
  principle applicable wherever a Poisson prior over complexity is appropriate.

## Score form (conceptual)

The score combines:

- A log-likelihood term logL, and
- A log prior term logP(graph) based on a Poisson distribution over edge counts
  or parent counts,

often summarized in a BIC-like or MAP-style objective.

## Parameters in Tetrad

Typical parameters include:

- `lambda` — Rate parameter of the Poisson prior controlling expected sparsity.
- `penaltyDiscount` — May interact with the prior in the overall score.
- `verbose` — Logging of prior contributions and total score.

## Strengths

- Explicitly encodes sparsity preferences in a probabilistic form.
- More interpretable than ad hoc penalties for some users.

## Limitations

- Choice of λ strongly influences sparsity and model selection.
- Calibration may be problem-specific.
