# Basis Function Likelihood Ratio Test

## Summary

The Basis Function Likelihood Ratio Test is a flexible **nonlinear
independence test** that models conditional relationships using a basis
expansion (for example, polynomial or orthogonal basis functions). It compares
a model that includes basis expansions linking X and Y to a reduced model in
which X and Y are independent given S.

## When to use

- Data may exhibit **nonlinear** relationships not well captured by simple
  linear or Gaussian models.
- Variables are continuous (or suitably transformed) and you want a parametric
  but flexible test.
- You are using algorithms such as PC, PC-Max, or FCIT in a **nonlinear**
  setting.

## Assumptions

- The conditional relationship can be reasonably approximated by a finite basis
  expansion up to some truncation level.
- Residuals are approximately independent with finite variance (often treated
  as Gaussian for the likelihood ratio).
- Sample size is large enough to support the chosen number of basis terms.

## Test details (conceptual)

For each X ⟂ Y | S query, the test:

1. Builds a basis expansion for the regression of X on (Y, S) and for X on S
   alone (or symmetrically for Y).
2. Fits both models using maximum likelihood or least-squares methods.
3. Forms a likelihood ratio statistic comparing the full and reduced models.
4. Uses an approximate chi-square distribution for the difference in model
   dimensions to obtain a p-value.

## Parameters in Tetrad

Typical parameters include:

- `alpha` — Significance level for rejecting independence.
- Basis-related settings, such as:
  - truncation order or maximum degree,
  - choice of basis family (e.g., Legendre, Hermite, Chebyshev).
- `robustRegression` or similar options for handling outliers (if enabled in
  the implementation).

## Strengths

- Can capture a wide range of **smooth nonlinear** relationships.
- Retains a parametric framework (likelihood ratio) with clear degrees of
  freedom.
- Often more scalable than kernel-based methods (e.g., KCI) for large N.

## Limitations

- Requires choosing a **basis family** and **truncation level**.
- Performance may degrade if the basis is mis-specified or too low-order.
- Still assumes finite-dimensional parametric structure, not arbitrary
  nonparametric behavior.

## References

- The underlying ideas are related to basis-expansion approaches to nonlinear
  modeling; a dedicated Tetrad paper on this method is in preparation.
