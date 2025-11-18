# Restricted BOSS — Target-Focused Best Order Score Search

**Type:** Score-based (CPDAG, variable-order search)  
**Output:** CPDAG (trimmed around specified targets)

Restricted BOSS is a **target-focused variant of BOSS** designed for **fast, repeated runs on large datasets** when you care about a **small set of target variables**.  
It first uses BOSS with tier constraints to identify a **restricted neighborhood** around the targets, then **re-runs BOSS only on that reduced variable set**, and finally trims the resulting CPDAG around the targets.

This makes it ideal as a **fast inner loop** for methods like **CStaR**, where many DAG/CPDAG fits are needed for different target choices.

---

## Key Idea

Restricted BOSS is a two-stage score-based procedure built on top of **BOSS (Best Order Score Search)**:

1. **Global but tier-constrained BOSS run**
   - Treat the user-specified target variables as **Tier 2** and all other variables as **Tier 1**.
   - Forbid edges *within* Tier 1, so non-target variables cannot form complex subnetworks among themselves.
   - Run BOSS (via `PermutationSearch`) under this knowledge to produce an initial CPDAG and, more importantly, to identify the **“first-layer” neighbors** of each target.

2. **Restriction to the target neighborhood**
   - Collect, for each target, the variables in its **first layer** (parents/children in the initial BOSS run).
   - Form the **restricted variable set** = {targets} ∪ {first-layer neighbors of targets}.
   - Subset the dataset to these variables only.

3. **Second BOSS run on restricted data**
   - On the restricted dataset, again place targets in **Tier 2** and the remaining neighbors in **Tier 1**.
   - Allow edges within Tier 1 this time, but still enforce that any edges respect the tier ordering (Tier 1 → Tier 2).
   - Run BOSS again over this smaller set to obtain a refined CPDAG focused on the targets and their local neighborhood.

4. **Graph trimming**
   - Finally, apply `GraphUtils.trimGraph(targets, graph, trimmingStyle)` to remove extraneous structure according to the selected trimming style.
   - The returned graph is a **CPDAG concentrated on the targets and their support**, suitable for downstream use in methods like CStaR.

---

## When to Use

Use **Restricted BOSS** when:

- You have one or more **designated target variables** (e.g., outcomes, endpoints) and care primarily about their **local causal structure**.
- You need to run **BOSS many times** (e.g., across different targets, resamples, or bootstrap runs) and cannot afford full BOSS over all variables each time.
- Your dataset has **many predictors** but you expect that only a **small subset** is relevant for each target.
- You are using or emulating **CStaR**-style pipelines that repeatedly fit target-centered CPDAGs.

It is especially useful in:

- **Large-p** settings where full BOSS over all variables is expensive.
- Pipelines that run **many DAG/CPDAG fits per dataset** for efficiency studies, stability selection, or effect-bounding.

If you instead want a **single global CPDAG over all variables**, you would typically use **BOSS** or **FGES** directly.

---

## Prior Knowledge Support

Restricted BOSS **internally constructs its own tier-based knowledge**:

- Targets are placed in **Tier 2**.
- Non-target variables are placed in **Tier 1**.
- In the **first pass**, edges within Tier 1 are **forbidden**, to quickly identify candidate neighbors of the targets.
- In the **second pass** (on the restricted variable set), edges within Tier 1 are **allowed**, but the tier ordering (Tier 1 → Tier 2) is still enforced.

At present, the wrapper focuses on this **hard-coded tiering scheme** for speed and reproducibility.  
User-specified `Knowledge` objects (for arbitrary required/forbidden edges) are not exposed as parameters in this algorithm.

---

## Strengths

- **Target-focused and efficient**
  - Avoids scoring the full variable set when only the **local neighborhood of the targets** is of interest.
- **Built on BOSS**
  - Inherits BOSS’s strengths for **order-based score optimization** and scalability.
- **Two-stage restriction**
  - The initial tier-constrained run acts as a **variable selection step**, focusing the second run on a smaller, more relevant set.
- **Good for repeated runs**
  - Well-suited as an **inner loop** in algorithms that repeatedly fit local CPDAGs (e.g., CStaR).

---

## Limitations

- **Targets must be specified**
  - Requires the user to provide a non-empty set of target variables; not a general global structure learner.
- **Assumes no latent confounding**
  - Like BOSS, the annotation `AlgType.forbid_latent_common_causes` indicates **causal sufficiency**; it is not designed for latent-variable PAGs.
- **Fixed tiering strategy**
  - The tier-based restriction strategy is **hard-coded**; if you need arbitrary prior knowledge patterns, plain BOSS or other algorithms may be more appropriate.
- **Trimming style matters**
  - The final graph shape depends on the `trimmingStyle` parameter; overly aggressive trimming can remove potentially relevant structure.

---

## Key Parameters in Tetrad

Restricted BOSS uses the same score infrastructure as BOSS; you select a **Score** via the scoring interface.

| Parameter (camelCase)  | Description |
|------------------------|-------------|
| `useBes`               | Whether to use **BES-style** search within BOSS. |
| `numStarts`            | Number of random restarts / starting permutations. |
| `targets`              | Comma- or space-separated list of target variable names. |
| `trimmingStyle`        | Controls how the final graph is pruned. |
| `seed`                 | Random seed for reproducibility. |

---

## Reference

Restricted BOSS is an **engineering variant** of:

- **BOSS (Best Order Score Search)** — see the BOSS documentation page for conceptual and theoretical details.

It is used in Tetrad as a **fast, target-focused alternative to full BOSS**, particularly within the **CStaR** algorithm.

---

## Summary

Restricted BOSS is a **target-centered, two-stage BOSS wrapper**:  
it identifies a small neighborhood around user-specified targets, refits BOSS on that restricted set, and trims the resulting CPDAG—making it a **fast workhorse** for large-scale, target-focused causal structure learning.
