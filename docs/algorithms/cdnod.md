# Cdnod — Causal Discovery from Nonstationary / Distribution-Shifted Data

**Type:** Constraint-based, distribution-shift aware  
**Output:** CPDAG over observed variables plus a continuous change-index C

`Cdnod` is a PC-style causal discovery algorithm for data with **nonstationarity or distribution shifts**.  
It assumes you have a **continuous change-index variable C** (for example time, domain index, or an ordering of environments) and uses this, together with conditional independence tests, to learn a **CPDAG** over the measured variables and C. This Tetrad implementation is a translation of the **CD-NOD** idea (Zhang et al.) and of the corresponding implementation in the `causal-learn` project, adapted to the PC/FAS + Meek rules framework.

---

## Key Idea

The core idea is:

> Treat a continuous **change index C** as an exogenous driver of distributional changes and look for **stable conditional independences** in the joint distribution over (X, C).

Internally, `Cdnod`:

1. **Builds a skeleton with FAS (PC-style)**
    - Runs FAS on all variables including C, using a user-supplied `IndependenceTest`.
    - Stores separating sets (sepsets) for later collider decisions.
    - Optionally uses the *stable* variant of FAS.

2. **Forces C → X adjacencies**
    - For any adjacency between C and a variable X, `Cdnod` orients it as C → X, unless:
        - that direction is forbidden by knowledge, or
        - the opposite direction is required.

3. **Orients unshielded colliders with a chosen style**
    - For each unshielded triple X–Z–Y (with X and Y non-adjacent), `Cdnod` can use:
        - **SEPSETS**: standard PC rule based on stored separating sets;
        - **CONSERVATIVE**: CPC-style logic (requires consistent evidence);
        - **MAX_P**: compares best p-values for sepsets including vs excluding the middle node Z and orients according to the stronger side.

4. **Applies Meek rules**
    - Runs Meek rules (with `Knowledge`) to propagate orientations and close under standard CPDAG implications.
    - The final output is a **CPDAG** over the X variables plus C.

Unlike FCI-based variants (such as a hypothetical `CdNodPag`), this `Cdnod` implementation **does not do PAG/MAG reasoning** and **does not model latent variables explicitly**; it is a PC-like method with an extra change-index variable and CD-NOD-informed collider rules.

---

## When to Use

Use `Cdnod` when:

- You have **nonstationary or heterogeneous data** and a **known change index C**, such as:
    - time (trend or slow drift),
    - an environment index (domains, sites, regimes),
    - a known ordering of batches or conditions.
- You want a **PC-style CPDAG** that accounts for distribution shifts, rather than assuming i.i.d. data.
- You have (or can define) a **continuous C** and a suitable **conditional independence test** over (X, C).
- You want more robust collider decisions around nonstationary structure using **CPC-style** or **MAX_P** rules.

Related algorithms:

- **PC / CPC / PC-Max**: same overall flavor, but assume stationarity, no special C.
- **CdNodPag** (if exposed): PAG-style CD-NOD variant with latent-variable semantics.
- **Cdnod** is the stationarity-aware, CPDAG version that plugs neatly into standard PC-style workflows.

---

## Prior Knowledge Support

**Does it accept background knowledge?**  
Yes.

`Cdnod` uses Tetrad’s `Knowledge` in several places:

- **Skeleton phase:** passes `Knowledge` into FAS to constrain allowed adjacencies.
- **C → X orientation:** respects forbidden/required edges and tiering when deciding whether to orient C → X.
- **Collider orientation:** checks `Knowledge` before orienting X → Z ← Y.
- **Meek rules:** runs with `Knowledge`, so implied orientations also respect required/forbidden edges and tiers.

You can therefore enforce:

- Required edges (X must cause Y),
- Forbidden edges (X must not cause Y),
- Tier/temporal constraints (edges must go forward in time / tier).

---

## Strengths

- **Explicitly models distribution shift via C**
    - Makes CD-NOD ideas available in a PC-style CPDAG framework.
- **Flexible collider orientation**
    - Choice of SEPSETS, CONSERVATIVE (CPC), or MAX_P collider logic.
- **Integrates with standard Tetrad components**
    - Uses FAS, Meek rules, `Knowledge`, and `IndependenceTest` in a familiar way.
- **Supports timeouts and depth caps**
    - More controllable in large or high-dimensional problems.

---

## Limitations

- **Requires a valid change index**
    - You must provide a meaningful continuous C; if C is arbitrary or noisy, results may degrade.
- **CPDAG only; no PAG semantics**
    - This implementation does not represent latent confounding or selection bias explicitly.
- **Same sensitivity to CI-test errors as PC**
    - Mis-specified tests or small samples can lead to missing or spurious edges, and to ambiguous collider decisions.
- **Assumes C is the last column**
    - When you provide `dataWithC` directly, the last column must be the change index C.

---

## Key Parameters in Tetrad / Scripting

`Cdnod` is typically constructed via its `Builder` in code, or wrapped by a higher-level Tetrad algorithm.  
The main knobs are:

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `stableFas` | Boolean. If `true`, uses the **stable** version of FAS for skeleton discovery (order-independent). |
| `colliderOrientationStyle` | Strategy for orienting colliders. Options include `SEPSETS`, `CONSERVATIVE`, or `MAX_P` depending on how aggressively to orient ambiguous triples. |
| `depth` | Maximum conditioning-set size for both FAS and collider detection. Use `-1` for unlimited depth. |
| `fdrQ` | False discovery rate threshold `q` for FDR-controlled independence testing. Used only when FDR is enabled. |
| `verbose` | If `true`, prints detailed diagnostic output for FAS, collider discovery, and orientation propagation. |

---

## Reference

The algorithmic idea is based on:

Zhang, K., Huang, B., Zhang, J., Glymour, C., & Schölkopf, B. (2017).  
**Causal discovery from nonstationary/heterogeneous data: Causal invariance and CD-NOD.**  
In *Proceedings of the 31st Conference on Neural Information Processing Systems (NeurIPS)*.

This Tetrad implementation is an adaptation of the CD-NOD procedure, and closely follows the implementation available in the **`causal-learn`** project, re-expressed in a **PC/FAS + Meek rules** framework to produce a CPDAG.

---

## Summary

`Cdnod` is a **PC-style constraint-based algorithm** for **nonstationary or distribution-shifted data**, treating a continuous change index C as an exogenous driver of changes and returning a **CPDAG over X and C** using CD-NOD-inspired collider decisions, with full support for Tetrad’s background knowledge and tools.