# Detail: SEM (Linear) Instantiated Models

This page describes **SEM (linear)** instantiated models in the
**Instantiated Model** box. These are **linear Gaussian structural equation
models that have been fitted to data**, starting from a SEM parametric model.

An instantiated SEM model contains:

- A **graph structure** (often a DAG or SEM-style graph).
- **Estimated path coefficients** for each directed edge.
- **Estimated error variances** (and possibly covariances).
- A set of **global fit indices** and diagnostics, when available.

## How SEM instantiated models are created

1. In the **Parametric Model** box, create a **SEM (linear)** model whose
   structure matches the SEM graph you want to test.
2. In the **Estimator** box, select:
   - The SEM parametric model, and
   - A continuous dataset (from the *Data* box).
3. Choose a SEM estimator (e.g., maximum likelihood).
4. Run the estimator; the result is a **fitted SEM**.
5. Save or send this fitted result to the **Instantiated Model** box.

Each instantiated SEM is tied to a particular dataset and estimation run.

## Instantiated Model box layout (SEM)

When you select a SEM instantiated model, the main panel typically displays:

- A **parameter table** with:
  - Estimated regression/path coefficients.
  - Standard errors and test statistics (when computed).
  - Estimated error variances (and covariances if allowed).
- **Global fit measures**, such as:
  - \(\chi^2\) and degrees of freedom.
  - RMSEA, CFI, SRMR, BIC, and related indices (depending on implementation).
- Possibly **residual information**, such as:
  - Residual covariance matrices.
  - Modification indices (in some versions).

This view is read-only with respect to the estimates; to change the model or
estimator you return to the Parametric Model and Estimator boxes.

## Typical uses

SEM instantiated models are useful when you want to:

- **Assess model fit** using standard SEM diagnostics.
- **Compare multiple SEMs** (e.g., nested models, alternative structures)
  based on fit indices or likelihood.
- **Simulate continuous data** from a fitted SEM using the *Simulation* box.

## Tips

- Check that the model is **identified**; poor identification can show up as
  huge standard errors or unstable estimates.
- When comparing models, keep the corresponding parametric models around so you
  can easily see the structural differences that led to different fits.
