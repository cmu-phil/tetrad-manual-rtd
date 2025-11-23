# Detail: EM Bayes Estimator

The **EM Bayes Estimator** fits a **Bayes Parametric Model** using the
**Expectation–Maximization (EM)** algorithm. It is designed to handle situations
with **missing data** and, where supported, **latent structure** more robustly
than plain ML or Dirichlet estimation.

This estimator is available when the **Parametric Model** is a **Bayes PM** and
the Estimator box offers EM-based options.

## Purpose

- Estimate CPTs in the presence of **missing values**.
- Provide improved parameter estimates for models with **partially observed**
  variables.
- Use EM to alternate between:
    - **E-step:** computing expected sufficient statistics under current parameters.
    - **M-step:** updating parameters to maximize expected complete-data likelihood.

## Inputs and requirements

- **Parametric Model**: A Bayes PM.
- **Data**:
    - May contain **missing entries** for some variables.
    - Variable names and states must still be consistent with the Bayes PM.
- **EM settings** (when exposed in the GUI), such as:
    - Maximum number of iterations.
    - Convergence tolerance for changes in log-likelihood.
    - Initialization scheme (e.g., random start or ML/Dirichlet warm start).

## How it works (conceptually)

1. Initialize CPT parameters (e.g., randomly or using ML/Dirichlet).
2. **E-step**:
    - Given current parameters, compute expected counts for each CPT entry,
      integrating over missing values using the current model.
3. **M-step**:
    - Update CPT entries using the expected counts (e.g., normalized to sum to 1).
4. Repeat E–M steps until:
    - Convergence (change in log-likelihood below tolerance), or
    - Maximum iterations reached.

## Output

- A **fitted Bayes model**:
    - CPT entries reflect EM-based estimates that account for missing data.
    - Optionally, the final **log-likelihood**, number of iterations, and
      convergence status.
- Can be saved as an **Instantiated Model** and used for:
    - Simulation,
    - Inference,
    - or comparison with other estimators.

## Tips and common issues

- EM can converge to **local optima**; different initializations may give
  different solutions.
- If EM fails to converge:
    - Increase the maximum number of iterations.
    - Relax the convergence tolerance.
    - Simplify the model or inspect data for severe missingness patterns.
- EM may be slower than ML or Dirichlet estimation, especially for larger
  networks or heavily missing data.

## Related pages

- `Tetrad Interface → Estimator Box`
- `Tetrad Interface → Bayes Parametric Model`
- `Tetrad Interface → ML Bayes Estimator`
- `Tetrad Interface → Dirichlet Estimator`
- `Tetrad Interface → Instantiated Model (Bayes)`