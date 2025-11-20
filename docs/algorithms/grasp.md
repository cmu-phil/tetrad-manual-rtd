# GRaSP — Greedy Relaxations of the Sparsest Permutation

**Type:** Score-based CPDAG search (order-based, SP-inspired)  
**Output:** CPDAG  
**Category:** 📏 Score-based

GRaSP is a **local-search relaxation** of the Sparsest Permutation (SP) algorithm: it searches over variable orderings to find a **sparse, high-scoring DAG**, but replaces SP’s exhaustive permutation search with a **greedy neighborhood search**. In Tetrad, GRaSP is further optimized using the **Grow–Shrink Tree** machinery introduced for [BOSS](boss.md).  [oai_citation:1‡arXiv](https://arxiv.org/abs/2010.14265?utm_source=chatgpt.com)

---

## Key idea

SP defines an ideal target: the ordering that yields the **sparsest** DAG (or equivalently, the sparsest Cholesky factorization of the precision matrix in the Gaussian case).  [oai_citation:2‡arXiv](https://arxiv.org/abs/1307.0366?utm_source=chatgpt.com)  
But enumerating all permutations is factorial in \( p \).

GRaSP relaxes this:

- Start from one or more **good initial permutations** (e.g., random, heuristic, or from other methods).
- Perform a **greedy local search** in permutation space via operations such as:
    - Adjacent swaps.
    - Small block moves / relaxations.
- Evaluate each candidate order by its induced DAG score (sparsity-aware).
- Use **GST-based optimizations** (in Tetrad’s implementation) to reuse parent-set computations, as in [BOSS](boss.md).

The result approximates the SP objective while retaining practical runtime for moderate \( p \).

---

## When to use

GRaSP is a good choice when:

- You like the **SP philosophy** (“the sparsest DAG consistent with the data”) but:
    - The number of variables is too large for exact SP.
    - You still want something closer to SP than a purely greedy equivalence-class method.
- You are working in **small-to-moderate dimension** (e.g., tens of variables), where a richer permutation neighborhood can be explored.
- You want a **DAG/CPDAG** that you may later feed into:
    - [GRaSP-FCI](grasp-fci.md) for latent-variable PAGs.
    - [LV-Dumb](lv-dumb.md) for a fast heuristic PAG.

Less ideal when:

- \( p \) is very large and you need maximal scalability (then [FGES](fges.md) or [BOSS](boss.md) may be more practical).
- You’re primarily interested in latent-variable structure—in that case use [GFCI](gfci.md), [BOSS-FCI](boss-fci.md), [GRaSP-FCI](grasp-fci.md), or [FCIT](fcit.md).

---

## How it works (at a glance)

Roughly:

1. **Initialization**
    - Choose one or more starting permutations.
    - For each permutation, construct the best DAG consistent with that order using a decomposable score.

2. **Permutation neighborhood**
    - Define a set of local moves (e.g., adjacent swaps, limited reshuffles).
    - For each current order, generate candidate neighbors.

3. **Greedy relaxation**
    - For each neighbor, compute or update the DAG score.
    - Move to the neighbor if it improves the global score, repeating until no beneficial move is found (local optimum).

4. **Grow–Shrink Tree optimization (Tetrad implementation)**
    - Reuse parent-set computations across related orders using the GST structure from [BOSS](boss.md).
    - This substantially reduces the cost of evaluating each permutation, especially when exploring rich neighborhoods.

5. **CPDAG output**
    - Convert the final DAG to its CPDAG equivalence class.

---

## Strengths

- **Closer to SP than simple greedy methods**  
  GRaSP retains the *spirit* of SP’s sparsity objective while avoiding factorial search.  [oai_citation:3‡arXiv](https://arxiv.org/abs/2010.14265?utm_source=chatgpt.com)

- **Flexible local search**  
  You can explore a rich neighborhood in permutation space (depending on implementation settings).

- **Beneficial GST optimization**  
  In Tetrad, the BOSS-style GST optimization makes GRaSP substantially more scalable than naive local permutation search.

- **Good starting point for latent-variable hybrids**  
  Feeds into [GRaSP-FCI](grasp-fci.md) and related algorithms.

---

## Limitations

- **Still more expensive than simple greedy CPDAG search**  
  Neighborhood exploration can be costly for large \( p \), even with GSTs.

- **Local optima**  
  Being a greedy method, GRaSP can get stuck in local minima in permutation space; results may depend on initialization and search schedule.

- **No explicit latent-variable modeling**  
  Like [BOSS](boss.md) and [FGES](fges.md), GRaSP itself assumes a DAG over observed variables.

---

## How it relates to other Tetrad algorithms

- **Versus SP**
    - [SP](sp.md) is conceptually the “gold standard” sparsest-permutation search, but factorial in \( p \).  [oai_citation:4‡arXiv](https://arxiv.org/abs/1307.0366?utm_source=chatgpt.com)
    - GRaSP is a **greedy relaxation**: it keeps the idea but replaces exhaustive enumeration with local moves.

- **Versus BOSS**
    - Both are **order-based** methods using decomposable scores and GSTs.
    - BOSS emphasizes fast exploration with strong GST-based pruning; GRaSP is more directly anchored to local permutation moves.

- **As a precursor to PAG methods**
    - [GRaSP-FCI](grasp-fci.md) uses GRaSP’s CPDAG as a starting point for FCI-style corrections.

---

## Prior knowledge support

GRaSP is **knowledge-aware**:

- **Tier / partial-order constraints** restrict the permutation space.
- **Required and forbidden edges** constrain admissible parent sets.
- Other structural restrictions are enforced during score evaluation and neighborhood exploration.

---

## Key parameters in Tetrad

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `graspDepth` | Maximum conditioning-set size for the GRaSP conditional-independence checks used during local greedy updates. `-1` means no limit. |
| `graspSingularDepth` | Depth used only for **singular** moves (insert/delete operations that change Meek-essential structures). |
| `graspNonsingularDepth` | Depth used for **nonsingular** moves (local score-improving steps not requiring full CI evaluation). |
| `graspOrderedAlg` | If `true`, use the *ordered* variant of GRaSP (deterministic variable ordering); if `false`, use the standard version. |
| `graspUseRaskuttiUhler` | If `true`, use the **Raskutti–Uhler** (RU) approximation for local score search; if `false`, use the standard GRaSP scoring. |
| `useDataOrder` | If `true`, initialize the search using the order of variables as they appear in the dataset; otherwise use the default heuristic initialization. |
| `allowInternalRandomness` | If `true`, allows randomized tie-breaking and randomized multi-start behavior inside the algorithm. |
| `outputCpdag` | If `true`, return the CPDAG of the final DAG; if `false`, return the DAG found by the greedy search. |
| `timeLag` | Time-series lag parameter. If greater than 0, apply the time-lag transform to the dataset before GRaSP search. |
| `timeLagReplicatingGraph` | If `true`, replicate the discovered structure across lags rather than shifting edges; interacts with `timeLag`. |
| `seed` | Random seed used when internal randomness is enabled. |
| `verbose` | If `true`, print detailed logs of greedy steps, local scores, and convergence. |
| `numStarts` | Number of **multi-start initializations** used by GRaSP. Each start runs an independent greedy search; the best-scoring structure is returned. |

---

## Reference

- **Primary paper**  
  Lam, W. Y., Andrews, B., & Ramsey, J. (2022).  
  *Greedy relaxations of the sparsest permutation algorithm.*  
  In *Uncertainty in Artificial Intelligence (UAI)*, pp. 1052–1062.  [oai_citation:5‡arXiv](https://arxiv.org/abs/2010.14265?utm_source=chatgpt.com)

- **Related**  
  Andrews et al. (2023) (BOSS & Grow–Shrink Trees) further optimize order-based search and inspire the GST-based implementation in Tetrad.

---

## Summary

GRaSP is Tetrad’s **SP-inspired order search**: it uses greedy relaxations in permutation space, enhanced with BOSS-style Grow–Shrink optimizations, to approximate the sparsest-permutation objective on graphs that are too large for exact SP.