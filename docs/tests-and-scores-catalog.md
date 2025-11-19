# Tests and Scores: A Catalog

Many Tetrad structure-learning algorithms rely on:

- an **independence test** (used by constraint-based algorithms such as PC, CPC, FCI, RFCI, PCMCI), and
- a **score** (used by score-based and hybrid algorithms such as FGES, BOSS, GRaSP, IMaGES, GFCI, FCIT).

This page explains the wrappers in:

- `edu.cmu.tetrad.algcomparison.independence`
- `edu.cmu.tetrad.algcomparison.score`

which are the selectable “Tests” and “Scores” in the Tetrad GUI.

---

## Independence Tests

Package: `edu.cmu.tetrad.algcomparison.independence`

These are the available CI tests, grouped by data type and modeling assumptions.

### Independence Tests Overview

| Name | Appropriate Data Type | Corrected Description |
|------|-----------------------|------------------------|
| **FisherZ** | Continuous (linear-Gaussian) | Fisher Z partial correlation test. Assumes linear relationships and Gaussian (or approximately Gaussian) residuals. Default for continuous data. |
| **GSquare** | Discrete (categorical) | Likelihood-ratio G test for discrete conditional independence. Default choice for purely discrete data. |
| **ChiSquare** | Discrete (categorical) | Pearson chi-square test for discrete CI; similar to GSquare but uses chi-square statistic. |
| **BasisFunctionLrt** | Mixed continuous/discrete; nonlinear continuous effects | LRT using truncated basis expansions (Legendre, Chebyshev, Hermite, etc.) for the continuous parts of a conditional Gaussian model. Supports nonlinear additive effects through basis expansions while allowing discrete parents. |
| **ConditionalGaussianLrt** | Mixed continuous/discrete | Classical CG CI test: continuous variables are linear-Gaussian conditional on configurations of discrete parents. Discrete variables are modeled with multinomial logistic regression. |
| **DegenerateGaussianLrt** | Mixed continuous/discrete, possibly rank-deficient | CG CI test that tolerates singular or nearly singular covariance blocks. Used when mixed CG assumptions hold but covariance matrices are degenerate because of collinearity or small sample size. |
| **CciTest** | Continuous (additive noise models) | Conditional Correlation Independence (CCI). Detects conditional independence under additive noise models where Y = f(X) + e. Often useful in nonlinear, non-Gaussian settings without full kernel methods. |
| **Kci** | Continuous (general nonlinear) | Kernel Conditional Independence test. Fully nonparametric; no linearity or Gaussian assumptions. More computationally expensive. |
| **PoissonBicTest** | Continuous with linear non-Gaussian (Poisson-like) residuals | Test for CI using Poisson regression with BIC. Useful for continuous variables modeled with Poisson log-link (linear non-Gaussian models, count-ish behavior). |
| **MultinomialLogisticRegressionWald** | Discrete multinomial response | Wald-type test using multinomial logistic models. Suitable for CI when the dependent variable is discrete with more than two categories. |
| **Mvplrt** | Mixed or continuous | Likelihood-ratio CI test from multivariate projection regressions. Compares full vs. restricted projection models. |
| **MSeparationTest** | Graph-based (no data) | “Test” that answers CI queries using m-separation in a given graph. Used when treating a known DAG/MAG/PAG as the oracle (simulation studies). |
| **ProbabilisticTest** | Any; Bayesian | Uses Bayesian sampling over conditional distributions to infer CI probabilistically. Useful for probabilistic or likelihood-based independence assessment. |

**Interfaces not included:**  
`IndependenceWrapper` and `TakesGraph` are interfaces and do not appear as user-selectable tests.

---

## Scores

Package: `edu.cmu.tetrad.algcomparison.score`

These are the scores used by score-based and hybrid search methods.

### Scores Overview

| Name | Appropriate Data Type | Corrected Description |
|------|------------------------|------------------------|
| **SemBicScore** | Continuous (linear-Gaussian) | Standard DAG BIC for linear SEMs. Default for FGES, BOSS, GRaSP, IMaGES, and hybrids. |
| **DiscreteBicScore** | Discrete | BIC for discrete Bayesian networks with multinomial CPDs. |
| **BdeuScore** | Discrete | Bayesian Dirichlet Equivalent Uniform (BDeu) score. Fully Bayesian alternative to discrete BIC. |
| **ConditionalGaussianBicScore** | Mixed continuous/discrete | CG BIC score: continuous nodes are linear-Gaussian conditional on discrete parent configurations. |
| **DegenerateGaussianBicScore** | Mixed continuous/discrete, possibly rank-deficient | CG BIC variant adapted for degenerate covariance blocks, allowing singular/near-singular Gaussian components. |
| **MagDgBicScore** | Mixed-graph structures, mixed Gaussian | Degenerate Gaussian BIC adapted to MAGs (latent confounding encoded in mixed graphs). |
| **BasisFunctionBicScore** | Mixed continuous/discrete; nonlinear continuous effects | BIC score for conditional Gaussian models where continuous variables are represented using basis expansions (polynomials or orthogonal bases). Nonlinear additive models become linear in the basis. |
| **EbicScore** | Continuous | Extended BIC for linear Gaussian models. Adds sparsity penalty; useful in high-dimensional settings. |
| **GicScores** | Continuous or mixed | Generalized Information Criterion (GIC) family for flexible penalty structures. |
| **MSepScore** | Latent blocks / clustered indicators | Score defined on measurement blocks using trek-/m-separation structure. Used for latent-variable search after clustering. |
| **MVPBicScore** | Mixed projections | BIC score for mixed-variable projection models. Useful for pipelines using projection-based covariance modeling. |
| **PoissonPriorScore** | Continuous with Poisson-like noise | Prior score for linear non-Gaussian models where noise is approximated by Poisson or Poisson-like distributions. |
| **ZhangShenBoundScore** | Continuous | Score with additional Zhang–Shen-type penalties for stronger complexity control than BIC. |

---

## How Tests and Scores Are Used in Algorithms

- **Constraint-based algorithms** (PC, CPC, RFCI, FCI, PCMCI) take **any independence test** listed above.
- **Score-based algorithms** (FGES, BOSS, GRaSP, SP, IMaGES) take **any score** listed above.
- **Hybrid algorithms** (GFCI, GRaSP-FCI, BOSS-FCI, SP-FCI, FCIT) use both:
    - a score to propose or prune adjacencies, and
    - a CI test for collider orientation or selective FCI-style checking.

In the Tetrad GUI:

1. Choose an algorithm.
2. Choose a test and/or score appropriate to the data type (continuous, discrete, mixed, non-Gaussian, nonlinear).
3. Optionally tune parameters such as `alpha`, penalty discount, prior equivalent sample size, or truncation level.

This page can later be expanded with **individual per-test** and **per-score** documentation pages.