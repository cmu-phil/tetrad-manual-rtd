# RFCI-BSC

**Type:** Hybrid (constraint-based + Bayesian scoring over constraints)  
**Output:** PAG (Partial Ancestral Graph) with edge-type probabilities

RfciBsc wraps RFCI in a Bayesian structural-constraints framework. It repeatedly runs RFCI with a probabilistic independence test, collects both the resulting PAGs and the probabilities of queried independence facts, then learns a Bayesian network over those facts. Each candidate PAG is scored under two Bayesian structural-constraints criteria (BSC-D and BSC-I), and the best-scoring PAG is returned, with edge-type probabilities attached from the ensemble.

---

## Key Idea

RfciBsc proceeds in several stages:

1. **Initial RFCI runs and constraint collection**
    - Uses the IndTestProbabilistic test inside an RFCI run to collect a map of independence facts and their estimated probabilities.
    - Repeats RFCI multiple times with a probabilistic test, saving the resulting PAGs.
    - From all queried facts, it selects only those whose independence probability lies in a “informative” band (between `lowerBound` and `upperBound`).

2. **Bootstrap and constraint data construction**
    - Creates many bootstrap resamples of the original data.
    - For each bootstrap sample, re-estimates whether each selected independence fact is independent or dependent and encodes these as 0/1 in a “constraint dataset,” where each column is an independence fact and each row is a bootstrap replicate.

3. **Learning a dependency structure over constraints**
    - Learns a Bayesian network over the constraint dataset using FGES with a BDeu score.
    - Converts the resulting CPDAG to a DAG and estimates conditional probability tables via Dirichlet-Bayes parameter learning.
    - This model captures dependence structure among the independence facts themselves.

4. **Bayesian structural-constraints scoring**
    - For each candidate PAG from the ensemble, RfciBsc computes two log-probability scores:
        - **BSC-I**: based directly on the independence probabilities from the original probabilistic test.
        - **BSC-D**: “dependence-filtered,” using the learned BN over constraints to refine probabilities.
    - It then normalizes these scores across the ensemble to obtain BSC-D and BSC-I “posterior-like” scores for each PAG.

5. **Select and annotate output PAG**
    - Identifies `graphRBD` (best under BSC-D) and `graphRBI` (best under BSC-I), and returns either `graphRBD` or `graphRBI` depending on `outputRBD`.
    - Adds edge-type probabilities to each edge, summarizing how often each edge type (tail–arrow, arrow–tail, circle–circle, etc.) occurs across the ensemble of PAGs.

The result is a single PAG that is both RFCI-compatible and globally scored using the joint behavior of all tested independence constraints.

---

## When to Use

- You want RFCI-style PAGs but would like a **Bayesian meta-criterion** to select among multiple candidate PAGs.
- You have **discrete data** and can reasonably model independence-test outcomes as random variables.
- You are willing to pay extra computation (multiple RFCIs, bootstrap resampling, and FGES) for a more globally coherent PAG.
- You’d like **edge-type probabilities** summarizing uncertainty in the PAG structure.

Related algorithms:

- RFCI (base constraint-based PAG learner)
- PagSamplingRfci (RFCI ensemble with simple frequency aggregation)
- FGES + BDeu (used internally to model dependencies among independence facts)

---

## Prior Knowledge Support

**Does it accept background knowledge?**  
Partially.

- The `Rfci` object passed into the `RfciBsc` constructor can be configured with knowledge (forbidden/required edges, tiers) for the **initial** RFCI runs.
- The randomized RFCI runs inside RfciBsc currently construct new RFCI instances with probabilistic tests and **do not explicitly reuse** the original knowledge. In practice this means:
    - Background knowledge may influence the initial constraint collection (through the original RFCI),
    - But randomized ensemble runs may not fully reflect that knowledge.

If knowledge is critical, you should be aware of this behavior and treat RfciBsc as an experimental or advanced method.

---

## Strengths

- Combines **constraint-based learning (RFCI)** with **Bayesian scoring over constraints**, offering a more global model selection criterion than local CI tests alone.
- Produces **two** principled candidate PAGs: one maximizing BSC-D (dependence-filtered) and one maximizing BSC-I (independence-based).
- Attaches **edge-type probabilities** to each edge, giving a richer summary of structural uncertainty.
- Uses **multi-threaded** computation (ForkJoinPool) for RFCI runs, bootstrap constraint evaluation, and scoring.

---

## Limitations

- **Discrete data only**: relies on SimpleDataLoader and discrete BDeu scoring.
- Computationally heavy: multiple RFCI runs, many bootstrap samples, and a separate FGES structure-learning step.
- Parameter-rich: performance and behavior can be sensitive to bounds (`lowerBound`, `upperBound`), bootstrap size, and threshold/cutoff settings for probabilistic tests.
- Background knowledge is not consistently propagated to all randomized RFCI runs in the current implementation.

---

## Key Parameters in Tetrad

The main RfciBsc-specific knobs are:

| Parameter (camelCase) | Description |
|------------------------|-------------|
| `numRandomizedSearchModels` | Number of RFCI runs for generating candidate PAGs and collecting independence facts. |
| `numBscBootstrapSamples` | Number of bootstrap samples used to build the constraint dataset. |
| `lowerBound` | Lower probability threshold for selecting “informative” independence facts from IndTestProbabilistic (facts with probability below this are excluded). |
| `upperBound` | Upper probability threshold for selecting “informative” independence facts (facts with probability above this are excluded). |
| `outputRBD` | If true, output the best PAG under BSC-D (`graphRBD`); if false, output the best under BSC-I (`graphRBI`). |
| `verbose` | Controls detailed logging of intermediate steps and scores. |
| `thresholdNoRandomDataSearch` | Whether to apply a threshold rule for probabilistic independence in the initial RFCI runs over the original data. |
| `cutoffDataSearch` | Probability cutoff for independence in the initial RFCI runs (used when `thresholdNoRandomDataSearch` is true). |
| `thresholdNoRandomConstrainSearch` | Whether to apply a threshold rule when re-estimating independence in each bootstrap sample. |
| `cutoffConstrainSearch` | Probability cutoff for independence in the bootstrap-based constraint estimation. |

Additional behavior is controlled by the underlying `Rfci` object you pass into the constructor, including:

- `depth` (maximum conditioning set size)
- `maxDiscriminatingPathLength` (limit on discriminating paths)
- `knowledge` (forbidden/required edges, tiers)
- `IndTestProbabilistic` settings used in the initial RFCI call

---

## Reference

There is no dedicated public paper for RfciBsc. It was implemented by:

- **Chirayu Kong Wongchokprasitti, PhD**

and builds on:

- RFCI (Fast Causal Inference with latent variables and selection)
- IndTestProbabilistic (probabilistic independence testing)
- BCInference (Bayesian constraints inference framework)
- FGES with BDeu (for learning a BN over independence facts)

---

## Summary

RfciBsc is an advanced hybrid method that uses RFCI, bootstrap resampling, and a Bayesian model over independence constraints to select a best-supported PAG and attach edge-type probabilities, trading extra computation for a more globally coherent and uncertainty-aware causal graph.