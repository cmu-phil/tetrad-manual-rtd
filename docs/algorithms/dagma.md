# DAGMA — Learning DAGs via M-Matrices and Log-Determinant Acyclicity

**Type:** Score-based, continuous optimization  
**Output:** DAG or CPDAG (depending on settings)

**DAGMA** (Bello, Aragam & Ravikumar 2022) is a continuous optimization method for learning **directed acyclic graphs** using a smooth, differentiable characterization of acyclicity based on **M-matrices** and **log-determinant penalties**. DAGMA directly optimizes a penalized likelihood objective under an exact acyclicity constraint, producing a weighted adjacency matrix whose thresholded structure represents a DAG. Tetrad’s implementation follows the original optimization loop closely and provides an option to convert the learned DAG into a CPDAG.

---

## Key Idea

DAGMA replaces the combinatorial acyclicity constraint with a **log-determinant characterization**:

- A matrix corresponds to a DAG iff a certain **M-matrix** constructed from it has **positive diagonal and nonpositive off-diagonals** and satisfies log-determinant conditions.
- DAGMA optimizes:
  - a least-squares likelihood term,
  - an L1 sparsity penalty,
  - plus a smooth acyclicity penalty.
- Optimization uses **ADAM** with continuation over:
  - decreasing central-path parameter μ,
  - a sequence of increasing s-values defining different M-matrices.

The result is a continuous weight matrix W that is then thresholded and optionally closed under Meek rules.

---

## When to Use

Use DAGMA when:

- You want a **purely score-based**, continuous optimization method for DAG learning.
- Data are **continuous**, reasonably large N, and roughly linear-Gaussian or linear-non-Gaussian.
- You prefer a **DAG** rather than CPDAG output.
- You want an alternative to NOTEARS, GraNDAG, GOLEM, or BOSS for continuous DAG learning.

Avoid DAGMA when:

- You need **latent-variable** handling.
- You need strict **knowledge constraints** (forbidden/required edges) — DAGMA does *not* support these.
- Data are strongly nonlinear or heavy-tailed (FASK, DirectLiNGAM, or nonlinear algorithms may be preferable).

---

## Prior Knowledge Support

**Does DAGMA accept background knowledge?**  
**No.**  
The current implementation in Tetrad **does not** honor:

- forbidden edges,
- required edges,
- tier/temporal constraints, or
- structural priors.

---

## Strengths

- Continuous optimization → **fast** for moderate dimensionality.
- Exact acyclicity.
- Often produces **clean, sparse DAGs**.
- No need for CI tests — works well when CI tests are unreliable.

---

## Limitations

- **No support for background knowledge**.
- Requires tuning of several optimization parameters.
- Sensitive to covariance estimation; works best with large N.
- Optimization can fail or slow down for high-dimensional, noisy datasets.

---

## Key Parameters in Tetrad

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `lambda1` | L1 sparsity penalty on edge weights. |
| `wThreshold` | Initial threshold for pruning small weights. |
| `cpdag` | Output CPDAG if true; otherwise return DAG. |

---

## Reference

Bello, K., Aragam, B., & Ravikumar, P. (2022).  
**DAGMA: Learning DAGs via M-Matrices and a Log-Determinant Acyclicity Characterization.**  
*NeurIPS 2022*, 35, 8226–8239.

---

## Summary

DAGMA is a smooth, score-based DAG learning algorithm enforcing exact acyclicity using M-matrix log-determinant constraints. It produces clean DAGs without CI tests but does **not** support knowledge constraints in Tetrad.
