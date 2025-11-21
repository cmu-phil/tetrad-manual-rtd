# m-Separation Test

## Summary

The m-Separation Test is a **graphical independence test** that does not use
data. Instead, it tests whether two variables X and Y are **m-separated** by a
set S in a given graph (for example, a DAG, MAG, or PAG). It is used when the
underlying independence information comes from a known causal graph rather than
from statistical tests.

## When to use

- You have a known or assumed causal graph and want to compute implied
  independences X ⟂ Y | S directly from the graph structure.
- You are debugging search algorithms or comparing learned graphs to ground
  truth.
- You are using **oracle experiments** where m-separation plays the role of an
  independence oracle.

## Assumptions

- The graph is interpreted under standard rules of **d-separation** (for DAGs)
  or **m-separation** (for MAGs/PAGs).
- The causal Markov and faithfulness assumptions relate graphical separation to
  statistical independence.

## Test details (conceptual)

For each independence query X ⟂ Y | S, the test:

1. Examines all paths between X and Y in the graph.
2. Determines whether every such path is **blocked** given S by the rules of
   m-separation (colliders, non-colliders, descendant conditions, etc.).
3. Returns “independent” if all paths are blocked, and “dependent” otherwise.
4. No numeric statistic or p-value is computed; the output is exact given the
   graph.

## Parameters in Tetrad

No Parameters.

## Strengths

- Exact given the graph; no sampling error.
- Ideal for debugging algorithms and running simulation studies with a known
  ground truth.
- Extremely fast for moderate graph sizes.

## Limitations

- Requires a **known graph**; not applicable when only data are available.
- Assumes that independences correspond exactly to m-separation in the graph.

## References

- Spirtes, P., Glymour, C. N., & Scheines, R. (2000).
  *Causation, Prediction, and Search* (2nd ed.). MIT Press.
- Zhang, J. (2008).
  On the completeness of orientation rules for causal discovery in the presence
  of latent confounders and selection bias.
  *Artificial Intelligence*, 172(16–17), 1873–1896.
