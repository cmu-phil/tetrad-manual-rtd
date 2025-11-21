# Mimbuild PCA

**Category:** Latent Structure / MIM Construction  
**Type:** PCA-based latent-variable construction

MimbuildPca creates latent variables by applying **principal component analysis**
within each pure cluster obtained from TSC, FOFC, FTFC, GFFC, or BPC. Instead of
using BlockSpec constraints (as in MimbuildBollen), it extracts the **first
principal component** of each cluster as the latent variable.

---

## Purpose

Use MimbuildPca when:
- you have pure clusters of indicators,
- you want fast, automatic latent-variable construction,
- you prefer a data-driven approach to estimating latent scores,
- and you do not need full SEM-style loadings or identifiability constraints.

---

## How It Works (Conceptual)

1. Take each pure cluster of observed variables.
2. Perform PCA on the covariance submatrix corresponding to the cluster.
3. Extract the first principal component as the cluster’s latent variable.
4. Link this latent to all indicators with directed edges.
5. Combine the latent variables into a measurement model.

This produces a simple latent-variable representation suitable for downstream
structure learning (e.g., PC using Blocks-Test-TS).

---

## Strengths

- Very fast and robust.
- Minimal assumptions; nonparametric relative to SEM.
- Works especially well when clusters are large.

---

## Limitations

- PCA does not disentangle causal relations among latent variables.
- Does not enforce Bollen-style identifiability.
- Loadings are determined purely by variance, not causal assumptions.

---

## Relation to Other Latent Tools

- **MimbuildBollen:** More principled SEM-style alternative with BlockSpec.
- **FactorAnalysis:** Parametric model-based approach; not cluster-driven.
- **Latent Clusters:** Required input (TSC/FOFC/FTFC/GFFC/BPC).

### Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `penaltyDiscount`       | Multiplicative factor applied to the model’s complexity penalty. Lower values favor more complex latent-variable structures; higher values penalize additional parameters more strongly. Typical range: 0.1–2.0. |

---

## References

- Jolliffe, I. T. (2002). *Principal Component Analysis*.  