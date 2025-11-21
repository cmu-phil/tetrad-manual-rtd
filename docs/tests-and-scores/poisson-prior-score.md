# Poisson Prior Score

## Summary

The Poisson Prior Score is a structural prior over graph complexity. Instead of
saying anything about the noise distribution, it places a Poisson distribution
on edge or parent counts (for example, the number of parents per node), and
uses the resulting log prior as an additive term in the scoring function.

This lets you express a belief that graphs should be “about this sparse” on
average, in a way that is more interpretable than an ad hoc penalty.

## When to use

- You want to encode sparsity preferences explicitly in a probabilistic way.
- You care about the distribution of parent counts or edge counts across the
  graph (for example: most nodes should have around two parents on average).
- You are doing score-based structure learning and want a prior over structures
  in addition to the usual likelihood or BIC-type terms.

It does not assume Poisson noise in the data; the Poisson part is purely about
graph structure, not about residuals.

## Model class

PoissonPriorScore is agnostic about the underlying likelihood model. It can be
combined with:

- linear Gaussian SEM scores (for example, Sem BIC Score),
- discrete scores (for example, BDeu Score),
- mixed or other custom likelihoods,

as long as the implementation adds the Poisson structural prior on top of the
base score.

In other words, it is a graph prior that sits on top of whatever data
likelihood you use.

## Score form (conceptual)

Conceptually, you can think of the total score as:

- a data-fit term (for example, a BIC-like score), plus
- a log prior term that comes from a Poisson distribution over some structural
  count.

The Poisson prior usually works like this:

- Choose a structural count K (for example, number of edges, or number of
  parents of a node).
- Assume that K follows a Poisson distribution with some rate parameter
  lambda.
- The log prior then contributes a term that increases when K is close to the
  expected count under the Poisson(lambda) distribution and decreases when K
  is much larger or much smaller.

The implementation may vary in exactly which count or counts get the Poisson
prior: total edges, parents per node, or a similar structural measure.

## Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `precomputeCovariances` | Boolean. If `true`, precomputes and caches covariance (and possibly cross-covariance) matrices used by the underlying likelihood part of the score. This speeds up repeated scoring at the cost of additional memory. If `false`, these quantities are recomputed on the fly, which saves memory but can be slower for large graphs or many score evaluations. |
| `poissonLambda`         | Double > 0. Lambda parameter for the Poisson prior on structure (for example, number of edges or parents). This controls the expected count under the prior. Smaller values favor sparser graphs (fewer edges or parents on average); larger values allow denser graphs. Default is 1.0; minimum is about 1e-10. |
| `singularityLambda`     | Double. Handles singular or nearly singular covariance matrices in the likelihood term. If `singularityLambda > 0`, that value is added to the diagonal (a ridge term) to stabilize matrix inverses. If `singularityLambda < 0`, a pseudoinverse is used instead. Default is 0.0. Use a small positive value if you encounter numerical-singularity warnings. |
| `effectiveSampleSize`   | Double > 0, or `-1`. If `-1` (default), the actual sample size N is used in the log(N) penalty or likelihood part of the score. If set to a positive value, the score behaves as if that were the sample size (for example, when treating weighted or subsampled data as having a different effective N). |

## Strengths

- Interpretable sparsity prior: directly encodes an expected number of
  edges or parents.
- Can be easier to reason about than tuning more abstract penalties such as
  EBIC gamma when you think in terms of “average parents per node”.
- Plays nicely with existing likelihood-based scores, adding a Bayesian-style
  prior on structure.

## Limitations

- Choosing a good lambda is problem dependent:
    - If lambda is too small, the result is over-sparse graphs that miss true
      edges.
    - If lambda is too large, the result is overly dense graphs.
- The Poisson assumption is only an approximation to your beliefs about
  structure; real-world prior knowledge may be more nuanced.
- Adds another hyperparameter to tune; it is not a drop-in replacement for all
  BIC or EBIC-type penalties.

## Relation to other penalties

- BIC, EBIC, and GIC use information-theoretic penalties that are functions of
  parameter counts and dimension. They do not correspond directly to a literal
  probability distribution over graph structures.

- PoissonPriorScore encodes a probabilistic prior directly over graph
  structure. It can be viewed as part of a maximum a posteriori (MAP)
  objective, where you add log P(graph) to the usual log-likelihood or BIC
  term.

This makes it a useful alternative when you want explicit prior control over
sparsity but still want to leverage the same likelihoods used by BIC-like
scores.