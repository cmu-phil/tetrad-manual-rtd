# SEM Updater

The **SEM Updater** performs updating for **linear Gaussian Structural Equation Models (SEMs)**. Given an
instantiated linear SEM and specified **evidence** and **manipulations**, it computes the implied
**conditional distributions** of variables under those conditions.

It is available when the **Updater** box is connected to an **Instantiated Model** or **Estimator** that
produces a **linear SEM**.

## Purpose

- Compute **conditional means and variances** in a linear Gaussian SEM given:
    - Observed values for some variables (evidence),
    - Interventions on others (manipulations/do-operations).
- Support queries like:
    - Expected value of \(Y\) given \(X = x\),
    - Expected value of \(Y\) under \(\text{do}(X = x)\),
    - Conditional distributions of subsets of variables.

## Inputs and setup

- **Input model**: a linear SEM instantiated by an Estimator or Instantiated Model box:
    - Contains path coefficients, error variances, and possibly intercepts.
- **User-specified information**:
    - **Evidence**: observed values on some variables.
    - **Manipulations**: variables to be intervened upon (do\(X = x\)), typically removing their parents and
      fixing them at specified values.

These are set in the Updater box via fields for variable values and manipulation flags.

## How it works (conceptually)

For a **linear Gaussian** SEM, the joint distribution over all variables is multivariate normal:

\[
\mathbf{V} \sim \mathcal{N}(\mu, \Sigma),
\]

where \(\mu\) and \(\Sigma\) are implied by the SEM structure and parameters.

The SEM Updater:

1. Constructs (or uses) the implied **mean vector** \(\mu\) and **covariance matrix** \(\Sigma\).
2. Incorporates **manipulations** by:
    - Modifying the structural graph (removing incoming edges into manipulated variables),
    - Recomputing the implied \(\mu\) and \(\Sigma\) under the intervention.
3. Incorporates **evidence** by conditioning:
    - For variables partitioned as \((X, Y)\), with observed \(X = x\), it uses the multivariate normal
      conditioning formula:
      \[
      Y \mid X=x \sim \mathcal{N}(\mu_{Y\mid X}, \Sigma_{Y\mid X}),
      \]
      where
      \[
      \mu_{Y\mid X} = \mu_Y + \Sigma_{Y X} \Sigma_{X X}^{-1} (x - \mu_X),
      \]
      \[
      \Sigma_{Y\mid X} = \Sigma_{Y Y} - \Sigma_{Y X} \Sigma_{X X}^{-1} \Sigma_{X Y}.
      \]
4. Reports **conditional means and variances** (and sometimes covariances) for variables of interest.

## Output

- Conditional summaries:
    - **Means** of variables given evidence and/or manipulations.
    - **Variances** (and possibly covariances) under the same conditions.
- These can be interpreted as:
    - Predictions,
    - Effects of interventions in a linear Gaussian setting.

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