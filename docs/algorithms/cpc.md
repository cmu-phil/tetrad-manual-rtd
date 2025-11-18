# Conservative PC (CPC) — Conservative Collider Orientation

**Type:** Constraint-based (conservative variant)  
**Output:** e-pattern (equivalence class of CPDAGs)

Conservative PC (CPC) is a modification of the PC algorithm designed to **avoid false-positive collider orientations** by requiring stronger evidence before declaring a triple a collider. Instead of orienting all unshielded colliders using a single separating set, CPC checks *all relevant separating sets* and only orients a collider when **all such tests agree**.

This prevents erroneous collider orientations when CI tests are noisy or unstable.

---

## Key Idea

Given an unshielded triple:

```
X — Y — Z     with    X not adjacent to Z
```

PC orients this as a collider `X → Y ← Z` **if Y ∉ sepset(X, Z)**.

CPC strengthens this:

### Conservative Collider Rule

For every separating set S such that  
`X ⟂ Z | S` and S is a subset of adj(X) ∪ adj(Z):

- If **Y ∉ S for all such S**, conclude:  
  **X → Y ← Z** (collider)

- If **Y ∈ S for all such S**, conclude:  
  **X — Y — Z** (noncollider)

- Otherwise:  
  **Leave the triple unoriented** (ambiguous)

The resulting graph is an **e-pattern** rather than a CPDAG—some orientations remain intentionally unresolved.

---

## When to Use

Use CPC when:

- You expect **small sample sizes**, **noisy CI tests**, or **unstable separating sets**
- False-positive collider orientations would be costly (e.g., downstream adjustment sets)
- You want a **more conservative, robust version** of PC

CPC is strictly more conservative than PC-Max and classic PC.

---

## Prior Knowledge Support

CPC **fully supports background knowledge**, including:

- Required edges  
- Forbidden edges  
- Tier/temporal constraints  
- Any other `Knowledge` box logic in Tetrad

All constraints are respected during adjacency and orientation phases.

---

## Strengths

- Greatly reduces **false-positive collider orientations**
- Robust under sampling variability
- Produces a **safe e-pattern** that captures uncertainty
- Still quite fast in practice

---

## Limitations

- May leave many triples unoriented (intentionally)
- Produces an **e-pattern** rather than a CPDAG, so fewer directions may be implied
- Conservative nature may propagate to downstream inference

---

## Key Parameters in Tetrad

CPC is implemented as a **collider orientation style** inside the PC search wrapper, so it shares PC’s parameters:

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `stableFas` | Use stable (order-independent) adjacency search. |
| `colliderOrientationStyle` | Set to **“Conservative”** to use CPC rules. |
| `allowBidirected` | Allow temporary bidirected edges. |
| `depth` | Maximum conditioning set size. |
| `fdrQ` | FDR-controlled CI testing option. |
| `timeLag` | Lag structure for time-series data. |
| `timeLagReplicatingGraph` | Replicate lag structure across slices. |
| `verbose` | Log CI tests and orientation steps. |

See the main **PC** documentation for general parameter behavior.

---

## Reference

The original peer-reviewed publication:

**Ramsey, J., Zhang, J., & Spirtes, P. (2006).**  
*Adjacency-faithfulness and conservative causal inference.*  
In Proceedings of the 22nd Conference on Uncertainty in Artificial Intelligence (UAI-06), pp. 401–408.

A later archival version:  
Ramsey, J., Zhang, J., & Spirtes, P. L. (2012). *Adjacency-faithfulness and conservative causal inference.* arXiv:1206.6843.

---

## Summary

Conservative PC provides a **safe, cautious** variant of PC, orienting only those colliders supported unanimously by all relevant separating sets. It is ideal when avoiding false orientations is more important than maximizing orientation coverage.
