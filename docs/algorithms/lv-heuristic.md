# LV-Heuristic — Heuristic Latent-Variable PAG from a Single DAG

**Type:** Heuristic latent-variable method  
**Output:** PAG  
**Knowledge:** Fully supported  
**Paper:** Ramsey, Andrews & Spirtes (2025)

LV-Heuristic (“Latent Variable *Heuristic*”) is the simplest of the mixed-strategy latent-variable algorithms introduced in **Ramsey, Andrews & Spirtes (2025)**. It is deliberately *not* a complete or theoretically guaranteed method — instead, it provides a **very fast**, **very stable**, and surprisingly **effective** heuristic for producing a PAG when latent confounding is present.

The idea is straightforward:

1. Run a **score-based DAG search** (usually BOSS).
2. Treat the DAG’s edges as representing **visible** relationships.
3. Use a simplified refinement pass to introduce only those latent-variable marks that are *clearly* supported by the independence structure.
4. Enforce **PAG legality** throughout (no directed cycles, no false colliders, no non-maximal edges).

The result is a **“good-enough” latent-variable PAG**, extremely clean and readable, suitable for downstream exploratory analysis.

---

## What LV-Heuristic Is (and Is Not)

LV-Heuristic **is**:

- a quick heuristic PAG generator
- highly stable (almost no spurious orientations)
- extremely fast (near-DAG-search speed)
- good for exploratory science
- easy to interpret
- robust to moderate CI-test noise

LV-Heuristic is **not**:

- a full replacement for FCI/GFCI/BOSS-FCI/FCIT
- guaranteed to detect all latent confounders
- theoretically complete

It is best viewed as a **lightweight companion** to the more powerful mixed-strategy algorithms.

Cross-refs:  
👉 [BOSS-FCI](boss-fci.md) •  
👉 [GRaSP-FCI](grasp-fci.md) •  
👉 [FCIT](fcit.md) •  
👉 [GFCI](gfci.md) •  
👉 [FCI](fci.md)

---

## Key Idea

LV-Heuristic follows a minimal pipeline:

### 1. Build a high-quality DAG
Usually with **BOSS**, but any good DAG search works.

The DAG is assumed to be a reasonable approximation of the *visible* structure.

### 2. Convert the DAG to a partial ancestral structure
Edges that appear strongly supported remain directed.  
Edges that look symmetric or ambiguous become “o–>”, “<–o”, or “o–o”.

### 3. Introduce latent-variable marks sparingly
Only when the DAG structure **cannot** be explained without a hidden common cause.  
This keeps false positive bidirected edges extremely low.

### 4. Enforce legality
Just like in FCIT and BOSS-FCI, LV-Heuristic ensures the output is:

- ancestral
- acyclic
- maximal
- collider-consistent

The result is a lightweight but well-formed PAG.

---

## When to Use LV-Heuristic

- You want a **quick, conservative latent-variable PAG**
- You don’t want to pay the cost of full FCI/GFCI/FCIT
- You want a **clean**, easy-to-read PAG for exploratory science
- You are working with **large number of variables** but want PAG-like output
- As a **warm-up** or **sanity check** before running more complete methods

LV-Heuristic often functions as a “first draft PAG.”

---

## Strengths

- **Extremely fast** (near score-based DAG speed)
- **Highly stable** — almost no spurious latent marks
- **Readable PAGs**
- Great exploratory tool
- Fully knowledge-aware
- Good for large models or analyst-driven workflows
- Compatible with BOSS, GRaSP, FGES, and other DAG search engines

---

## Limitations

- Not a complete characterization of the latent structure
- Will miss subtle unmeasured confounders that require CI-based reasoning
- Not designed to detect selection bias
- Not a replacement for BOSS-FCI or FCIT in scientific inference

---

## How LV-Heuristic Differs From Other Mixed-Strategy Algorithms

### vs. **BOSS-FCI** / **GRaSP-FCI**
- LV-Heuristic is **much simpler**.
- It does **not** perform the full refinement / collider-correction logic.
- It produces cleaner but more **conservative** PAGs.

### vs. **FCIT**
- FCIT uses score-guided **targeted CI testing**.
- LV-Heuristic uses none of the CI information (purely score-based).
- LV-Heuristic is faster but less expressive.

### vs. **GFCI/FCI**
- LV-Heuristic avoids the combinatorial CI-testing explosion entirely.
- As a result: fewer false positives, but also fewer discovered latent structures.

---

## Prior Knowledge Support

LV-Heurstic **fully supports background knowledge**, including:

- required edges
- forbidden edges
- temporal/tier constraints
- ancestral constraints
- selection-bias assumptions

Knowledge is respected during:

- initial DAG search
- latent-mark introduction
- legality refinement

---

## Key Parameters in Tetrad

LV-Heuristic shares parameters with its underlying DAG search (often **BOSS**):

| Parameter | Meaning |
|----------|---------|
| `penaltyDiscount` | BIC penalty multiplier for BOSS. |
| `maxDegree` | Maximum parent set size. |
| `numThreads` | Parallel scoring. |
| `faithfulnessAssumed` | Controls BOSS’s initial adjacency filtering. |
| `verbose` | Print detailed decisions. |

LV-Heuristic itself has few additional parameters—its simplicity is part of the design.

---

## Reference

**Ramsey, J., Andrews, B., & Spirtes, P. (2025).**  
*Efficient Latent Variable Causal Discovery: Combining Score Search and Targeted Testing.*  
arXiv:2510.04263.

---

## Summary

**LV-Heuristic = DAG → conservative PAG.**  
A near-zero-cost heuristic PAG generator that produces clean, stable, easy-to-interpret graphs — ideal for exploratory or large-scale workflows.