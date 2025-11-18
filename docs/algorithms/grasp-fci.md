# GRaSP-FCI — Greedy Relaxations of Sparsest Permutation + FCI Refinement

**Type:** Hybrid (score-based permutation search + CI tests)  
**Output:** PAG  
**Knowledge:** Fully supported (all Tetrad knowledge constraints)

GRaSP-FCI is one of the mixed-strategy latent-variable algorithms introduced in  
**Ramsey, Andrews & Spirtes (2025)**. It follows the same *X-FCI template* as BOSS-FCI and GFCI, but uses **GRaSP**—a permutation-based score search—for the initial CPDAG before performing an FCI-style latent-variable correction.

The result is a **PAG** that often shows better adjacency recall than FGES-based hybrids and more stable performance on certain permutation-favorable models.

---

## Key Idea

GRaSP-FCI has two stages:

1. **Score-based permutation search (GRaSP)**
    - GRaSP searches over **variable permutations** and evaluates their implied DAGs using a sparsity-oriented SEM-BIC score.
    - Rather than exploring graph space directly, it uses the fact that every permutation induces a unique DAG skeleton.
    - The best-scoring permutation yields a **CPDAG** to serve as the skeleton for refinement.

2. **Latent-variable correction (FCI refinement)**
    - Starting from the GRaSP CPDAG, apply the full set of **FCI refinement procedures**:
        - Possible-D-SEP checks
        - Sepset-based collider identification
        - Orientation propagation rules
        - PAG legality restoration
    - Produces the final **PAG**.

GRaSP-FCI thus combines **permutation scoring** (which behaves well for some data regimes) with **robust FCI latent reasoning**.

---

## When to Use

- You expect the model to benefit from **permutation-based scoring** rather than purely order-based scoring.
- GRaSP performs well empirically on your dataset (especially moderate-sized continuous data).
- You want a PAG but find GFCI too noisy or FGES-derived skeletons too brittle.
- You want a hybrid method that preserves **causal discovery under latent confounding** while leveraging permutation sparsity.

---

## Strengths

- Often superior adjacency discovery on datasets where **permutation DAGs capture sparsity** better than order-based DAGs.
- More stable than FCI alone; fewer spurious adjacencies.
- Fully **knowledge-aware**.
- Leverages GRaSP’s **nonparametric flexibility** and sparsity logic.
- PAG refinement ensures latent confounders and selection bias are handled.

---

## Limitations

- Permutation scoring can be slower than order-based BOSS for large $begin:math:text$ p $end:math:text$.
- Still requires CI tests in the refinement stage.
- Accuracy depends strongly on **permutation quality** in the GRaSP step.
- Does not guarantee legality during scoring — legality is restored only in the FCI stage.

---

## How It Differs From Related Algorithms

- **vs. BOSS-FCI**
    - GRaSP-FCI uses **permutations**, not variable orders.
    - Typically slower than BOSS-FCI; sometimes better on medium-sized datasets with specific structure.

- **vs. GFCI**
    - GFCI uses FGES for skeleton discovery; GRaSP-FCI uses GRaSP.
    - GRaSP-FCI can outperform when score-based permutation sparsity is informative.

- **vs. FCIT**
    - FCIT directs CI tests using score priorities; GRaSP-FCI still uses a classical FCI refinement.
    - FCIT guarantees PAG legality at all steps; GRaSP-FCI guarantees legality only at the end.

- **vs. LV-Dumb**
    - LV-Dumb is a heuristic PAG-from-DAG transformer.
    - GRaSP-FCI is a principled hybrid algorithm with full correctness of FCI refinement.

Cross-references:  
👉 [GRaSP](grasp.md) •  
👉 [BOSS-FCI](boss-fci.md) •  
👉 [GFCI](gfci.md) •  
👉 [FCIT](fcit.md) •  
👉 [LV-Dumb](lv-dumb.md)

---

## Prior Knowledge Support

GRaSP-FCI is **fully knowledge-aware**.

You may supply a **Knowledge** object in the GUI or programmatically. Constraints apply to:

- Permutation scoring (forbidden ancestors/descendants, tiers)
- CPDAG construction
- FCI refinement (required/forbidden edges, temporal structure)

Knowledge is respected throughout all phases.

---

## Key Parameters in Tetrad

GRaSP-FCI combines parameters from:

### GRaSP scoring stage

| Parameter | Meaning |
|----------|---------|
| `penaltyDiscount` | BIC penalty multiplier (sparsity control). |
| `maxDegree` | Restricts search to graphs with limited degree. |
| `numThreads` | Parallel evaluation of permutations. |
| `verbose` | Print detailed scoring decisions. |

### FCI refinement stage

| Parameter | Meaning |
|----------|---------|
| `depth` | Maximum conditioning-set size for CI tests. |
| `stableFas` | Order-invariant adjacency removal. |
| `excludeSelectionBias` | Whether to interpret circle–circle as selection structures. |
| `verbose` | Print refinement steps and orientations. |

(Exact parameter list may vary by Tetrad version.)

---

## Reference

**Ramsey, J., Andrews, B., & Spirtes, P. (2025).**  
*Efficient Latent Variable Causal Discovery: Combining Score Search and Targeted Testing.*  
arXiv:2510.04263.

---

## Summary

**GRaSP-FCI = GRaSP permutation CPDAG + FCI latent-variable refinement.**  
A hybrid PAG learner that combines permutation sparsity with principled FCI logic, producing cleaner PAGs than FCI and often more reliable adjacencies than GFCI.