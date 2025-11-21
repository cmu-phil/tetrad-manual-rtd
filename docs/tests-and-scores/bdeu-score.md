# BDeu Score

## Summary

The BDeu Score is a **Bayesian score** for discrete Bayesian networks. It uses
a Dirichlet prior with a specified **equivalent sample size (ESS)** and a
uniform prior over CPT parameters, yielding a score that is **score equivalent**
across Markov-equivalent DAGs.

## When to use

- Variables are **discrete**.
- You want a Bayesian score with a tunable prior strength (ESS).
- You care about score equivalence across equivalent DAG structures.

## Model class

- Discrete Bayes nets with Dirichlet priors over CPT rows.

## Score form (conceptual)

The BDeu score is the log marginal likelihood of the data given the DAG under a
Dirichlet-multinomial model with a uniform Dirichlet prior of strength ESS.
The score depends on:

- counts in each CPT cell,
- the prior hyperparameters determined by ESS and uniformity,
- the DAG structure.

## Parameters

| Parameter (camelCase)           | Description |
|---------------------------------|-------------|
| `priorEquivalentSampleSize`     | Double ≥ 1.0. The **prior equivalent sample size** for the BDeu Dirichlet prior. This total prior count is spread uniformly across all parent–child configurations in the conditional probability tables. Larger values make the prior stronger relative to the data (smoother estimates and stronger regularization); smaller values let the data dominate more. Default is 10.0. |
| `structurePrior`                | Double ≥ 0.0. **Structure prior coefficient** controlling a binomial-style prior on graph structure (for example, expected number of parents per node). When set to 0.0 (the default), BDeu uses essentially a uniform structure prior. Increasing this value biases the score toward graphs whose parent counts match the implied binomial prior; larger values therefore encourage particular sparsity levels. |

## Strengths

- Score equivalent under standard conditions.
- Incorporates prior information via ESS.
- Often preferred over pure BIC in small-sample discrete settings.

## Limitations

- Sensitive to the choice of ESS; too large or too small values can bias
  results.
- Uniform Dirichlet priors may not reflect domain knowledge.
