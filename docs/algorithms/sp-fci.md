# SP-FCI — Sparsest-Permutation FCI

**Type:** Hybrid (Score + Constraint)  
**Output:** PAG  
**Takes Knowledge:** ✔️ fully knowledge-aware  
**Parent Algorithms:** [FCI](algorithms/fci.md), [SP](algorithms/sp.md)  
**Sibling Variants:** [BOSS-FCI](algorithms/boss-fci.md), [GRaSP-FCI](algorithms/grasp-fci.md), [FCIT](algorithms/sp-fcit.md)

SP-FCI is an **FCI-style latent-variable causal discovery algorithm** that swaps FCI’s **exhaustive adjacency search** for a **permutation-based score search** (the **Sparsest Permutation** algorithm, SP).  
It follows the same design philosophy as BOSS-FCI and GRaSP-FCI: use a **model-based adjacency search** to obtain a high-precision skeleton, then run FCI’s orientation procedures (including all latent-variable edge marks).

Because **SP evaluates every variable permutation**, SP-FCI is only usable for **very small models (≈10 variables)**—but within that regime it is **extremely accurate**, often outperforming all other FCI-style methods.

## Key Idea

1. **Permutation-based adjacency search (SP)**  
   - Consider all permutations of the variables.  
   - For each permutation, fit linear regressions parent-set-by-parent-set.  
   - Score each DAG via BIC (or score equivalent).  
   - Choose the DAG with the **fewest edges** among all **BIC-optimal** graphs.  
   - Extract the **adjacencies** from this DAG.

2. **Latent-variable refinement (FCI)**  
   - Start from the SP skeleton.  
   - Run the FCI orientation rules.  
   - Produce a **PAG** representing the latent variable equivalence class.

## When to Use

- Very small models (5–10 variables)
- High accuracy desired despite high cost
- Need for latent-variable robustness
- Want a non-CI-test adjacency phase

## Strengths

- Extremely accurate for small p  
- CI-test-free adjacency search  
- Clean skeleton for FCI refinement  
- Fully knowledge-aware  
- Useful as a gold-standard baseline

## Limitations

- Exponential in variable count — limited to ≤10  
- Typically linear-Gaussian scoring  
- Orientation still uses CI tests  
- Not for moderate or large graphs

## Key Parameters in Tetrad

| Parameter | Meaning |
|----------|---------|
| `penaltyDiscount` | BIC penalty discount for SP |
| `semBicStructurePrior` | Prior weight for SP scoring |
| `semBicRule` | Scoring rule for permutations |
| `faithfulnessAssumed` | Enforce faithfulness in scoring |
| `maxDegree` | Optional parent-set pruning |
| `numThreads` | Parallel scoring |
| `allowBidirected` | Allow ↔ during FCI orientation |
| `verbose` | Log SP + FCI operations |

## Knowledge Support

✔ Fully supports background knowledge:  
- Required/forbidden edges  
- Tier/ancestral constraints  
- Forbidden arrowheads  
- Temporal/ordering constraints  

## Relation to Other Algorithms

- **FCI** — SP-FCI replaces CI-test adjacency with SP  
- **BOSS-FCI** — scalable SP-free score-first variant  
- **GRaSP-FCI** — scalable permutation-relaxation variant  
- **FCIT** — BOSS-guided targeted testing  
- **SP** — adjacency-only version

## References

- Raskutti & Uhler (2018). *Learning directed acyclic graphs based on sparsest permutations.* Biometrika.
- Spirtes et al. (2000). *Causation, Prediction, and Search (2nd ed.).*
- Ramsey, Andrews & Spirtes (2025). *Efficient Latent Variable Causal Discovery.* arXiv:2510.04263.

## Summary

SP-FCI is the **high-accuracy, small-variable-count** member of the hybrid FCI family, using SP to generate precise adjacencies and FCI to infer a PAG that accounts for latent confounding.
