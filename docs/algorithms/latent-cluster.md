# Latent Clusters

Latent cluster algorithms identify measurement clusters—groups of observed variables that are likely explained by the same latent factor. These methods assume that each cluster corresponds to a single underlying cause, and they aim to recover a partition of the measured variables into pure clusters. Each cluster can then be used to construct a latent variable for downstream structural learning (e.g., MIM-building or DAG/PAG search).

Latent cluster algorithms in Tetrad are unsupervised and model-free: they operate directly on covariance patterns or conditional independences and do not require specifying the number of clusters in advance.

## Key Idea

All latent cluster algorithms in Tetrad exploit the theory of trek separation, which characterizes the covariance structure induced by latent variables. Roughly:

- Variables sharing a latent cause exhibit distinctive covariance patterns.
- Variables with different latent ancestors obey different sets of rank or independence constraints.
- These constraints allow consistent clustering without estimating the latent variables.

Different algorithms implement different approximations or statistical heuristics, but they all aim to recover clusters of indicators that behave as if they shared a single latent parent.

## When to Use

Use latent cluster algorithms when:

- You expect latent variables whose indicators appear in clusters.
- You have many observed variables, and want to reduce dimensionality before structural learning.
- You aim to fit a measurement model (MIM) or SEM but do not know the factor structure.
- You want a model-free method that does not assume linear loadings or Gaussian noise.

## Prior Knowledge Support

Does it accept background knowledge?  
No.  
Latent clustering algorithms operate purely on observed covariance relations and do not incorporate forbidden/required edges or tier constraints.

## Strengths

- Recovers pure measurement clusters without specifying the number of clusters.
- Does not require estimating latent variables or loadings.
- Based on principled structural constraints (trek-separation).
- Works well as preprocessing for SEM, MIMBUILD, or latent-structure PC/FGES.
- Scales well to moderately large numbers of indicators.

## Limitations

- Assumes that each observed variable belongs to at most one cluster.
- Does not estimate the structural graph among latent variables—only clusters.
- Requires reasonably reliable covariance estimates (sample size considerations apply).
- Some methods assume linear-Gaussian covariance structure for consistency.

## Latent Cluster Algorithms in Tetrad

The following algorithms implement latent clustering:

- **TSC** — [Trek Separation Clusters](tsc.md)  
  Rank-based trek-separation clustering using Wilks tests.

- **FOFC** — [First-Order Factor Clustering](fofc.md)  
  Classic pure tetrad (2×2) clustering with substitution checks.

- **FTFC** — [Fast Tetrad-Factor Clustering](ftfc.md)  
  FOFC-style clustering specialized for 3×3 “sextad” structures.

- **GFFC** — [Generalized Factor Finding Clustering](gffc.md)  
  Multi-stage clustering: first 2×2, then 3×3, then larger blocks on the remainder.

- **BPC** — [Build Pure Clusters](bpc.md)  
  Silva–Scheines–Glymour–Spirtes–style global pure clustering with merging and overlap resolution.

## Relationship to Latent Structure Algorithms

Latent cluster algorithms identify measurement blocks. Once clusters are obtained, they can be converted into latent variables, and then:

- **Blocks-Test-TS** (trek-separation independence test)
- **Blocks-BIC** (latent-aware score)

allow standard algorithms like PC, FGES, BOSS, GFCI, etc., to be used for the structural causal graph among latent variables.

## Summary

Latent cluster algorithms recover groups of observed variables that behave as indicators of common latent variables, using covariance and trek-separation constraints. They serve as an essential first step for building latent variable models and for causal discovery in settings with hidden factors.
