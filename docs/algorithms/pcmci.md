# PCMCI — Time-Series Causal Discovery (Runge et al.)

**Type:** Constraint-based (time series)  
**Output:** Lagged causal graph (optionally collapsed to base-time DAG)  
**Reference:**  
Runge, J. et al. (2019). *Detecting causal associations in large nonlinear time series datasets.* Science Advances.  
Canonical implementation: Tigramite (Runge Lab) — https://github.com/jakobrunge/tigramite

PCMCI is a time-series causal discovery algorithm designed for high-dimensional, autocorrelated data.  
Tetrad includes a **minimal lagged-edge version** for benchmarking, although full practical use is best handled with the Tigramite package.

---

## Key Idea

PCMCI proceeds in two stages:

1. **PC-style parent pre-selection**  
   For each target variable `Y_t`, eliminate candidate parents using conditional independence tests restricted to the strict past (lags >= 1).

2. **MCI (Momentary Conditional Independence) test**  
   A lagged edge from `X_(t–tau)` to `Y_t` is kept if it remains dependent conditional on:
    - the parents of `Y_t` (excluding `X_(t–tau)`), plus
    - the parents of `X_(t–tau)`.

Tetrad’s PCMCI only orients lagged edges (`tau >= 1`) and does not include instantaneous (tau = 0) steps from PCMCI+.

---

## When to Use

Use PCMCI in Tetrad when:

- You need **lagged causal structure** in time-series data.
- You want to compare Tetrad’s algorithms to a standard baseline for time series.
- You have moderate-sized data and simple CI tests (e.g., Fisher Z).

Do **not** rely on the Tetrad version for:

- PCMCI+ (instantaneous causal effects)
- nonlinear CI tests
- large-scale time-series pipelines

Use the **Tigramite** implementation for those.

---

## Prior Knowledge Support

PCMCI in Tetrad respects:

- Forbidden edges
- Required edges
- Tiered temporal constraints
- Any Knowledge object compatible with PC/FCI-style algorithms

---

## Strengths

- Designed specifically for **time-series causal discovery**.
- Handles autocorrelation via PC-style pre-selection and MCI.
- More scalable than naive time-series PC.
- Integrates into Tetrad’s benchmarking and visualization tools.

---

## Limitations

- Tetrad version is intentionally minimal:
    - No PCMCI+ instantaneous paths
    - No nonlinear CI tests
    - No advanced false-positive controls from Tigramite

- Sensitive to:
    - choice of CI test
    - significance level
    - max lag
    - sample size

---

## Key Parameters in Tetrad

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `maxLag`               | Maximum lag considered (tau >= 1). |
| `independenceTest`     | CI test (Fisher Z, etc.). |
| `alpha`                | Significance level for both phases. |
| `collapse`             | Collapse lagged edges into a base-time graph. |
| `knowledge`            | Required/forbidden edges and tier constraints. |
| `verbose`              | Print detailed logs. |

---

## Reference

Runge, J., Nowack, P., Kretschmer, M., Flaxman, S., & Sejdinovic, D. (2019).  
*Detecting causal associations in large nonlinear time series datasets.*  
**Science Advances**, 5(11).  
Tigramite package: https://github.com/jakobrunge/tigramite

---

## Summary

PCMCI in Tetrad is a **time-series causal discovery algorithm** using PC-style pre-selection plus the MCI test to recover lagged causal structure.  
It is intended for **comparisons and educational use**, while the full Tigramite implementation should be used for advanced nonlinear or PCMCI+ analyses.