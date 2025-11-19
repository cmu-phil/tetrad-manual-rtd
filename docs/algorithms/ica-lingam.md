# ICA Lingam — ICA-Based LiNGAM

**Type:** Non-Gaussian / Moment-based / ICA-based  
**Output:** DAG  
**Assumptions:** Linear SEM with independent, non-Gaussian errors

ICA-LiNGAM is the original LiNGAM algorithm. It uses **Independent Component Analysis (ICA)** to estimate the mixing matrix of a linear, non-Gaussian SEM. After ICA identifies independent components, the algorithm determines a causal ordering and constructs a fully directed DAG.

---

## Key Idea

ICA-LiNGAM assumes:

- The system is linear.
- The error terms are independent and non-Gaussian.
- The causal structure is acyclic.

Under these assumptions, the structural equation model  
X = B X + e  
can be rewritten as  
X = A e,  
where A is the mixing matrix.

Independent Component Analysis can estimate A up to:

- permutation of rows, and
- scaling of rows.

ICA-LiNGAM:

1. Runs ICA to estimate a mixing matrix.
2. Resolves the permutation that matches each independent component to the correct observed variable.
3. Rescales so diagonal entries take a standard form.
4. Converts the matrix to a causal ordering.
5. Uses that ordering to regress each variable on its predecessors, giving the DAG.

---

## When to Use

ICA-LiNGAM is appropriate when:

- The system is **linear**.
- The error terms are **non-Gaussian**.
- You want a **fully oriented DAG**.
- You are comfortable with ICA’s numerical properties.
- You want a historically established baseline method.

It is often used for:

- Biological and neuroimaging data
- Econometric or social-science modeling
- Benchmarking newer non-Gaussian methods

---

## Prior Knowledge Support

The Tetrad implementation supports:

- Required edges
- Forbidden edges
- Tier-based temporal ordering

These constraints limit which orderings ICA-LiNGAM is allowed to accept after the permutation step.

---

## Strengths

- Produces a **fully directed** DAG.
- The classic and most historically cited version of LiNGAM.
- Useful as a baseline for later non-Gaussian methods.
- Works well when ICA converges cleanly.

---

## Limitations

- Sensitive to ICA numerical instability.
- ICA results are only identifiable up to permutation and scaling, so extra steps are required to recover a correct ordering.
- Assumes no latent confounders.
- Performance degrades if noise is close to Gaussian.
- Slower and less stable than DirectLiNGAM.

---

## Key Parameters in Tetrad

| Parameter (camelCase) | Meaning |
|------------------------|---------|
| numRestarts | ICA restarts used to stabilize the solution. |
| maxIterations | Maximum ICA iterations. |
| icaAlgorithm | Choice of ICA backend (FastICA, extended-infomax, etc.). |
| useBootstrap | Whether to compute bootstrap DAGs. |
| knowledge | Required/forbidden edges and tiers. |
| verbose | Detailed diagnostic output. |

Parameters differ depending on which ICA backend is installed.

---

## Reference

**Shimizu, S., Hoyer, P. O., Hyvärinen, A., & Kerminen, A. (2006).**  
*A Linear Non-Gaussian Acyclic Model for causal discovery.*  
Journal of Machine Learning Research, 7, 2003–2030.

This is the original LiNGAM paper and the definitive source for ICA-based causal discovery.

---

## Summary

ICA-LiNGAM is the original non-Gaussian causal discovery method.  
It uses Independent Component Analysis to recover the mixing matrix of a linear SEM, resolves permutation and scaling ambiguities, produces a causal order, and constructs a fully oriented DAG.