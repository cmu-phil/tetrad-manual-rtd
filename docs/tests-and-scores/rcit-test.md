# Random Conditional Independence Test (RCIT)

## Summary

The **Random Conditional Independence Test (RCIT)** is a **nonparametric,
kernel-based conditional independence test** designed to scale to large
datasets.

RCIT approximates kernel conditional independence testing using **random
Fourier features**, allowing it to retain much of the flexibility of kernel
methods while being **far more computationally efficient** than KCI.

RCIT tests whether  
**X ⟂ Y | S**  
by estimating conditional cross-covariances in a randomized feature space.

---

## When to use

RCIT is appropriate when:

- Relationships may be **nonlinear** or **non-Gaussian**
- Sample sizes are **large**, making KCI too slow
- You want a **general-purpose CI test** that scales well in causal discovery
- You need a practical alternative to kernel CI tests in algorithms such as
  PC, FCI, or FCIT

RCIT is often preferred over KCI for **medium to large datasets** due to its
substantially lower computational cost.

---

## Assumptions

- Data are i.i.d. samples from a joint distribution over (X, Y, S)
- Conditional independence can be captured via kernel embeddings
- Random feature approximations are sufficiently accurate for the chosen
  feature dimension

As with all CI tests, results depend on sample size and parameter choices.

---

## Test details (conceptual)

For each conditional independence query X ⟂ Y | S, RCIT:

1. Uses **random Fourier features** to approximate Gaussian kernel mappings
   for X, Y, and S.
2. Projects variables into a randomized finite-dimensional feature space.
3. Estimates the **conditional cross-covariance** between X and Y given S
   in this feature space.
4. Uses a chi-square or Gamma approximation to obtain a p-value for the null
   hypothesis of conditional independence.

By avoiding full kernel matrix construction, RCIT achieves substantial
speedups compared to KCI.

---

## Parameters

| Parameter (camelCase) | Description |
|----------------------|-------------|
| `alpha` | Significance level for the test. Smaller values make the test more conservative. |
| `rcitNumFeatures` | Number of random Fourier features used in the approximation. Larger values improve accuracy but increase runtime. |
| `rcitRegularization` | Regularization parameter added to covariance estimates for numerical stability. |
| `rcitKernelScale` | Bandwidth (scale) parameter for the underlying Gaussian kernel. |
| `rcitUseGammaApproximation` | If true, uses a Gamma approximation to the null distribution for faster computation. |

In practice, the defaults provide a good balance between accuracy and speed.

---

## Strengths

- Captures **nonlinear** and **non-Gaussian** dependencies
- **Much faster** than KCI for large sample sizes
- Scales well to high-dimensional conditioning sets
- Well suited for **large-scale causal discovery**

---

## Limitations

- Approximate: accuracy depends on the number of random features
- Less sensitive than KCI in very small samples
- Still more expensive than simple parametric CI tests

RCIT trades a small amount of statistical efficiency for a large gain in
computational efficiency.

---

## Relationship to other CI tests in Tetrad

- **KCI**: More exact, more computationally expensive
- **RCIT**: Approximate, scalable alternative to KCI
- **Fisher Z / Partial Correlation**: Fast but assumes linear-Gaussian structure
- **Basis-function tests (BF-LRT, BF-BIC)**: Efficient under additive-noise or
  basis-expansion assumptions

RCIT is a good default choice when nonlinear structure is suspected but kernel
tests are too slow.

---

## References

- Strobl, E. V., Zhang, K., & Visweswaran, S. (2019).  
  *Approximate kernel-based conditional independence tests for fast nonparametric causal discovery.*  
  Journal of Causal Inference, 7(1).

- Original implementation adapted from the **causal-learn** Python package.