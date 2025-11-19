# TSC — Trek Separation Clusters

**Category:** Latent clusters / measurement structure  
**Code:** `edu.cmu.tetrad.search.Tsc`

TSC (“Trek Separation Clusters”) is a rank-based latent *cluster* finder.
Given a covariance (or correlation) matrix over observed variables, it searches
for disjoint groups of indicators that behave as if they share one or more
latent parents.

The implementation in Tetrad is a **NOLAC** version (“no overlapping clusters”):
each observed variable is assigned to at most one cluster.

---

## Intended use

Use **TSC** when:

- You believe your data come (approximately) from a **linear-Gaussian latent
  variable model** with **pure indicators**.
- Each observed variable should load on **one latent at most** (no overlapping
  measurement clusters).
- You want an *automatic* partition of variables into clusters that can then be
  fed into higher-level latent-structure algorithms (e.g., FOFC/FTFC/GFFC/BPC or
  manual SEM modeling).

TSC works directly on a **covariance matrix** (internally converted to a
correlation matrix) and is therefore agnostic to the original sample size and
data format, provided you give a correct effective sample size.

---

## Model assumptions (NOLAC version)

TSC is designed to be (asymptotically) sound under the following stylized
assumptions:

1. **Linear-Gaussian SEM with a latent DAG**

    - Latent variables form a DAG.
    - Observed indicators are linear functions of their latent parents plus
      independent Gaussian noise.

2. **Pure measurement within clusters**

    - Each observed variable has exactly one latent parent (within the latent
      structure you care about).
    - Unique errors of indicators belonging to different clusters are
      independent.

3. **No overlapping clusters (NOLAC)**

    - Each observed variable belongs to **at most one** true cluster.

4. **Generic parameters**

    - There are no exact parameter cancellations that artificially change matrix
      ranks.

5. **Consistent rank test**

    - Cross-block matrix rank is tested using Wilks’ likelihood-ratio test (or a
      similar rank test), with a significance level `alpha` that decreases with
      `n` (for example, `alpha = 1 / log n`) or with an information-criterion
      cutoff.

Under these assumptions, the algorithm aims to recover, asymptotically, the true
indicator clusters and their “boundary ranks” (typically 1 for a single latent).

---

## High-level algorithm sketch

Let `V` be the index set of all observed variables, and let `Sigma` be the
correlation matrix. For a candidate cluster `C ⊂ V`, define `D = V \ C`.  
TSC examines the rank of the cross-covariance block `Sigma[C, D]`.

Very roughly:

1. **Base clusters by rank**

   For each rank `r = 0, …, rMax`:

    - Let the base size be `|C| = r + 1`.
    - Enumerate all subsets `C` of that size.
    - Keep those where

      `rank(Sigma[C, D]) = r`

      according to a Wilks rank test with parameters `(nEff, alpha)`.

2. **Seed and grow clusters (union / extension)**

    - Starting from unused base subsets at rank `r`, pick a seed cluster.
    - Try to union it with other overlapping base subsets at the same rank.
    - Accept a union `C' = C ∪ C_candidate` when:
        - `rank(Sigma[C', V \ C'])` is still `r`, and
        - `|C'| >= r + 1 + minRedundancy`.
    - This iteratively produces maximal rank-`r` clusters that do not overlap
      previously committed variables.

3. **Bifactor-style augmentation**

    - For each new cluster `C1`, look for a nearby variable that, when added,
      causes a one-step rank drop:

        - `rank(Sigma[C1, V \ C1]) = r`
        - `rank(Sigma[C2, V \ C2]) = r - 1`, where `C2 = C1 ∪ {x}` and  
          `|C2| = |C1| + 1`.

    - This step is designed to capture bifactor-like or multi-dimensional
      boundaries in which adding a “spanning” indicator reduces cross-rank by 1.
    - Candidate augmentations that create internal rank-0 splits are rejected
      (see step 5).

4. **Conditional-rank refinement (Rule 3)**

   For each candidate cluster `C` of intended rank `r_C`:

    - Let `D = V \ C`.
    - Search for subsets `Z ⊂ C` with `|Z| >= r_C` such that

      `rank(C \ Z, D | Z) = 0`.

    - If such a `Z` is found, it is treated as an observed bottleneck or
      mediator; the variables in `Z` are removed from `C`.
    - Repeat until no such `Z` remains or the cluster becomes too small.

   Intuition: in a purely observed DAG (no latents), a mediator can d-separate
   `C \ Z` from `D` when conditioned on. This pattern should not persist for a
   genuine latent cluster under the measurement assumptions above.

5. **Internal rank-0 check**

   Finally, for each refined cluster `C`:

    - Examine nontrivial splits `C = C1 ∪ C2` and test

      `rank(C1, C2) = 0`.

    - If a cluster hides such a rank-0 partition inconsistent with its assigned
      rank, it is rejected.

6. **Output**

    - The method `findClusters()` returns a map

      ```java
      Map<Set<Integer>, Integer>  // cluster -> rank
      ```

      where each `Set<Integer>` indexes a disjoint indicator cluster and the
      associated `Integer` is the estimated cross-rank of that cluster.

---

## Inputs and outputs

### Inputs

TSC is constructed from:

- `List<Node> variables`
- `CovarianceMatrix cov`

Internally, the covariance is converted to a correlation matrix and the
sample size `n` is read from `cov.getSampleSize()`.

### Output

- `Map<Set<Integer>, Integer> clusterToRank`

Each entry:

- Key: a cluster (set of integer indices into the original variable list).
- Value: the estimated cross-rank at the boundary with the rest of the
  variables. For single-latent clusters this is typically `1`.

In the GUI and wrapper algorithms, these indices are converted back to variable
names and used to define latent-indicator blocks.

---

## Key parameters

These are set on the `Tsc` object before calling `findClusters()`:

| Parameter | Method | Meaning |
|-----------|--------|---------|
| `alpha` | `setAlpha(double)` | Significance level for Wilks rank tests. Lower values make rank increases/decreases harder to accept. |
| `nEff` | `setEffectiveSampleSize(int)` | Effective sample size. Use `-1` (default) to fall back to `cov.getSampleSize()`. Important if your covariance comes from a transformed or weighted sample. |
| `rMax` | `setRmax(int)` | Maximum rank to consider. The search runs ranks `0` through `rMax`. Defaults to `3`. |
| `minRedundancy` | `setMinRedundancy(int)` | Minimum extra indicators beyond `r + 1` required for a cluster to be accepted. Clusters must satisfy `|C| >= r + 1 + minRedundancy`. |
| `verbose` | `setVerbose(boolean)` | If `true`, logs detailed progress and rank decisions via `TetradLogger`. |

---

## Practical guidance

- **Alpha scheduling.** For large samples, consider an `n`-dependent `alpha`
  (for example `alpha = 1 / log n`) or an information-criterion-based cutoff to
  control false rank changes.
- **Redundancy.** Set `minRedundancy >= 1` to avoid unstable clusters of size
  exactly `r + 1`, which cannot be cross-checked internally.
- **Effective sample size.** If your covariance comes from:
    - weighted data,
    - time-series with autocorrelation, or
    - a pre-averaged dataset,

  adjust `nEff` accordingly to avoid overly optimistic rank tests.
- **NOLAC limitation.** This implementation enforces disjoint clusters. If your
  theory requires indicators to belong to multiple factors, TSC in its current
  form is not appropriate.

---

## Limitations

- Designed for linear-Gaussian models; non-Gaussian data can still work but the
  Wilks-based rank test may be less well calibrated.
- Assumes pure measurement and no overlapping clusters. Violation of these
  assumptions can fragment or merge clusters in undesirable ways.
- Sensitive to sampling noise when:
    - sample sizes are small, or
    - true cross-ranks are close to the decision boundary.

In such cases, adjust `alpha`, `nEff`, and `minRedundancy`, and inspfect clusters
visually or via domain knowledge.

---

## Related methods

TSC is typically used as a building block for other latent cluster or
measurement-model procedures in Tetrad, including:

- **FOFC / FTFC / GFFC / BPC** — methods that take TSC-style clusters as input
  or use similar rank-based ideas to construct measurement structures.
- **Blocks-TS test** and **Blocks-BIC score** — latent-structure tests/scores
  that can be paired with PC or other algorithms to recover latent structure
  over pre-identified blocks.ff