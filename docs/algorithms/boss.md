# BOSS — Best Order Score Search

**Type:** Score-based CPDAG search (order-based)  
**Output:** CPDAG (equivalence class of DAGs)  
**Category:** 📏 Score-based

BOSS is a fast, scalable order-based score search that finds high-scoring DAGs by exploring the space of **variable orderings** with aggressive pruning via **Grow–Shrink Trees (GSTs)**.

---

## Key idea

Instead of searching directly over DAG structures, BOSS searches over **variable permutations**:

- For a given ordering, the best DAG consistent with that order can be found by local score optimization over parent sets.
- BOSS uses **Grow–Shrink Trees** to reuse computations across similar orders and aggressively prune the search space.
- The result is a high-scoring DAG (and CPDAG) at a fraction of the cost of exhaustive order search.

Compared to classical score-based methods like [FGES](fges.md), BOSS trades equivalence-class moves for a **permutation-based** view with sophisticated caching and pruning.

---

## When to use

BOSS is a good default when:

- You want **high structural accuracy** in moderate to large models.
- You want a **score-based DAG/CPDAG search** with strong empirical performance.
- You are comfortable assuming that a **good score** (e.g., BIC/BDeu/BF-BIC/BF-LRT) will identify high-quality structures.
- You want a method that **scales well even for moderately or very dense graphs** (e.g., average degree up to 20, as demonstrated in the paper).
- You may later feed the DAG into downstream algorithms such as:
    - [BOSS-FCI](boss-fci.md) for latent-variable PAGs.
    - [LV-Dumb](lv-dumb.md) for a fast preliminary PAG.

Less suitable when:

- The graph is **extremely** dense **and** the sample size is **very small** (scores become unstable, and many DAGs tie).
- You explicitly need a **latent-variable–capable PAG** search; in that case consider  
  [FCI](../search-algorithms-full-list.md#-constraint-based-algorithms-cpdag--pag),  
  [GFCI](gfci.md), or  
  [FCIT](fcit.md).
- 
---

## How it works (at a glance)

Very roughly:

1. **Initialize an ordering**  
   Start from one or several candidate permutations of the variables (e.g., random or heuristic).

2. **Best DAG for a given order**  
   For each variable in the order, select a parent set from earlier variables that maximizes a decomposable score (e.g., BIC), subject to sparsity constraints.

3. **Grow–Shrink Trees (GSTs)**
    - Organize candidate parent sets in a tree where nearby orders share nodes.
    - Prune branches that cannot improve the score (monotonicity + local bounds).
    - Reuse computations across similar orders to avoid re-scoring all parent sets.

4. **Order search with pruning**  
   Iteratively propose local changes in the order (e.g., swaps) and accept moves that improve the global score. GSTs make this feasible for larger \( p \).

5. **Convert to CPDAG**  
   The final DAG is mapped to its equivalence class (CPDAG), which is the algorithm’s reported structure.

The BOSS paper shows that GSTs give **near-SP-level accuracy** with far better scalability.

---

## Strengths

- **High accuracy**  
  Often more accurate than purely greedy equivalence-class searches when tuned appropriately.

- **Scalable order search**  
  GST-based pruning and caching make order-based search practical for substantially larger graphs than naive SP-style permutation search.

- **Good foundation for latent-variable extensions**  
  Serves as the backbone for [BOSS-FCI](boss-fci.md) and as the DAG input to [LV-Dumb](lv-dumb.md).

- **Parallelizable**  
  Scoring of different candidate parents/orders can be parallelized across threads.

---

## Limitations

- **No explicit latent variables**  
  BOSS outputs a CPDAG over the observed variables; latent confounding must be handled by downstream methods (e.g., BOSS-FCI, FCIT, etc.).

- **Score and penalty sensitive**  
  As with other score-based methods, performance depends on:
    - Choice of score (Gaussian / discrete / mixed).
    - Penalty strength (e.g., BIC multiplier).

- **Assumes DAG structure**  
  Feedback/cycles are not allowed; use methods like [CCD](../search-algorithms-full-list.md#-nonlinear--distribution-shift-algorithms) for cyclic models.

---

## How it relates to other Tetrad algorithms

- **Versus FGES**
    - FGES performs **equivalence-class** moves on CPDAGs.
    - BOSS searches in **ordering space**, with GSTs providing strong pruning.
    - Empirically, BOSS can be more accurate in many regimes, at similar or slightly higher computational cost.

- **Versus SP / GRaSP**
    - [SP](sp.md) is the “ideal” sparsest-permutation method but is combinatorial in \( p! \) and only feasible for very small \( p \).  [oai_citation:0‡arXiv](https://arxiv.org/abs/1307.0366?utm_source=chatgpt.com)
    - [GRaSP](grasp.md) relaxes SP into a greedy local search; BOSS uses a related order-based perspective but with **GSTs** and design choices that improve scalability.

- **As a building block for latent-variable PAGs**
    - [BOSS-FCI](boss-fci.md) and [FCIT](fcit.md) use BOSS as their score-based component.

---

## Prior knowledge support

BOSS is **fully knowledge-aware** in Tetrad:

- **Forbidden edges** (never include).
- **Required edges** (always include if consistent with a DAG).
- **Tiers / partial orders** (restrict permissible permutations).
- Grouping / intervention metadata where supported by the score.

These constraints are enforced at the **ordering and parent-selection** levels, pruning incompatible permutations and parent sets.

---

## Key parameters in Tetrad

Exact names may vary by version, but typical BOSS-related parameters include:

- **Score family & options**
    - Choice of score (Gaussian BIC, discrete BIC, mixed scores, etc.).
    - Penalty discount / sparsity weight.

- **Search controls**
    - Maximum parents or maximum degree (sparsity constraint).
    - Number of permutations / restarts to explore.
    - Maximum Grow–Shrink Tree depth or branching controls (where exposed).
    - Number of threads.

- **Output options**
    - Return CPDAG only (default).
    - Verbosity and logging.

For precise parameter names and defaults, see the main **Parameter Definitions** page.

---

## Reference

- **Primary paper**  
  Andrews, B., Ramsey, J., Sanchez-Romero, R., Camchong, J., & Kummerfeld, E. (2023).  
  *Fast scalable and accurate discovery of DAGs using the best order score search and grow shrink trees.*  
  NeurIPS 36, 63945–63956.

---

## Summary

BOSS is Tetrad’s **workhorse order-based score search**: it leverages Grow–Shrink Trees to explore permutations efficiently, yielding accurate DAGs/CPDAGs at meaningful scales and serving as a core building block for modern latent-variable methods like BOSS-FCI and FCIT.