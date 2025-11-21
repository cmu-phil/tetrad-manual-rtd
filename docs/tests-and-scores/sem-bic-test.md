# SEM BIC Test

## Summary

The SEM BIC Test is simply the **SEM BIC Score used as a conditional-independence
decision rule**.

For each query of the form “X independent of Y given S”, the test compares
two models (or local graphs):

- a model where the edge between X and Y is **present** (given S), and
- a model where that edge is **absent**.

Both models are evaluated using the **same SEM BIC Score** (linear Gaussian
SEM likelihood plus BIC-type penalty and any chosen structure prior).  
The difference in score is then thresholded at **0**:

- if the SEM-BIC-based score difference is **less than 0**, the test treats  
  X and Y as **independent** given S;
- otherwise, it treats them as **dependent**.

There is **no explicit alpha parameter**; the decision is purely based on
whether the SEM BIC score prefers the model with or without the edge.

## When to use

- You want a CI test that is **tightly aligned** with the SEM BIC Score used
  by your search algorithm (FGES, BOSS, GRaSP, etc.).
- You are already using **[Sem BIC Score](sem-bic-score.md)** for structure
  learning and want your CI tests to reflect the same linear-Gaussian modeling
  assumptions and penalty.
- You prefer a **score-difference rule** instead of p-values.

## Relation to SEM BIC Score

The **Sem BIC Score** is a standard linear-Gaussian SEM BIC criterion, possibly
augmented with a structure prior and different penalty rules. The SEM BIC Test:

- reuses that **same score** (likelihood + BIC penalty + optional structure prior),
- evaluates a model with the edge and a model without the edge,
- then decides independence by checking whether the **score difference is
  negative (BIC < 0 threshold)**.

So, SEM BIC Test does not introduce a new model or extra parameters; it just
turns the Sem BIC Score into a CI test with a fixed **zero score-difference
threshold**.

## Test details (conceptual)

For each X, Y, and conditioning set S, the test:

1. Constructs two models:
    - `M_with`: a model (or local SEM) including the edge between X and Y
      conditioned on S.
    - `M_without`: the corresponding model with that edge removed.
2. Computes the SEM BIC Score for each model:
    - `score_with` = Sem BIC Score(`M_with`),
    - `score_without` = Sem BIC Score(`M_without`).
3. Forms the **score difference** (for example, `score_with − score_without`).
4. If this score difference is **less than 0**, then the edge is not supported
   by the SEM-BIC criterion, and the test declares:
   > X and Y are independent given S.
5. Otherwise, the test declares:
   > X and Y are dependent given S.

There is no mapping to p-values; the decision is directly based on the sign of
the BIC score difference.

### Parameters

| Parameter (camelCase)   | Description |
|-------------------------|-------------|
| `penaltyDiscount`       | Double ≥ 0.0. Penalty multiplier “c” in the BIC-type score used inside the test (for example, a score of the form 2·log-likelihood − c·k·log(N), where k is the number of free parameters and N is the sample size). Larger values impose a stronger complexity penalty and tend to favor sparser graphs; smaller values allow denser graphs. |
| `structurePrior`        | Double ≥ 0.0. Structure prior coefficient controlling a binomial-style prior on the number of parents per node. When 0.0, the test uses essentially a flat structure prior. Positive values encode a preference for certain in-degree patterns (typically sparser graphs). |
| `precomputeCovariances` | Boolean. If `true`, precomputes and caches covariance (and possibly cross-covariance) matrices used by the internal Sem BIC Score. This speeds up repeated scoring at the cost of additional memory. If `false`, covariances are computed on the fly, which saves memory but may be slower for large graphs or many CI queries. |
| `singularityLambda`     | Double. Handles singular or nearly singular covariance matrices. If `singularityLambda > 0`, that value is added to the diagonal (a ridge term) to stabilize matrix inverses. If `singularityLambda < 0`, a pseudoinverse is used instead. Default is often 0.0; use a small positive value if you encounter numerical-singularity warnings. |

## Strengths

- **Perfectly aligned** with SEM BIC: CI decisions and score search share the
  same modeling assumptions and penalty.
- No need to choose an alpha level; the decision rule is fixed at a **zero
  score-difference threshold**.
- Exploits a familiar, well-studied criterion (BIC) for CI testing in linear
  Gaussian SEMs.

## Limitations

- There is no p-value calibration; decisions are based solely on **score
  differences** and the chosen penalty and structure prior.
- The result depends on the choice of `penaltyDiscount`, `semBicStructurePrior`,
  and `semBicRule`. Very aggressive penalties can force over-sparse graphs
  (missing edges), while weak penalties can allow too many edges.
- Requires computing scores for **two models per CI query**, which can be
  more expensive than tests such as Fisher Z that only use local partial
  correlations.