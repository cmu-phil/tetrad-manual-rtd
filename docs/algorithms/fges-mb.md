# FgesMb — FGES Markov Blanket Search

**Type:** Score-based, local / Markov blanket  
**Output:** CPDAG (around a target)

FgesMb is a **local variant of FGES** that focuses on the **Markov blanket of a single target variable** rather than the full graph.  
Given a target T, it runs a greedy equivalence search but **concentrates scoring and edge updates on the neighborhood of T**, returning a **local CPDAG** that encodes all candidate Markov blankets of T consistent with the score.

It is the **score-based counterpart** of PcMb: instead of conditional independence tests and a significance level, FgesMb uses **BIC-type scores** to select and orient edges.

---

## Key idea

Use **FGES-style greedy search**, but restrict attention to **edges that matter for the target T**:

- In a DAG, the **Markov blanket** of T consists of:
  - the parents of T,
  - the children of T,
  - and the parents of those children.
- Instead of learning a full CPDAG over all variables, FgesMb:
  - runs a **score-based forward–backward search**,
  - but **prioritizes changes that affect the local structure around T**,
  - and returns a CPDAG whose neighborhood around T encodes all Markov blankets compatible with the score.

Internally, the search uses the same ideas as FGES:

1. **Forward phase:** greedily add edges that give the largest score improvement, subject to acyclicity and background knowledge.
2. **Backward phase:** greedily remove edges that most improve the score.
3. **Equivalence-class representation:** maintain and update a CPDAG rather than a single DAG.

FgesMb adopts these mechanisms but is tuned for **local Markov blanket recovery** instead of global structure.

---

## When to use FgesMb

Use FgesMb when:

- You care primarily about **one target variable T** (for example, an outcome or label).
- You prefer a **score-based approach** (BIC, mixed BIC, etc.) rather than CI tests.
- The number of variables is large and learning a full CPDAG would be expensive or unnecessary.
- You want a **principled, score-based Markov blanket** for downstream tasks like regression or classification.

Typical applications:

- **Feature selection for supervised learning**, where the goal is to identify a **causally motivated feature set** around a target.
- **High-dimensional problems** where global structure learning (full FGES, BOSS, GRaSP) is too expensive.
- Comparative studies: **PcMb vs FgesMb**, CI-based vs score-based Markov blankets.

If you need global structure, you would normally use **FGES, BOSS, or GRaSP** instead.

---

## Prior knowledge support

**Does it accept background knowledge?**  
Yes. FgesMb respects the same knowledge constraints as FGES:

- **Required edges**
  - Force certain arrows to be present (for example, “X must cause T”).
- **Forbidden edges**
  - Disallow particular adjacencies or orientations.
- **Tiers / temporal constraints**
  - Enforce a partial order over variables, so that edges must go from earlier to later tiers.

All search operations (adds/removals) are restricted to be consistent with this knowledge.

---

## Strengths

- **Local and target-focused**
  - Efficient when you only care about **one target T**, not the entire graph.

- **Score-based semantics**
  - Uses BIC-type scores instead of CI tests, which can be appealing when:
    - sample sizes are large,
    - model assumptions (for example, linear Gaussian, discrete multinomial) are reasonable.

- **Causal Markov blanket interpretation**
  - The local CPDAG around T encodes **all DAGs (and hence all Markov blankets)** consistent with the score and knowledge.

- **Comparable to FGES**
  - Inherits FGES optimizations (caching, heuristic speedups, parallelism), making it usable in moderately high dimensions.

---

## Limitations

- **Model assumptions**
  - The score typically assumes:
    - linear Gaussian SEMs for continuous data,
    - multinomial models for discrete data,
    - or a specified mixed-data model.
  - Misspecification (for example, strong nonlinearities) can degrade performance.

- **Local only**
  - FgesMb is designed for **one target at a time**.
  - If you need Markov blankets for many variables, you must run it multiple times or learn a global CPDAG.

- **Heuristic nature**
  - Greedy search may get stuck in local optima.
  - Heuristic speedups (for example, correlation pre-screening) can trade off exactness for speed.

- **Finite-sample sensitivity**
  - As with any score-based method, sampling noise can:
    - add spurious neighbors,
    - or miss true neighbors of T.

---

## Key parameters in Tetrad

Exact names can vary slightly between GUI and code, but conceptually FgesMb exposes the same controls as FGES plus a **target variable**.

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `targetName`            | The distinguished target variable whose Markov blanket is to be learned. |
| `scoreType`             | Choice of score (for example, SemBicScore, DiscreteBicScore, MixedBicScore). |
| `penaltyDiscount`       | Multiplier on the complexity penalty (larger values favor sparser blankets). |
| `maxDegree`             | Optional cap on the maximum number of neighbors any node (including T) may have. |
| `useHeuristicSpeedup`   | Enable correlation-based edge pre-screening. |
| `numThreads`            | Number of threads for parallel scoring. |
| `verbose`               | Print progress and score changes. |

---

## Reference

FgesMb is a **local Markov blanket variant** of the FGES algorithm:

- Ramsey, J., Glymour, M., Sanchez-Romero, R., & Glymour, C. (2017).  
  *A million variables and more: the fast greedy equivalence search algorithm for learning high-dimensional graphical causal models, with an application to functional magnetic resonance images.*  
  International Journal of Data Science and Analytics, 3, 121–129.

This paper introduces and studies FGES; FgesMb applies the same score-based ideas to **Markov blanket discovery for a single target**.

---

## Summary

FgesMb is a **score-based Markov blanket learner** built on FGES: it focuses on a single target T, runs a greedy equivalence search tuned to the local neighborhood of T, and returns a CPDAG encoding **all score-consistent Markov blankets** of T under your chosen BIC-type score and knowledge constraints.
