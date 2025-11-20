# Pairwise Orientation Methods — FaskPw & RSkew

**Type:** Non-Gaussian, pairwise orientation algorithms  
**Output:** Directed graph (using a fixed skeleton provided as input)  
**Implements:** Pairwise orientation rules from FASK and LOFS  
**References:**
- Sánchez-Romero et al. (2019) — FASK supplement
- Hyvärinen & Smith (2013). *Pairwise likelihood ratios for estimation of non-Gaussian structural equation models*. JMLR 14(1):111–152.

Pairwise orientation methods take a **fixed adjacency graph** and assign **edge directions** using **non-Gaussianity**, typically skewness or likelihood ratios. They avoid conditional independence tests and do not alter the skeleton; instead, they apply a simple, fast, directional scoring rule to each adjacent pair.

This page documents the two most practically useful pairwise methods in Tetrad:

- **FaskPw** — The pairwise left–right rule used in FASK
- **RSkew** — A robust skewness-based pairwise rule from Hyvärinen & Smith (2013)

Both are implemented within **LOFS** (`Lofs.java`) and support background knowledge (forbidden/required edges, tiers).

---

## Overview

Pairwise methods assume a **linear, non-Gaussian structural equation model**.  
For an adjacency X—Y, they evaluate a **direction score** such as:

- Which direction produces more skewed residuals?
- Which model has larger likelihood under a non-Gaussian SEM?
- Which direction better aligns with conditional or marginal skewness patterns?

Because these methods are **pairwise**, they scale extremely well and require no CI tests beyond the initial skeleton.

---

## FaskPw — FASK Pairwise Left–Right Orientation

**Type:** Pairwise skewness  
**Origin:** Supplementary material of Sánchez-Romero et al. (2019)  
**Goal:** Provide a fast, lightweight version of the FASK orientation step.

FaskPw starts with a **given skeleton** (usually obtained via FAS, PC-like pruning, or IMaGES) and orients each edge X—Y using the **left–right skewness heuristic**:

## Key Idea

For an edge X—Y:

1. Regress each variable on the other:
    - Y = aX + e₁
    - X = bY + e₂
2. Compare the **skewness** of residuals e₁ vs e₂.
3. The direction with **more Gaussian**, *less skewed* residuals is the *effect*;  
   the direction with more skewed residuals is the *cause*.

Formally (but heuristically):

- If `skew(e₁) < skew(e₂)` → X → Y
- If `skew(e₂) < skew(e₁)` → Y → X
- If approximately equal → leave undirected

This rule is the *pairwise* version of the full FASK method used inside the FASK algorithm.

## When to Use

- You want **FASK-like orientation** but:
    - You already have a skeleton
    - You need a much faster method than full FASK
- Non-Gaussianity (especially skewness) is expected
- Large graphs where full FASK may be expensive

## Strengths

- Extremely fast (purely pairwise)
- Captures the main orientation behavior of FASK
- Works well on large high-dimensional datasets
- Respects prior knowledge (forbidden/required edges)

## Limitations

- Uses only **pairwise** information—no collider/propagation rules
- Requires non-Gaussianity (especially skewness)
- Can be unstable when skewness is weak or sample size is small

## Parameters in Tetrad

Mainly inherited from LOFS:

| Parameter | Description |
|----------|-------------|
| `score = LEFT_RIGHT` | Pairwise left-right skewness score |
| `rule = ORIENT_EACH` | Apply orientation independently to each edge |
| Knowledge constraints | Forbidden/required edges, tiers |

---

## RSkew — Robust Skewness Orientation (Hyvärinen & Smith, 2013)

**Type:** Pairwise likelihood / skewness method  
**Origin:** Hyvärinen & Smith (2013), JMLR  
**Implements:** One of the LOFS scores based on **robust non-Gaussian likelihood ratios**

RSkew implements a **robust** direction rule derived from the pairwise likelihood-ratio family proposed by Hyvärinen & Smith:

- Fit linear SEMs X → Y and Y → X
- Compute **non-Gaussian likelihood approximations** (robustified for outliers)
- Prefer the direction with the **higher likelihood** (or lower penalized score)

The resulting rule often performs better than naive skewness comparison when data contain:

- Heavy tails
- Outliers
- Nonlinear distortions that affect skewness estimation

## Key Idea (informal)

For a pair X—Y,

- Compute a robust estimate of the non-Gaussian log-likelihood for models  
  X → Y and Y → X
- Choose the direction with the **greater** log-likelihood
- If scores are similar, keep undirected

This score is implemented in LOFS as `Score.RSkew`.

## When to Use

- Skeleton is known and fixed
- Strong non-Gaussian signals are present
- Data contain **outliers** or are **heavy-tailed**
- You want Hyvärinen-style *likelihood ratio orientation*

## Strengths

- More robust than plain skewness heuristics
- Based on a well-studied likelihood approximation
- Often gives better orientations with noisy/non-ideal data
- Works edge-by-edge, so scales extremely well

## Limitations

- Requires non-Gaussianity to be effective
- Purely pairwise—cannot detect colliders or propagate orientations
- Sensitive to regression model mis-specification if nonlinearities are strong

## Parameters in Tetrad

| Parameter | Description |
|----------|-------------|
| `score = RSKEW` | Hyvärinen & Smith robust skewness likelihood score |
| `rule = ORIENT_EACH` | Apply to each edge independently |
| Knowledge | Forbidden/required edges, tiers |

---

## Prior Knowledge Support

Both **FaskPw** and **RSkew** respect Tetrad’s standard Knowledge constraints:

- Required edges
- Forbidden edges
- Tiers / temporal ordering
- Partial ordering constraints

Since orientations are performed pairwise after the skeleton is fixed, knowledge constraints apply directly and cleanly.

---

## Summary

Pairwise orientation methods offer **extremely fast, purely non-Gaussian direction estimation** on a fixed skeleton:

- **FaskPw**: FASK’s left–right skewness rule; fast, simple, effective on many datasets.
- **RSkew**: Hyvärinen–Smith robust likelihood-ratio orientation; more stable under outliers or heavy tails.

These are the two most useful LOFS-based pairwise options for practical work in Tetrad, and they provide complementary trade-offs in robustness vs simplicity.