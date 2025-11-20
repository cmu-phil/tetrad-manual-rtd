# FASK — Fast Adjacency Skewness

**Type:** Non-Gaussian / Skewness-based orientation (hybrid)  
**Output:** Fully oriented graph (directed graph)  
**Assumptions:** Linear or nonlinear relationships with **non-Gaussian**, **skewed** disturbances

FASK (“Fast Adjacency Skewness”) is a hybrid causal discovery algorithm that begins with a **FAS (Fast Adjacency Search)** skeleton and then applies **skewness-based directional tests** to orient each undirected adjacency.  

It is designed to be **fast, lightweight, and sensitive to non-Gaussian direction-of-causation signals** that are invisible to correlation or conditional independence alone.

FASK performs exceptionally well in settings where variables exhibit **skewness**, even mild, and provides a fast alternative to full ICA-based LiNGAM methods.

---

## Key Idea

FASK has two stages:

### 1. Skeleton discovery using FAS
- Run Fast Adjacency Search (from PC / PC-Max), using an independence test.
- Produce an undirected skeleton that captures adjacency reliably.

### 2. Edge orientation using skewness differences
For an adjacency X — Y:

- FASK evaluates **skewness-weighted conditional moments** of X predicting Y and Y predicting X.
- The direction with the **larger skewness-adjusted dependence measure** is chosen as the causal direction.
- If the skew-based test is inconclusive, FASK leaves the edge unoriented or uses small auxiliary rules for resolution.

Because skewness provides directional information even in the presence of confounding (in many models), FASK can often orient edges that PC, FGES, and LiNGAM leave ambiguous.

---

## When to Use

FASK is particularly useful when:

- The data are **non-Gaussian** with noticeable skew.
- The underlying causal relationships may be **mildly nonlinear**.
- You need an algorithm **faster than LiNGAM** but that still exploits non-Gaussianity.
- You want directed edges, not just a CPDAG skeleton.
- You want a fast orientation module to compare with PC/FCI/FGES.

Common applications include:

- Neuroimaging (fMRI, EEG)
- Biological signaling pathways
- Economics and finance (skewed residuals)
- Any domain where non-Gaussianity is expected

---

## Prior Knowledge Support

FASK honors the same kinds of background knowledge used in PC and FAS:

- Required edges
- Forbidden edges
- Temporal/tier constraints

Knowledge is enforced during skeleton discovery and orientation.

---

## Strengths

- **Very fast**: skeleton from FAS, lightweight orientation.
- **Robust** to mild nonlinearity.
- **Orientations even when correlations are small** if skewness is present.
- **No ICA** required; avoids permutation instability and high-dimensional ICA issues.

---

## Limitations

- Requires **non-Gaussian**, **skewed** disturbances.
- Does not explicitly account for latent confounding (unlike FCI or GFCI).
- Reliability decreases when sample sizes are very small.

---

## Key Parameters in Tetrad

| Parameter (camelCase) | Description |
|------------------------|-------------|
| penaltyDiscount | Penalty for the FAS phase (e.g., BIC penalty multiplier). |
| independenceTest | CI test used in skeleton discovery. |
| alpha | Significance level for removing edges in FAS. |
| threshold | Minimum skewness-based score required to orient an edge. |
| depth | Maximum conditioning-set depth in FAS. |
| verbose | Print internal diagnostics and skewness comparisons. |

---

## Reference

FASK is presented in the supplement of:

**Sanchez-Romero, R., Ramsey, J., Zhang, K., Glymour, C., Huang, B., & Spirtes, P.** (2019).  
*Causal discovery of feedback networks with functional interventions.*  
Proceedings of the Conference on Causal Learning and Reasoning (CLeaR).

(Full FASK details appear in the online supplement and technical appendix.)

---

## Summary

FASK combines a fast PC-style skeleton with a **skewness-based orientation test**, producing fully directed graphs when non-Gaussian skewness is present. It is a fast, practical alternative to LiNGAM for discovering causal directionality in skewed, continuous data.