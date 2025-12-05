# Detail: Parametric & Instantiated Model Types

This page summarizes the main model families currently supported in the **Parametric Model** and
**Instantiated Model** boxes, and how they interact with estimation and simulation.

## Model families

- **Bayes (multinomial)**  
  Discrete Bayesian networks where each variable has a finite set of states and conditional
  probability tables (CPTs). Suitable for fully discrete data.

- **SEM (linear SEM)**  
  Linear Gaussian structural equation models with path coefficients and Gaussian error terms.
  Often used for continuous data and covariance-structure analysis.

- **Hybrid (conditional Gaussian)**  
  Conditional Gaussian (CG) models that combine discrete and continuous variables:
  discrete parents with conditional linear-Gaussian distributions for continuous children.
  This corresponds to the Hybrid API we introduced in the Tetrad library.

- **Generalized**  
  A flexible framework in which the functional form and error distribution for each variable
  are specified by hand (e.g., nonlinear functions, non-Gaussian errors). This is intended for
  advanced users who need fine-grained control over the data-generating mechanism.

For more details on each family, see:

- `Tetrad Interface → Detail: Bayes (Multinomial) Parametric Model`
- `Tetrad Interface → Detail: SEM (Linear) Parametric Model`
- `Tetrad Interface → Detail: Hybrid (Conditional Gaussian) Parametric Model`
- `Tetrad Interface → Detail: Generalized Parametric Model`

- `Tetrad Interface → Detail: Bayes (Multinomial) Instantiated Model`
- `Tetrad Interface → Detail: SEM (Linear) Instantiated Model`
- `Tetrad Interface → Detail: Hybrid (Conditional Gaussian) Instantiated Model`
- `Tetrad Interface → Detail: Generalized Instantiated Model`

## Interaction with Estimator and Simulation

- Not all estimators support all model families; SEM models, for example, have specialized
  covariance-structure estimators with rich fit indices.
- Simulation from a parametric or instantiated model depends on:
    - The availability of a generative interpretation for that model family.
    - The configuration of error distributions and link functions (especially for Generalized models).

For practical guidance, see the **Parametric Model** and **Instantiated Model** box pages and the
**Simulation** box page.