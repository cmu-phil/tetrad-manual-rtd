# SEM BIC Score

## Summary

The SEM BIC Score is a **BIC-type score** for **linear structural equation
models (SEMs)** with continuous variables and Gaussian errors. It evaluates the
fit of a DAG or SEM structure by combining the log-likelihood of the implied
covariance matrix with a penalty on model complexity.

## When to use

- Data are continuous and reasonably **Gaussian**.
- You are learning a DAG or SEM using algorithms like FGES, BOSS, or GRaSP.
- You want a consistent, likelihood-based score that trades off fit and
  complexity.

## Model class

- Linear structural equation models with Gaussian noise.
- Equivalent to evaluating a DAG with linear regressions at each node.

## Score form (conceptual)

The SEM BIC Score is of the form:

    BIC = 2 * logL − k * ln(N)

where:

- `logL` is the maximized log-likelihood for the model,
- `k` is the number of free parameters (edges and variances),
- `N` is the sample size.

In Tetrad’s convention, **larger BIC values are better**.

## Parameters

| Parameter (camelCase)     | Description |
|---------------------------|-------------|
| `penaltyDiscount`         | Double ≥ 0.0. The penalty multiplier “c” in the modified BIC-type criterion (for example, a score of the form 2·log-likelihood minus c·k·log(N), where k is the number of free parameters and N is the sample size). Larger values impose a stronger complexity penalty and yield sparser graphs; smaller values allow denser graphs. Default is 2.0. |
| `semBicStructurePrior`    | Double ≥ 0.0. Structure prior coefficient specific to the SEM BIC score. When 0.0 (default), the score uses essentially a flat structure prior. Positive values encode a preference for certain in-degree patterns (for example, sparser graphs), acting as an additional prior on the number of edges or parents per node. |
| `semBicRule`              | Integer. Choice of SEM BIC rule for how likelihood differences are translated into edge decisions: `1 = Chickering`, `2 = Nandy`. The Chickering rule uses likelihood differences directly; the Nandy rule uses a transformation based on the absolute value of partial correlations in place of the raw likelihood difference. Default is 1 (Chickering). |
| `precomputeCovariances`   | Boolean. If `true`, precomputes and caches covariance (and possibly cross-covariance) matrices used by the score. This speeds up repeated scoring at the cost of additional memory. If `false`, covariances are computed on the fly, which saves memory but may be slower for large graphs or many score evaluations. Recommended: `true` for up to a few thousand variables; `false` when p is very large. |
| `singularityLambda`       | Double. Handles singular or nearly singular covariance matrices. If `singularityLambda > 0`, that value is added to the diagonal (a ridge term) to stabilize matrix inverses. If `singularityLambda < 0`, a pseudoinverse is used instead. Default is 0.0. Use a small positive value if you encounter numerical-singularity warnings. |
| `effectiveSampleSize`     | Integer > 0, or `-1`. If `-1` (default), the actual sample size N is used in the log(N) penalty term. If set to a positive value, the score behaves as if that were the sample size (for example, when treating weighted or subsampled data as having a different effective N). |

## Strengths

- Well-studied, consistent under standard regularity conditions.
- Efficient to compute using regression or covariance matrix factorizations.
- Natural choice for continuous linear DAG/SEM learning.

## Limitations

- Assumes linear-Gaussian structure; may mis-score strong nonlinear or
  non-Gaussian relationships.
- Sensitive to outliers and heteroskedasticity.
