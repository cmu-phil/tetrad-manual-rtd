# Probabilistic Independence Test

## Summary

The Probabilistic Independence Test is a **wrapper test** that uses explicit
probability or density models (for example, from an instantiated Bayesian
network or parametric model) to answer independence queries X ⟂ Y | S. It is
used when the probability model, not the data, is considered the source of
truth.

## When to use

- You have a fully specified **probabilistic model** (e.g., a Bayes net or
  parametric SEM) and want to query its implied independences.
- You are performing oracle-style experiments where the model encodes the
  ground truth.
- You wish to test search algorithms in controlled synthetic settings.

## Assumptions

- The provided probabilistic model is correct (for the purpose of the
  experiment).
- Independence decisions are made by checking whether the model assigns the
  same conditional distribution to X given S, with and without conditioning on
  Y (or equivalent factorizations).

## Test details (conceptual)

For each X ⟂ Y | S query, the test:

1. Uses the underlying probability model to compute or compare
   P(X | S) and P(X | Y, S), or an equivalent characterization.
2. Declares independence if these distributions are equal (within numerical
   tolerance), and dependence otherwise.
3. Does not rely on raw data; the model itself is the oracle.

## Parameters in Tetrad

- The primary “parameter” is the **instantiated probabilistic model**.
- Tolerance thresholds for numeric comparisons may be configurable.
- `verbose` — Whether to report underlying probability queries.

## Strengths

- Provides exact or near-exact independence decisions given the model.
- Ideal for algorithm evaluation and theoretical experiments.

## Limitations

- Not applicable when only raw data are available and no model is given.
- Results are only as good as the underlying model specification.
