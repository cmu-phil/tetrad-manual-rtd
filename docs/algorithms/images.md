# IMaGES — Independent Multiple-sample Greedy Equivalence Search

**Type:** Score-based (multi-dataset)  
**Output:** CPDAG

IMaGES extends GES/FGES to the case where you have **multiple datasets** measured on the *same set of variables*, assuming that **all datasets share the same causal structure** even if their noise distributions differ.

Typical use cases:
- fMRI data from multiple subjects performing the same task
- Multi-site or multi-scanner datasets
- Repeated measurements or multiple sessions
- Any situation with several independent datasets measuring the same variables

IMaGES modifies the scoring step of GES/FGES:

## Key Idea
For each candidate edge addition or removal, compute **one BIC score per dataset**, then **average the scores**:

    Score_IMaGES = (1/M) * Σ_{m=1}^M BIC_m

This produces:
- More stable structure estimates
- Fewer false positives due to dataset-specific noise
- The ability to use multiple small datasets without concatenating them

The greedy search (forward + backward phases) proceeds just like FGES, but uses this averaged score.

---

## Variants

### IMaGES
Uses **FGES** as the greedy engine with the IMaGES averaged score.  
Output: CPDAG.

### IMaGES-BOSS
Uses **BOSS** as the search engine but applies the IMaGES score at each step.  
Often more scalable and robust than FGES-based IMaGES, especially for mixed data or larger models.

---

## When to Use

- You have **multiple independent datasets** with identical variable sets
- You believe the underlying **causal structure is shared**
- You want a more **stable CPDAG estimate** than running searches separately
- Particularly effective for:
    - fMRI studies
    - clinical multi-site data
    - repeated measurements
    - large cohorts with multiple sessions

---

## Strengths

- Highly stable compared to single-dataset GES/FGES
- Avoids incorrect concatenation of datasets
- Reduces sampling noise
- Parallelizable (each dataset’s score can be computed independently)
- Still outputs a clean, interpretable **CPDAG**

---

## Limitations

- Requires the assumption of a **shared causal structure** across datasets
- Not appropriate if datasets differ meaningfully in mechanisms
- Cannot by itself handle latent confounding (use GFCI/BOSS-FCI/FCIT for that)

---

## Key Parameters in Tetrad

IMaGES exposes several parameters that control both the FGES/BOSS search step and the multi-dataset scoring behavior. All parameters appear in the Tetrad GUI and scripting interfaces using the **camelCase** versions shown here.

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `penaltyDiscount` | Multiplies the BIC penalty term. Larger values → sparser graphs. |
| `semBicStructurePrior` | Prior over graph structures used in SEM-BIC scoring. |
| `semBicRule` | Choice of local scoring rule (e.g., “SEM-BIC Score Rule”). |
| `precomputeCovariances` | Whether to cache covariances for efficiency across datasets. |
| `singularityLambda` | Regularization constant applied when covariance matrices are near-singular. |
| `effectiveSampleSize` | Overrides sample size used in scoring (used with weighting or meta-designs). |
| `symmetricFirstStep` | Whether the initial forward step uses a symmetric score evaluation. |
| `maxDegree` | Maximum allowed degree per node (structural regularization). |
| `numThreads` | Number of threads for parallel FGES/BOSS operations. |
| `faithfulnessAssumed` | If true, assumes perfect faithfulness during adjacency search. |
| `timeLag` | Lag (τ) when IMaGES is applied to time-series or lagged datasets. |
| `timeLagReplicatingGraph` | Whether lagged graphs should be structurally replicated across time slices. |
| `randomSelectionSize` | Size of random subsets considered during order or edge evaluation. |
| `imagesMetaAlg` | Which score-driven meta-algorithm to use for multi-dataset merging. |
| `verbose` | Print detailed scoring/decision information during search. |

These parameters allow IMaGES to:

- share information across multiple datasets,
- encourage stability and reduce noise in scoring,
- scale to large multi-subject studies (e.g., neuroimaging),
- and enforce structural constraints across datasets or time-slices.

---

## Reference

Ramsey, J. D., Hanson, S. J., & Glymour, C. (2011).  
**Multi-subject search correctly identifies causal connections and most causal directions in the DCM models of the Smith et al. simulation study.**  
*NeuroImage*, 58(3), 838–848.

## Summary

**IMaGES = GES/FGES/BOSS + averaged BIC scores across datasets.**  
A robust and stable multi-sample CPDAG algorithm for repeated-measure or multi-subject data.