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

## Parameters

| Parameter (camelCase)     | Description |
|---------------------------|-------------|
| `semGicRule`              | Choice of generalized information criterion rule for SEM. Selects which GIC formula is applied (for example, a Zhang–Shen–type rule versus more BIC-like variants). In the GUI, this is exposed as a drop-down of named options; the underlying code uses an integer or enum to represent the choice. |
| `penaltyDiscountZs`       | Double ≥ 0.0. Penalty discount (or weight) specific to the Zhang–Shen–style GIC rule. Larger values impose a stronger complexity penalty under that rule and tend to yield sparser graphs; smaller values allow denser graphs. Has an effect only when a Zhang–Shen–type GIC rule is selected. |
| `precomputeCovariances`   | Boolean. If `true`, precomputes and caches covariance (and possibly cross-covariance) matrices used by the score. This speeds up repeated scoring at the cost of additional memory. If `false`, these quantities are recomputed on the fly, which saves memory but can be slower for large graphs or many score evaluations. |
| `singularityLambda`       | Double. Handles singular or nearly singular covariance matrices. If `singularityLambda > 0`, that value is added to the diagonal (a ridge term) to stabilize matrix inverses. If `singularityLambda < 0`, a pseudoinverse is used instead. Default is often 0.0. Use a small positive value if you encounter numerical-singularity warnings. |
| `effectiveSampleSize`     | Double > 0, or `-1`. If `-1` (default), the actual sample size N is used in the log(N) penalty part of the GIC. If set to a positive value, the score behaves as if that were the sample size (for example, when treating weighted or subsampled data as having a different effective N). |

## Strengths

- Highly flexible; can replicate AIC, BIC, EBIC, and other criteria as special
  cases.
- Useful for sensitivity analysis and method comparison.

## Limitations

- Theoretical guarantees depend on the specific penalty chosen.
- Parameter tuning can be nontrivial.

## References

- Kim, Y., Kwon, S., & Choi, H. (2012). *Consistent model selection criteria on high dimensions.* Journal of Machine Learning Research, 13(1), 1037–1057.