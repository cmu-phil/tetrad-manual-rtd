## CStaR (Causal Stability Ranking)

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

### High-level idea

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

### Inputs

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

### Outputs

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

### Key parameters

- **Number of subsamples** (`numSubsamples`, default ~30)  
  How many half-samples to draw. Larger values give more stable estimates but require more computation.

- **Top bracket** (`topBracket`)  
  Controls how many strong edges per subsample are considered “selected.”  
  For each subsample, CStaR sorts all cause–effect effects and takes the top  
  `topBracket × #effects` entries as the selected set for that subsample.

- **Selection alpha** (`selectionAlpha`)  
  Minimum average effect size required for an edge to be reported.  
  Useful for filtering out edges that are stable but very small in magnitude.

- **CPDAG algorithm** (`cpdagAlgorithm`)  
  Which method to use to learn the CPDAG on each subsample:
    - **PC-Stable** – constraint-based, order-independent.
    - **FGES** – greedy score-based search over DAG equivalence classes.
    - **BOSS / Restricted BOSS** – permutation-based searches that can be more targeted or constrained.

- **Sample style** (`sampleStyle`)
    - **Bootstrap** – sample with replacement (half the rows).
    - **Subsample** – sample without replacement (half the rows).  
      Both are compatible with stability selection; subsampling is closer to the original CStaR formulation.

- **Parallelization** (`parallelized`)  
  Subsamples can be processed in parallel (one per thread) to speed up large runs.

- **Verbose** (`verbose`)  
  If enabled, logs the CPDAG algorithm, subsample index, and IDA runs to the Tetrad log.

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

### When to use CStaR

CStaR is most useful when:

- You have **many potential predictors** and a smaller number of key outcomes, and you want a **prioritized list** of robust causal candidates.
- You are worried about **model-selection instability**: different subsamples might suggest different graphs, and you want edges that “survive” this variability.
- You care about **controlling false positives** in a stability-selection sense, rather than recovering a single “best” graph.

It pairs naturally with workflows where:

- The **full causal graph** is complex or high-dimensional, but
- You mainly need a **short, interpretable list** of predictors that are repeatedly supported by the data across resamples and CPDAG variations.