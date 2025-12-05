# Detail: SEM Updater

The **SEM Updater** performs updating for **linear Gaussian Structural Equation Models (SEMs)**. Given an
instantiated linear SEM and specified **evidence** and **manipulations**, it computes the implied
**conditional distributions** of variables under those conditions.

It is available when the **Updater** box is connected to an **Instantiated Model** or **Estimator** that
produces a **linear SEM**.

```{figure} ../../_static/images/tetrad-interface/box-by-box/sem-updater.png
:name: tetrad-sem-updater-screenshot
:alt: SEM Updater

SEM Updater
```

## Purpose

- Compute **conditional means and variances** in a linear Gaussian SEM given:
    - Observed values for some variables (evidence),
    - Interventions on others (manipulations / do-operations).
- Support queries like:
    - Expected value of Y given X = x,
    - Expected value of Y under an intervention that sets X = x (often written do(X = x)),
    - Conditional distributions of subsets of variables.

## Inputs and setup

- **Input model**: a linear SEM instantiated by an Estimator or Instantiated Model box:
    - Contains path coefficients, error variances, and possibly intercepts.
- **User-specified information**:
    - **Evidence**: observed values on some variables.
    - **Manipulations**: variables to be intervened upon (do-operations), typically removing their parents and
      fixing them at specified values.

These are set in the Updater box via fields for variable values and manipulation flags.

## How it works (conceptually)

For a **linear Gaussian** SEM, the joint distribution over all variables is a **multivariate normal**
distribution. The SEM implies a particular **mean vector** (often written mu) and **covariance matrix**
(often written Sigma) for this multivariate normal.

The SEM Updater:

1. Constructs (or uses) the implied mean vector and covariance matrix from the SEM structure and parameters.
2. Incorporates **manipulations** (interventions) by:
    - Modifying the structural graph (removing incoming edges into manipulated variables),
    - Recomputing the implied mean vector and covariance matrix under the intervention.
3. Incorporates **evidence** by conditioning:
    - Conceptually, the variables are partitioned into observed variables X (with values x) and variables Y of
      interest. The updater uses the standard multivariate normal conditioning formulas to obtain the
      conditional mean and covariance of Y given X = x.
4. Reports **conditional means and variances** (and sometimes covariances) for variables of interest.

You do not need to know or enter the conditioning formulas yourself; they are handled internally by the
SEM Updater.

## Output

- Conditional summaries:
    - **Means** of variables given evidence and/or manipulations.
    - **Variances** (and possibly covariances) under the same conditions.
- These can be interpreted as:
    - Predictions under observation (what you expect to see given evidence),
    - Effects of interventions in a linear Gaussian setting (what you expect to see when variables are set by do-operations).

The underlying SEM parameters remain fixed; the Updater computes conditional distributions “on top” of them.

## Tips

- Use the SEM Updater whenever you are working with a **linear SEM** and want to ask “what-if” questions
  about interventions and observations.
- Make sure the SEM is:
    - Properly estimated (no severe Heywood cases),
    - Reasonably well-fitting; otherwise, conditional predictions may be misleading.
- When comparing conditional predictions under different scenarios:
    - Duplicate the Updater configuration and change only the evidence/manipulation values,
    - Keep the underlying SEM fixed.

## Related pages

- `Tetrad Interface → Updater Box`
- `Tetrad Interface → Instantiated Model (SEM)`
- `Tetrad Interface → SEM Estimator`
- `Tetrad Interface → Simulation (SEM)`