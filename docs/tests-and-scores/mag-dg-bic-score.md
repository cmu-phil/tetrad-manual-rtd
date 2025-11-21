# MAG Degenerate Gaussian BIC Score

## Summary

The MAG Degenerate Gaussian BIC Score is a BIC-type score specialized for
**Maximal Ancestral Graphs (MAGs)** in the presence of degeneracies in the
Gaussian covariance structure. It is intended for latent-variable models where
the observed margin may be singular or nearly singular.

## When to use

- You are scoring **MAG structures** with continuous Gaussian variables.
- Latent variables or selection mechanisms induce degeneracies or near-
  singular covariance matrices.
- You want a BIC-like criterion for MAG learning or evaluation.

## Model class

- Gaussian MAGs, representing the marginal structure over measured variables
  induced by latent-variable DAGs.

## Score form (conceptual)

The score adapts Gaussian BIC ideas to the MAG context, with regularized or
pseudo-inverse covariance operations:

    BIC ≈ 2 * logL_mag − k_mag * ln(N)

where `logL_mag` and `k_mag` reflect the marginalized Gaussian likelihood and
parameter count for the MAG.

## Parameters in Tetrad

Typical parameters include:

- `penaltyDiscount` — Complexity-penalty scaling.
- Regularization and numerical stability settings.
- `verbose` — Logging of MAG-specific likelihood and convergence issues.

## Strengths

- Tailored to **latent-variable** Gaussian settings in MAG form.
- More stable than naive Gaussian likelihood in degenerate cases.

## Limitations

- Requires careful implementation of MAG likelihood and parameter counting.
- Approximate in severely degenerate or ill-conditioned problems.
