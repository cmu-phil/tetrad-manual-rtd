# StabilitySelection

**Type:** Wrapper / resampling ensemble (bootstrap-based)  
**Output:** Same graph class as the wrapped algorithm (typically CPDAG / PAG / DAG / etc.)

`StabilitySelection` is a **generic wrapper** that repeatedly runs a base Tetrad algorithm on bootstrap resamples of the data and then **keeps only edges that appear often enough** across runs.  
It does not define its own score or CI test; instead, it delegates all modeling assumptions and graph semantics to the **wrapped `Algorithm`**, and then performs stability selection on that algorithm’s output.

---

## Key Idea

The idea is to take any causal discovery algorithm that returns a graph (DAG, CPDAG, PAG, …) and make its output **more robust** by:

1. **Resampling the data**
    - Draw `numSubsamples` bootstrap samples (with replacement) of size `percentSubsampleSize * N`.

2. **Running the base algorithm on each resample**
    - For each sample, run the wrapped `Algorithm` with the same `Parameters`.
    - Collect the resulting graphs in a list.

3. **Counting edge frequencies**
    - For each edge (including its orientation), count how many graphs contain it.

4. **Thresholding by stability**
    - Include an edge in the final graph if its selection frequency exceeds `percentStability` (e.g., 0.7 → kept if present in > 70% of runs).

The final graph is built over the original variable set and contains **only those edges (and orientations) that are sufficiently stable** under resampling.

---

## When to Use

Use `StabilitySelection` when:

- You have a base algorithm (e.g., **FGES**, **BOSS**, **PC**, **FCI**, **RFCI**, **DAGMA**, etc.) and want a **more conservative, robust** edge set.
- You are concerned that a single run over one dataset may give **unstable edges** due to sampling variability or tuning choices.
- You want a **simple stability heuristic** without designing a new score or CI test.

Typical settings:

- High-dimensional data where many edges are near the detection threshold.
- Situations where you are willing to trade **recall** for **precision** (i.e., fewer but more reliable edges).

Related algorithms:

- **StARS** (separate wrapper) — more specifically modeled after the StARS criterion for regularization paths.
- **Bootstrapping** in general — `StabilitySelection` is a specific bootstrap-with-threshold pattern for edge selection.

---

## Prior Knowledge Support

**Does it accept background knowledge?**  
Indirectly, **yes** — through the wrapped `Algorithm`.

- `StabilitySelection` itself does **not** manage `Knowledge` objects.
- Whatever knowledge / constraints you pass to the **base algorithm** (e.g., forbidden/required edges, tiers) will be **honored on each bootstrap run**.
- The final stable graph only contains edges that:
    1. Are allowed by the base algorithm’s knowledge configuration, and
    2. Survive the stability threshold.

So: **knowledge support = that of the wrapped algorithm.** The wrapper does not add or override any constraints.

---

## Strengths

- **Algorithm-agnostic**
    - Works with any Tetrad `Algorithm` that takes a `DataSet` and `Parameters` and returns a `Graph`.

- **More robust edge set**
    - Edges must appear consistently across many resampled datasets to survive, which often improves **precision**.

- **Parallelized implementation**
    - Uses a `ForkJoinPool` to run subsample searches in parallel across available CPU cores.

- **Easy to drop in**
    - You can wrap an existing algorithm in code or scripting with a one-line change and reuse its parameter set.

---

## Limitations

- **Computationally expensive**
    - If the base algorithm is already heavy, repeating it `numSubsamples` times multiplies runtime.

- **Heuristic thresholding**
    - `percentStability` is a user-chosen cutoff; there is no built-in theoretical guarantee that a particular value is “optimal.”

- **Bootstrap-with-replacement, not pure subsampling**
    - Implementation uses a `BootstrapSampler` with replacement (sample size `percentSubsampleSize * N`). This is close to subsampling but not identical to the original Meinshausen–Bühlmann stability selection setup.

- **Edge orientation stability mirrors the base algorithm**
    - If the base algorithm’s orientations are themselves unstable, stability selection may discard many of them; orientation robustness is no better than what repeated runs can support.

---

## Key Parameters in Tetrad

All parameters appear alongside the wrapped algorithm’s parameters.  
In addition to the base algorithm’s parameters, `StabilitySelection` adds:

| Parameter (camelCase)       | Description |
|-----------------------------|-------------|
| `numSubsamples`             | Number of bootstrap replications. For each replication, a new bootstrap sample is drawn and the base algorithm is run. |
| `percentSubsampleSize`      | Fraction of the original sample size used for each bootstrap (e.g., `0.8` → each bootstrap sample has `0.8 * N` rows, with replacement). |
| `percentStability`          | Stability threshold in `[0, 1]`. An edge is kept if its selection frequency across all runs exceeds `percentStability`. |
| `depth`                     | Passed through to the underlying algorithm’s parameter set. Not used directly by `StabilitySelection` itself, but often relevant for constraint-based base learners. |
| `verbose`                   | Passed through to the underlying algorithm’s parameter set if used there; `StabilitySelection` itself does not log per-run details. |

Remember: the **wrapped algorithm’s parameters** (e.g., `alpha`, `penaltyDiscount`, `useBes`, etc.) are still fully respected and typically dominate the **causal semantics** of the result.

---

## Reference

This wrapper is inspired by the general idea of **stability selection**:

- Meinshausen, N., & Bühlmann, P. (2010).  
  *Stability selection.*  
  Journal of the Royal Statistical Society: Series B (Statistical Methodology), 72(4), 417–473.

Tetrad’s `StabilitySelection` adapts this idea to **graph-structure selection** by counting edge frequencies rather than variable inclusion in a regression model.

---

## Summary

`StabilitySelection` is a generic **bootstrap-based ensemble** that wraps any Tetrad algorithm, repeatedly runs it on resampled data, and keeps only those edges (and orientations) that appear with high frequency—giving you a more conservative, stable graph built on top of whatever assumptions the base algorithm makes.