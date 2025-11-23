# Detail: SEM Estimator

The **SEM Estimator** fits a **Structural Equation Model (SEM) Parametric Model**
to continuous data, typically assuming **linear relations** with **Gaussian
errors**. It produces parameter estimates (path coefficients, variances, and
possibly means) and global fit statistics.

This estimator is available when the **Parametric Model** connected to the
Estimator box is a **SEM PM**.

## Purpose

- Estimate:
    - **Regression/path coefficients** between variables.
    - **Error variances** and possibly covariances.
    - Optionally, intercepts/means (depending on model specification).
- Provide **model fit statistics** such as:
    - χ², degrees of freedom, and p-value.
    - Additional indices like RMSEA, CFI, TLI, BIC (when available).

## Inputs and requirements

- **Parametric Model**: A **SEM PM** specifying:
    - Directed edges (structural equations),
    - (Optional) latent variables and measurement relations.
- **Data**:
    - Continuous measurements aligned with observed variables in the SEM.
    - Sufficient sample size and variance structure for identification.

- **Estimation options** (when exposed), e.g.:
    - Handling of means (with or without mean structure).
    - Missing-data method (e.g., listwise deletion, FIML).
    - Optimization tolerance and maximum iterations.
    - Robust corrections (if supported).

## How it works (conceptually)

The SEM Estimator typically:

1. Constructs an implied covariance (and mean) model from the SEM PM.
2. Finds parameters that **minimize a discrepancy function** between:
    - the observed sample covariance (and mean) structure, and
    - the model-implied covariance (and mean) structure.
3. Uses numerical optimization (e.g., ML-based) to obtain parameter estimates and
   compute fit statistics.

## Output

- **Parameter table** showing:
    - Path coefficients (regression weights).
    - Error variances and (where applicable) covariances.
    - Standard errors and test statistics (if available).
- **Fit indices**:
    - χ², df, p-value.
    - Additional indices (RMSEA, CFI, TLI, BIC, etc.), depending on the
      implementation.
- Convergence information and any warnings (e.g., non-positive definite
  covariance, Heywood cases).

The result can be stored as an **Instantiated Model (SEM)** for later use.

## Tips and common issues

- Check that the model is **identified**; non-identified models may fail to
  converge or produce unstable estimates.
- Watch for:
    - Negative error variances (Heywood cases),
    - Very large standard errors,
    - Poor fit indices suggesting misspecification.
- If problems occur:
    - Simplify the model or add constraints.
    - Check data for outliers or multicollinearity.
    - Try alternative estimation options (e.g., robust variants, different
      missing-data handling).

## Related pages

- `Tetrad Interface → Estimator Box`
- `Tetrad Interface → SEM Parametric Model`
- `Tetrad Interface → Instantiated Model (SEM)`
- `Tetrad Interface → Simulation (SEM)`