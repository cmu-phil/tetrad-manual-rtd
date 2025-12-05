# Detail: Dirichlet Estimator

The **Dirichlet Estimator** fits a **Bayes Parametric Model** to data using a
**Dirichlet prior** over each row of the conditional probability tables (CPTs).
It is a Bayesian-smoothing alternative to plain ML estimation, reducing
zero-probability problems in sparse data.

This estimator is available whenever the **Parametric Model** connected to the
Estimator box is a **Bayes PM**.

```{figure} ../../_static/images/tetrad-interface/box-by-box/dirichlet-estimator.png
:name: tetrad-dirichlet-estimator-screenshot
:alt: Dirichlet Estimator

Dirichlet Estimator
```

## Purpose

- Estimate CPTs using **posterior mean** probabilities under a Dirichlet prior.
- Provide **smoothed** probability estimates that avoid zero counts.
- Improve stability when sample sizes are modest or some parent configurations
  are rare or unobserved.

## Inputs and requirements

- **Parametric Model**: A **Bayes PM** specifying nodes, states, and parents.
- **Data**: Discrete data with variables matching the Bayes PM.
- **Prior settings** (when exposed in the GUI):
    - Often summarized as a **strength** or **equivalent sample size** for a
      uniform Dirichlet prior (e.g., α > 0).
    - Some versions may allow non-uniform priors.

## How it works (conceptually)

For each node X with parents Pa(X), and each parent configuration pi:

1. Start with a Dirichlet prior written as Dir(alpha_1, ..., alpha_k) over the k states of X.
2. Observe empirical counts n_1, ..., n_k from the data.
3. Compute the posterior Dirichlet Dir(alpha_1 + n_1, ..., alpha_k + n_k).
4. Use the posterior mean as the CPT entries:

   P(X = x_i | Pa(X) = pi) = (alpha_i + n_i) / sum_j (alpha_j + n_j).

## Output

- A **fitted Bayes model** whose CPT rows are posterior-mean probabilities under
  the specified Dirichlet prior(s).
- Optionally, a summary of:
    - Log-marginal likelihood or other scores (depending on implementation).
- The result can be saved as an **Instantiated Model**.

## Tips and common issues

- Larger prior strengths (equivalent sample sizes) lead to **heavier smoothing**,
  shrinking probabilities toward the prior.
- For very small datasets or models with many parents, Dirichlet smoothing is
  often preferable to raw ML.
- If you are using the model for **score-based structure learning**, keep in
  mind that different Dirichlet hyperparameters can significantly affect scores.

## Related pages

- `Tetrad Interface → Estimator Box`
- `Tetrad Interface → Bayes Parametric Model`
- `Tetrad Interface → ML Bayes Estimator`
- `Tetrad Interface → EM Bayes Estimator`
- `Tetrad Interface → Instantiated Model (Bayes)`