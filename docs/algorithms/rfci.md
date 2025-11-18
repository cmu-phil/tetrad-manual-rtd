# Rfci — Really Fast Causal Inference

**Type:** Constraint-based (latent-capable)  
**Output:** RFCI-PAG (a slightly weaker form of a PAG)

RFCI is a **computationally streamlined alternative to FCI** for situations where **latent confounders** and **selection bias** may be present, but where the full FCI algorithm is too slow.  
It uses a **reduced set of CI tests** and **simplified orientation rules** to produce a graph that is always *sound* and *compatible* with FCI, but may be less oriented.  
RFCI is designed for **high-dimensional** problems where FCI’s Possible-D-SEP phase would be prohibitively expensive.

---

## Key Idea

RFCI follows the PC/FCI template but **avoids the most expensive component of FCI**:  
the **Possible-D-SEP edge-removal phase**, which searches for long-range separating sets.

Instead:

1. **Local adjacency search** (PC-style)  
   Uses conditional independence tests with *local* conditioning sets.

2. **Reduced edge-removal step**  
   Performs additional CI tests only on adjacency neighborhoods, not full Possible-D-SEP sets.

3. **Simplified orientation rules**  
   Applies a subset of the FCI rule set, orienting only what can be *soundly inferred* without long-range separations.

The result is a **PAG-like graph** with **fewer orientations** than full FCI, but obtained at a much lower computational cost.

---

## When to Use

- When you need **latent-capable causal discovery** but **FCI is too slow**.
- When the dataset is **high-dimensional** (hundreds or thousands of variables).
- When you want a method that is:
    - faster than FCI,
    - more informative than PC/CPC in the presence of latent confounding.
- When you want a **sound method**—RFCI never produces an orientation that FCI would not.

Related algorithms:
- Use **FCI** when full orientation power is needed.
- Use **GFCI**, **BOSS-FCI**, **GRaSP-FCI**, or **FCIT** when hybrid score–test methods are preferred.

---

## Prior Knowledge Support

**Yes. RFCI accepts background knowledge.**

Supported types:

- **Required edges** (force X → Y or X—Y)
- **Forbidden edges** (prohibit adjacency or direction)
- **Tier/temporal constraints** (edges must point forward in time/tier)

All constraints are enforced consistently throughout adjacency search and orientation.

---

## Strengths

- **Much faster** than FCI — avoids Possible-D-SEP
- **Latent- and selection-capable**
- **Provably sound** under an independence oracle
- **Works well in high-dimensional settings**
- **Never over-orients** compared to FCI
- **Fully knowledge-aware** (required/forbidden edges, tiers)

---

## Limitations

- **Less informative than full FCI**  
  (some edges remain circle–circle where FCI would orient)

- **Finite-sample sensitivity**  
  As in PC/FCI, CI-test errors can propagate.

- **Outputs an RFCI-PAG**, not a fully general PAG  
  (same semantics for edges it does orient, but fewer orientations overall)

---

## Key Parameters in Tetrad

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `indTest`             | Choice of CI test (Fisher Z, G-test, KCI/RCIT, etc.) |
| `alpha`               | Significance level for CI tests |
| `depth`               | Maximum conditioning-set size |
| `knowledge`           | Background knowledge object defining constraints |
| `verbose`             | Controls progress/debug output |
| `numThreads`          | Parallel CI-test execution (if supported) |

---

## Reference

Colombo, D., Maathuis, M. H., Kalisch, M., & Richardson, T. S. (2012).  
**Learning high-dimensional directed acyclic graphs with latent and selection variables.**  
*The Annals of Statistics*, 40(1), 294–321.

---

## Summary

RFCI is a **sound, high-dimensional alternative to FCI** that handles latent confounders and selection bias while avoiding FCI’s costly long-range separation search. It produces a slightly less oriented PAG but is far more scalable and still fully knowledge-aware.