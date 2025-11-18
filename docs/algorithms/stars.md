# StARS

**Type:** Wrapper / regularization-path stability tuner (Stability Approach to Regularization Selection)  
**Output:** Same graph class as the wrapped algorithm (DAG / CPDAG / PAG / etc.)

StARS wraps a base Tetrad `Algorithm` and selects a value of a single tuning parameter (such as a penalty λ) using the Stability Approach to Regularization Selection.  
It repeatedly runs the base algorithm on bootstrap subsamples across a range of parameter values, measures how unstable the adjacencies are, and chooses the largest parameter that keeps instability below a user-specified cutoff.

---

## Key Idea

The workflow is:

1. Generate bootstrap subsamples.  
   Draw `numSubsamples` bootstrap samples (with replacement) of size `percentSubsampleSize * N`.

2. Scan a parameter grid.  
   For each parameter value between `low` and `high` (stepped by 0.5), set  
   `parameters[parameter] = lambda`,  
   then run the base algorithm on each subsample.

3. Measure instability D(lambda).  
   For each pair of variables i and j, compute theta(i,j), the fraction of subsample graphs in which they are adjacent.  
   Compute xsi(i,j) = 2 * theta(i,j) * (1 - theta(i,j)).  
   Then D(lambda) is the average of xsi(i,j) over all i < j.  
   (Only adjacency is considered; orientations are ignored.)

4. Pick the chosen parameter.  
   Among all parameter values where D(lambda) is below the cutoff (StARS.cutoff), choose the one with the largest D(lambda).  
   If using `logScale = true`, transform the chosen value via a base-10 exponential; otherwise use it directly.

5. Final graph.  
   Run the base algorithm once, on the full dataset, with this selected parameter value, and return its graph.

---

## When to Use

Use StARS when:

- You have an algorithm with a penalty or tuning parameter and want a principled, stability-based way to choose it.
- You want adjacency robustness across subsamples, not just overall fit.
- You are willing to spend extra time on a bootstrap + parameter scan to get a better-tuned model.

Typical use cases:

- Score-based methods with penalty parameters (FGES, BOSS, DAGMA variants, etc.)
- Constraint-based methods that use a threshold or alpha playing the role of a regularization parameter.

Related:

- StabilitySelection — which aggregates edges by frequency instead of choosing a single parameter.

---

## Prior Knowledge Support

StARS passes all knowledge constraints directly to the wrapped algorithm.

- StARS itself has no knowledge object.
- If the wrapped algorithm supports forbidden edges, required edges, tiers, or background knowledge, those constraints are fully honored during every subsample run and in the final full-data run.

Thus: knowledge support = whatever the wrapped algorithm supports.

---

## Strengths

- Provides a principled way to pick a regularization parameter.
- Works with any Tetrad algorithm that exposes a tunable numeric parameter.
- Parallelized (ForkJoinPool) for efficient subsample evaluation.
- Returns a single, interpretable graph from the underlying algorithm.

---

## Limitations

- Computationally expensive (subsamples × parameter values × algorithm cost).
- Only tunes one parameter.
- Uses a fixed parameter grid (increments of 0.5).
- Measures only adjacency instability, not orientation instability.
- Some GUI parameters (e.g., StARS.tolerance) are currently placeholders.

---

## Key Parameters in Tetrad

These appear in addition to the wrapped algorithm’s own parameters.

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `parameter` (constructor arg) | Name of the parameter to tune (e.g., "penaltyDiscount"). |
| `low`, `high` (constructor args) | Range of parameter values to scan. Stepped internally by 0.5. |
| `percentSubsampleSize` | Fraction of N to use for bootstrap samples. |
| `numSubsamples` | Number of subsamples used to estimate instability. |
| `StARS.cutoff` | Instability cutoff. StARS chooses the largest lambda with D(lambda) < cutoff. |
| `logScale` | If true, interpret the scanned parameter values as log-base-10 values. |
| `StARS.percentageB` | Present in the parameter list for symmetry; not used in the current implementation. |
| `StARS.tolerance` | Placeholder; not used by the current code. |
| `depth`, `verbose` | Passed through to the wrapped algorithm. |

---

## Reference

Adapted from:

- Liu, Roeder, and Wasserman (2010).  
  “Stability Approach to Regularization Selection (StARS) for High-Dimensional Graphical Models.”

Tetrad generalizes this from graphical LASSO to arbitrary causal discovery algorithms by measuring adjacency instability between subsamples.

---

## Summary

StARS selects a stability-optimal value of a tuning parameter by running a base Tetrad algorithm on many subsamples, measuring adjacency instability, and choosing the largest parameter that remains below a user-chosen stability cutoff. It produces a single, better-tuned result from the wrapped algorithm.