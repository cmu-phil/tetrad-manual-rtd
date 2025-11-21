# G-Square Test

## Summary

The G-square test (likelihood ratio chi-square) is a test of (conditional)
independence for **discrete** variables. It compares the likelihood of a model
where two variables are independent given a conditioning set S to a model where
they are allowed to depend on each other given S.

## When to use

- Variables are **discrete** (categorical).
- Sample sizes per cell are reasonably large.
- You want a standard, likelihood-based CI test for PC, CPC, FCI, RFCI, or
  other constraint-based algorithms on discrete data.

## Assumptions

- Variables are discrete with a manageable number of categories.
- Expected cell counts in the contingency tables are not too small (as for
  chi-square-type tests generally).
- The multinomial model for counts is a reasonable approximation.

## Test details (conceptual)

For each candidate independence X ⟂ Y | S, the G-square test:

1. Constructs contingency tables for X, Y, and S.
2. Compares the **log-likelihood** of the full model (X and Y possibly
   dependent given S) to the **restricted model** (X and Y independent given
   S).
3. Forms the test statistic G² = 2 * (logL_full − logL_restricted).
4. Uses an approximate chi-square distribution with degrees of freedom equal
   to the difference in the number of parameters to compute a p-value.

## Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `alpha`                 | Significance level (p-value cutoff) for the G² likelihood-ratio test of (conditional) independence. The null hypothesis is that the variables are independent given the conditioning set. P-values below `alpha` lead to rejection. Smaller values make the test more conservative (fewer edges); larger values make the graph denser. Typical range: 0.0–1.0. |
| `minCountPerCell`       | Minimum allowed count in each cell of the contingency table. If some cells fall below this threshold, the asymptotic chi-square approximation for the G² statistic becomes less reliable. Increasing this value can improve accuracy but may reduce power when sample size is small. Default is 1; minimum is 1; maximum is 1,000,000. |
| `cellTableType`         | Optimization choice for how to build contingency tables: `1 = AD Tree`, `2 = Count Sample`. This affects how counts are computed internally (data structure and performance), but should not change the numerical results. Default is 1 (AD Tree). |

## Strengths

- Standard likelihood-based test for **discrete** contingency tables.
- Works naturally with multinomial models used in discrete Bayes nets.
- Symmetric in X and Y and straightforward to interpret.

## Limitations

- Can be unreliable when **sample sizes per cell are small**.
- Complexity can grow quickly with the number of categories and conditioning
  variables.
- Not suitable for continuous variables without discretization.

## References

- Agresti, A. (2002). *Categorical Data Analysis* (2nd ed.). Wiley.
