# Detail: Approximate Updater

The **Approximate Updater** performs **approximate Bayesian updating** for **discrete** models. It uses
sampling-based or approximate inference methods rather than an exact junction tree, which can be useful for
larger or more complex models.

It is available when the **Updater** box is connected to a discrete **Instantiated Model** or **Estimator**
output, and the updater type is set to *Approximate Updater*.

## Purpose

- Provide a **faster or more scalable** alternative to exact junction-tree updating.
- Approximate \(P(Y \mid \text{evidence}, \text{manipulations})\) when exact inference is expensive or
  impractical.
- Allow exploration of posterior beliefs in large discrete models.

## Inputs and setup

Same as the Junction Tree Updater:

- **Input model**: a discrete Bayesian model from an Instantiated Model or Estimator.
- **User-specified information**:
    - Evidence (variable=value assignments),
    - Manipulations/interventions (do\(X = x\)).

Additional **approximation settings** may be exposed, such as:

- Number of **samples**,
- Convergence thresholds,
- Random seeds for reproducibility.

## How it works (conceptually)

The Approximate Updater typically uses a **sampling-based** or otherwise approximate method:

1. Incorporates **manipulations** by modifying the generative process (e.g., clamping manipulated variables).
2. Incorporates **evidence** by:
    - Rejecting or reweighting samples that contradict evidence (e.g., likelihood weighting, importance sampling),
    - Or using MCMC methods conditioned on evidence.
3. Generates a large number of **samples** from the (approximate) posterior.
4. Estimates posterior quantities (marginal probabilities, expectations) from these samples.

Because it is approximate:

- Results can have **Monte Carlo noise**,
- Success depends on the number of samples and mixing properties of the sampler.

## Output

- **Approximate posterior distributions** for variables of interest.
- These are typically displayed similarly to the Junction Tree Updater, but with the understanding that they
  are estimates, not exact values.
- Diagnostics (if provided) may include:
    - Number of samples used,
    - Basic convergence indicators.

## Tips

- Use the Approximate Updater for:
    - Very large discrete models,
    - Highly connected graphs where the junction tree becomes too large.
- Increase the **number of samples** to improve accuracy, at the cost of runtime.
- If exact and approximate updaters are both feasible, you can:
    - Run both and compare results, to assess the approximation quality.

## Related pages

- `Tetrad Interface → Updater Box`
- `Tetrad Interface → Instantiated Model (Bayes)`
- `Tetrad Interface → Junction Tree Updater`
- `Tetrad Interface → Row Summing Updater`