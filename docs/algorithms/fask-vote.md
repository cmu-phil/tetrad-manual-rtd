# FASK-Vote — Multi-Dataset FASK Voting over IMaGES

**Type:** Non-Gaussian / skewness-based orientation, multi-dataset ensemble wrapper  
**Output:** Directed graph (with possible undirected edges when votes tie)  
**Status:** Experimental / work-in-progress

FaskVote is a **meta-algorithm** that combines **IMaGES** (for multi-dataset adjacency discovery) with **FASK** (for skewness-based orientation) across multiple datasets.  
Given several datasets over overlapping variables, FaskVote:

1. Learns a **consensus adjacency graph** with IMaGES, and then
2. Runs **FASK separately on each dataset**, constrained to that adjacency graph, and
3. **Votes on edge orientation** across datasets to obtain a final directed graph.

Conceptually, it is an **alternative to bootstrapping** for orientation: instead of repeatedly resampling one dataset, it leverages **multiple subject-level datasets** directly.

---

## Key Idea

FaskVote assumes you have **multiple datasets** on (approximately) the same variables (for example, one dataset per subject or per group).

It proceeds in two phases:

### 1. Multi-dataset skeleton via IMaGES

- Standardize each dataset (z-scoring).
- Run **IMaGES** (using the `Images` wrapper) across the list of datasets with a chosen score (for example, SEM-BIC).
- IMaGES returns a **consensus graph G0** whose adjacencies reflect edges that are supported across datasets.

This step focuses on **where edges exist**, not on their direction.

### 2. Orientation voting via FASK

Given the IMaGES adjacency graph G0:

- For each dataset:
    - Run **FASK** on that dataset, but:
        - Supply **G0 as an external skeleton** (undirected version of G0).
        - Use skewness-based FASK orientation (LeftRight.FASK2 in the code).
    - Replace nodes so all FASK graphs share the same node objects.

- For each adjacency X–Y in G0:
    - Count how many FASK runs orient X → Y (sum1).
    - Count how many orient Y → X (sum2).
    - Let count be the number of runs that oriented the edge in either direction.
    - Compute mean1 = sum1 / count and mean2 = sum2 / count.

Then:

- If mean1 and mean2 are both 0.5, keep X–Y **undirected** (tie).
- If mean1 > 0.5, add X → Y.
- If mean2 > 0.5, add Y → X.

The result is a graph G whose **adjacencies come from IMaGES** and whose **orientations come from skewness-based majority votes across FASK runs**.

---

## When to Use

FaskVote is appropriate when:

- You have **multiple datasets** over similar or overlapping variable sets (for example, multi-subject fMRI, multi-site studies).
- Non-Gaussianity and especially **skewness** are plausible, so FASK’s orientation logic is informative.
- You want an orientation procedure that uses **between-dataset variation** rather than bootstrapping a single dataset.
- You already think **IMaGES is a reasonable choice** for multi-dataset adjacency discovery and want to add a skew-based orientation layer.

Typical scenarios:

- **Neuroimaging**, where each subject provides one dataset, and you want a group-level causal graph.
- **Multi-site clinical or observational studies**, with one dataset per site or cohort.
- Any situation where multiple datasets should **vote on direction**, not just on adjacency.

---

## Prior Knowledge Support

FaskVote uses and respects a **Knowledge** object:

- Knowledge is passed into **IMaGES** to constrain the adjacency search.
- The same knowledge is passed into **each FASK run** when orienting edges.

Supported constraints include:

- Required edges
- Forbidden edges
- Temporal or tiered constraints

These constraints are enforced consistently across IMaGES and all FASK runs.

---

## Strengths

- **Multi-dataset aware**: integrates information from several datasets, not just one.
- **Robust orientation via voting**: unstable directions in individual datasets are averaged out.
- **Separation of concerns**:
    - IMaGES handles **multi-dataset structure discovery** (adjacencies).
    - FASK handles **non-Gaussian orientation** on a fixed skeleton.
- Can be seen as a **multi-dataset alternative to bootstrap ensembles** for edge direction.

---

## Limitations

- Requires at least **two datasets**; otherwise voting is pointless.
- Inherits assumptions and limitations from both:
    - **IMaGES** (score-based, acyclic, multi-dataset assumptions), and
    - **FASK** (skewness, non-Gaussianity, linear or mildly nonlinear).
- If skewness is weak or sample sizes are small, orientations may be unreliable and often remain undirected due to ties.

---

## Key Parameters (via `Parameters`)

FaskVote itself does not introduce many new parameters; it passes parameters through to IMaGES and FASK. Relevant parameters include:

From IMaGES (via `Images`):

- `penaltyDiscount`
- `structurePrior` (or equivalent, depending on score)
- Any other score-related parameters used by the `ScoreWrapper`

From FASK:

- `skewEdgeThreshold` (SKEW_EDGE_THRESHOLD): minimum skew-based score needed for orientation.
- `depth` (DEPTH): maximum conditioning-set depth used during the FAS stage inside FASK.
- `faskDelta` (FASK_DELTA): threshold used in FASK’s skew-based conditional moment comparisons.
- `orientationAlpha` (ORIENTATION_ALPHA): significance level for certain orientation decisions (for example, additional tests supporting orientation).

Other controls:

- **Knowledge**: handed in via `setKnowledge(Knowledge knowledge)`.
- **ScoreWrapper** and **IndependenceWrapper**: provided at construction time and used respectively by IMaGES and FASK.

---

## Reference

FaskVote builds directly on:

- **IMaGES (multi-dataset FGES)**  
  Ramsey, J., Hanson, S. J., Hanson, C., Halchenko, Y., Poldrack, R., & Glymour, C. (2010).  
  *Six problems for causal inference from fMRI.* NeuroImage, 49(2), 1545–1558.  
  (IMaGES is introduced and discussed in this and related work.)

- **FASK (Fast Adjacency Skewness)**  
  Sanchez-Romero, R., Ramsey, J., Zhang, K., Glymour, C., Huang, B., & Spirtes, P. (2019).  
  *Causal discovery of feedback networks with functional interventions.*  
  Proceedings of the Conference on Causal Learning and Reasoning (CLeaR).  
  (FASK is described in detail in the supplementary materials.)

There is no separate paper devoted solely to FaskVote; it is an extension that combines these two ideas.

---

## Summary

FaskVote is an **multi-dataset voting wrapper**: it uses **IMaGES** to learn a consensus adjacency graph and then applies **FASK** to each dataset to determine edge direction, combining these via a simple **majority vote**. It is useful when you have many related datasets and want a non-Gaussian, skewness-based group-level orientation mechanism without resorting to bootstrapping a single dataset.