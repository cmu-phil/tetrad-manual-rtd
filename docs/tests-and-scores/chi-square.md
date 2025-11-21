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

## Parameters in Tetrad

Typical parameters include:

- `alpha` — Significance level for declaring dependence.
- `depth` — Maximum conditioning set size used by the search algorithm.
- `verbose` — Whether to log details of test calls.

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
