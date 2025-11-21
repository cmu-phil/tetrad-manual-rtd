# Poisson BIC Test

## Summary

The Poisson BIC Test is simply the **Poisson Prior Score used as a
conditional-independence decision rule**.

For each query of the form “X independent of Y given S”, the test compares
two models (or graphs):

- a model where the edge between X and Y is **present** (given S), and
- a model where that edge is **absent**.

Both models are evaluated using the **same underlying likelihood score plus
the Poisson Prior Score** over structure. The difference in score is then
thresholded at **0**:

- if the Poisson-BIC-based score difference is **less than 0**, the test
  treats X and Y as **independent** given S;
- otherwise, it treats them as **dependent**.

There is **no explicit alpha parameter**; the decision is purely based on
whether the Poisson-augmented BIC score prefers the graph with or without the
edge.

## When to use

- You want a **CI test that is tightly aligned with a Poisson-based
  structural prior** on graphs.
- You are already using **PoissonPriorScore** (or a BIC-like score plus a
  Poisson structural prior) for structure learning and want your CI tests to
  reflect the same sparsity assumptions.
- You prefer a **zero-threshold, score-difference** rule instead of
  p-values.

## Relation to Poisson Prior Score

The Poisson Prior Score is a **structural prior over graph complexity**. It
places a Poisson distribution on edge or parent counts and adds the resulting
log prior as a term in the score, on top of the usual likelihood or BIC-type
term.

The Poisson BIC Test:

- reuses that **same score** (likelihood + Poisson structural prior),
- evaluates a model with the edge and a model without the edge,
- then decides independence by checking whether the **score difference is
  negative (BIC < 0 threshold)**.

So, Poisson BIC Test does not introduce a new noise model; it only reuses the
existing Poisson-based **structural prior** as a test statistic.

## Test details (conceptual)

For each X, Y, and conditioning set S, the test:

1. Constructs two models:
    - M_with: a model (or local graph) including the edge between X and Y
      conditioned on S.
    - M_without: the corresponding model with that edge removed.
2. Computes the Poisson-augmented score for each model:
    - score_with = base likelihood/BIC + PoissonPriorScore(M_with),
    - score_without = base likelihood/BIC + PoissonPriorScore(M_without).
3. Forms the **score difference** (for example, score_with − score_without).
4. If this score difference is **less than 0**, then the edge is not
   supported by the Poisson-BIC criterion, and the test declares:
   > X and Y are independent given S.
5. Otherwise, the test declares:
   > X and Y are dependent given S.

There is no rescaling to p-values; the decision is directly based on the sign
of the score difference.

## Parameters

The Poisson BIC Test exposes the same structural-prior parameters as
PoissonPriorScore, restricted to what is needed for testing:

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `precomputeCovariances` | Boolean. If `true`, precomputes and caches covariance (and possibly cross-covariance) matrices used by the underlying likelihood part of the score. This speeds up repeated evaluations at the cost of additional memory. If `false`, these quantities are recomputed on the fly, which saves memory but can be slower for large graphs or many score calls. |
| `poissonLambda`         | Double > 0. Lambda parameter for the Poisson **structural prior** on the number of edges or parents. This controls the expected count under the prior. Smaller values favor sparser graphs (fewer edges or parents on average); larger values allow denser graphs. Default is 1.0; minimum is about 1e-10. |
| `singularityLambda`     | Double. Handles singular or nearly singular covariance matrices in the underlying likelihood calculation. If `singularityLambda > 0`, that value is added to the diagonal (a ridge term) to stabilize matrix inverses. If `singularityLambda < 0`, a pseudoinverse is used instead. Default is 0.0. Use a small positive value if you encounter numerical-singularity warnings. |

## Strengths

- **Fully aligned** with the PoissonPriorScore: the CI decisions and score
  search share the same sparsity prior.
- No need to choose an alpha level; the decision rule is fixed at a **zero
  score-difference threshold**.
- Naturally expresses a belief in **Poisson-distributed complexity** (for
  example, typical number of parents per node) directly in the CI testing
  step.

## Limitations

- There is no p-value calibration; decisions are based solely on **score
  differences and the chosen Poisson prior**.
- The result depends on the choice of `poissonLambda` and the base score:
  overly small lambda can force over-sparse graphs (missing edges), while
  overly large lambda can allow too many edges.
- Requires computing scores for **two models per CI query**, which can be
  more expensive than tests that only use local partial correlations or
  contingency tables.