# FCIT — FCI with Targeted Testing

**Type:** Hybrid (score-guided constraint method)  
**Output:** PAG (guaranteed legal at all intermediate stages)  
**Knowledge:** Fully supported (all Tetrad knowledge types)

FCIT (FCI with Targeted Testing) is one of the mixed-strategy latent-variable algorithms introduced in  
**Ramsey, Andrews & Spirtes (2025)**. It enhances FCI by using **score information**, typically from **BOSS**, to prioritize *which conditional independence tests to perform*, drastically reducing spurious independences and search instability.

It preserves full **PAG correctness**, and importantly, every intermediate orientation is enforced to be **legal**, preventing the common “illegal PAG” errors observed in FCI/GFCI under finite samples.

---

## Key Idea

FCIT modifies FCI in two fundamental ways:

### 1. **Score-guided targeted testing**
Instead of performing CI tests in all possible orders or sizes, FCIT uses:

- A scoring engine (usually **BOSS**, optionally GRaSP or FGES)
- A ranked list of edges or conditioning sets

to prioritize tests that are likely to be informative.  
Low-value or low-priority independence tests are performed **later or not at all**, reducing the chance of spurious edge removals.

### 2. **Legality-enforced refinement**
At each orientation step, FCIT applies a legality check:

- Reject any orientation that would create a **directed cycle**,
- Or violate ancestral relations,
- Or create a non-maximal PAG,
- Or violate separation constraints.

Thus, FCIT produces a **legal PAG at every intermediate step**, not just at the end.

---

## When to Use

- Standard FCI or GFCI give unstable or noisy results
- Latent confounding is believed to be present
- The dataset is medium–large (hundreds to thousands of variables)
- You want a **clean, readable PAG** suitable for scientific interpretation
- You prefer **high precision** in adjacencies and orientations

---

## Strengths

- **High stability**: fewer spurious independences
- **High precision** in both adjacencies and orientations
- Produces a **legal PAG at every step**
- Handles latent confounders and selection bias
- Fully knowledge-aware
- Often faster than FCI/GFCI for moderate-to-large datasets
- Excellent accuracy for medium–high dimensional models

---

## Limitations

- Requires a score engine (default: **BOSS**) — adds computation
- Slightly slower than GFCI on very small models
- Still depends on CI tests in refinement, so extremely small samples may be difficult
- Uses heuristics (targeted testing): still empirically strong, not yet theoretically proven to be complete

---

## How It Differs From Related Algorithms

### vs. **FCI**
- FCI performs many CI tests (may be noisy); FCIT **prioritizes and reduces** them.
- FCI can produce intermediate illegal PAGs; FCIT **never** does.

### vs. **GFCI**
- GFCI uses FGES for skeletons; FCIT uses **score-guided test prioritization** instead.
- FCIT tends to produce cleaner PAGs with fewer false positives.

### vs. **BOSS-FCI / GRaSP-FCI**
- BOSS-FCI and GRaSP-FCI replace the skeleton; FCIT replaces the **testing schedule**.
- FCIT is often the most **stable** of the mixed-strategy algorithms.

### vs. **LV-Dumb**
- LV-Dumb is a heuristic PAG-from-DAG transformer.
- FCIT is a principled hybrid consistent with FCI logic.

Cross-references:
👉 [BOSS-FCI](boss-fci.md) •  
👉 [GRaSP-FCI](grasp-fci.md) •  
👉 [GFCI](gfci.md) •  
👉 [FCI](fci.md) •  
👉 [LV-Dumb](lv-heuristic.md)

---

## Prior Knowledge Support

**FCIT is fully knowledge-aware**, just like PC, FGES, FCI, GFCI, and BOSS-FCI.

Knowledge constraints affect:

- Edge removals
- Orientation decisions
- Legality checks
- Selection-bias assumptions
- Allowed/forbidden ancestral relations
- Tier constraints

All constraints are respected throughout scoring, prioritization, and refinement.

---

## Key Parameters in Tetrad

FCIT exposes parameters from:

### Score engine (typically BOSS)

| Parameter | Meaning |
|----------|---------|
| `penaltyDiscount` | Strength of BIC penalty; higher → sparser score proposals. |
| `maxDegree` | Restrict max parent set size (structural regularization). |
| `numThreads` | Parallel scoring/testing. |
| `verbose` | Print BOSS scoring decisions and test rankings. |

### FCI-style refinement

| Parameter | Meaning |
|----------|---------|
| `depth` | Maximum size of conditioning sets for CI tests. |
| `stableFas` | Order-invariant adjacency pruning. |
| `excludeSelectionBias` | Whether to interpret tail–tail edges as selection-induced. |
| `fdrQ` | Optional FDR correction level. |
| `verbose` | Print CI testing and orientation steps. |

### FCIT-specific

| Parameter | Meaning |
|----------|---------|
| `useBestTestFirst` | Whether to rank tests by BOSS scoring (always true in FCIT). |
| `maxTests` | Optional cap on total CI tests (rarely needed). |
| `scoreEngine` | Choose BOSS/GRaSP/FGES as the scoring backend. |

(Names depend slightly on Tetrad version; these reflect Tetrad 7.6.9.)

---

## Reference

**Ramsey, J., Andrews, B., & Spirtes, P. (2025).**  
*Efficient Latent Variable Causal Discovery: Combining Score Search and Targeted Testing.*  
arXiv:2510.04263.

---

## Summary

**FCIT = FCI + score-guided test prioritization + legality checks.**

A high-precision, high-stability PAG algorithm for latent-variable causal discovery that suppresses noisy independence tests and guarantees a legal PAG throughout the search.