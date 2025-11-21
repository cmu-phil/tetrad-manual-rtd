# Degenerate Gaussian Likelihood Ratio Test

## Summary

The Degenerate Gaussian Likelihood Ratio Test is a conditional independence test for **mixed discrete/continuous data**. It is paired with the Degenerate Gaussian BIC Score and uses the same modeling idea: discrete multinomial variables are expanded into sets of binary indicator variables, and a (possibly rank-deficient) **Gaussian model** is fit to these expanded variables.

Conditional independence of X and Y given a conditioning set Z is assessed by comparing two degenerate Gaussian models on the expanded variables:

- a **full model** in which X and Y may be dependent given Z, and
- a **restricted model** in which X and Y are constrained to be conditionally independent given Z.

The difference in maximized log-likelihoods defines a likelihood-ratio statistic, which is converted into a p-value under a chi-square approximation and compared to a user-specified significance level `alpha`.

## When to use

Use the Degenerate Gaussian Likelihood Ratio Test when:

- Your data contain both **multinomial (discrete)** and **continuous** variables.
- You want a relatively fast, parametric conditional independence test suitable for large mixed-data graphs.
- You are comfortable modeling discrete variables via **indicator encodings** and a degenerate Gaussian approximation.
- You intend to run constraint-based or hybrid algorithms (for example, PC, FCI variants, or FCIT-style methods) on mixed data.

If all variables are continuous and the covariance matrix is well conditioned, Fisher Z or related Gaussian tests may be simpler. The degenerate Gaussian test is primarily designed for the mixed multinomial/Gaussian case.

## Assumptions

- Each multinomial variable with K categories is represented by K−1 binary indicator variables (0/1 columns), with the last category implied deterministically.
- Continuous variables are used as-is.
- The joint distribution of all expanded variables is approximated by a **multivariate Gaussian distribution that can be rank-deficient** (degenerate) because of linear constraints among indicators.
- Conditional independence is encoded as the absence of certain regression coefficients (or equivalently, as constraints on the covariance structure) in this degenerate Gaussian model.

## Test details (conceptual)

For a given triple (X, Y, Z):

1. **Expand discrete variables**  
   For all variables involved in the local models for X and Y (including parents in the conditioning set Z), replace each multinomial variable with its set of binary indicator variables.

2. **Fit full models**  
   Fit the relevant local degenerate Gaussian models that allow X and Y to depend on each other (given Z) and compute the maximized log-likelihood `logL_full`.

3. **Fit restricted models**  
   Fit the corresponding models under the restriction that X and Y are conditionally independent given Z, obtaining `logL_restricted`.

4. **Form the likelihood-ratio statistic**  
   The test statistic is proportional to the difference `logL_full − logL_restricted`, scaled by 2.

5. **Approximate null distribution**  
   Under the null hypothesis that X and Y are conditionally independent given Z, the test statistic is approximated by a chi-square distribution with degrees of freedom equal to the difference in the effective number of parameters between the two models.

6. **Decision rule**  
   A p-value is computed from this chi-square approximation and is compared to the user-specified significance level `alpha`. If the p-value is less than `alpha`, the null of conditional independence is rejected.

Internally, the test uses linear algebra routines capable of handling **singular or nearly singular** covariance structures created by the indicator expansion.

## Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `alpha`                 | Significance level (p-value cutoff) for the likelihood-ratio test of conditional independence. The null hypothesis is that the variables are conditionally independent given the conditioning set. P-values below `alpha` lead to rejection. Smaller values make the test more conservative (fewer edges); larger values make the graph denser. Typical range: 0.0–1.0. |
| `singularityLambda`     | Double. Handles singular or nearly singular covariance matrices. If `singularityLambda > 0`, that value is added to the diagonal (a ridge term) to stabilize inverses. If `singularityLambda < 0`, a pseudoinverse is used instead. Default is 0.0. Use a small positive value if you encounter numerical-singularity warnings. |
| `effectiveSampleSize`   | Double > 0, or `-1`. If `-1` (default), the actual sample size N is used when computing test statistics and chi-square approximations. If set to a positive value, the test behaves as if that were the sample size (for example, when you want to treat weighted or subsampled data as having a different effective N). |

## Strengths

- Provides a **parametric, likelihood-ratio-based** conditional independence test for mixed multinomial/Gaussian data.
- Avoids the need to fit full multinomial conditional distributions by working with a degenerate Gaussian approximation on indicator variables.
- Typically faster than nonparametric or fully multinomial tests in high dimensions or with many discrete variables.
- Designed to integrate with the Degenerate Gaussian BIC Score so that tests and scores are conceptually aligned.

## Limitations

- The test relies on a **Gaussian approximation** to multinomial structure via indicator variables. When cell counts are very small or category probabilities are highly unbalanced, this approximation may be inaccurate.
- The indicator expansion can increase dimensionality and magnify numerical issues, making the choice of `singularityLambda` important in practice.
- The chi-square approximation for the likelihood-ratio statistic is asymptotic and may be less reliable in small samples.

## References

- Andrews, B., Ramsey, J. D., & Cooper, G. F. (2019). Learning high-dimensional directed acyclic graphs with mixed data-types. In *Proceedings of the 2019 KDD Workshop on Causal Discovery* (CD@KDD 2019), PMLR 104, 4–21.
- Ramsey, J. D., Andrews, B., & Spirtes, P. (2024). *Choosing DAG models using Markov and minimal edge count in the absence of ground truth.* arXiv:2409.20187.