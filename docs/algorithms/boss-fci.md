# BOSS-FCI — Best-Order Score Search + FCI Refinement

**Type:** Hybrid (score-based + CI tests)  
**Output:** PAG  
**Knowledge:** Fully supported (all Tetrad knowledge constraints)

BOSS-FCI is one of the *mixed-strategy latent-variable algorithms* introduced in  
**Ramsey, Andrews & Spirtes (2025)**. It combines:

1. **BOSS** — a *score-based ordering search* that produces a high-quality CPDAG, and
2. **An FCI-style latent-variable correction stage**, which transforms the CPDAG into a **PAG**.

The resulting algorithm is faster than GFCI and usually more accurate, particularly in medium- and high-dimensional settings.

---

## Key Idea

BOSS-FCI follows the general ***X-FCI template***:

1. **Score phase**
    - Run **BOSS** to produce a CPDAG (causal sufficiency assumed for this step).
    - BOSS evaluates local SEM-BIC scores under different orderings, using memoization and efficient updates.

2. **Latent-variable correction**
    - Treat the BOSS CPDAG exactly as an “oracle skeleton” and apply:
        - Orientation from separating sets
        - Possible-D-SEP pruning
        - Meek-style propagation
        - PAG legality checks
    - This yields a **PAG** that accounts for latent confounders and selection bias.

BOSS-FCI is therefore a **hybrid** algorithm: it uses score-based reasoning for adjacency decisions and constraint-based logic for PAG completion.

---

## When to Use

- You want a **PAG** but pure FCI is too noisy or too slow.
- BOSS performs well on your data (medium-to-large $begin:math:text$ p $end:math:text$, moderate sparsity).
- You want a *drop-in alternative* to **GFCI** with better scalability.
- You have mixed continuous/discrete data (BOSS supports mixed BIC scoring).
- You want a method that scales to dozens–hundreds of variables with latent confounding.

---

## Strengths

- **More accurate than GFCI** in most regimes (Ramsey et al. 2025).
- **Fewer false positives** and cleaner PAGs than standard FCI.
- Leverages BOSS’s **robust adjacency selection**.
- **Parallelizable** and efficient for larger variable counts.
- Fully **knowledge-aware** (forbidden edges, required edges, tiers, temporal constraints).

---

## Limitations

- BOSS phase assumes **causal sufficiency**, so the initial CPDAG can still suffer mis-orientations in heavily confounded models.
- Still requires CI tests for the correction phase (although *fewer* than GFCI).
- For extremely dense graphs, score-based phases can slow down.

---

## How It Differs From Related Algorithms

- **vs. GFCI**
    - Same conceptual pipeline but with **BOSS replacing FGES**.
    - Usually more accurate and efficient.

- **vs. GRaSP-FCI**
    - GRaSP uses permutation scoring; BOSS uses order-based BIC optimization.
    - BOSS-FCI is typically more stable on mixed/continuous data.

- **vs. FCIT**
    - FCIT uses targeted CI testing guided by BOSS and guarantees PAG legality,  
      whereas BOSS-FCI still uses a traditional FCI refinement phase.

- **vs. LV-Dumb**
    - LV-Dumb heuristically converts a BOSS DAG directly to a PAG.
    - BOSS-FCI is a *principled* algorithm with sound PAG-correction steps.

Cross-references:  
👉 [BOSS](boss.md) •  
👉 [GFCI](gfci.md) •  
👉 [GRaSP-FCI](grasp-fci.md) •  
👉 [FCIT](fcit.md) •  
👉 [LV-Dumb](lv-dumb.md)

---

## Prior Knowledge Support

BOSS-FCI **fully supports knowledge**.

You may connect a **Knowledge** box in the Tetrad GUI or provide a  
`Knowledge` object programmatically.

Enforced constraints:

- Required edges
- Forbidden edges
- Tier / temporal ordering
- Forbidden ancestor/descendant relations
- Any additional Tetrad structural constraints

Knowledge is enforced during **both**:
- The BOSS adjacency/orientation decisions, and
- The FCI-style PAG refinement.

---

## Key Parameters in Tetrad

BOSS-FCI inherits parameters from **BOSS** *and* from the FCI refinement step.  
CamelCase names (GUI / script API) shown.

### BOSS-stage parameters

| Parameter | Meaning |
|----------|---------|
| `penaltyDiscount` | BIC penalty multiplier (higher → sparser). |
| `maxDegree` | Maximum degree allowed during scoring. |
| `numThreads` | Parallelism level for scoring. |
| `verbose` | Print decision logs. |

### FCI-refinement parameters

| Parameter | Meaning |
|----------|---------|
| `depth` | Max conditioning set size for CI tests. |
| `stableFas` | Order-independent adjacency removal. |
| `excludeSelectionBias` | Whether to disallow interpreting circles as selection bias. |
| `verbose` | Print CI tests / orientations. |

(Exact list depends on the current Tetrad release.)

---

## Reference

**Ramsey, J., Andrews, B., & Spirtes, P. (2025).**  
*Efficient Latent Variable Causal Discovery: Combining Score Search and Targeted Testing.*  
arXiv:2510.04263.

---

## Summary

**BOSS-FCI = BOSS CPDAG + FCI latent-variable correction.**  
A fast, accurate hybrid PAG learner that outperforms GFCI in most settings while remaining fully knowledge-aware and scalable.