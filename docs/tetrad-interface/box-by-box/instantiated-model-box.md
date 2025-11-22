# Instantiated Model Box

```{figure} ../../_static/images/tetrad-interface/box-by-box/instantiated-model-box.png
:name: tetrad-instantiated-model-box-screenshot
:alt: Instantiated Model Box in the Tetrad interface.

Instantiated Model Box in the Tetrad interface sidebar and main panel.
```

## Purpose

The **Instantiated Model** box is where you work with **models that have been tied to data and (typically) estimated**.
Conceptually, an instantiated model =

- a **parametric model specification** (from the *Parametric Model* box),
- plus a **dataset** (from the *Data* box),
- plus a particular set of **parameter values** (often obtained via the *Estimator* box).

You use this box to:

- Store fitted models as concrete objects.
- Inspect fit statistics and parameter estimates.
- Pass the fitted models on to other tools (e.g., simulation, comparison, or effect estimation).

### Model types and fit results

Instantiated models can belong to any of the same four families as parametric models:

- Bayes (multinomial)
- SEM (linear SEM)
- Hybrid (conditional Gaussian)
- Generalized

The available fit statistics and parameter summaries depend on the model family and estimator used.
For example, SEM models may report χ², RMSEA, CFI, and BIC, while other families may expose different
summary measures.

For a concise overview of these families and their typical estimators, see:

- `Tetrad Interface → Detail Callouts → Parametric & Instantiated Model Types`

## Typical workflow

1. **Build a parametric model**
   - In the *Parametric Model* box, create a model whose structure matches your intended graph or SEM.
   - Make sure variable names match those in your dataset.

2. **Estimate the model**
   - In the *Estimator* box, select:
     - A parametric model, and
     - A dataset.
   - Run the estimator to obtain parameter estimates and fit statistics.

3. **Create an instantiated model**
   - The result of estimation can be stored as an **instantiated model**.
   - In many workflows, this happens automatically when you choose to save or keep the fitted result;
     otherwise, you may have an explicit “instantiate” step depending on the version.

4. **Inspect and reuse**
   - In the Instantiated Model box:
     - Select a model to see parameter estimates, standard errors (if available), and fit indices.
     - Use the model as input to:
       - *Simulation* (to generate synthetic data),
       - *Compare* (to compare fits across models),
       - or other tools that require fully specified, data-tied models.

## Key controls

- **Toolbar**
  - **Rename / Duplicate / Delete** – manage instantiated models.
  - **Export** – save a fitted model (and possibly its estimates) to a file, if supported.

- **Instantiated model list**
  - Shows all instantiated models currently stored in the project.
  - Each entry typically corresponds to a particular combination of:
    - Parametric model,
    - Dataset,
    - Estimation settings.

- **Main panel**
  - Displays details of the selected instantiated model, such as:
    - Parameter estimates and (optionally) standard errors.
    - Overall fit measures (e.g., χ², RMSEA, CFI, BIC), when provided by the estimator.
    - Links or summaries pointing back to the underlying data and parametric specification.

## Common patterns & tips

- Use **descriptive names** that encode:
  - The parametric model name,
  - The dataset,
  - And key estimation settings (e.g., estimator type).
- Keep both the **parametric model** and the **instantiated model** when doing model comparison:
  - The parametric model describes the form you want to test.
  - The instantiated model stores what happened for a particular dataset and estimator.
- If you re-estimate the same parametric model on different datasets (e.g., cross-validation folds or
  different populations), keep separate instantiated models for each case.

## Related pages

- `Tetrad Interface → Overview` – high-level tour of the GUI.
- Other boxes that commonly interact with **Instantiated Model**:
  - *Parametric Model* (provides the structural specification).
  - *Estimator* (produces the parameter estimates that define an instantiated model).
  - *Data* (provides the dataset to which the model is fitted).
  - *Simulation* (generates data from instantiated models).
  - *Compare* (compares multiple instantiated models by fit or structure).
