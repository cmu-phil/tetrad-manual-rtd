# CAM — Causal Additive Model

**Type:** Nonlinear / Additive Noise • Score-based (order search + regression)  
**Output:** DAG  
**Reference:** Bühlmann, P., Peters, J., & Ernest, J. (2014). *CAM: Causal additive models, high-dimensional order search and penalized regression*. Annals of Statistics.

CAM is a **nonlinear causal discovery algorithm** for **additive noise models (ANMs)**.  
It assumes each variable is generated from a sum of nonlinear functions of its parents plus independent noise.  
Tetrad includes a standalone implementation because the original R package (`CAM`) is no longer maintained on CRAN.

---

## Key Idea

CAM decomposes causal discovery into **two stages**:

1. **Order Search (High-Dimensional)**  
   - Search over variable orderings consistent with an additive SEM.  
   - Uses a score based on regression residuals to evaluate the plausibility of each order.

2. **Pruning & Refitting**  
   - Given a candidate order, regress each variable on its predecessors using **generalized additive models (GAMs)** or penalized regression.  
   - Remove weak parent relationships using a pruning step (e.g., stability selection).

This yields a **fully directed acyclic graph (DAG)** representing nonlinear causal relationships.

---

## When to Use CAM

- You expect **nonlinear causal mechanisms**, but still additive in structure.  
- Noise terms are **independent**, though not necessarily Gaussian.  
- You want a **DAG**, not a CPDAG or PAG.  
- Datasets of moderate size.  
- You prefer a **non-Gaussian regression-based ANM** method.

CAM is useful for:

- Nonlinear scientific systems  
- Gene regulatory network discovery  
- Benchmarking nonlinear SEM-based methods  
- Replacing the discontinued R CAM implementation

---

## Prior Knowledge Support

CAM in Tetrad supports:

- **Required / forbidden edges**  
- **Tier constraints** (temporal or domain-based)  
- **Variable exclusion / inclusion rules**

Knowledge constrains admissible variable orders and regressions.

---

## Strengths

- Handles **nonlinear** relationships naturally  
- Produces a **fully directed DAG**  
- Includes **pruning** for false-parent removal  
- Strong theoretical foundations for additive-noise models  
- Robust to non-Gaussian noise

---

## Limitations

- Assumes **additive** noise  
- Regression step can be computationally expensive  
- Sensitive to hyperparameters  
- Not designed for latent confounding (assumes causal sufficiency)

---

## Key Parameters in Tetrad

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `maxNumParents` | Limit on parent set size during pruning |
| `numBootstrapSamples` | Optional stability selection |
| `penalty` | Regularization strength for regression |
| `knowledge` | Background knowledge constraints |
| `verbose` | Display progress and regression diagnostics |

---

## Reference

Bühlmann, P., Peters, J., & Ernest, J. (2014).  
*CAM: Causal additive models, high-dimensional order search and penalized regression.*  
The Annals of Statistics, 42(6), 2526–2556.

---

## Summary

CAM is a **nonlinear additive-noise causal discovery algorithm** combining order search and penalized regression to produce a fully directed DAG. It serves as Tetrad’s internal replacement for the discontinued R CAM package.
