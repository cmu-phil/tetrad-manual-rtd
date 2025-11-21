# Degenerate Gaussian BIC Score

## Summary

The Degenerate Gaussian BIC Score is a BIC-type score for **mixed discrete/continuous data**. It is designed for the case where some variables are multinomial (categorical with finitely many levels) and others are continuous. Each multinomial variable is expanded into a set of binary indicator variables (one indicator per category, with one category omitted so that the last category is implied deterministically). A multivariate **Gaussian** model is then fit to this expanded set of variables.

Because the indicator variables for a single multinomial variable are linearly dependent (their sum is constrained), the resulting joint Gaussian distribution is **degenerate**: the covariance matrix is not full rank. The Degenerate Gaussian BIC Score is implemented so that it can evaluate the likelihood and BIC **in the presence of this degeneracy**, providing a practical score for large mixed multinomial/Gaussian DAG models.

## When to use

Use the Degenerate Gaussian BIC Score when:

- You have a mixture of **multinomial (discrete)** and **continuous** variables.
- You want to use a **score-based DAG search** (for example, FGES, GRaSP, or BOSS) on mixed data.
- The discrete variables can be reasonably modeled via a Gaussian approximation on their indicator (one-hot) encodings.
- You prefer a BIC-type criterion that is relatively fast and scales to **high-dimensional mixed** problems.

If all variables are continuous and the covariance matrix is well behaved, the standard SEM BIC score is usually sufficient. The Degenerate Gaussian BIC Score is primarily intended for the mixed multinomial/Gaussian setting.

## Model class

Conceptually, the model class is:

- A **linear Gaussian DAG model** over an expanded set of variables:
    - Continuous variables appear as themselves.
    - Each multinomial variable with K categories is represented by K−1 binary indicator variables (0/1 columns), with the remaining category implied deterministically.
- The joint distribution over these expanded variables is treated as **multivariate Gaussian but possibly rank-deficient** (degenerate) because of the linear constraints among indicators.

In practice, this score is used as an **approximation** to the exact mixed multinomial/Gaussian model: instead of fitting multinomial conditional distributions directly, we fit a degenerate Gaussian model to the indicator variables and the continuous variables.

## Score form (conceptual)

The score is a BIC-type criterion of the form:

- “BIC” is approximately **two times the maximized log-likelihood** of the (local) degenerate Gaussian model,
- minus a penalty proportional to the **effective number of free parameters** times the logarithm of the (effective) sample size.

Because the covariance structure is allowed to be singular, the implementation uses linear algebra routines that can handle rank deficiency (for example, via regularization or pseudo-inverse techniques) when computing the likelihood.

## Parameters

| Parameter (camelCase)       | Description |
|-----------------------------|-------------|
| `penaltyDiscount`           | Double ≥ 0.0. The penalty multiplier “c” in the modified BIC-type criterion (for example, a score of the form 2·log-likelihood − c·k·log(N), where k is the number of free parameters and N is the sample size). Larger values impose a stronger complexity penalty and yield sparser graphs; smaller values allow denser graphs. Default is 2.0. |
| `structurePrior`            | Double ≥ 0.0. Structure prior coefficient controlling a binomial-style prior on the number of parents per node. When 0.0 (default), the score uses essentially a flat structure prior. Increasing this value encodes a stronger preference for a particular expected parent count and can bias the search toward graphs with that typical in-degree. |
| `precomputeCovariances`     | Boolean. If `true`, precomputes and caches covariance (and possibly cross-covariance) matrices used by the score. This speeds up repeated scoring at the cost of additional memory. If `false`, covariance quantities are recomputed on the fly, which saves memory but can be slower for large graphs or many score evaluations. |
| `singularityLambda`         | Double. Handles singular or nearly singular covariance matrices. If `singularityLambda > 0`, that value is added to the diagonal (a ridge term) to stabilize inverses. If `singularityLambda < 0`, a pseudoinverse is used instead. Default is 0.0. Use a small positive value when you see numerical-singularity warnings. |
| `effectiveSampleSize`       | Double > 0, or `-1`. If `-1` (default), the actual sample size N is used in the log(N) penalty term. If set to a positive value, the score behaves as if that were the sample size (for example, when you want to treat weighted or subsampled data as having a different effective N). |

## Strengths

- Handles **mixed multinomial/Gaussian** data through a unified (approximate) Gaussian framework.
- Can be much faster than fully nonparametric or exact multinomial likelihoods, especially when there are many discrete variables or categories.
- Designed to work even when the expanded indicator representation leads to **degenerate covariance matrices**.
- Integrates seamlessly with existing score-based search algorithms in Tetrad.

## Limitations

- The multinomial components are approximated via a **degenerate Gaussian model** on indicator variables, rather than using exact multinomial likelihoods. This is an approximation and may be less accurate when category probabilities are very extreme or sample sizes are very small for some configurations.
- As the number of categories and discrete parents grows, the indicator expansion can lead to many columns and potential numerical issues, making regularization important.
- Like any BIC-type score, performance depends on how well the underlying (approximate) model family matches the true data-generating process.

## References

- Andrews, B., Ramsey, J. D., & Cooper, G. F. (2019). Learning high-dimensional directed acyclic graphs with mixed data-types. In *Proceedings of the 2019 KDD Workshop on Causal Discovery* (CD@KDD 2019), PMLR 104, 4–21.
- Ramsey, J. D., Andrews, B., & Spirtes, P. (2024). *Choosing DAG models using Markov and minimal edge count in the absence of ground truth.* arXiv:2409.20187.