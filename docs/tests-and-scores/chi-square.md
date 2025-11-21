# Chi-Square Test

## Summary

The Chi-square test of independence is a standard contingency-table test for
**discrete** variables. In Tetrad, it is used as a CI test for categorical
variables by comparing observed counts to expected counts under independence.

## When to use

- Data are **discrete** (categorical).
- You want a classical Pearson chi-square test instead of the likelihood ratio
  (G-square) test.
- Sample sizes per cell are moderately large.

## Assumptions

- Multinomial sampling with fixed margins is approximately valid.
- Expected cell counts are not too small (a common rule of thumb is at least 5
  in most cells).
- Variables and conditioning sets are discrete with moderate arity.

## Test details (conceptual)

For each candidate independence X ⟂ Y | S:

1. Form contingency tables of counts for X and Y given each configuration of S.
2. Compute expected counts under the assumption that X and Y are independent
   given S.
3. Compute Pearson’s chi-square statistic as the sum over cells of
   (observed − expected)² / expected.
4. Use a chi-square distribution with appropriate degrees of freedom to obtain
   a p-value.

## Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `alpha`                 | Significance level (p-value cutoff) for the chi-square test of (conditional) independence. The null hypothesis is that the variables are independent given the conditioning set. P-values below `alpha` lead to rejection. Smaller values make the test more conservative (fewer edges); larger values make the graph denser. Typical range: 0.0–1.0. |
| `minCountPerCell`       | Minimum allowed count in each cell of the contingency table. If some cells fall below this threshold, the chi-square approximation becomes less reliable. Increasing this value can improve accuracy but may reduce power when sample size is small. Default is 1; minimum is 1; maximum is 1,000,000. |
| `cellTableType`         | Optimization choice for how to build contingency tables: `1 = AD Tree`, `2 = Count Sample`. This affects how counts are computed internally (data structure / performance), but should not change the numerical results. Default is 1 (AD Tree). |
| `effectiveSampleSize`   | The effective sample size to use in computing p-values. If set to `-1` (the default), the actual data sample size is used. If set to a positive integer, the test behaves as if that were the sample size, which can be useful for reweighted or subsampled data. |

## Strengths

- Widely known and understood.
- Easy to implement and interpret.
- Works well when cell counts are sufficiently large.

## Limitations

- Performs poorly with **sparse tables** (many small expected counts).
- Not appropriate for continuous data without discretization.
- As conditioning sets grow, tables can become very large and sparse.

## References

- Agresti, A. (2002). *Categorical Data Analysis* (2nd ed.). Wiley.
