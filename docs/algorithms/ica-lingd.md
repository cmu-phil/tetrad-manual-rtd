# ICA LingD — Cyclic LiNGAM (Lacerda et al.)

**Type:** Non-Gaussian / Moment-based / ICA-based  
**Output:** Directed cyclic graph (DCG)  
**Assumptions:** Linear SEM with independent, non-Gaussian noise; cycles allowed

IcaLingD is the **cyclic extension** of the LiNGAM framework proposed by Lacerda et al. It generalizes ICA-LiNGAM so that **feedback cycles** are permitted. Instead of assuming a strictly acyclic causal ordering, IcaLingD recovers an **almost-directed** structure that can include **strongly connected components (SCCs)** corresponding to causal feedback loops.

It is one of the earliest practical methods capable of learning **linear, non-Gaussian feedback systems**.

---

## Key Idea

Classic LiNGAM uses ICA to estimate a mixing matrix for an acyclic model.  
In the **cyclic** case, the mixing matrix does not factor cleanly into a triangular form.

IcaLingD proceeds by:

1. Running ICA to obtain an estimated mixing matrix.
2. Analyzing the absolute values of this matrix to identify **directed influence strengths**.
3. Constructing a weighted directed graph from these influences.
4. Identifying cycles through strongly connected components (SCC decomposition).
5. Orienting edges wherever the ICA information yields a clear sign of influence.
6. Representing SCCs as **feedback components** rather than trying to force a DAG orientation.

The result is a **directed cyclic graph**:
- Outside cycles, edges reflect directed causal influence.
- Inside cycles, the algorithm outputs SCCs indicating feedback relationships.

---

## When to Use

Use IcaLingD when:

- The underlying system may involve **feedback loops**.
- The structural equations are **linear**.
- The noise terms are **independent and non-Gaussian**.
- You want to detect **cyclic components**, not just a DAG.
- DirectLiNGAM or ICA-LiNGAM fails due to the presence of cycles.

Typical domains:

- Econometrics (supply-and-demand feedback)
- Neuroscience or physiology (mutually regulating components)
- Engineering control systems
- Any domain where reciprocal causation is plausible

---

## Prior Knowledge Support

The Tetrad implementation respects:

- Required edges
- Forbidden edges
- Tier constraints (although tiers interact with cycles in a limited way)

Knowledge constraints help restrict the search space for the ICA permutation stage and for the cycle decomposition.

---

## Strengths

- Handles **cycles**, which LiNGAM and DirectLiNGAM cannot.
- Produces explicit **feedback components** via SCC detection.
- Non-Gaussianity makes the system **identifiable** in many cases where Gaussian SEMs fail.
- A natural extension of ICA-LiNGAM.

---

## Limitations

- Less statistically stable than DirectLiNGAM and ICA-LiNGAM.
- Interpretation can be harder when cycles are large.
- Assumes linearity; does not handle nonlinear feedback.
- Still sensitive to ICA numerical issues.

---

## Key Parameters in Tetrad

| Parameter (camelCase) | Description |
|------------------------|-------------|
| numRestarts | ICA restarts to stabilize the decomposition. |
| maxIterations | Maximum ICA iterations. |
| icaAlgorithm | Choice of ICA backend. |
| threshold | Cutoff for treating ICA coefficients as edges. |
| detectCycles | Whether to run SCC decomposition explicitly. |
| verbose | Show details of ICA and SCC steps. |

---

## Reference

**Lacerda, G., Spirtes, P., Ramsey, J., & Hoyer, P.** (2008).  
*Discovering cyclic causal models by independent component analysis.*  
Proceedings of the 24th Conference on Uncertainty in Artificial Intelligence (UAI).

---

## Summary

IcaLingD generalizes LiNGAM to **feedback systems**.  
It applies ICA to linear, non-Gaussian data, identifies directed influences and strongly connected components, and outputs a cyclic causal graph that can reveal feedback loops.