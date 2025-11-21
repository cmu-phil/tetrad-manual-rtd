# Basis Function Likelihood Ratio Test

## Summary

The Basis Function Likelihood Ratio Test is a flexible nonlinear conditional-independence test using finite basis expansions. It supports **continuous**, **categorical**, and **mixed** data by expanding:

- continuous variables using polynomial/orthogonal basis functions, and
- discrete variables using indicator basis functions.

It compares a full model (X depends on Y and S) to a reduced model (X depends only on S) using a likelihood ratio statistic.

## When to use

- Relationships may be **nonlinear** or **smooth but non-Gaussian**.
- Dataset includes **mixed variable types**.
- You want a parametric and scalable test for PC, PC-Max, BOSS-FCI, FCIT, or other nonlinear workflows.

## Assumptions

- Conditional means can be approximated with a finite set of basis functions.
- Errors have finite variance (typically treated as independent Gaussian for the LRT).
- Sufficient sample size to fit full and reduced models.

## Test details (conceptual)

To test X ⟂ Y | S:

1. Expand all variables (continuous + discrete) into basis functions up to the truncation limit.
2. Fit:
    - **full model**: X ~ basis(Y, S)
    - **reduced model**: X ~ basis(S)
3. Compute the likelihood ratio statistic.
4. Use a chi-square approximation (difference in number of basis terms) to obtain a p-value.
5. Compare p-value to `alpha`.

## Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `alpha`                 | Significance level for rejecting conditional independence. |
| `truncationLimit`       | Maximum degree/order for continuous-variable basis functions. |
| `singularityLambda`     | Ridge parameter for handling nearly singular basis regression matrices (or negative for pseudoinverse). |

## Strengths

- Works with **mixed continuous/discrete data** without pre-discretization.
- Captures **nonlinear** relationships missed by Fisher-Z or discrete tests.
- More scalable than kernel methods (e.g., KCI) for large N.

## Limitations

- Requires selecting basis type and truncation level.
- May underperform if true relationships require richer bases than provided.

## References

- Ramsey, J., Andrews, B., & Spirtes, P. (2025). *Scalable causal discovery from recursive nonlinear data via truncated basis function scores and tests.* arXiv:2510.04276.