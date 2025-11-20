# FGES — Fast Greedy Equivalence Search

**Type:** Score-based (GES implementation)  
**Output:** CPDAG  
**Reference:** Ramsey, Glymour, Sanchez-Romero & Glymour (2017)  
*A Million Variables and More…*, IJDSA.

FGES is a highly optimized implementation of the classical **GES** algorithm. It performs score-based search over Markov equivalence classes of DAGs, using BIC (or related scores) to add and remove edges in a greedy fashion.

FGES is widely used because:
- It scales gracefully to **high-dimensional** problems.
- It is easy to parallelize.
- It provides **interpretable** score-based decisions.
- It is consistent under mild, well-understood conditions.

---

## Key Idea

FGES performs two greedy phases:

1. **Forward Phase**  
   Add edges that provide the greatest improvement in score (typically SEM-BIC).  
   Uses cached local scores and memoized arrow considerations to avoid recomputation.

2. **Backward Phase**  
   Remove edges whose deletion improves the score.

The output is a **CPDAG** representing the Markov equivalence class of all DAGs with highest score.

FGES **is GES** — the same greedy equivalence‐search algorithm, but engineered with optimizations (memoization, cached covariance operations, and parallel scoring) that make it feasible in very high dimensions, from thousands up to millions of variables on large machines.

---

## A Nuanced View of Scalability and Sparsity

FGES can scale to extremely large models — even **hundreds of thousands to over a million variables** — but this depends crucially on the **effective sparsity** of the underlying graph.

### 1. High-dimensional ≠ dense
In causal discovery, *density* is avg degree / (#vars - 1). For large graphs, even average degree in the teens yields extremely low density.Thus, “dense” high-dimensional settings are typically **structurally sparse**.

### 2. Million-variable demonstration
The 2017 paper’s million-variable run:
- Used **linear Gaussian** SEM-BIC.
- Had **average degree ≈ 2**, though with some dense subregions.
- Employed FGES-specific optimizations:
    - aggressive memoization
    - cached covariance blocks
    - pruning of non-improving parent sets
    - parallelization

These engineering choices were essential for 1M-variable performance.

### 3. Higher average degree: slower, but often *more accurate*
As true average degree rises:
- Candidate parent sets grow → **runtime increases**.
- But accuracy often **improves**, especially in *high-dimensional* regimes.

FGES has what practitioners sometimes call the **“blossoming effect”**:
> In thousands of variables, accuracy can *increase* dramatically, even as the model becomes more complex, provided true density remains low relative to the dimension.

Theoretical results (Nandy, Hauser & Maathuis, 2018) support this high-dimensional consistency.

### 4. Summary

FGES is not a universal silver bullet for all densities. But in genuinely high-dimensional problems with structural sparsity, FGES becomes one of the most accurate and scalable causal discovery algorithms available.

---

## When to Use FGES

- High-dimensional datasets (hundreds to tens of thousands of variables)
- Linear, Gaussian, or mixed data
- Situations where score-based global optimization is appropriate
- When you need scalability, parallelizability, and interpretability

FGES is often the baseline for:
- neuroimaging,
- genetics/genomics,
- climate systems,
- large observational datasets.

---

## Prior Knowledge Support

FGES supports the full Tetrad `Knowledge` interface. You can specify:

- forbidden edges
- required edges
- tier/temporal ordering
- custom constraints

All constraints are enforced consistently during the forward and backward phases.

---

## Strengths

- **Massively scalable** (largest known causal discovery runs for random Erdos-Renyi graphs)
- Interpretable: every step is justified by a score improvement
- Strong high-dimensional accuracy
- Parallelizable
- Produces clear CPDAGs
- Implementation in Tetrad includes several engineering improvements over reference GES

---

## Limitations

- Less accurate on **very small** or **very dense** models
- Requires a well-behaved score (BIC, SEM-BIC, GLM-BIC, etc.)
- Assumes causal sufficiency unless hybridized (see GFCI, BOSS-FCI, FCIT)

---

## Key Parameters in Tetrad

FGES exposes the following parameters (camelCase names shown):

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `symmetricFirstStep` | Whether the initial forward-search step evaluates score improvements symmetrically across candidate edges. |
| `maxDegree` | Maximum allowed degree per node (helps regularize or constrain search in large graphs). |
| `numThreads` | Number of worker threads used for parallel scoring computations. |
| `faithfulnessAssumed` | If true, assumes the underlying distribution is faithful to some DAG, allowing certain search optimizations. |
| `timeLag` | Lag τ when FGES is applied to time-series or lagged datasets. |
| `timeLagReplicatingGraph` | Whether the structure is replicated across time slices when using lagged data. |
| `verbose` | Print detailed scoring and decision information during search. |

---

## Reference

Ramsey, J., Glymour, M., Sanchez-Romero, R., & Glymour, C. (2017).  
**A million variables and more: the fast greedy equivalence search algorithm for learning high-dimensional graphical causal models**,  
*International Journal of Data Science and Analytics*, 3(2), 121–129.

See also:  
Nandy, P., Hauser, A., & Maathuis, M. H. (2018).  
**High-dimensional consistency in score-based and hybrid structure learning.**  
*Annals of Statistics*, 46(6A), 3151–3183.

---

## Summary

FGES is a highly optimized, scalable implementation of GES.  
In the high-dimensional sparse regime, it can achieve exceptional accuracy and performance, making it one of the most powerful score-based structure-learning methods available.