# Detail: ML Bayes Estimator

The **ML Bayes Estimator** fits a **Bayes Parametric Model** to data using
**maximum likelihood** (or equivalently, empirical relative frequencies in the
purely discrete case). It is the simplest option for estimating the conditional
probability tables (CPTs) of a Bayesian network, given fully observed data.

This estimator is available whenever the **Parametric Model** connected to the
Estimator box is a **Bayes PM** and a compatible dataset is selected.

```{figure} ../../_static/images/tetrad-interface/box-by-box/ml-bayes-estimator.png
:name: tetrad-ml-bayes-estimator-screenshot
:alt: Bayes (Multinomial) Estimator

Bayes (Multinomial) Estimator
```

## Purpose

- Estimate **CPT entries** directly from the observed data.
- Provide a **baseline** Bayesian-network fit without prior smoothing.
- Support downstream use in:
    - **Instantiated Model** (for simulation and prediction),
    - **Compare** (to compare different learned Bayes structures),
    - and other tools that rely on a fully specified Bayes model.

## Inputs and requirements

- **Parametric Model**: A **Bayes PM** specifying:
    - Nodes and their states.
    - Parent sets for each node (the graph structure).
- **Data**:
    - Typically a discrete dataset whose variables match the Bayes PM nodes.
    - Each row is treated as an i.i.d. sample.
    - Rows with missing or invalid values may be discarded or treated according to
      the Estimator’s missing-data settings (if available in your version).

## How it works (conceptually)

For each node \(X\) with parents \(\mathrm{Pa}(X)\), the ML Bayes Estimator:

1. Counts how many times each configuration of \(\mathrm{Pa}(X)\) appears.
2. For each such configuration, counts how many times each state of \(X\) occurs.
3. Forms **relative frequencies**:
   \[
   \hat{P}(X = x \mid \mathrm{Pa}(X) = \pi)
   = \frac{\text{count}(X = x, \mathrm{Pa}(X) = \pi)}
   {\text{count}(\mathrm{Pa}(X) = \pi)}.
   \]

No prior smoothing is applied, so zero-count events yield zero probabilities.

## Output

- A **fitted Bayes model** with:
    - All CPT entries filled by ML estimates.
    - (When available) basic fit information such as log-likelihood and possibly
      information criteria (e.g., BIC).
- The result can be registered as an **Instantiated Model** for:
    - Simulation,
    - Prediction,
    - or comparison with other parameterizations.

## Tips and common issues

- If the data are **sparse**, ML estimates may assign **zero probability** to
  some configurations. If this is problematic (e.g., for simulation or
  inference), consider using the **Dirichlet Estimator** instead, which adds
  prior smoothing.
- Ensure that dataset variable names and state encodings match those in the
  Bayes PM exactly.
- If estimation fails, check for:
    - Rows containing states not defined in the Bayes PM.
    - Incompatible variable types (e.g., continuous variables in a discrete model).

## Related pages

- `Tetrad Interface → Estimator Box`
- `Tetrad Interface → Bayes Parametric Model`
- `Tetrad Interface → Dirichlet Estimator`
- `Tetrad Interface → EM Bayes Estimator`
- `Tetrad Interface → Instantiated Model (Bayes)`