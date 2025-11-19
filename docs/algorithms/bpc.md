# BPC — Build Pure Clusters

**Type:** Latent cluster discovery (measurement model)  
**Output:** Disjoint clusters of observed variables interpreted as indicators of latent factors  
**Reference:** Silva, Scheines, Glymour, Spirtes (JMLR, 2006)

BPC (Build Pure Clusters) is a **tetrad-based latent clustering** procedure inspired by the JMLR paper by Silva et al. It searches for groups of observed variables that:

1. Are mutually dependent (correlated enough to plausibly share a latent cause), and
2. Satisfy **tetrad constraints** consistent with a single latent factor,
3. Have **at least three indicators** (the paper’s rule to avoid fragile latents).

The implementation in Tetrad follows the *spirit* of the original paper but uses a practical, deterministic set of rules for growing, merging, and purifying clusters.

---

## Basic Assumptions

BPC is intended for:

- **Continuous, approximately Gaussian indicators**
- **Linear latent factor models**
- **Pure clusters**: each observed variable ideally loads on a single latent (no cross-loadings)

It operates on a **covariance or correlation matrix**, not on raw data, and uses Wilks-based rank tests for tetrads plus Fisher-Z tests for pairwise dependence.

---

## High-Level Algorithm

BPC proceeds in several stages:

### 1. Build a dependence pattern

- Compute a **pairwise dependence mask** `canLink[i][j]` using Fisher-Z tests on correlations with a relatively **loose alpha**:
    - `canLink[i][j] = true` if variables i and j are significantly dependent.
- This acts as a **screen**: tetrad checks only consider variables that are pairwise dependent.

Result: a graph-like pattern of variables that can plausibly belong to the same latent cluster.

---

### 2. Enumerate tetrad seeds and grow local groups

- For every 4-tuple of variables that passes the dependence screen:
    - Test whether all 3 tetrads in that quartet correspond to **rank 1** (latent-factor compatible).
    - If so, that 4-tuple is a **pure seed**.
- For each pure seed, BPC **grows a locally maximal pure group**:
    - Repeatedly try adding any other variable x:
        - If the enlarged set still passes **all tetrad tests**, keep x.
    - Stop when no more variables can be added without breaking purity.

Important: at this stage **variables are not marked as “used”**. Different seeds can grow into overlapping candidate groups.

---

### 3. Global merging of compatible groups

From all locally grown candidate groups:

1. **Merge rule:**  
   Repeatedly consider pairs of groups A and B:
    - Let U = A ∪ B.
    - If U is still tetrad-pure, and its **average absolute correlation** does not drop too much compared to A and B (by more than a small threshold), then merge:
        - Replace A and B by U.
2. This merging step is applied iteratively until **no more compatible merges** are found.

This stage encourages **larger, more coherent clusters** when a single latent can plausibly explain them.

---

### 4. Resolve overlaps (variable assignment)

After merging, some variables may still appear in **multiple groups**. BPC resolves these overlaps globally:

- For each variable that belongs to more than one group:
    - Compute its **average absolute correlation** with the other variables in each group.
    - Optionally also look at how many tetrads involving that variable pass within the group.
    - Assign the variable to the **best-fitting group**:
        - Highest compatibility score (average absolute correlation plus tie-breaking by tetrads).
    - Remove it from all other groups.

At the end of this step, the groups become **disjoint**: each variable is assigned to at most one cluster.

---

### 5. Filter and finalize clusters

Finally, BPC enforces two conditions:

1. **Cluster size:**
    - Drop any cluster with **fewer than 3 indicators** (as in the JMLR paper: latents with fewer than 3 children are discarded).
2. **Purity check:**
    - Make sure each remaining group:
        - Has at least 3 variables, and
        - Either is too small to form tetrads (size 3), or
        - Still passes the tetrad purity checks if size ≥ 4.

The output is a list of **disjoint pure clusters**, each intended to represent one latent variable.

---

## Output and Interpretation

- The algorithm returns a list of clusters: each cluster is a set of observed variables believed to share a **single latent parent**.
- Clusters are **disjoint**: no observed variable belongs to more than one latent factor in the BPC solution.
- These clusters can be used to:
    - Build a **measurement model** (one latent per cluster), then
    - Run a structural discovery algorithm (e.g., PC, GFCI, BOSS-FCI) on the latents.

---

## Parameters in Tetrad

| Parameter | Description |
|-----------|-------------|
| `alpha` | Significance level for tetrad-based rank tests (purity checks). Smaller values demand stronger evidence for a latent structure. |
| `ess` | Effective sample size used in statistical tests; `-1` means use the actual sample size. |
| `verbose` | If true, logs details: seeds found, merges, overlap resolutions, and tetrad statistics. |

Some internal “knobs” are fixed to practical defaults in the current implementation (not exposed as GUI parameters), such as:

- `alphaPairs`: looser alpha for pairwise dependence screening,
- `deltaMerge`: small allowable drop in average absolute correlation when merging two groups.

---

## Strengths

- Follows the **Silva et al. (2006)** spirit:
    - Find **pure measurement clusters** using tetrads.
    - Apply **global purification** instead of greedy, once-through clustering.
- Allows flexible resolution of overlaps and merges, which can help in noisy or borderline cases.
- Works entirely from the covariance structure, without fitting full SEMs.

---

## Limitations

- Requires reasonably large sample sizes for reliable tetrad tests.
- Assumes approximately **Gaussian, linear, and pure** measurement relations.
- Will discard latent candidates with fewer than 3 indicators, even if they exist in the data.
- Not designed to model **cross-loadings**; those variables will be forced into a single cluster or may cause that cluster to be rejected.

---

## Summary

BPC builds latent clusters by:

1. Screening for pairwise dependence,
2. Finding tetrad-pure seeds,
3. Growing them to locally maximal groups,
4. Globally merging compatible groups,
5. Resolving overlaps by assigning each variable to its best-fitting group, and
6. Dropping any small or impure groups.

The result is a set of **pure, disjoint indicator clusters** that can be interpreted as latent factors and used as input to further causal structure learning.