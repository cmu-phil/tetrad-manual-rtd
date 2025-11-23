# Detail: Hybrid CG Estimator

The **Hybrid CG Estimator** fits a **Hybrid Conditional Gaussian (CG)
Parametric Model** to data where some variables are discrete and others are
continuous. In such models, continuous variables are typically Gaussian
**conditional on the discrete parents**, allowing mixtures of discrete and
continuous nodes in a single graphical model.

This estimator is available when the **Parametric Model** connected to the
Estimator box is a **Hybrid CG PM**.

## Purpose

- Estimate parameters in **mixed discrete–continuous graphical models**, where:
    - Discrete variables have CPTs (like in a Bayes network).
    - Continuous variables have **conditional Gaussian** distributions, with
      means/variances depending on the configuration of discrete parents.
- Provide a fitted model suitable for:
    - Simulation,
    - Prediction,
    - and comparison with alternative CG structures.

## Inputs and requirements

- **Parametric Model**: A **Hybrid CG PM** specifying:
    - Which variables are discrete vs. continuous.
    - Graph structure (parents for each node).
- **Data**:
    - Mixed data with discrete and continuous variables matching the model.
    - Sufficient samples for each discrete configuration to estimate continuous
      parameters reasonably.

- **Estimation options** (where available), such as:
    - Missing-data handling.
    - Regularization or minimum-variance safeguards for continuous parts.
    - Convergence settings if iteratively optimized.

## How it works (conceptually)

Roughly:

1. For **discrete variables**, estimate CPTs similarly to Bayes estimation
   (ML or smoothed variants, depending on the implementation).
2. For **continuous variables**:
    - For each configuration of discrete parents (and possibly continuous
      parents), fit a **Gaussian regression**:
        - Means become linear functions of continuous parents.
        - Variances (and possibly covariances) are estimated for each configuration.
3. Combine these into a coherent **hybrid CG** parameterization.

## Output

- A **fitted Hybrid CG model** specifying:
    - Discrete CPTs.
    - Conditional Gaussian parameters for continuous variables:
        - Regression coefficients,
        - Conditional variances,
        - (Where applicable) covariance structure.
- May also provide:
    - Log-likelihood,
    - Information criteria such as BIC.

The fitted model can be used as an **Instantiated Model (Hybrid CG)**.

## Tips and common issues

- Hybrid CG estimation can be **data-hungry**:
    - If discrete parents have many states, some configurations may be under-
      represented, leading to unstable estimates.
- Verify that the coding of discrete vs. continuous variables in the data
  matches the Hybrid CG PM.
- If estimation is unstable:
    - Consider simplifying the model (reducing parent sets).
    - Merge categories for discrete variables where appropriate.
    - Increase sample size if possible.

## Related pages

- `Tetrad Interface → Estimator Box`
- `Tetrad Interface → Hybrid CG Parametric Model`
- `Tetrad Interface → Instantiated Model (Hybrid CG)`
- `Tetrad Interface → Simulation (Hybrid CG)`