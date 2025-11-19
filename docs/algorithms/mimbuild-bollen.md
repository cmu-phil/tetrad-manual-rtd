# MimbuildBollen

**Category:** Latent Structure / MIM Construction  
**Type:** BlockSpec-based MIM builder (Bollen-style)

MimbuildBollen constructs a **measurement–intermediate–measurement (MIM)**
model from a set of **pure clusters** produced by TSC, FOFC, FTFC, GFFC, or BPC.
It uses *BlockSpec* constraints in the spirit of Bollen & Pearl’s measurement-model
construction rules.

This algorithm is the standard way in Tetrad to convert latent clusters into a
full latent-variable graph.

---

## Purpose

Use MimbuildBollen when:
- you have clusters of indicators (latent measurement blocks),
- you want a **latent-variable model** (not just clusters),
- you prefer a principled, SEM-style construction with interpretable loadings,
- and you want consistency with the classic SEM literature (Bollen 1989).

---

## How It Works (Conceptual)

1. Input a set of clusters identified by a latent clustering algorithm.
2. Create one latent variable for each cluster.
3. Connect each latent to its observed indicators with directed edges.
4. Apply **BlockSpec** constraints:
    - loadings within a block follow SEM identifiability conventions,
    - cross-cluster loadings are suppressed,
    - latent–latent covariances or edges are included according to the BlockSpec.
5. Output a complete MIM model with latent variables in place.

MimbuildBollen creates a measurement model only; it does not infer causal
relations among the latent variables themselves.

---

## Strengths

- Produces measurement models compatible with SEM literature.
- Provides identifiability through BlockSpec.
- Works directly with clusters from TSC/FOFC/etc.

---

## Limitations

- Requires **pure clusters**—impure indicators violate Bollen-style assumptions.
- Does not infer the *causal* structure among the latent variables.
  (Use Blocks-Test-TS + PC/BOSS/FGES/etc. for that.)

---

## Relation to Other Latent Tools

| Tool | Relationship |
|------|--------------|
| **MimbuildPca** | Alternative construction using PCA instead of BlockSpec. |
| **FactorAnalysis** | Traditional factor model; does not use clusters. |
| **Latent Clusters** | Supplies the pure clusters for MimbuildBollen. |

---

## References

- Bollen, K. A. (1989). *Structural Equations with Latent Variables*.f