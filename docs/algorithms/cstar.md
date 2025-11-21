# CStaR (Causal Stability Ranking)

**CStaR** (Stekhoven et al., 2012) is a *ranking* method rather than a pure structure-learning algorithm.  
Given a set of **possible causes** and **possible effects**, it repeatedly:

1. Subsamples the data.
2. Learns a **CPDAG** on that subsample.
3. Uses **IDA** on that CPDAG to compute a *minimum total effect* for each candidate cause–effect pair.
4. Records which pairs are among the “top” strongest effects in that subsample.

Over many subsamples, CStaR estimates for each edge \(X \to Y\):

- how **often** \(X\) behaves like a cause of \(Y\) (`π`), and
- how **large** the effect tends to be (`minBeta` / “Effect” column),

and then uses **stability selection** ideas (Meinshausen & Bühlmann, 2010) to bound the expected number of false positives.

It is especially useful when you care about *prioritizing* a small set of robust, high-confidence effects (e.g., candidate causal predictors of a biological or clinical outcome) rather than recovering the entire causal graph.

---

## High-level idea

For each effect variable \(Y\) and each candidate cause \(X\):

1. **Subsample the data**
    - Draw a half-sample (with or without replacement, depending on the chosen sampling style).

2. **Learn a CPDAG on the subsample**
    - Use one of several CPDAG-producing algorithms:
        - PC-Stable
        - FGES
        - BOSS
        - Restricted BOSS

3. **Run IDA on the CPDAG**
    - For each candidate effect \(Y\), CStaR runs IDA to compute the **minimum total effect** of each possible cause \(X\) on \(Y\) across all DAGs in the CPDAG equivalence class.
    - This produces an effects matrix for that subsample: one effect size per (cause, effect) pair.

4. **Select the strongest effects in that subsample**
    - For each subsample, CStaR sorts all cause–effect effects and identifies a **“top bracket”** of strongest effects (size = `topBracket × #effects`).
    - Any pair whose effect lies in that top bracket is regarded as “selected” in that subsample.

5. **Aggregate across subsamples**
    - Over all subsamples:
        - `π` = proportion of subsamples in which \(X \to Y\) falls into the top bracket.
        - `Effect` = average of the minimal total effects from IDA across subsamples.

6. **Rank and filter**
    - Pairs are ranked primarily by `π` (more stable first), then by effect size.
    - Pairs with effect size below `selectionAlpha` are discarded.
    - A **PCER** (Per-Comparison Error Rate) is reported using the stability-selection bound.

The final output is a ranked **table of candidate causal edges**, with stability and effect-size information, and a simple graph view that keeps the most stable edges.

---

## Inputs

CStaR requires:

- A **continuous data set** (or at least, data for which the chosen score and test are appropriate).
- A set of **possible causes** (predictor variables).
- A set of **possible effects** (outcome variables) — often one or a small number of “targets” of interest.
- Choices for:
    - **CPDAG algorithm** (PC-Stable, FGES, BOSS, Restricted BOSS)
    - **Sampling style** (bootstrap or subsample)
    - **Number of subsamples**
    - **Top bracket size** (`q`)
    - **Selection threshold** (`selectionAlpha`)

Background knowledge about forbidden/required edges is **not** currently used; CStaR relies purely on the chosen CPDAG algorithm.

---

## Outputs

CStaR produces:

1. **A ranked table of records**

   Each row corresponds to a candidate edge \(X \to Y\) and includes:

    - `Cause` – the candidate predictor \(X\).
    - `Effect` – the target \(Y\).
    - `PI` – the stability frequency \( \hat{\pi} \) (fraction of subsamples where \(X \to Y\) lies in the top bracket).
    - `Effect` – the average minimal IDA effect for \(X \to Y\) across subsamples.
    - `PCER` – an estimated *per-comparison error rate* bound based on Meinshausen–Bühlmann stability selection; for edges with low stability (π ≤ 0.5), `PCER` is replaced by `*` to flag them as below the reliable range.
    - `#Potential causes` and `#Potential effects` – the sizes of the candidate sets used to compute the table.

2. **A graph view (optional)**

   CStaR can be used to construct a graph where:

    - Nodes are the variables that appear in the records.
    - A directed edge \(X \to Y\) is drawn when `π > 0.5`.

   This graph highlights **highly stable candidate causal relations** but is *not* meant as a full causal discovery result; it is a visualization of the top-ranked edges.

3. **Optional intermediate files**

   For reproducibility and resumability, CStaR can write:

    - The subsampled data sets,
    - The CPDAGs fitted on each subsample, and
    - The matrices of IDA effects per subsample.

   If rerun with the same output directory, CStaR will reload existing intermediate results instead of recomputing them.

---

## Parameters

| Parameter (camelCase)        | Description |
|------------------------------|-------------|
| `selectionMinEffect`         | Non-negative double. Minimum absolute effect size required for a variable to be considered statistically relevant during stability selection. Smaller values make selection more permissive; larger values make it conservative. |
| `numSubsamples`              | Integer ≥ 1. Number of subsamples (bootstrap or subsample splits) to use for stability scoring. Higher values give more stable results but increase computation. Typical range: 20–200. |
| `targets`                    | List of variable names. Restricts CStaR to estimating the parent sets only for the specified target variables. If empty, CStaR analyzes all variables. |
| `topBracket`                 | Integer ≥ 1. Number of top-ranked candidate graphs (or parent sets) retained per subsample before voting. Controls model diversity and stability. |
| `parallelized`               | Boolean. If `true`, processes subsamples in parallel across multiple threads. Strongly recommended for large datasets. |
| `cstarCpdagAlgorithm`        | String. The algorithm used to convert the aggregated results into a CPDAG (e.g., `"PC"`, `"GFCI"`, `"FGES"`). Determines how CStaR interprets the final graph structure. |
| `fileOutPath`                | String path. If non-empty, results (e.g., subsample graphs, selection frequencies) are written to disk at the given location. Useful for large studies or reproducibility. |
| `removeEffectNodes`          | Boolean. If `true`, nodes that never meet the minimum effect threshold across subsamples are excluded before final aggregation. |
| `sampleStyle`                | String. Controls how subsamples are constructed (e.g., `"bootstrap"`, `"half-sample"`, `"cross-validation"`). Affects stability and runtime. |
| `verbose`                    | Boolean. If `true`, prints detailed progress information during subsampling, scoring, and aggregation. |

---

### Interpreting the table

For a given row \(X \to Y\):

- **PI (stability)**
    - Close to 1.0: \(X \to Y\) consistently appears among the strongest effects across subsamples.
    - Around 0.5: borderline; may be interesting but less robust.
    - Close to 0: rarely selected; often noise.

- **Effect (average minimal effect)**
    - Positive values indicate a consistent positive causal effect estimate.
    - Larger magnitude suggests a stronger effect, but interpretation depends on scale and model assumptions.

- **PCER**
    - Gives an upper bound on the expected per-comparison error rate for that edge, given the overall selection procedure.
    - Edges with `*` (π ≤ 0.5) are not in the reliable regime of the bound and should be treated cautiously.

A typical use is to pick a **PI threshold** (e.g. `π ≥ 0.8`) and an **effect threshold** (e.g. `Effect ≥ 0.1`), and then focus on that shortlist as **candidate causal predictors** for follow-up analysis or experiments.

---

## When to use CStaR

CStaR is most useful when:

- You have **many potential predictors** and a smaller number of key outcomes, and you want a **prioritized list** of robust causal candidates.
- You are worried about **model-selection instability**: different subsamples might suggest different graphs, and you want edges that “survive” this variability.
- You care about **controlling false positives** in a stability-selection sense, rather than recovering a single “best” graph.

It pairs naturally with workflows where:

- The **full causal graph** is complex or high-dimensional, but
- You mainly need a **short, interpretable list** of predictors that are repeatedly supported by the data across resamples and CPDAG variations.

## References

Stekhoven, D. J., Moraes, I., Sveinbjörnsson, G., Hennig, L., Maathuis, M. H., & Bühlmann, P. (2012).  
**Causal stability ranking.** *Bioinformatics*, 28(21), 2819–2823.

Meinshausen, N., & Bühlmann, P. (2010).  
**Stability selection.** *Journal of the Royal Statistical Society: Series B (Statistical Methodology)*, 72(4), 417–473.

Colombo, D., & Maathuis, M. H. (2014).  
**Order-independent constraint-based causal structure learning.** *Journal of Machine Learning Research*, 15(1), 3741–3782.

## Summary

- CStaR is a stability-based causal ranking method that repeatedly subsamples the data, fits a CPDAG, and applies IDA to estimate minimal total effects for each candidate cause–effect pair. It aggregates these results using stability selection, producing a ranked list of robust causal candidates with interpretable stability frequencies and effect sizes.

- CStaR is ideal when the goal is prioritizing reliable causal predictors rather than recovering a full graph, especially in high-dimensional settings where model-selection variability is high. It supports multiple CPDAG learners (PC-Stable, FGES, BOSS, RBOSS), parallelization, and reproducible output, but does not currently incorporate background-knowledge constraints.

⸻
