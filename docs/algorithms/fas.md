# FAS — Fast Adjacency Search

**Type:** Constraint-based  
**Output:** Undirected graph (skeleton)  
📌 **Used as the adjacency phase of PC, PC-Max, CPC, FCI, RFCI, GFCI, FCIT, and others**

FAS is the **adjacency discovery** component of the PC algorithm as described in  
**Spirtes, Glymour & Scheines (2000), *Causation, Prediction, and Search*.**

It takes a dataset and a conditional independence (CI) test and returns a **skeleton** — an undirected graph representing all pairs of variables that *might* be causally connected. FAS is often used when the user wants **the adjacencies without orientations**, especially as a preprocessing step or when orientations are handled separately.

---

## Key Idea

1. Start with a **complete undirected graph** over all variables.
2. For increasing conditioning-set sizes (0, 1, 2, ...):
    - Test each adjacency `X — Y` for conditional independence given subsets of neighbors.
    - If `X ⫫ Y | S`, remove the edge and store the separating set `S`.

This is identical to the first phase of PC, but without orientation of any kind.

FAS is:
- **order-independent** if the *stable* option is used,
- consistent under faithfulness (in the oracle case),
- extremely fast on sparse graphs.

---

## When to Use

- You only want the **adjacency structure**, not a CPDAG or PAG.
- You want a **lightweight “graph shrinker”** to pass as input to:
    - LOFS or skew-based orientation rules
    - IGCI or additive-noise orientation
    - custom score-based orientation
    - domain-driven orientation constraints
- You want to **speed up expensive algorithms** that benefit from a pruned skeleton:
    - FGES (by restricting candidate parent sets)
    - BOSS or GRaSP (restricting adjacency search)
    - DCM model selection
    - high-dimensional fMRI pipelines
- You want a **quick test** of whether a dataset looks sparse or dense.  
  (FAS is very fast and provides immediate structural insight.)

---

## Case Study: High-dimensional fMRI Preprocessing

FAS is widely used in neuroimaging pipelines as a **preprocessing step** before orientation-heavy algorithms.

**Typical scenario:**
- 200–500 brain regions
- limited samples (e.g., 300–800 time points)
- heavy skewness or non-Gaussian structure
- need a **small skeleton** before applying
    - LOFS,
    - FASK,
    - non-Gaussian ICA-based orientation, or
    - domain constraints.

Using full PC or FCI can be slow and may over-test high-order conditioning sets.  
But **FAS alone** gives a clean adjacency pattern that is:
- sparse
- quick to compute
- reflectively conservative under stable-FAS
- easy to combine with other, domain-specific orientation rules.

Research groups (e.g., cognitive neuroscience labs) routinely run:

1. **FAS** to prune the graph
2. **FASK/LOFS or domain-based rules** to orient edges
3. **SEM model fitting** or causal effect estimation on the pruned DAG

FAS is ideal for this because it is the *fastest and least opinionated* structural reduction step available.

---

## Prior Knowledge Support

FAS **fully supports background knowledge**:

- forbidden edges (immediately removed)
- required edges (never removed)
- tier/temporal orders (limit conditioning sets)
- maximum depth constraints

---

## Strengths

- Very fast, even on high-dimensional data
- Provides the **exact skeleton** used by PC-style algorithms
- Order-independent when using stable-FAS
- Works with any CI test in Tetrad
- A natural preprocessing step for orientation-only or hybrid workflows

---

## Limitations

- Does **not orient** any edges
- Assumes the CI test matches the data distribution
- Faithfulness assumed for correctness guarantees
- Large conditioning sets may become unstable in finite samples

---

## Key Parameters in Tetrad

| Parameter (camelCase)     | Description |
|---------------------------|-------------|
| `stableFas`               | Use the order-independent version of FAS |
| `depth`                   | Max conditioning-set size (`-1` = unlimited) |
| `fdrQ`                    | Use FDR correction instead of fixed α |
| `timeLag`                 | Lag τ for time-series datasets |
| `timeLagReplicatingGraph` | Whether structure should replicate across lags |
| `verbose`                 | Print CI test decisions |

---

## Reference

Spirtes, P., Glymour, C. N., & Scheines, R. (2000).  
*“Causation, Prediction, and Search.”* MIT Press.

---

## Summary

**FAS is the adjacency engine behind PC-style algorithms.**  
It is the fastest way to obtain a consistent, faithfulness-respecting skeleton and is widely used as a preprocessing step for orientation-only methods or hybrid pipelines.