# Row Summing Updater

The **Row Summing Updater** is a specialized **discrete** updater that computes posterior quantities by
**summing over rows** of the conditional probability tables (CPTs) consistent with the specified evidence and
manipulations. It is intended for simpler or more structured cases where such row-wise calculations are
convenient.

It is available when the **Updater** box is connected to a discrete **Instantiated Model** or **Estimator**
output and the updater type is set to *Row Summing Updater*.

## Purpose

- Provide a conceptually simple, table-based updating mechanism in discrete models.
- Compute exact or semi-exact posterior probabilities by **explicitly summing over CPT rows** that match
  evidence and intervention patterns.
- Serve as an alternative to the junction-tree and approximate updaters in specific situations.

## Inputs and setup

- **Input model**: discrete Bayesian model from an Instantiated Model or Estimator.
- **Evidence and manipulations**:
    - The user specifies observed values and manipulations for variables, as in other discrete updaters.

No junction tree is built; instead, the updater works more directly with the **tabular representation** of the
model.

## How it works (conceptually)

At a high level:

1. Interpret the discrete Bayes model as a **joint distribution** factored into CPTs.
2. For each query variable \(Y\):
    - Enumerate (or efficiently traverse) combinations of parent configurations / CPT rows consistent with:
        - The specified **evidence**,
        - The specified **manipulations**.
    - For each such configuration, accumulate contributions of its **joint probability** to:
        - The desired event (e.g., \(Y = y\)),
        - The normalizing constant.
3. Normalize to obtain posterior probabilities:
   \[
   P(Y = y \mid \text{evidence, manipulations}) =
   \frac{\sum_{\text{consistent rows}} P(Y = y, \text{rest})}
   {\sum_{\text{consistent rows}} P(\text{rest})}.
   \]

In practice, the implementation may use factorization tricks to avoid brute-force enumeration, but the
conceptual picture is **row-based summation** over table entries.

## Output

- Posterior probabilities computed by row summation.
- Displayed similarly to other discrete updaters (probability tables or marginal distributions).

## Tips

- Best suited to:
    - Smaller discrete models, or
    - Structured networks where row-wise calculations are efficient.
- For general large models, the **Junction Tree Updater** will often be more scalable; for very large models
  where exact methods are too slow, the **Approximate Updater** may be preferable.
- If you are teaching or debugging, the Row Summing Updater can be useful because it closely mirrors the
  textbook calculation “sum over all configurations consistent with the evidence.”

## Related pages

- `Tetrad Interface → Updater Box`
- `Tetrad Interface → Instantiated Model (Bayes)`
- `Tetrad Interface → Junction Tree Updater`
- `Tetrad Interface → Approximate Updater`