# Fisher Z Test

## Summary

The Fisher Z test is a parametric independence test for **continuous,
approximately Gaussian variables**. It tests whether the **partial correlation**
between two variables X and Y, conditional on a set of variables S, is zero.

## When to use

- Data are reasonably **continuous** and **approximately multivariate normal**.
- You want a fast, well-understood CI test for use in PC, CPC, FCI, RFCI,
  GFCI, and related algorithms.
- Conditioning sets can be moderately large, and you need an efficient test.

## Assumptions

- Variables are continuous and jointly approximately **Gaussian**.
- The relationship between variables can be captured by **linear partial
  correlations**.
- Sample size is large enough for the normal approximation of the Fisher
  Z-transformed correlation to be reasonable.

## Test details (conceptual)

For each candidate independence X ⟂ Y | S, the Fisher Z test:
1. Computes the **sample partial correlation** r(X, Y | S).
2. Applies the **Fisher Z transform**, z = 0.5 * ln((1 + r)/(1 - r)).
3. Uses a normal approximation for z * sqrt(N - |S| - 3) under the null
   hypothesis that the true partial correlation is zero.
4. Compares the resulting statistic to a standard normal distribution to obtain
   a p-value.

If the p-value is below a user-specified alpha level, the test rejects
independence and the edge is kept; otherwise, the edge may be removed in
constraint-based algorithms.

## Parameters

| Parameter (camelCase)    | Description |
|--------------------------|-------------|
| `alpha`                  | Significance level (p-value cutoff) for rejecting the null hypothesis of (conditional) independence. Default is 0.01. Smaller values make the test more conservative (fewer edges); larger values make the graph denser. Typically chosen between 0 and 1. |
| `shrinkageMode`          | Shrinkage mode for the covariance or correlation matrix: `1 = None`, `2 = Ridge`, `3 = Ledoit–Wolf`. Use `None` for clean, well-conditioned data; `Ridge` or `Ledoit–Wolf` can help when the covariance matrix is ill-conditioned, high-dimensional, or nearly singular. Default is `1` (None). |
| `regularizationLambda`   | Nonnegative regularization constant added to the diagonal of the covariance/correlation matrix (a small “ridge” term). Default is `1e-8`. Increasing this can improve numerical stability when matrices are nearly singular, at the cost of slightly biasing correlations toward zero. |
| `effectiveSampleSize`    | The effective sample size to use in computing p-values. If set to `-1`, the actual data sample size is used (default). If set to a positive integer, the test behaves as if that were the sample size, which can be useful for reweighted or subsampled data. |

## Strengths

- Very fast and scales well to **moderate and large graphs**.
- Theoretical properties are well understood.
- Default workhorse for many continuous-variable causal discovery workflows.

## Limitations

- Sensitive to **non-Gaussianity**, **nonlinearity**, and **strong
  heteroskedasticity**.
- Performance may degrade if there are strong nonlinear relationships or heavy
  tails.
- Not appropriate for discrete or highly mixed data without preprocessing.

## References

- Spirtes, P., Glymour, C. N., & Scheines, R. (2000).
  *Causation, Prediction, and Search* (2nd ed.). MIT Press.
