# Detail: Generalized SEM Estimator

The **Generalized SEM Estimator** fits a **Generalized SEM Parametric Model**,
allowing for **non-Gaussian outcomes** (such as binary or count variables) and
a variety of **link functions** (e.g., logistic, probit, log link). It extends
the classical SEM framework to a broader family of response types.

This estimator is available when the **Parametric Model** connected to the
Estimator box is a **Generalized SEM PM**.

```{figure} ../../_static/images/tetrad-interface/box-by-box/generalized-sem-estimator.png
:name: tetrad-beneralized-sem-estimator-screenshot
:alt: Generalized SEM Estimator

Generalized SEM Estimator
```

## Purpose

- Estimate structural relations in models where:
    - Some variables are binary, ordinal, or counts.
    - Different nodes may use different link functions and distributions.
- Provide parameter estimates and fit measures appropriate for generalized
  linear/SEM-type models.

## Inputs and requirements

- **Parametric Model**: A **Generalized SEM PM** specifying:
    - Which variables are treated with which distribution/link (e.g., logistic
      for binary, Poisson for counts).
    - Structural relations between variables (regressions, latent variables, etc.).
- **Data**:
    - Variables conforming to the specified distributions.
    - Sufficient variation across categories and ranges.

- **Estimation options** (when available), such as:
    - Choice of link functions (if configurable).
    - Optimization method and convergence tolerance.
    - Handling of missing data.
    - Maximum number of iterations.

## How it works (conceptually)

The estimator typically:

1. For each endogenous variable, sets up a **generalized linear model** (GLM) or
   related component consistent with the generalized SEM specification.
2. Uses iterative procedures (e.g., **iteratively reweighted least squares** or
   other gradient-based methods) to jointly estimate parameters across the
   system, respecting cross-equation constraints and latent structure, if
   present.
3. Computes:
    - Parameter estimates,
    - Standard errors (if available),
    - Overall or per-component fit statistics.

## Output

- **Parameter estimates**:
    - Regression coefficients on the scale of the chosen link function.
    - Variance components or dispersion parameters, when applicable.
- **Fit information**, which may include:
    - Log-likelihood,
    - Information criteria (AIC, BIC),
    - Convergence diagnostics.
- The fitted model can be stored as an **Instantiated Model (Generalized SEM)**.

## Tips and common issues

- Ensure that the **variable coding** (e.g., 0/1 for binary) matches the
  distribution and link choices.
- Check convergence diagnostics; generalized SEMs can be more numerically
  demanding than standard SEMs.
- If estimation fails or yields extreme parameter values:
    - Inspect for separation in binary outcomes or very low counts.
    - Consider simplifying the model or changing link functions.
    - Verify that the data support the specified distributional assumptions.

## Related pages

- `Tetrad Interface → Estimator Box`
- `Tetrad Interface → Generalized SEM Parametric Model`
- `Tetrad Interface → Instantiated Model (Generalized SEM)`
- `Tetrad Interface → Simulation (Generalized SEM)`