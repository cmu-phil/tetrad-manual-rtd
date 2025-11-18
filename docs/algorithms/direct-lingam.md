# DirectLiNGAM

**Type:** Non-Gaussian / Moment-based / Orientation  
**Output:** DAG  
**Assumptions:** Linear structural equation model + non-Gaussian independent errors

DirectLiNGAM is a version of LiNGAM (Linear Non-Gaussian Acyclic Model) that identifies a causal ordering **directly**, without using ICA. It uses asymmetries in regression residuals that arise whenever error terms are non-Gaussian. Once a causal ordering is found, the algorithm constructs the DAG by regressing each variable on its predecessors.

---

## Key Idea

LiNGAM models assume:

- The system is linear.
- The error terms are independent and non-Gaussian.
- A causal ordering exists in which each variable is a linear function of earlier variables plus a non-Gaussian noise term.

DirectLiNGAM proceeds by:

1. **Finding an exogenous variable**  
   An exogenous variable (a variable with no parents) has residuals that are independent of all other variables when each variable is regressed on it.

2. **Removing the exogenous variable**  
   Once identified, its effect is regressed out of the rest of the system.

3. **Repeating the process**  
   Each iteration finds the next variable in the causal order.

4. **Estimating the DAG**  
   After the ordering is known, each variable is regressed on all earlier variables. Nonzero coefficients correspond to directed edges.

This produces a fully oriented DAG.

---

## When to Use

DirectLiNGAM is appropriate when:

- The underlying model is **linear**.
- The noise terms are **non-Gaussian** (skewed or heavy-tailed).
- You want a **fully oriented DAG**, not just a CPDAG.
- You prefer an algorithm that avoids ICA (which can be unstable).

Especially useful for:

- Biological data (gene expression)
- Econometric and social-science data
- fMRI or other data where non-Gaussianity is expected

---

## Prior Knowledge Support

The Tetrad implementation supports:

- Required edges
- Forbidden edges
- Temporal tiers and ordering restrictions

These constraints are used while searching for the causal ordering.

---

## Strengths

- Recovers a **fully directed** causal graph.
- More numerically stable than ICA-LiNGAM.
- Does not require conditional independence tests.
- Works well in moderately high dimensions.
- Deterministic ordering search.

---

## Limitations

- Requires **linearity**.
- Requires **strong enough non-Gaussianity** to detect asymmetries.
- Not suitable when the true structure contains latent variables.
- Performance degrades if noise terms are nearly Gaussian.
- Computational cost grows with the number of variables.

---

## Key Parameters in Tetrad

| Parameter (camelCase) | Meaning |
|------------------------|---------|
| useBootstrap | Whether to compute bootstrap DAG estimates. |
| numBootstrapSamples | Number of bootstrap samples. |
| knowledge | Background knowledge such as required/forbidden edges or tiers. |
| verbose | Print detailed logs during ordering and regression. |

---

## Reference

- Shimizu, S., Hoyer, P. O., Hyvärinen, A., & Kerminen, A. (2011).  
  *DirectLiNGAM: A direct method for learning a linear non-Gaussian structural equation model.*  
  Journal of Machine Learning Research, 12: 1225–1248.

### Python implementation by the authors

A maintained Python package containing DirectLiNGAM and related methods:  
https://github.com/cdt15/lingam

---

## Summary

DirectLiNGAM is a non-Gaussian, moment-based method that identifies a causal ordering directly from asymmetries in regression residuals. It is stable, ICA-free, and ideal for linear models with independent non-Gaussian errors.