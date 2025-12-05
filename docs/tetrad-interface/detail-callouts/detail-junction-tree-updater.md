# Detail: Junction Tree Updater

The **Junction Tree Updater** is the default updater for **discrete** models. It performs **exact Bayesian
updating** on an instantiated discrete model, given specified **evidence** (observed variable values) and
**manipulations** (interventions).

It is available when the **Updater** box is connected to an **Instantiated Model** (IM) or **Estimator** that
produces a **discrete Bayesian model**.

```{figure} ../../_static/images/tetrad-interface/box-by-box/junction-tree-updater.png
:name: tetrad-junction-tree-updater-screenshot
:alt: Junction Tree Updater

Junction Tree Updater
```

## Purpose

- Compute **posterior distributions** for query variables given:
    - Observations on some variables,
    - Manipulations/interventions on others.
- Support “learning from data” within a **fixed model**:
    - The structure and CPTs come from the IM/Estimator,
    - The Updater propagates new information through the graph.

Typical uses:

- Compute \(P(Y \mid X = x)\) or \(P(Y \mid \text{do}(X = x))\) in a discrete Bayes model.
- Explore how different evidence or interventions change posterior beliefs.

## Inputs and setup

The **Updater box** takes as input:

- An **Instantiated Model** or **Estimator** output that is a **discrete Bayes model**.
- The user then specifies:
    - **Evidence**: values for some variables (e.g., \(X = x\), \(Z = z\)).
    - **Manipulations**: variables to intervene on (e.g., do\(X = x\)), typically by marking them as manipulated
      and assigning a value.

These are set via the Updater’s interface (e.g., a table of variables with columns for value and manipulation).

## How it works (conceptually)

Internally, the Junction Tree Updater:

1. Takes the discrete Bayes model and builds a **junction tree / clique tree** representation.
2. Initializes clique potentials based on the model’s CPTs.
3. Incorporates **evidence**:
    - Potentials inconsistent with the observed values are zeroed out.
    - Potentials are renormalized.
4. Incorporates **manipulations** (do-interventions) by:
    - Clamping manipulated variables to their specified values, and
    - Removing or neutralizing incoming influences, depending on the underlying implementation.
5. Runs **message passing** on the junction tree until all cliques are calibrated.
6. Reads off **posterior marginals** for variables of interest from the calibrated cliques.

Because it is junction-tree based, this updater is **exact** for the given model (up to numerical precision).

## Output

- **Posterior distributions** for variables given evidence and manipulations.
- In the GUI this may be shown as:
    - Updated probabilities for each state of a chosen variable,
    - Updated expectations for functions of the variables (where supported).
- The underlying instantiated model typically remains fixed; the updater operates “on top” of it.

## Tips

- Use the Junction Tree Updater whenever exact inference is feasible; it is the **default** discrete updater.
- For large or highly connected models, exact junction-tree inference may be computationally expensive; in those
  cases the **Approximate Updater** may be preferable.
- Be clear about the distinction between:
    - **Evidence** (observations: “we saw \(X = x\)”),
    - **Manipulations** (interventions: “we set \(X = x\)”).

## Related pages

- `Tetrad Interface → Updater Box`
- `Tetrad Interface → Instantiated Model (Bayes)`
- `Tetrad Interface → Approximate Updater`
- `Tetrad Interface → Row Summing Updater`