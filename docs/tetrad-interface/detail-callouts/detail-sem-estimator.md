# Detail: SEM (Linear) Estimator

The **SEM (Linear) Estimator** fits a **Structural Equation Model (SEM)
Parametric Model** to continuous data, assuming **linear relations** with
**Gaussian errors**. It produces parameter estimates (path coefficients,
variances, and possibly means) and global fit statistics.

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

The SEM (Linear) Estimator typically:

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

## File menu options (SEM Estimator)

The **File** menu of the SEM (Linear) Estimator provides several ways to export
or reuse the fitted model and its matrices:

- **Save SEM as XML**  
  Saves the fitted SEM in Tetrad’s **XML format**, including the graph
  structure, estimated parameters, and error (co)variances. This XML can be
  reloaded into Tetrad as an instantiated SEM or processed by external tools.

- **Copy Implied Covariance Matrix**  
  Copies the **model-implied covariance matrix** \(\hat\Sigma\) of the fitted
  SEM to the system clipboard as tabular text. You can paste this into a
  spreadsheet, R, Python, or another program.

- **Copy Coefficient Matrix**  
  Copies the matrix of **regression/path coefficients** (the structural
  coefficient matrix) to the clipboard as tabular text.

- **Copy Error Covariance Matrix**  
  Copies the **residual/error covariance matrix** to the clipboard as tabular
  text.

- **Save Graph Image…**  
  Saves an image of the SEM graph corresponding to the fitted parametric model.
  This is useful for including the estimated model in papers, slides, or
  reports.

- **Save SEM as Lavaan**  
  Saves the fitted SEM as **lavaan model syntax** in a `.lav` file.  
  When you choose this option, a dialog lets you select:

    - Whether to **include intercepts** (`Y ~ c*1`),
    - Whether to **include residual variances** (`Y ~~ v*Y`),
    - Whether to **include residual covariances** (`Y ~~ c*Z`),
    - And whether to **fix parameters** to their current values or export them as
      **lavaan `start()` values** for re-estimation.

  The resulting `.lav` file can be read directly in R using the `lavaan`
  package, for example:

  ```r
  model <- readLines("sem-im.lav")
  fit   <- lavaan::sem(model, data = mydata)