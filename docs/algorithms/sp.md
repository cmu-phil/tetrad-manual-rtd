# SP — Sparsest Permutation

**Type:** Score-based CPDAG search (exact/ideal, order-based)  
**Output:** CPDAG  
**Category:** 📏 Score-based

SP (Sparsest Permutation) is a conceptually simple but combinatorial algorithm: it evaluates **all permutations** of the variables and returns the DAG with the **sparsest structure** consistent with the data. It is only feasible for **very small graphs** but serves as an important theoretical and practical reference.  [oai_citation:6‡arXiv](https://arxiv.org/abs/1307.0366?utm_source=chatgpt.com)

---

## Key idea

The SP principle:

1. For each permutation (ordering) of the variables:
    - Construct the **best DAG consistent with that ordering**, typically by allowing each variable to take parents only from variables earlier in the order.
    - Use a sparsity-aware score (e.g., penalized likelihood, sparsity in the Cholesky factor).

2. Among all permutations, select the DAG that:
    - Minimizes the number of edges (or a sparsity-penalized score).
    - In the Gaussian case, this corresponds to the **sparsest Cholesky factorization** of the precision matrix.

Under appropriate conditions, SP is **statistically consistent** under assumptions strictly weaker than full faithfulness.  [oai_citation:7‡arXiv](https://arxiv.org/abs/1307.0366?utm_source=chatgpt.com)

---

## When to use

In Tetrad, SP is primarily a **small-scale, high-accuracy** algorithm:

- Suitable for:
    - Very small problems (roughly up to ~10 variables), where enumerating permutations is still feasible.
    - Benchmarking or validating other methods (e.g., [BOSS](boss.md), [GRaSP](grasp.md), [FGES](fges.md)) on toy problems.
    - Didactic purposes (illustrating the sparsest-permutation principle).

- Not suitable for:
    - Medium or large graphs (permutation space grows as `p!`).
    - Routine large-scale structure learning.

For anything beyond very small `p`, consider [GRaSP](grasp.md) or [BOSS](boss.md), both of which are SP-inspired but scalable.

---

## How it works (at a glance)

1. **Enumerate permutations**  
   Loop over all permutations of the variable set.

2. **For each permutation**
    - Construct a DAG by allowing each node to take parents among earlier variables in the order.
    - Select the parent set that optimizes a local score (subject to sparsity), e.g., penalized likelihood.

3. **Measure sparsity**
    - Count number of edges, or use an equivalent sparsity-penalized score.
    - In the Gaussian case, this is closely tied to the sparsity of the Cholesky factor of the inverse covariance.  [oai_citation:8‡arXiv](https://arxiv.org/abs/1307.0366?utm_source=chatgpt.com)

4. **Select the winner**
    - Choose the permutation/DAG with the sparsest structure (or best global score).
    - Convert the resulting DAG to its CPDAG equivalence class for reporting.

The algorithm is simple but factorial in `p`, which is why it is mostly used for small problems and theory.

---

## Strengths

- **Conceptually clean and principled**  
  Directly encodes the idea that the true DAG should be *sparser* than alternatives consistent with the data.

- **Strong theoretical guarantees**  
  SP is consistent under conditions weaker than classical faithfulness (e.g., sparsest Markov representation assumptions).  [oai_citation:9‡arXiv](https://arxiv.org/abs/1307.0366?utm_source=chatgpt.com)

- **Useful as a gold standard**  
  For small graphs, SP can serve as a “ground truth” structure-learning method to benchmark other algorithms.

---

## Limitations

- **Factorial complexity in `p`**  
  Evaluating all permutations makes SP quickly infeasible beyond roughly ~10 variables.

- **No explicit latent-variable modeling**  
  SP is defined for DAGs over observed variables; latent confounding must be addressed via other methods or hybrids (e.g., [SP-FCI](sp-fci.md) in Tetrad).

- **Score and model assumptions**  
  As with other score-based methods, performance depends on score choice (Gaussian vs discrete, etc.) and model adequacy.

---

## How it relates to other Tetrad algorithms

- **Parent of GRaSP**
    - [GRaSP](grasp.md) can be viewed as a **greedy relaxation** of SP: it explores a neighborhood of permutations rather than the full factorial space.  [oai_citation:10‡arXiv](https://arxiv.org/abs/2010.14265?utm_source=chatgpt.com)

- **Motivational ancestor for BOSS**
    - [BOSS](boss.md) adopts a permutation-based viewpoint (like SP) but uses Grow–Shrink Trees and heuristic pruning to scale to much larger graphs.

- **Hybrid latent-variable extensions**
    - [SP-FCI](sp-fci.md) combines SP with FCI-style corrections to produce PAGs; it is practical only for very small models but provides a useful comparison point to [BOSS-FCI](boss-fci.md) and [GRaSP-FCI](grasp-fci.md).

---

## Prior knowledge support

Within Tetrad, SP is **knowledge-aware**:

- **Tier / ordering constraints** restrict the set of permutations to those consistent with user-specified partial orders.
- **Required / forbidden edges** constrain admissible parent sets under each permutation.

These constraints significantly reduce the effective search space in small problems.

---

## Key parameters in Tetrad

Typical SP-related controls:

- **Score / penalty**
    - Score family (Gaussian, discrete, etc.).
    - Penalization strength controlling sparsity.

- **Search limits**
    - Maximum number of permutations (if a cutoff or heuristic enumeration is used).
    - Optional pruning settings where available.

- **Threads / performance**
    - Parallelization across permutations (for very small `p`) but many datasets or restarts).

As always, see the **Parameter Definitions** page for exact names and defaults.

---

## Reference

- Raskutti, G., & Uhler, C. (2018).  
  *Learning directed acyclic graph models based on sparsest permutations.*  
  **Stat**, 7(1), e183.  [oai_citation:11‡arXiv](https://arxiv.org/abs/1307.0366?utm_source=chatgpt.com)

---

## Summary

SP is the **ideal sparsest-permutation search**: simple, consistent, and conceptually appealing, but factorial in dimension. In Tetrad it is mainly a **small-graph, high-accuracy benchmark**—a theoretical reference point that motivates scalable relaxations such as GRaSP and BOSS, and their latent-variable hybrids.