# Detail: Simulation types

Tetrad includes several built-in simulators for generating synthetic
data from a known causal model. These are mainly used for:

-   testing algorithms on data where the "true" graph is known,
-   sanity-checking modeling assumptions (linearity, additivity,
    discreteness, Gaussianity),
-   benchmarking and debugging search and estimation code.

Most simulators follow the same high-level pattern:

1.  Generate (or accept) a graph, usually a DAG.
2.  Assign a structural equation or conditional distribution to each
    node.
3.  Sample exogenous noise terms (or latent randomness).
4.  Generate samples in a valid causal (topological) order (or, for time
    series, in temporal order).
5.  Return a dataset (continuous, discrete, mixed, or time series).

Below are the main simulation types available in Tetrad, what they
assume, and when to use them.

------------------------------------------------------------------------

## Bayes net

**Use when:** you want fully discrete data generated from a DAG using
conditional probability tables (CPTs).

**What it generates** - All variables are discrete. - Each node is
sampled from a multinomial distribution conditional on its parents'
discrete states. - The local conditional distribution is represented as
a CPT (or an equivalent discrete parameterization).

**Conceptual form** For each node X_i with parents Pa(i), P(X_i \|
X_Pa(i)).

------------------------------------------------------------------------

## Linear structural equation model

**Use when:** you want a classic linear SEM-style simulator.

**What it generates** - Continuous variables. - Linear relationships
between variables. - Either Gaussian or non-Gaussian noise.

**Model form** X_i = sum\_{j in Pa(i)} b\_{ij} X_j + E_i.

**Noise structure** - **Gaussian case:** the error terms E_i may be
specified with a full covariance matrix, allowing errors to be
statistically dependent. - **Non-Gaussian case:** the error terms E_i
are mutually independent.

**Notes** - Allowing correlated Gaussian errors makes this simulator
suitable for modeling latent confounding at the noise level. - With
independent non-Gaussian noise, the model aligns more closely with
assumptions used in some identifiability results.

------------------------------------------------------------------------

## Linear Fisher model

**Use when:** you want large linear datasets generated using a
stimulate-then-settle (equilibrium) mechanism.

**What it generates** - Continuous data. - Linear dependencies.

**Conceptual behavior** - The system is repeatedly stimulated with
noise. - Variables are updated according to linear relations. -
Iteration continues until values settle to equilibrium. - The settled
values are recorded as observations.

------------------------------------------------------------------------

## Nonlinear additive SEM (CAM)

**Use when:** you want nonlinear causal mechanisms with **additive
contributions from parents**, following the Causal Additive Model (CAM)
framework of Peters et al.

**What it generates** - Continuous data. - Each parent contributes
additively, but possibly nonlinearly. - Noise is additive and
independent.

**Model form** X_i = sum\_{j in Pa(i)} f\_{ij}(X_j) + E_i,

where each f\_{ij} is a univariate nonlinear function and E_i is an
independent noise term.

**Notes** - This is more structured than a general additive-noise model
because the nonlinearity is decomposed parent-by-parent. - Many
theoretical results in nonlinear causal discovery are stated for this
model class.

------------------------------------------------------------------------

## General noise SEM

**Use when:** you want a flexible nonlinear simulator that does not
enforce additive noise.

**What it generates** - Continuous data. - Nonlinear mechanisms where
noise can enter the function in a general way.

**Model form** X_i = f_i(X_Pa(i), E_i),

where E_i is an exogenous noise term that is independent across nodes
but not required to appear additively.

**Notes** - Noise may interact with parent variables inside
nonlinearities. - This simulator is useful for stress-testing robustness
beyond additive-noise assumptions.

------------------------------------------------------------------------

## Additive noise SEM

**Use when:** you want a general additive-noise model without the CAM
restriction of additive parent contributions.

**What it generates** - Continuous data. - A (possibly multivariate)
nonlinear function of all parents, plus additive noise.

**Model form** X_i = f_i(X_Pa(i)) + E_i,

where E_i is independent noise.

**Contrast with nonlinear additive SEM (CAM)** - CAM: sum of univariate
functions, one per parent. - Additive noise SEM: a single (possibly
multivariate) nonlinear function of all parents.

------------------------------------------------------------------------

## Lee and Hastie

**Use when:** you want simulated mixed continuous and discrete data
following the Lee and Hastie framework.

**What it generates** - A mix of discrete and continuous variables. -
Structured conditional distributions ensuring coherent mixed-type
behavior.

**Conceptual behavior** - Discrete parents of continuous children
primarily affect distributional parameters (e.g., the mean). -
Continuous parents influence continuous children in a regression-like
way. - Discrete children are generated from appropriate discrete
conditional models.

------------------------------------------------------------------------

## Conditional Gaussian

**Use when:** you want mixed discrete/continuous data from a conditional
Gaussian model.

**What it generates** - Variables designated as discrete or
continuous. - Continuous variables are Gaussian conditional on discrete
parent configurations.

**Conceptual form** X_i \| (D=d, C=c) \~ N(mu(d,c), Sigma(d)),

with mu often linear in c for each discrete configuration d.

------------------------------------------------------------------------

## Time series

**Use when:** you want temporally ordered data with lagged dependencies.

**What it generates** - Time-indexed variables. - Dependencies across
time lags.

**Conceptual form** X_i(t) = f_i({X_j(t-l)}) + E_i(t),

where l ranges over specified lags and E_i(t) are innovation terms.

------------------------------------------------------------------------

## Choosing a simulator

-   Discrete only: Bayes net
-   Linear continuous: Linear structural equation model or Linear Fisher
    model
-   Nonlinear additive (parent-wise): Nonlinear additive SEM (CAM)
-   Nonlinear additive (general): Additive noise SEM
-   Nonlinear with general noise injection: General noise SEM
-   Mixed discrete/continuous: Lee and Hastie or Conditional Gaussian
-   Temporal structure: Time series
