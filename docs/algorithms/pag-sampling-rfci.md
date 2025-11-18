# PagSamplingRfci

**Type:** Ensemble / resampling wrapper for constraint-based PAG discovery  
**Output:** PAG (Partial Ancestral Graph)

PagSamplingRfci repeatedly runs RFCI on the same dataset under randomized probabilistic-independence modeling, collects a set of PAGs, filters out those that violate PAG legality, and then aggregates them into a single consensus PAG. It is designed to stabilize RFCI in difficult settings, especially when data are small-sample or highly non-Gaussian. The method was implemented in the Pitt Causal Discovery Toolkit and integrated into Tetrad.

---

## Key Idea

PagSamplingRfci is a multi-run ensemble adaptation of RFCI:

1. For each sample run, it constructs an IndTestProbabilistic test (likelihood-based test using posterior probabilities).
2. It runs RFCI with user-specified depth, threshold rules, discriminating-path length, and prior sample size.
3. It checks whether the resulting PAG is legal using the PagLegalityCheck tool.
4. It collects all legal PAGs.
5. After enough legal PAGs are obtained, it aggregates them using GraphSampling.createGraphWithHighProbabilityEdges, forming a consensus PAG where each edge appears with high frequency across runs.

This produces a single PAG that encodes high-confidence structural information, while smoothing over instability and sampling noise present in any single RFCI run.

---

## When to Use

Use PagSamplingRfci when:

- RFCI is unstable on your dataset (small N, strong non-Gaussianity, selection bias, or many latents).
- You want a consensus PAG that reflects robust features rather than one fragile estimate.
- You want to exploit RFCI's speed while mitigating its sensitivity to sampling fluctuations.
- You prefer not to use bootstrapping over resampled datasets; this method resamples the **graph space** by stochastic independence judgments.

Related algorithms:

- RfciBsc (bootstrap-style resampling of RFCI)
- StabilitySelection (frequency-based edge selection)
- StARS (stability-based parameter selection)

---

## Prior Knowledge Support

Yes — PagSamplingRfci accepts background knowledge:

- forbidden edges
- required edges
- tiers (temporal constraints)

Knowledge is passed directly to each RFCI run inside the ensemble.

---

## Strengths

- Produces a more stable PAG than any single RFCI call.
- Exploits RFCI’s speed while adding robustness.
- Uses probabilistic independence tests, which can be smoother than sharp-threshold CI tests.
- Automatically filters out illegal PAGs before aggregation.
- Parallelized using ForkJoinPool for fast multi-threaded execution.

---

## Limitations

- More computationally expensive than one RFCI run (multiple RFCIs + legality checks).
- Does not resample the data; randomness arises only from the probabilistic independence test.
- Sensitive to parameters of IndTestProbabilistic (threshold, cutoff, priorEquivalentSampleSize).
- Aggregation uses adjacency and orientation frequency heuristics, not likelihood weighting.

---

## Key Parameters in Tetrad

These parameters exist on the PagSamplingRfci object itself:

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `numRandomizedSearchModels` | Number of RFCI models to generate before forming the consensus PAG. |
| `verbose` | Print debug output during ensemble runs. |
| `depth` | RFCI search depth (same meaning as RFCI’s depth parameter). |
| `maxDiscriminatingPathLength` | Limits discriminating-path exploration; -1 means unlimited. |
| `threshold` | IndTestProbabilistic setting controlling probability thresholding. |
| `cutoff` | Probability cutoff for independence decisions. |
| `priorEquivalentSampleSize` | Equivalent sample size parameter for probabilistic tests. |
| `knowledge` | Required/forbidden-edge background knowledge passed into each RFCI run. |

Internal (not exposed in the GUI):

- `NUM_THREADS` = number of parallel workers (defaults to 10).

---

## Reference

There is **no dedicated publication** for PagSamplingRfci.  
However, it is based on:

- Tetrad RFCI implementation
- IndTestProbabilistic (probabilistic independence testing)
- PagLegalityCheck (graph legality validator)
- GraphSampling.createGraphWithHighProbabilityEdges (ensemble aggregator)

Original implementation by **Kevin V. Bui**, later integrated into Tetrad.

---

## Summary

PagSamplingRfci is an ensemble method that runs RFCI multiple times under probabilistic independence testing, filters illegal PAGs, and aggregates the remainder into a high-confidence consensus PAG. It is useful when RFCI is unstable or data are noisy, providing a more robust and reliable PAG without altering RFCI’s underlying logic.