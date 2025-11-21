# PC-Max — PC with Maximum-p Collider Orientation

**Type:** Constraint-based  
**Output:** CPDAG  
**Implements:** Ramsey (2016)  
**Knowledge:** Fully supported (same as PC)

PC-Max is an enhanced collider-orientation variant of the PC algorithm. It keeps the **entire adjacency phase unchanged**, but modifies the orientation of unshielded colliders by selecting the **separating set with the maximum p-value** among all valid separating sets. This greatly reduces false collider orientations and improves arrowhead precision—especially in high-dimensional or moderate-sample settings.

In Tetrad, **PC-Max is the default configuration** of PC.

---

## Key Idea

PC-Max improves collider orientation while leaving all other PC operations unchanged.

1. **Collect all separating sets** S such that X ⟂ Z | S.  
2. **Compute p-values** for each CI test.  
3. **Choose the separating set with the maximum p-value.**  
4. **Orient X → Y ← Z** iff Y ∉ S*.

All further orientations use standard Meek rules.

---

## When to Use

- You want **higher orientation accuracy** than standard PC.
- Datasets are high-dimensional, noisy, or small-sample.
- You want a drop-in replacement for PC with no extra settings.

---

## Relation to Standard PC

- **Adjacency phase:** identical  
- **CI tests:** identical  
- **Orientation propagation:** identical except collider selection  
- **Knowledge support:** identical  
- **Output:** CPDAG  

See the **PC** page for details.

---

## Prior Knowledge Support

PC-Max inherits full background knowledge support:

- forbidden/required edges  
- temporal/tier constraints  
- partial orientations  

All constraints are enforced consistently during adjacency removal and orientation.

---

## Strengths

- Markedly fewer false colliders  
- Higher arrowhead precision  
- No additional computation  
- No new parameters  
- Tetrad’s default and recommended method

---

## Limitations

- Same as PC: assumes DAGs without latent confounding  
- Faithfulness and suitable CI tests required  
- For latent confounders, use FCI/GFCI/BOSS-FCI/FCIT

---

## Key Parameters in Tetrad

PC-Max adds **no new parameters**.  
Enabled with:

```
colliderOrientationStyle = "maxP"
```

**All other parameters match PC.**

---

## Reference

Ramsey, J. (2016).  
**Improving accuracy and scalability of the PC algorithm by maximizing p-value.**  
arXiv:1610.00378.

---

## Summary

**PC-Max = PC + maximum-p separating sets for collider identification.**  
A simple but powerful improvement that yields cleaner, more reliable CPDAG orientations.

